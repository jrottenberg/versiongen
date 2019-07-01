import pytest
import os


# If we run on gitlab, we need the tests to pass still...
del os.environ['CI_PIPELINE_IID']


@pytest.fixture()
def emulate_gitlab(monkeypatch):
    monkeypatch.setenv('CI_PIPELINE_IID', '0')
    monkeypatch.setenv('CI_PROJECT_DIR', 'versiongen')
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'local')
    monkeypatch.setenv('CI_COMMIT_SHA', '01234sha1')
    monkeypatch.setenv('CI_PROJECT_PATH', 'path/to/myproject')


@pytest.fixture()
def emulate_jenkins(monkeypatch):
    monkeypatch.setenv('BUILD_ID', '0')


@pytest.fixture()
def emulate_travis(monkeypatch):
    monkeypatch.setenv('TRAVIS_BUILD_ID', '0')


@pytest.fixture()
def emulate_azure(monkeypatch):
    monkeypatch.setenv('BUILD_BUILDID', '0')


@pytest.fixture()
def emulate_circle(monkeypatch):
    monkeypatch.setenv('CIRCLE_BUILD_NUM', '0')
