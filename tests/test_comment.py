from bbprc.comment import _make_data
from bbprc.readfile import _get_content


COMMENT = """Don’t Panic!
```text
Panic! Panic! Panic!
```"""

TRUNCATED_COMMENT = """```text
Panic! Panic! Panic!
<...> Some lines were truncated <...>
```"""


def test_comment_data():
    data = _make_data("Don’t Panic!", "tests/file.txt")
    assert data["text"] == COMMENT


def test_truncated_data():
    content = _get_content("tests/file_bigger.txt", 20)
    assert content == TRUNCATED_COMMENT
