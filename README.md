# versiongen
Generate a version file for CI


## Goal

Each ci system presents environment variables to the project being built. Every project could use a simple version file generated at build time and read at runtime to give information about the build artifact.



```
export CI_COMMIT_SHA=01234567890
export CI_PIPELINE_IID=0
export BUILD_NUMBER=0
export CI_PROJECT_PATH=local/local
export CI_COMMIT_REF_NAME=n/a
export CI_REPOSITORY_URL=git@git.local:local
```

-->

Generates version.json with :

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



## The CIs

https://docs.gitlab.com/ee/ci/variables/predefined_variables.html

https://wiki.jenkins.io/display/JENKINS/Building+a+software+project#Buildingasoftwareproject-belowJenkinsSetEnvironmentVariables

https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml

https://circleci.com/docs/2.0/env-vars/#built-in-environment-variables


## Usage

### Gitlab-ci

```
init:
  stage: init
  image: versiongen
  script:
  - versiongen -o path/to/version.json
  artifacts:
    paths:
    - path/to/version.json
```