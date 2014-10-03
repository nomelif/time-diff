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

import log_parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = log_parser.LogParser()
        self.log = """Oct  3 09:31:14 zaphod kernel: [    6.091718] Bluetooth: SCO socket layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096223] Bluetooth: RFCOMM TTY layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096231] Bluetooth: RFCOMM socket layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096234] Bluetooth: RFCOMM ver 1.11
Oct  3 09:31:14 zaphod kernel: [    6.120631] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
Oct  3 09:31:14 zaphod kernel: [    6.120636] Bluetooth: BNEP filters: protocol multicast
Oct  3 09:31:16 zaphod kernel: [    7.559940] r8169 0000:02:00.0: eth0: link up
Oct  3 09:31:16 zaphod kernel: [    7.563020] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
Oct  3 09:31:18 zaphod rsyslogd-2177: imuxsock begins to drop messages from pid 2918 due to rate-limiting
Oct  3 09:31:23 zaphod rsyslogd-2177: imuxsock lost 56 messages from pid 2918 due to rate-limiting
!"""
 
    def test_parse_logs(self):
        expected_output = [
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.091718] Bluetooth: SCO socket layer initialized"),
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.096223] Bluetooth: RFCOMM TTY layer initialized"),
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.096231] Bluetooth: RFCOMM socket layer initialized"),
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.096234] Bluetooth: RFCOMM ver 1.11"),
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.120631] Bluetooth: BNEP (Ethernet Emulation) ver 1.3"),
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "Oct  3 09:31:14 zaphod kernel: [    6.120636] Bluetooth: BNEP filters: protocol multicast"),
        (datetime.timedelta(seconds=2), datetime.timedelta(seconds=2), "Oct  3 09:31:16 zaphod kernel: [    7.559940] r8169 0000:02:00.0: eth0: link up"),
        (datetime.timedelta(seconds=2), datetime.timedelta(seconds=0), "Oct  3 09:31:16 zaphod kernel: [    7.563020] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready"),
        (datetime.timedelta(seconds=4), datetime.timedelta(seconds=2), "Oct  3 09:31:18 zaphod rsyslogd-2177: imuxsock begins to drop messages from pid 2918 due to rate-limiting"),
        (datetime.timedelta(seconds=9), datetime.timedelta(seconds=5), "Oct  3 09:31:23 zaphod rsyslogd-2177: imuxsock lost 56 messages from pid 2918 due to rate-limiting"),
        None
        ]
        actual_output = self.parser.parse_logs(self.log.split("\n"), {"-p":False, "-v":False}, "%b %d %H:%M:%S")
        self.assertEqual(expected_output, actual_output)

    def test_parse_line(self):
    	self.parser = log_parser.LogParser()
    	secs = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 2), (2, 0), (4, 2), (9, 5)]
    	for times, line in zip(secs, self.log.split("\n")):
        	self.assertEqual((datetime.timedelta(seconds=times[0]), datetime.timedelta(seconds=times[1]), line), self.parser.parse_line(line, {"-p":False}, "%b %d %H:%M:%S"))
        self.assertEqual(None, self.parser.parse_line("!", {"-p":False}, "%b %d %H:%M:%S"))

if __name__ == '__main__':
    unittest.main()