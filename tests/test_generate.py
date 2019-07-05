#!/usr/bin/env python3


from versiongen.generate import gen_gitlab, gen_azure


def test_generate_gitlab(emulate_gitlab):
    assert gen_gitlab()['buildNumber'] == '0'


def test_generate_azure(emulate_azure):
    assert gen_azure()['buildNumber'] == '0'
