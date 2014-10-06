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
        self.assertEqual("         1 seconds", self.out.format_timedelta(datetime.timedelta(seconds=1)))
        self.assertEqual("       300 seconds", self.out.format_timedelta(datetime.timedelta(seconds=300)))
        self.assertEqual("     15001 seconds", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250)))
        # Milliseconds
        self.assertEqual("         1000 milliseconds", self.out.format_timedelta(datetime.timedelta(seconds=1), "ms"))
        self.assertEqual("       300000 milliseconds", self.out.format_timedelta(datetime.timedelta(seconds=300), "ms"))
        self.assertEqual("     15001000 milliseconds", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250), "ms"))
        # Minutes
        self.assertEqual("         0 minutes", self.out.format_timedelta(datetime.timedelta(seconds=1), "minutes"))
        self.assertEqual("         5 minutes", self.out.format_timedelta(datetime.timedelta(seconds=300), "minutes"))
        self.assertEqual("       250 minutes", self.out.format_timedelta(datetime.timedelta(seconds=1, minutes=250), "minutes"))
        #Hours
        self.assertEqual("         0 hours", self.out.format_timedelta(datetime.timedelta(seconds=1), "hours"))
        self.assertEqual("        12 hours", self.out.format_timedelta(datetime.timedelta(minutes=300), "hours"))
        
    def test_format_line(self):
        self.assertEqual("         1 seconds          2 seconds : c", self.out.format_line((datetime.timedelta(seconds=1), datetime.timedelta(seconds=2), "c")))
        self.assertEqual(None, self.out.format_line(("a")))

if __name__ == '__main__':
    unittest.main()