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
    version['buildNumber'] = os.environ['CI_PIPELINE_IID']
    version['buildTag'] = os.environ['CI_PIPELINE_IID']
    version['buildTime'] = now
    version['scmBranch'] = os.environ['CI_COMMIT_REF_NAME']
    version['scmCommit'] = os.environ['CI_COMMIT_SHA']
    version['scmUrl'] = os.environ['CI_REPOSITORY_URL']
    version['version'] = os.environ['CI_PIPELINE_IID']
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
    if ('BUILD_BUILDID' in os.environ):
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

    version = gen_gitlab()

    with open(filename, 'w') as f:
        json.dump(version, f)