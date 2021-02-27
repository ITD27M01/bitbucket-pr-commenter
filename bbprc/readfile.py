import logging
from os import stat

_log = logging.getLogger(name=__name__)

MAX_TEXT_SIZE = 32768
HEADER = "```text\n"
FOOTER = "\n```"
TRUNCATE_COMMENT = "\n<...> Some lines were truncated <...>"


def _get_string_size(string: str) -> int:
    size = len(string.encode('utf-8'))

    return size


def _get_content(file, size):
    # NOTE(igortiunov): The size of the BB comment is limited by MAX_TEXT_SIZE, so, I need to calculate the borders
    read_size = size - _get_string_size(HEADER) - _get_string_size(FOOTER) - _get_string_size(TRUNCATE_COMMENT)
    if read_size <= 0:
        read_size = size

    with open(file, 'r') as fd:
        _log.debug(f"Try to read {file} content")
        content = fd.read(read_size)

    text = ""
    if content:
        text += HEADER
        text += content

        if stat(file).st_size > size:
            text += TRUNCATE_COMMENT

        text += FOOTER

    return text


def read_file(file, greeting):
    greeting_size = _get_string_size(greeting)

    return _get_content(file, size=MAX_TEXT_SIZE - greeting_size)
