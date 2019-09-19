from subprocess import Popen


class GitError(Exception):
    """Raise error when git command runner has error."""

    pass


class GitUtility:
    """Utility functions for operate git."""

    def run(self, cmd, *args):
        if isinstance(args[0], tuple):
            command = ("git", cmd) + tuple([arg for arg in args[0]])
        else:
            command = ("git", cmd) + args

        proc = Popen(command, stdin=-1, stdout=-1, stderr=-1)
        out, err = proc.communicate()

        if not err:
            return out.strip()
        else:
            raise GitError(err.strip())

    def add(self, path):
        self.run("add", path)

    def commit(self, commit_msg):
        self.run("commit", "-m", commit_msg)

    def rev_parse(self, *args):
        self.run("rev-parse", args)

    def get_toplevel(self):
        self.rev_parse("--show-toplevel")
