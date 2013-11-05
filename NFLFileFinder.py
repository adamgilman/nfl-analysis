from os import listdir
from os.path import isfile, join
from datetime import date
import pytz

class FileFinder(object):
	def __init__(self, testFileList=None, dirs=None):
		if (testFileList is None) and (dirs is None):
			raise AttributeError("Must include directory or testFileList")
		if (dirs is None) and (type(testFileList) is list):
			self.test = True
			self.fileList = testFileList
		else:
			self.fileList = [ f for f in listdir(self.dirs) if isfile(join(self.dirs,f)) ]
		self.weeks = self._setUpNFLSchedule()

	def _setUpNFLSchedule(self):
		return {
			'1'		:	{'start' : date(2013, 9, 5),	'end' : date(2013, 9, 9)},
			'2'		:	{'start' : date(2013, 9, 12),	'end' : date(2013, 9, 16)},
			'3'		:	{'start' : date(2013, 9, 19),	'end' : date(2013, 9, 23)},
			'4'		:	{'start' : date(2013, 9, 19),	'end' : date(2013, 9, 23)},
			'5'		:	{'start' : date(2013, 10, 3),	'end' : date(2013, 10, 7)},
			'6'		:	{'start' : date(2013, 10, 10),	'end' : date(2013, 10, 14)},
			'7'		:	{'start' : date(2013, 10, 17),	'end' : date(2013, 10, 21)},
			'8'		:	{'start' : date(2013, 10, 24),	'end' : date(2013, 10, 28)},
			'9'		:	{'start' : date(2013, 10, 31),	'end' : date(2013, 11, 04)},
			'10'	:	{'start' : date(2013, 11, 07),	'end' : date(2013, 11, 11)},
			'11'	:	{'start' : date(2013, 11, 14),	'end' : date(2013, 11, 18)},
			'12'	:	{'start' : date(2013, 11, 21),	'end' : date(2013, 11, 25)},
			'13'	:	{'start' : date(2013, 11, 28),	'end' : date(2013, 12, 2)},
			'14'	:	{'start' : date(2013, 12, 5),	'end' : date(2013, 12, 9)},
			'15'	:	{'start' : date(2013, 12, 12),	'end' : date(2013, 12, 16)},
			'16'	:	{'start' : date(2013, 12, 22),	'end' : date(2013, 12, 23)},
			'17'	:	{'start' : date(2013, 12, 29),	'end' : date(2013, 12, 29)},

		}

	def _convertEpochToDate(self, epoch):
		return date.fromtimestamp(epoch)

	def _convertDateToEpoch(self, pdate):
		return int((pdate - date(1970,1,1)).total_seconds())

	def _convertEpochToNFLWeek(self, epoch):
		for week, startend in self.weeks.iteritems():
			start = self._convertDateToEpoch( startend['start'] )
			end = self._convertDateToEpoch( startend['end'] )
			print epoch, week, start, end
			if (epoch > start) and (epoch < end):
				print week

		

	
	def getNFLSpreadFiles(self):
		results = []
		for f in self.fileList:
			if ("spread" in f) and (".dat" in f) and not ("offshore" in f):
				results.append(f)
		#print results
		return results












	