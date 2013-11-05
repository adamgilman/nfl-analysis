from os import listdir
from os.path import isfile, join
'''
self.fixtureFileList = [	'fetch_all.py',
										 'future_odds1379108571.dat',
										 'future_odds1380643263.dat',
										 'future_odds1380645046.dat',
										 'lists.py',
										 'lists.pyc',
										 'nflodds_money_11379108554.dat',
										 'nflodds_money_11379109625.dat',
										 'nflodds_money_11379111424.dat',
										 'nflodds_money_21380641440.dat',
										 'nflodds_money_21380643245.dat',
										 'nflodds_money_21380645040.dat',
										 'nflodds_spread_11379108532.dat',
										 'nflodds_spread_11379109602.dat',
										 'nflodds_spread_11379111401.dat',
										 'nflodds_spread_11379629802.dat',
										 'nflodds_spread_11379631602 copy.html',
										 'nflodds_spread_11379631602.dat',
										 'nflodds_spread_11380643202.dat',
										 'nflodds_spread_11380645001.dat',
										 'offshore_money_11379108548.dat',
										 'offshore_money_11379109620.dat',
										 'offshore_money_21380645035.dat',
										 'offshore_spread_11379108538.dat',
										 'offshore_spread_11379109609.dat',
										 'offshore_spread_11379111408.dat',
										 'offshore_spread_21380643224.dat',
										 'offshore_spread_21380645013.dat']
										 '''


class FileFinder(object):
	def __init__(self, testFileList=None, dirs=None):
		if (testFileList is None) and (dirs is None):
			raise AttributeError("Must include directory or testFileList")
		if (dirs is None) and (type(testFileList) is list):
			self.test = True
			self.fileList = testFileList
		else:
			self.fileList = [ f for f in listdir(self.dirs) if isfile(join(self.dirs,f)) ]
			
	
	def getNFLSpreadFiles(self):
		results = []
		for f in self.fileList:
			if ("spread" in f) and (".dat" in f) and not ("offshore" in f):
				results.append(f)
		#print results
		return results












	