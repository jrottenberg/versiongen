#!/usr/bin/env python3


import os
import json
from datetime import datetime, timezone

import argparse

now = datetime.now(timezone.utc).isoformat()


def gen_gitlab():
    """
    Generate version object when running on gitlab
    """
    version = {}
    version['buildNumber'] = os.getenv('CI_PIPELINE_IID')
    version['buildTag'] = F"gitlab-{os.getenv('CI_PROJECT_PATH_SLUG')}-{os.getenv('CI_PIPELINE_IID')}"
    version['buildTime'] = now
    version['scmBranch'] = os.getenv('CI_BUILD_REF_SLUG')
    version['scmCommit'] = os.getenv('CI_COMMIT_SHA')
    version['scmUrl'] = os.getenv('CI_PROJECT_PATH')
    version['version'] = F"{os.getenv('CI_PIPELINE_IID')}_{os.getenv('CI_BUILD_REF_SLUG')}"
    return version


def gen_azure():
    """
    Generate version object when running on azure
    """
    version = {}
    version['buildNumber'] = os.getenv('BUILD_BUILDNUMBER')
    version['buildTag'] = F"azure-{os.getenv('BUILD_REPOSITORY_NAME')}-{os.getenv('BUILD_BUILDNUMBER')}"
    version['buildTime'] = now
    version['scmBranch'] = os.getenv('BUILD_SOURCEBRANCHNAME')
    version['scmCommit'] = os.getenv('BUILD_SOURCEVERSION')
    version['scmUrl'] = os.getenv('BUILD_REPOSITORY_URI')
    version['version'] = F"{os.getenv('BUILD_BUILDNUMBER')}_{os.getenv('BUILD_SOURCEBRANCHNAME')}"
    return version


def determine_ci():
    """
    Guess the running ci system based on environment variables
    """
    if ('CI_PIPELINE_IID' in os.environ):
        return "gitlab"
    if ('BUILD_ID' in os.environ):
        return "jenkins"
    if ('TRAVIS_BUILD_ID' in os.environ):
        return "travis"
    if ('BUILD_BUILDNUMBER' in os.environ):
        return "azure"
    if ('CIRCLE_BUILD_NUM' in os.environ):
        return "circle"
    return "unknown_ci"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Will generate a version file')

    parser.add_argument('-o', '--output', default='version.json',
                        help='where to store the file')

    args = parser.parse_args()

    filename = args.output
    current_ci = determine_ci()

    if current_ci == 'gitlab':
        version = gen_gitlab()

    if current_ci == 'azure':
        version = gen_azure()

    with open(filename, 'w') as f:
        json.dump(version, f)
