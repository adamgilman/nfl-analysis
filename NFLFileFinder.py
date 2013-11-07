from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup as bs4

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

	def getNFLMatchups(self, path):
		results = []
		f = open(path, 'r')
		data = f.read()
		soup = bs4(data)
		grid = soup.findAll("td", {'class' : 'viCellBg1 cellTextNorm cellBorderL1', 'width':158})
		for g in grid:
			teams = g.findAll("a", {'class' : 'tabletext'})
			match = {}
			match['away'] = teams[0].text
			match['home'] = teams[1].text
			results.append(match)
		return results











	