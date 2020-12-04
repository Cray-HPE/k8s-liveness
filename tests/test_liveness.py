# Copyright 2020, Cray Inc.
""" Test the liveness package """

import os
import unittest
import tempfile
from datetime import datetime, timedelta
from mock import patch

from liveness.timestamp import Timestamp


class TestSetup(object):
    def __enter__(self):
        self.path = tempfile.NamedTemporaryFile().name
        return self

    def __exit__(self, type, value, traceback):
        try:
            os.remove(self.path)
        except OSError:
            pass


def test_creation():
    """
    Test that a new timestamp object can be initialized.
    """
    with TestSetup() as ts:
        t = Timestamp(path=ts.path)
        assert os.path.exists(t.path)
    
        # Test that this object counts as having a maximum viable age)
        assert isinstance(t.max_age, timedelta)
        print("Exercising string magic method: %s" %(t))


def test_creation_with_timestamp():
    with TestSetup() as ts:
        t = Timestamp(path=ts.path, when=datetime.now())
        assert os.path.exists(t.path)


def test_uninitiated_value():
    with TestSetup() as ts:
        t = Timestamp(path=ts.path)
        os.unlink(ts.path)
        assert t.value == datetime.fromtimestamp(0)


def test_alive():
    with TestSetup() as ts:
        t = Timestamp(path=ts.path)
        assert t.alive


def test_byref_instantiation():
    with TestSetup() as ts:
        original = Timestamp(path=ts.path)
        reference = Timestamp.byref(ts.path)
        assert original.value == reference.value


def test_age():
    with TestSetup() as ts:
        t = Timestamp(path=ts.path)
        # Tests taht a non-zero amoutn of time has elapsed
        assert t.age > timedelta(seconds=0)

def test_dead():
    with TestSetup() as ts:
        t = Timestamp(path=ts.path)
        one_minute_ago = datetime.now() - timedelta(minutes=1)
        with open(ts.path, 'w') as tstamp_file:
            tstamp_file.write(str(one_minute_ago.timestamp()))
        assert not t.alive
