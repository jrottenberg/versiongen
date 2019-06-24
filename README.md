# versiongen
Generate a version file for CI



```
export CI_COMMIT_SHA=01234567890
export CI_PIPELINE_IID=0
export BUILD_NUMBER=0
export CI_PROJECT_PATH=local/local
export CI_COMMIT_REF_NAME=n/a
export CI_REPOSITORY_URL=git@git.local:local
```

-->

```
{
    "buildNumber": "0",
    "buildTag": "0",
    "buildTime": "2019-06-24T03:02:51.128071+00:00",
    "scmBranch": "n/a",
    "scmCommit": "01234567890",
    "scmUrl": "git@git.local:local",
    "version": "0"
}
```