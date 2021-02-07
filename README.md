# BitBucket Pull Request commenter

![tests_workflow](https://github.com/ITD27M01/bitbucket-pr-commenter/workflows/tests_workflow/badge.svg)

This simple utility just sends comment to BitBucket server pull request.
It is useful in CI automation to comment PR with build results and include
some data from output text file.

## Example
Send content of output.txt for some build to BitBucket pull request comment: 
```shell
bbprc --server %bitbucket_url% --token %bitbucket_password% \
    --project %bitbucket_project% \
    --repo %bitbucket_repo% \
    --greeting "%system.teamcity.buildConfName%" \
    --pr %teamcity.build.branch% \
    --file %teamcity.build.checkoutDir%/output.txt
```

## Authentication

For security reasons it only supports [personal access token](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html)
as a bearer for authentication.

## Requirements

* requests
