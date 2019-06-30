FROM python:3


CMD ["/opt/versiongen/generate.py.py"]


ADD versiongen /opt/versiongen