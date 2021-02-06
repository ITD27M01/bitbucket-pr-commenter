from urllib3.util import parse_url
from bbprc.comment import _construct_url

URL = "https://server/rest/api/latest/projects/test_project/repos/test_repo/pull-requests/42/comments"
URL_PARSED = parse_url(URL)


def test_pr_number():
    assert _construct_url(URL_PARSED.host, 'test_project', 'test_repo', '42') == URL_PARSED.url


def test_pr_string():
    assert _construct_url(URL_PARSED.host, 'test_project', 'test_repo', 'pull-requests/42') == URL_PARSED.url


def test_pr_from():
    assert _construct_url(URL_PARSED.host, 'test_project', 'test_repo', '42/from') == URL_PARSED.url
