import logging
from os import stat

_log = logging.getLogger(name=__name__)

# NOTE(igortiunov): Size is dictated by max comment size on BB plus truncate comment
MAX_TEXT_SIZE = 32728
HEADER = "```text\n"
FOOTER = "\n```"
TRUNCATE_COMMENT = "\n<...> Some lines were truncated <...>"


def _get_content(file, size=MAX_TEXT_SIZE):
    with open(file, 'r') as fd:
        _log.debug(f"Try to read {file} content")
        content = fd.read(size)

    text = ""
    if content:
        text += HEADER
        text += content

        if stat(file).st_size > size:
            text += TRUNCATE_COMMENT

        text += FOOTER

    return text


def read_file(file):
    return _get_content(file)
