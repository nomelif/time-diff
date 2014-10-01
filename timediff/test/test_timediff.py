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

import TimeDiff

class TestTimeDiff(unittest.TestCase):

    def setUp(self):
        self.d = TimeDiff.TimeDiff()
 
    def test_formatting_preset_short_existing(self):
        self.assertEqual("%Y%m%d_%H%M%S", self.d.set_formatting(["!", "-F=custom1"]))

    def test_bad_arg(self):
        self.assertEqual("Argument {0} not understood, only -p, -r, -h, --help, -l, --locale, -f, --format, -F and --format-preset are known, ignoring argument.".format("bad_data"), self.d.respond_to_wrong_parameters(["!", "bad_data"], platform.system(), True))

    def test_formatting_preset_long_existing(self):
        self.assertEqual("%Y%m%d_%H%M%S", self.d.set_formatting(["!", "--format-preset=custom1"]))

    def test_formatting_preset_short_wrong(self):
        self.assertEqual("%b %d %H:%M:%S", self.d.set_formatting(["!", "-F=diibadaabaduu"]))

    def test_formatting_preset_long_wrong(self):
        self.assertEqual("%b %d %H:%M:%S", self.d.set_formatting(["!", "--format-preset=diibadaabaduu"]))

    def test_formatting_short(self):
        self.assertEqual("input", self.d.set_formatting(["!", "-f=input"]))

    def test_formatting_long(self):
        self.assertEqual("input", self.d.set_formatting(["!", "--format=input"]))

    def test_formatting_no_args(self):
        self.assertEqual("%b %d %H:%M:%S", self.d.set_formatting(["!"]))

    def test_formatting_bad_args(self):
        self.assertEqual("%b %d %H:%M:%S", self.d.set_formatting(["!", "bad_data"]))

    def test_stdin_caching_non_tty(self):
    	input_data = ["a", "b", "c", "d"]
    	self.assertEqual(input_data, self.d.cache_input(input_data, ["!"], True))

    def test_stdin_caching_tty(self):
        input_data = ["a", "b", "c", "d"]
        self.assertEqual([], self.d.cache_input(input_data, ["!"]))

    def test_check_first_line_matches_positive(self):
        input_data = ["%", "b", "c", "d"]
        self.assertEqual(True, self.d.check_first_line_matches("%%", input_data))

    def test_check_first_line_matches_negative(self):
        input_data = ["a", "b", "c", "d"]
        self.assertEqual(False, self.d.check_first_line_matches("%%", input_data))

    def test_display_help_short(self):
        self.assertEqual(self.d.get_help_text(), self.d.display_help(["!", "-h"], platform.system(), True))

    def test_display_help_long(self):
        self.assertEqual(self.d.get_help_text(), self.d.display_help(["!", "--help"], platform.system(), True))

    def test_display_help_not_asked(self):
        self.assertEqual(False, self.d.display_help(["!"], platform.system(), True))

    def test_locale_none_given_unix(self):
        if platform.system() != "Windows":
            self.d.set_formatting(["!"])
            eng_locale = "en_US"
            self.assertEqual(eng_locale, locale.getlocale()[0])
        else:
            try:
                self.d.set_formatting(["!"], "Generic Unix OS", True)
                this.fail("Should throw exception!")
            except:
                pass

    def test_locale_none_given_windows(self):
        if platform.system() == "Windows":
            self.d.set_formatting(["!"])
            eng_locale = "en-US"
            self.assertEqual(eng_locale, locale.getlocale()[0])
        else:
            try:
                self.d.set_formatting(["!"], "Windows", True)
                this.fail("Should throw exception!")
            except:
                pass

    def test_locale_good_given_short(self):
        if platform.system() == "Windows":
            self.d.set_formatting(["!"], "-l=en-US")
            eng_locale = "en-US"
            self.assertEqual(eng_locale, locale.getlocale()[0])
        else:
            self.d.set_formatting(["!"], "-l=en_US")
            eng_locale = "en_US"
            self.assertEqual(eng_locale, locale.getlocale()[0])

    def test_locale_good_given_long(self):
        if platform.system() == "Windows":
            self.d.set_formatting(["!"], "--locale=en-US")
            eng_locale = "en-US"
            self.assertEqual(eng_locale, locale.getlocale()[0])
        else:
            self.d.set_formatting(["!"], "--locale=en_US")
            eng_locale = "en_US"
            self.assertEqual(eng_locale, locale.getlocale()[0])

    def test_parse_line(self):
        log = """Sep 30 09:29:54 zaphod kernel: [    5.862256] Bluetooth: RFCOMM TTY layer initialized
Sep 30 09:29:54 zaphod kernel: [    5.862263] Bluetooth: RFCOMM socket layer initialized
Sep 30 09:29:54 zaphod kernel: [    5.862265] Bluetooth: RFCOMM ver 1.11
Sep 30 09:29:56 zaphod kernel: [    7.474110] r8169 0000:02:00.0: eth0: link up
Sep 30 09:29:56 zaphod kernel: [    7.477213] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
Sep 30 09:29:58 zaphod rsyslogd-2177: imuxsock begins to drop messages from pid 2896 due to rate-limiting
Sep 30 09:30:03 zaphod rsyslogd-2177: imuxsock lost 56 messages from pid 2896 due to rate-limiting
Sep 30 09:34:54 zaphod rsyslogd: [origin software="rsyslogd" swVersion="5.8.11" x-pid="2049" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
Sep 30 09:34:54 zaphod rsyslogd: [origin software="rsyslogd" swVersion="5.8.11" x-pid="2049" x-info="http://www.rsyslog.com"] rsyslogd was HUPed"""
        log = log.split("\n")
        expected_output = """0:00:00 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    5.862256] Bluetooth: RFCOMM TTY layer initialized
0:00:00 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    5.862263] Bluetooth: RFCOMM socket layer initialized
0:00:00 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    5.862265] Bluetooth: RFCOMM ver 1.11
0:00:02 0:00:02 : Sep 30 09:29:56 zaphod kernel: [    7.474110] r8169 0000:02:00.0: eth0: link up
0:00:02 0:00:00 : Sep 30 09:29:56 zaphod kernel: [    7.477213] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
0:00:04 0:00:02 : Sep 30 09:29:58 zaphod rsyslogd-2177: imuxsock begins to drop messages from pid 2896 due to rate-limiting
0:00:09 0:00:05 : Sep 30 09:30:03 zaphod rsyslogd-2177: imuxsock lost 56 messages from pid 2896 due to rate-limiting
0:05:00 0:04:51 : Sep 30 09:34:54 zaphod rsyslogd: [origin software="rsyslogd" swVersion="5.8.11" x-pid="2049" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
0:05:00 0:00:00 : Sep 30 09:34:54 zaphod rsyslogd: [origin software="rsyslogd" swVersion="5.8.11" x-pid="2049" x-info="http://www.rsyslog.com"] rsyslogd was HUPed"""
        expected_output = expected_output.split("\n")
        i = 1
        try:
            self.d.first_time = time.strptime(log[0], "%b %d %H:%M:%S") # Time of first message as time.struct_time
        except ValueError, v:
            self.d.first_time = log[0].split(v.args[0][26:])[0]
            self.d.first_time = time.strptime(self.d.first_time, "%b %d %H:%M:%S")
        self.d.previous_time = self.d.first_time
        while i < len(log):
            line = self.d.parse_line(log[i], "%b %d %H:%M:%S")
            self.assertEqual(expected_output[i], line.strip("\n"))
            i = i + 1

    def test_parse_log(self):
        pass

    def test_check_add_zero_pads_negative(self):
        self.assertEqual(False, self.d.check_add_zero_pads(["!", "-p"]))

    def test_check_add_zero_pads_positive(self):
        self.assertEqual(True, self.d.check_add_zero_pads(["!"]))

    def test_check_remove_zero_pads_negative(self):
        self.assertEqual(True, self.d.check_remove_zero_pads(["!", "-r"]))

    def test_check_remove_zero_pads_positive(self):
        self.assertEqual(False, self.d.check_remove_zero_pads(["!"]))

    def test_remove_zero_pads_none(self):
        self.assertEqual("1 4 Tue", self.d.remove_zero_pads("1 4 Tue"))

    def test_remove_zero_pads_present(self):
        self.assertEqual("1 4 0 0 9007 Tue", self.d.remove_zero_pads("01 004 000 0 9007 Tue"))

if __name__ == '__main__':
    unittest.main()