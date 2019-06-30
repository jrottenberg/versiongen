#!/usr/bin/env python3


from versiongen.generate import determine_ci


def test_determine_gitlab(emulate_gitlab):
    assert determine_ci() == 'gitlab'


def test_determine_jenkins(emulate_jenkins):
    assert determine_ci() == 'jenkins'


def test_determine_travis(emulate_travis):
    assert determine_ci() == 'travis'


def test_determine_azure(emulate_azure):
    assert determine_ci() == 'azure'


def test_determine_circle(emulate_circle):
    assert determine_ci() == 'circle'
