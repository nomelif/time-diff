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
        self.log2 = """20140929_103401 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"8\" ] -
20140929_103402 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"9\" ] -
20140929_103404 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"10\" ] -
20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 6.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK
20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 5.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK
20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 2.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK
20140929_103405 debug trix1221 AAA[4521]: [ sub=\"Tracker::select\" ] SELECTED @(12099)
20140929_113405 debug trix1221 AAA[4521]: [ sub=\"Tracker::send\" ] -
20140929_123405 warning trix1221 AAA[4521]: [ sub=\"Tracker::send\" reason=\"x\" ] 12099
20140929_133408 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT A\" ] -
20140929_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B" ] -
20140930_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B" ] -
20141001_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B" ] -
20141007_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B" ] -
20141007_143412 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B" ] -
"""
 
    def test_parse_logs_type_a(self):
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
        actual_output = self.parser.parse_logs(self.log.split("\n"), "%b %d %H:%M:%S")
        self.assertEqual(expected_output, actual_output)

    def test_parse_logs_type_b(self):
        expected_output = [
        (datetime.timedelta(seconds=0), datetime.timedelta(seconds=0), "20140929_103401 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"8\" ] -"),
        (datetime.timedelta(seconds=1), datetime.timedelta(seconds=1), "20140929_103402 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"9\" ] -"),
        (datetime.timedelta(seconds=3), datetime.timedelta(seconds=2), "20140929_103404 debug trix1221 AAA[4521]: [ sub=\"WebRequest::event\" bytes=\"787\" reason=\"WRITING DATA\" sock_fileno=\"10\" ] -"),
        (datetime.timedelta(seconds=3), datetime.timedelta(seconds=0), "20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 6.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK"),
        (datetime.timedelta(seconds=3), datetime.timedelta(seconds=0), "20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 5.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK"),
        (datetime.timedelta(seconds=3), datetime.timedelta(seconds=0), "20140929_103404 debug trix1221 AAA[4521]: [ sub=\"Tracker::ddd\" ] 1 RESPONSE 2.1411971819 response: HTTP/1.1 200 OK  Content-Type: text/plain;charset=ISO-8859-1  Content-Length: 2  Connection: close  Server: Jetty(9.1.z-SNAPSHOT)    OK"),
        (datetime.timedelta(seconds=4), datetime.timedelta(seconds=1), "20140929_103405 debug trix1221 AAA[4521]: [ sub=\"Tracker::select\" ] SELECTED @(12099)"),
        (datetime.timedelta(seconds=3604), datetime.timedelta(seconds=3600), "20140929_113405 debug trix1221 AAA[4521]: [ sub=\"Tracker::send\" ] -"),
        (datetime.timedelta(seconds=7204), datetime.timedelta(seconds=3600), "20140929_123405 warning trix1221 AAA[4521]: [ sub=\"Tracker::send\" reason=\"x\" ] 12099"),
        (datetime.timedelta(seconds=10807), datetime.timedelta(seconds=3603), "20140929_133408 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT A\" ] -"),
        (datetime.timedelta(seconds=14410), datetime.timedelta(seconds=3603), "20140929_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B\" ] -"),
        (datetime.timedelta(seconds=100810), datetime.timedelta(seconds=86400), "20140930_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B\" ] -"),
        (datetime.timedelta(seconds=187210), datetime.timedelta(seconds=86400), "20141001_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B\" ] -"),
        (datetime.timedelta(seconds=705610), datetime.timedelta(seconds=518400), "20141007_143411 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B\" ] -"),
        (datetime.timedelta(seconds=705611), datetime.timedelta(seconds=1), "20141007_143412 debug trix1221 AAA[5046]: [ sub=\"Tracker::db\" reason=\"COMMIT B\" ] -"),
        None
        ]
        actual_output = self.parser.parse_logs(self.log2.split("\n"), "%Y%m%d_%H%M%S")
        self.assertEqual(expected_output, actual_output)

    def test_parse_line(self):
    	self.parser = log_parser.LogParser()
    	secs = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 2), (2, 0), (4, 2), (9, 5)]
    	for times, line in zip(secs, self.log.split("\n")):
        	self.assertEqual((datetime.timedelta(seconds=times[0]), datetime.timedelta(seconds=times[1]), line), self.parser.parse_line(line, "%b %d %H:%M:%S"))
        self.assertEqual(None, self.parser.parse_line("!", "%b %d %H:%M:%S"))

if __name__ == '__main__':
    unittest.main()