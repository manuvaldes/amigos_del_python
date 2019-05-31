#!/usr/bin/env python

import pyramide
import pytest
import sys


@pytest.fixture()
def x():
    return 1


def test_example(x, capsys):
    captured = capsys.readouterr()                                              
    print(captured.out, file=sys.stderr)                                        
    assert False, 'TODO'
