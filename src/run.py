#!/usr/bin/env python3


import os
import json
from datetime import datetime, timezone
now = datetime.now(timezone.utc).isoformat()

version = {}
filename = 'version.json'


# {
#   "buildNumber": "47",
#   "buildTag": "jenkins-Dmvrbackend-Build-Master-47",
#   "buildTime": "2018-10-18T20:55:02Z",
#   "scmBranch": "origin/master",
#   "scmCommit": "2059d816be6a863df08b8803245812e0ac7010eb",
#   "scmUrl": "git@code.wds.io:redshift/metadata_read.git",
#   "version": "47_master"
# }

version['buildNumber'] = os.environ['CI_PIPELINE_IID']
version['buildTag'] = os.environ['CI_PIPELINE_IID']
version['buildTime'] = now
version['scmBranch'] = os.environ['CI_COMMIT_REF_NAME']
version['scmCommit'] = os.environ['CI_COMMIT_SHA']
version['scmUrl'] = os.environ['CI_REPOSITORY_URL']
version['version'] = os.environ['CI_PIPELINE_IID']


with open(filename, 'w') as f:
    json.dump(version, f)
