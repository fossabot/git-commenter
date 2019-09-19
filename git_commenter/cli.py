import argparse

import pyperclip
from termcolor import cprint

from .git import GitUtility
from .question import Question


class InvalidArgumentError(ValueError):
    def __str__(self):
        return "The multiple modes can not be specified."


class CLI:
    def __init__(self, message):
        """
        Args:
            message (str, None): Message input as an argument
        """
        self.git = GitUtility()
        self.question = Question()

        self.message = message

        self.modes = []

    def register_mode(self, args):
        self.modes = [mode for mode, value in vars(args).items() if value]

        if not self.modes or self.modes == ["clipboard"]:
            self.modes.append("normal")

        if "message" in self.modes and "template" in self.modes:
            raise InvalidArgumentError()

    def run(self):
        if "clean" in self.modes:
            if self.question.ask_clean_use_history():
                self.question.data_loader.clean_use_history()
                cprint("Use history cleaned.", "yellow")

        else:
            emoji, verb, object_, template = (None, None, None, None)

            # ask
            if "normal" in self.modes:
                emoji = self.question.ask_emoji()
                verb = self.question.ask_verb()
                object_ = self.question.ask_object()
                modifier = self.question.ask_modifier()

                self.message = self.make_message(verb, object_, modifier)
                commit_message = f"{emoji} :  {self.message}"

            elif "message" in self.modes:
                emoji = self.question.ask_emoji()
                commit_message = f"{emoji} :  {self.message}"

            elif "template" in self.modes:
                template = self.question.ask_template()
                commit_message = template

            # commit
            if self.question.ask_commit(commit_message):
                self.question.data_loader.store_history(
                    emoji, verb, object_, template
                )

                if "clipboard" in self.modes:
                    pyperclip.copy(commit_message)
                    cprint("Commit message copied to clipboard.", "yellow")

                else:
                    self.git.commit(commit_message)

    @staticmethod
    def make_message(verb, object_, modifier):
        if verb is not None:
            verb = verb.capitalize()

        words = [
            word for word in [verb, object_, modifier] if word is not None
        ]
        message = " ".join(words)
        return message


def main():
    from . import __version__

    cprint(
        r"""   ____     ____    ____  _
U /"___|uU /"___|U /"___||"|        ___
\| |  _ /\| | u  \| | uU | | u     |_"_|
 | |_| |  | |/__  | |/__\| |/__     | |
  \____|   \____|  \____||_____|  U/| |\u
  _)(|_   _// \\  _// \\ //  \\.-,_|___|_,-.
 (__)__) (__)(__)(__)(__|_")("_)\_)-' '-(_/
""",
        "magenta",
    )

    parser = argparse.ArgumentParser(description="Git Commenter")
    parser.add_argument(
        "-c", "--clipboard", action="store_true", help="copy to clipboard"
    )
    parser.add_argument(
        "-m", "--message", help="commit with input message", type=str
    )
    parser.add_argument(
        "-t",
        "--template",
        action="store_true",
        help="commit with selected template",
    )
    parser.add_argument(
        "--clean", action="store_true", help="clean up use history"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="show version and exit",
    )
    args = parser.parse_args()

    cli = CLI(message=args.message)
    cli.register_mode(args)
    cli.run()
