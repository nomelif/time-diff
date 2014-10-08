#!/usr/bin/python
import unittest
import os
import sys
import platform
import locale
import StringIO
import time

ROOT_PATH = os.path.abspath(os.path.abspath(os.path.dirname(__file__)) + '/../')
TIMEDIFF_PATH = ROOT_PATH

sys.path.append(TIMEDIFF_PATH)

import conf_reader

class TestConfReader(unittest.TestCase):

    def setUp(self):
        
        self.conf = conf_reader.ConfReader()

    def test_PRESETS(self):

        for key in self.conf.PRESETS.keys():

            # Test whether parameters are strings

            self.assertIsInstance(key, basestring)
            self.assertIsInstance(self.conf.PRESETS[key], basestring)

            # Test whether parameters' length is greater than 0

            self.assertTrue(len(key) > 0)
            self.assertTrue(len(self.conf.PRESETS[key]) > 0)

    def test_DEFAULT_PRESET(self):

        # Test whether default preset is a string

        self.assertIsInstance(self.conf.DEFAULT_PRESET, basestring)

        # Test whether default preset's length is greater than 0

        self.assertTrue(len(self.conf.DEFAULT_PRESET) > 0)

if __name__ == '__main__':
    unittest.main()