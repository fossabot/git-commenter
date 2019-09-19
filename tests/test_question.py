import pytest

from git_commenter.question import Question


class TestQuestion:
    @pytest.mark.parametrize(
        "string, actual", [("N/A", "N/A"), ("(0) add", "add")]
    )
    def test_remove_frequency(self, string, actual):
        expected = Question().remove_frequency_string(string)
        assert expected == actual
