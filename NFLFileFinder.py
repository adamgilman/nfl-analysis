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
		soup = bs4( open(path, 'r').read() )
		##grid = soup.find("td", {"class" : "viBodyBorderNorm"})
		### bigger table but, seemingly can get more specificity by color
		grid = soup.find("table", {"bgcolor" : "C48F1B"})
		#tr color:d6bd7b are rows with info, that I don't need so remove
		extraneous_rows = grid.findAll("tr", {"bgcolor" : "d6bd7b"})
		[row.extract() for row in extraneous_rows]
		game_rows = grid.findAll("tr")
		#note; the above game_rows have all betting information, helful for future stories
		for game in game_rows:
			dirty_teams = game.findAll("a", {"target":None})
			row = {'home' : dirty_teams[1].text, 'away' : dirty_teams[0].text}
			results.append(row)

		return results











	