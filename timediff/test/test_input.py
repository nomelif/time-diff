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

import cli_input

class TestCliInput(unittest.TestCase):

    def setUp(self):
        
        self.input = cli_input.CliInput()
        self.log = """Oct  3 09:31:14 zaphod kernel: [    6.091718] Bluetooth: SCO socket layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096223] Bluetooth: RFCOMM TTY layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096231] Bluetooth: RFCOMM socket layer initialized
Oct  3 09:31:14 zaphod kernel: [    6.096234] Bluetooth: RFCOMM ver 1.11
Oct  3 09:31:14 zaphod kernel: [    6.120631] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
Oct  3 09:31:14 zaphod kernel: [    6.120636] Bluetooth: BNEP filters: protocol multicast
Oct  3 09:31:16 zaphod kernel: [    7.559940] r8169 0000:02:00.0: eth0: link up
Oct  3 09:31:16 zaphod kernel: [    7.563020] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
Oct  3 09:31:18 zaphod rsyslogd-2177: imuxsock begins to drop messages from pid 2918 due to rate-limiting
Oct  3 09:31:23 zaphod rsyslogd-2177: imuxsock lost 56 messages from pid 2918 due to rate-limiting"""

    def test_get_params_dict(self):

        params_dict = self.input.get_params_dict(["-f=\"value for f\"", "-p", "-F"])
        self.assertEqual(params_dict["-f"], "\"value for f\"")
        self.assertEqual(params_dict["-p"], True)
        self.assertEqual(params_dict["-v"], False)
        self.assertEqual(params_dict["-F"], None)

    def test_match_arg(self):
        
        # Positive test, trivial case

        self.assertEqual(True, self.input.match_arg(["-b"], "-b"))

        # Positive test, complex case

        self.assertEqual(True, self.input.match_arg(["-a","-b=arg's_value"], "-b"))

        # Negative test, trivial case

        self.assertEqual(False, self.input.match_arg(["-b"], "-c"))

        # Negative test, complex case

        self.assertEqual(False, self.input.match_arg(["-a","-b=arg's_value"], "-c"))

    def test_get_get_log_arr(self):

        log_input = StringIO.StringIO(self.log)
        log_arr = self.input.get_log_arr(log_input)
        self.assertEqual(self.log.split("\n"), log_arr)

    def test_parse_args_dict(self):

        expected_out = {"err code":1, "err msg":"No input specified\n", "format":"%Y%m%d_%H%M%S", "proceed to parse":False}
        self.assertEqual(expected_out, self.input.parse_args_dict({"-h":False, "-F":None, "-f":None, "-l":None}))
        expected_out = {"err code":0, "err msg":"", "format":"%Y%m%d_%H%M%S", "proceed to parse":True}
        self.assertEqual(expected_out, self.input.parse_args_dict({"-h":False, "-F":None, "-f":None, "-l":None}, True))
        expected_out = {"err code":0, "err msg":"", "format":"test", "proceed to parse":True}
        self.assertEqual(expected_out, self.input.parse_args_dict({"-h":False, "-F":None, "-f":"test", "-l":None}, True))
        expected_out = {"err code":0, "err msg":"", "format":"%b %d %H:%M:%S", "proceed to parse":True}
        self.assertEqual(expected_out, self.input.parse_args_dict({"-h":False, "-F":"custom1", "-f":None, "-l":None}, True))
        expected_out = {"err code":0, "err msg":"", "format":"test", "proceed to parse":True}
        self.assertEqual(expected_out, self.input.parse_args_dict({"-h":False, "-F":"custom1", "-f":"test", "-l":None}, True))


if __name__ == '__main__':
    unittest.main()