import argparse


def args_parser():
    parser = argparse.ArgumentParser(description='Sends comment to BitBucket Pull Request')
    parser.add_argument('--server', type=str, action='store',
                        help='BitBucket server address or url')

    parser.add_argument('--token', type=str, action='store',
                        help='BitBucket Bearer token for authorization')

    parser.add_argument('--project', type=str, action='store',
                        help='BitBucket project name')

    parser.add_argument('--repo', type=str, action='store',
                        help='BitBucket repository name')

    parser.add_argument('--pr', type=str, action='store',
                        help='BitBucket Pull Request number')

    parser.add_argument('--greeting', type=str, action='store',
                        help='Some text you want to save in the PR comment')

    parser.add_argument('--file', type=str, action='store',
                        help='Filepath to load comment from')

    parser.add_argument('--verify', default=False, action='store_true',
                        help='Verify server cert')

    parser.add_argument('--debug', default=False, action='store_true',
                        help='Shows detailed process')

    return parser.parse_args()
