import re

from PyInquirer import prompt

from .color import STYLE
from .data import DataLoader


class Question:
    def __init__(self):
        self.data_loader = DataLoader()

    @staticmethod
    def format_choices(choices, formatter):
        formatted_choices = [formatter(rank) for rank in range(len(choices))]
        return formatted_choices

    @staticmethod
    def remove_frequency_string(string):
        # "(0) add" -> "add"
        return re.sub(r"^\([0-9]+\)\ ", "", string, 1)

    def ask_emoji(self):
        """Display CLI to select an emoji.

        Returns:
            str: Selected emoji
        """
        emojis = self.data_loader.load_emojis()

        def formatter(rank):
            return "({}) {} : {}".format(
                emojis[rank]["frequency"],
                emojis[rank]["emoji"],
                emojis[rank]["name"],
            )

        question = {
            "type": "list",
            "name": "emoji",
            "message": "Select emoji",
            "choices": [*self.format_choices(emojis, formatter)],
        }

        return self.remove_frequency_string(
            prompt(question, style=STYLE)["emoji"]
        )[0]

    def ask_verb(self):
        """Display CLI to select a verb.

        If N/A is selected, go to input question.

        Returns:
            str: Selected verb
        """
        verbs = self.data_loader.load_verbs()

        def formatter(rank):
            return "({}) {}".format(
                verbs[rank]["frequency"], verbs[rank]["verb"]
            )

        question = {
            "type": "list",
            "name": "verb",
            "message": "Select verb",
            "choices": ["N/A", *self.format_choices(verbs, formatter)],
        }

        verb = self.remove_frequency_string(
            prompt(question, style=STYLE)["verb"]
        )
        if verb != "N/A":
            return verb

        alt_question = {
            "type": "input",
            "name": "verb_input",
            "message": "Input verb",
        }

        return prompt(alt_question, style=STYLE)["verb_input"]

    def ask_object(self):
        """Display CLI to select a object.

        If N/A is selected, go to input question.

        Returns:
            str: Selected object
        """
        objects = self.data_loader.load_objects()

        def formatter(rank):
            return "({}) {}".format(
                objects[rank]["frequency"], objects[rank]["object"]
            )

        question = {
            "type": "list",
            "name": "object",
            "message": "Select object",
            "choices": ["N/A", *self.format_choices(objects, formatter)],
        }

        object_ = self.remove_frequency_string(
            prompt(question, style=STYLE)["object"]
        )
        if object_ != "N/A":
            return object_

        alt_question = {
            "type": "input",
            "name": "object_input",
            "message": "Input object",
        }

        return prompt(alt_question, style=STYLE)["object_input"]

    def ask_modifier(self):
        """Display CLI to input modifier.

        Returns:
            str: Input modifier
        """
        question = {
            "type": "input",
            "name": "modifier",
            "message": "Input modifier",
        }

        return prompt(question, style=STYLE)["modifier"]

    def ask_message(self):
        """Display CLI to input message.

        Returns:
            str: Input message
        """
        question = {
            "type": "input",
            "name": "message",
            "message": "Input message",
        }

        return prompt(question, style=STYLE)["message"]

    def ask_template(self):
        """Display CLI to select a template.

        If N/A is selected, go to emoji/message question.

        Returns:
            str: Selected template
        """
        templates = self.data_loader.load_templates()

        def formatter(rank):
            return "({}) {}".format(
                templates[rank]["frequency"], templates[rank]["template"]
            )

        question = {
            "type": "list",
            "name": "template",
            "message": "Select template",
            "choices": ["N/A", *self.format_choices(templates, formatter)],
        }

        template = self.remove_frequency_string(
            prompt(question, style=STYLE)["template"]
        )
        if template != "N/A":
            return template

        return "{} :  {}".format(self.ask_emoji(), self.ask_message())

    def ask_commit(self, commit_message):
        """Display CLI to confirm a commit message.

        Args:
            commit_message (str): A processed commit message

        Returns:
            bool: Is committable
        """
        question = {
            "type": "confirm",
            "name": "commit",
            "message": f"Commit `{commit_message}`?",
        }

        return prompt(question, style=STYLE)["commit"]

    def ask_clean_use_history(self):
        """Display CLI to confirm whether to clean use history.

        Returns:
            bool: Is cleanable
        """
        question = {
            "type": "confirm",
            "name": "clean",
            "message": "Clean use history?",
        }

        return prompt(question, style=STYLE)["clean"]
