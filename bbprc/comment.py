import requests
import logging
from urllib3 import disable_warnings as disable_urllib3_warnings
from urllib3 import exceptions as urllib3_exceptions
from re import match, compile


_log = logging.getLogger(name=__name__)

SCHEME = 'https'
DEFAULT_GREETING = "I know you're working hard. I have some results, what do you think of them?"
PR_PATTERN = compile('(pull-requests)?\/?([0-9]+)\/?(from)?')


def _construct_url(server, project, repo, pr):
    pr_number_match = match(PR_PATTERN, pr)
    if pr_number_match and pr_number_match.groups()[1]:
        url = f"{SCHEME}://{server}/" \
              f"rest/api/latest/" \
              f"projects/{project}/" \
              f"repos/{repo}/" \
              f"pull-requests/{pr_number_match.groups()[1]}/comments"

        _log.debug(f"Construct url: {url}")
        return url
    else:
        raise ValueError("Cannot understand pull request number")


def _make_data(greeting, file):
    _log.debug("Construct data to send")

    comment_greeting = greeting if greeting else DEFAULT_GREETING
    data = {
        "text": comment_greeting + "\n"
    }

    if file:
        with open(file, 'r') as fd:
            lines = fd.read()

        if lines:
            data["text"] += "```text\n"
            data["text"] += lines
            data["text"] += "\n```"

    return data


def _do_send_comment(url, data, token, verify):
    if not verify:
        disable_urllib3_warnings(urllib3_exceptions.InsecureRequestWarning)

    response = requests.post(url, json=data, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }, verify=verify)

    _log.debug(response.text)

    return response.ok


def send_comment(server, token, project, repo, pr, greeting, file, verify):
    url = _construct_url(server, project, repo, pr)

    data = _make_data(greeting, file)

    return _do_send_comment(url, data, token, verify)
