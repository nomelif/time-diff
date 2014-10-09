import json
import sys
from pkg_resources import Requirement, resource_filename

class ConfReader():
	"""

Class used to parse command-line input. Currently holds presets for formatting options

	"""
	DEFAULT_PRESET = ""
	"""
Default formatting if no options are given.
	"""
	PRESETS = {}
	"""

List of all possible formatting presets and their values.

	"""
	VERSION = "1.0"
	"""

Current version of program.

	"""
	OUTPUT_FORMAT = ".png"
	def __init__(self):
		"""

Reads configuration file and 

		"""
		config = {"version":"1.0", "default-preset":"custom1", "image-out":".png", "presets":{"custom1":"%Y%m%d_%H%M%S", "linux1":"%b %d %H:%M:%S"}}
		try:
			with open("/etc/timediff/timediff.json", "r") as f:
				config = json.load(f)
		except IOError:
			sys.stderr.write("Error loading configuration file timediff.json.\n")
			sys.exit(1)
		self.DEFAULT_PRESET = config["default-preset"]
		self.PRESETS = config["presets"]
		if config["version"] == "1.0":
			self.OUTPUT_FORMAT = config["image-out"]
