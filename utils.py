import time as time_

class TimeUtils:

	@staticmethod
	def millis():
		return int(round(time_.time() * 1000))

