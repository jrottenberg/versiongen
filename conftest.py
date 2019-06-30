import pytest
import os


# If we run on gitlab, we need the tests to pass still...
del os.environ['CI_PIPELINE_IID']


@pytest.fixture()
def emulate_gitlab(monkeypatch):
    monkeypatch.setenv('CI_PIPELINE_IID', '0')


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
