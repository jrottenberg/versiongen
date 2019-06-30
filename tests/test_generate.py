#!/usr/bin/env python3


from versiongen.generate import gen_gitlab


def test_generate_gitlab(emulate_gitlab):
    assert gen_gitlab()['buildNumber'] == '0'
