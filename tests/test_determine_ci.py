#!/usr/bin/env python3


from versiongen.generate import determine_ci


def test_determine_gitlab(monkeypatch):
    monkeypatch.setenv('CI_PIPELINE_IID', '0')
    assert determine_ci() == 'gitlab'


def test_determine_jenkins(monkeypatch):
    monkeypatch.setenv('BUILD_ID', '0')
    assert determine_ci() == 'jenkins'


def test_determine_travis(monkeypatch):
    monkeypatch.setenv('TRAVIS_BUILD_ID', '0')
    assert determine_ci() == 'travis'


def test_determine_azure(monkeypatch):
    monkeypatch.setenv('BUILD_BUILDID', '0')
    assert determine_ci() == 'azure'


def test_determine_azure(monkeypatch):
    monkeypatch.setenv('CIRCLE_BUILD_NUM', '0')
    assert determine_ci() == 'circle'
