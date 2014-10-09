#!/usr/bin/python
import unittest
import os
import sys
import platform
import locale
import StringIO
import time
import datetime

ROOT_PATH = os.path.abspath(os.path.abspath(os.path.dirname(__file__)) + '/../')
TIMEDIFF_PATH = ROOT_PATH

sys.path.append(TIMEDIFF_PATH)

import cli_output

class TestCliOutput(unittest.TestCase):

    def setUp(self):
        self.out = cli_output.CliOutput()
 	
    def test_format_timedelta(self):
    	# Seconds
        self.assertEqual("         1 s", self.out.format_timedelta(datetime.timedelta(seconds=1)))
        self.assertEqual("       300 s", self.out.format_timedelta(datetime.timedelta(seconds=300)))
        self.assertEqual("     15001 s", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250)))
        # Milliseconds
        self.assertEqual("         1000 ms", self.out.format_timedelta(datetime.timedelta(seconds=1), "ms"))
        self.assertEqual("       300000 ms", self.out.format_timedelta(datetime.timedelta(seconds=300), "ms"))
        self.assertEqual("     15001000 ms", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250), "ms"))
        # Minutes
        self.assertEqual("         0 min", self.out.format_timedelta(datetime.timedelta(seconds=1), "min"))
        self.assertEqual("         5 min", self.out.format_timedelta(datetime.timedelta(seconds=300), "min"))
        self.assertEqual("       250 min", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250), "min"))
        #Hours
        self.assertEqual("         0 h", self.out.format_timedelta(datetime.timedelta(seconds=1), "h"))
        self.assertEqual("        12 h", self.out.format_timedelta(datetime.timedelta(minutes=300), "h"))
        
    def test_format_line(self):
        self.assertEqual("         1 s          2 s : c", self.out.format_line((datetime.timedelta(seconds=1), datetime.timedelta(seconds=2), "c")))
        self.assertEqual(None, self.out.format_line(("a")))

if __name__ == '__main__':
    unittest.main()