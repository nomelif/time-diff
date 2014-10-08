import select
import sys
import locale


class CliInput():
	"""

Class used to parse command-line input. Currently holds presets for formatting options

	"""
	DEFAULT_PRESET = "custom1"
	"""
Default formatting if no options are given.
	"""
	PRESETS = {"custom1":"%Y%m%d_%H%M%S", "linux1":"%b %d %H:%M:%S"}
	"""

List of all possible formatting presets and their values.

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass