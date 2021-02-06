# BitBucket Pull Request commenter

This simple utility just sends comment to BitBucket server pull request.
It is useful in CI automation to comment PR with build results and include
some data from output text file.

```shell
> bbprc --help
usage: bbprc [-h] [--server SERVER] [--token TOKEN] [--project PROJECT] [--repo REPO] [--pr PR] [--greeting GREETING] [--file FILE] [--verify] [--debug]

Sends comment to BitBucket Pull Request

optional arguments:
  -h, --help           show this help message and exit
  --server SERVER      BitBucket server name or address
  --token TOKEN        BitBucket Bearer token for authorization
  --project PROJECT    BitBucket project name
  --repo REPO          BitBucket repository name
  --pr PR              BitBucket Pull Request number
  --greeting GREETING  Some text you want to save in the PR comment
  --file FILE          Filepath to load comment from
  --verify             Verify server cert
  --debug              Shows detailed process
```

## Authentication

For security reasons it only supports [personal access token](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html)
as a bearer for authentication.

## Requirements

* requests
