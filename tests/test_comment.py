from bbprc.comment import _make_data

COMMENT = """Don’t Panic!
```text
Panic! Panic! Panic!
```"""


def test_comment_data():
    data = _make_data("Don’t Panic!", "tests/file.txt")
    assert data["text"] == COMMENT
