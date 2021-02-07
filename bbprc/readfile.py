import logging
from os import stat

_log = logging.getLogger(name=__name__)

MAX_TEXT_SIZE = 16384


def _get_content(file, size=MAX_TEXT_SIZE):
    with open(file, 'r') as fd:
        content = fd.read(size)

    text = ""
    if content:
        text += "```text\n"
        text += content

        if stat(file).st_size > size:
            text += "\n<...> Some lines were truncated <...>"

        text += "\n```"

    return text


def read_file(file):
    return _get_content(file)
