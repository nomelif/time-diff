import select
import sys
import locale


class CliInput():
	DEFAULT_PRESET = "custom1"
	PRESETS = {"custom1":"%Y%m%d_%H%M%S", "linux1":"%b %d %H:%M:%S"}
	"""

Class used to parse command-line input.

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass