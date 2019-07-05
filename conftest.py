import pytest
import os


# If we run on a CI, we need the tests to pass still...
try:
    del os.environ['CI_PIPELINE_IID']
except KeyError:
    print("Run tests on gitlab")

try:
    del os.environ['BUILD_BUILDNUMBER']
except KeyError:
    print("Run tests on azure")


@pytest.fixture()
def emulate_gitlab(monkeypatch):
    monkeypatch.setenv('CI_PIPELINE_IID', '0')
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'local')
    monkeypatch.setenv('CI_COMMIT_SHA', '01234sha1')
    monkeypatch.setenv('CI_PROJECT_PATH_SLUG', 'path-to-myproject')


@pytest.fixture()
def emulate_jenkins(monkeypatch):
    monkeypatch.setenv('BUILD_ID', '0')
    monkeypatch.setenv('CI_PROJECT_DIR', 'versiongen')
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'local')
    monkeypatch.setenv('CI_COMMIT_SHA', '01234sha1')
    monkeypatch.setenv('CI_PROJECT_PATH_SLUG', 'path-to-myproject')


@pytest.fixture()
def emulate_travis(monkeypatch):
    monkeypatch.setenv('TRAVIS_BUILD_ID', '0')
    monkeypatch.setenv('CI_PROJECT_DIR', 'versiongen')
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'local')
    monkeypatch.setenv('CI_COMMIT_SHA', '01234sha1')
    monkeypatch.setenv('CI_PROJECT_PATH_SLUG', 'path-to-myproject')


@pytest.fixture()
def emulate_azure(monkeypatch):
    monkeypatch.setenv('BUILD_BUILDNUMBER', '0')
    monkeypatch.setenv('BUILD_SOURCEBRANCHNAME', 'local')
    monkeypatch.setenv('BUILD_SOURCEVERSION', '01234sha1')
    monkeypatch.setenv('BUILD_REPOSITORY_URI', 'path-to-myproject')


@pytest.fixture()
def emulate_circle(monkeypatch):
    monkeypatch.setenv('CIRCLE_BUILD_NUM', '0')
    monkeypatch.setenv('CI_PROJECT_DIR', 'versiongen')
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'local')
    monkeypatch.setenv('CI_COMMIT_SHA', '01234sha1')
    monkeypatch.setenv('CI_PROJECT_PATH_SLUG', 'path-to-myproject')
