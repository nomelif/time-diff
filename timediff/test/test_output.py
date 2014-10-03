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

import cli_output

class TestCliOutput(unittest.TestCase):

    def setUp(self):
        self.out = cli_output.CliOutput()
 
    def test_format_line(self):
        self.assertEqual("a b : c", self.out.format_line(("a", "b", "c")))
        self.assertEqual(None, self.out.format_line(("a")))

if __name__ == '__main__':
    unittest.main()