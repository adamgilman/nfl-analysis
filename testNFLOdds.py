import unittest
from NFLFileFinder import FileFinder

class TestFileIdentifier(unittest.TestCase):
	# find all files that contain the odds which we want to analyzea
    def setUp(self):
        self.fixtureFileList = ['fetch_all.py','future_odds1379108571.dat','future_odds1380643263.dat','future_odds1380645046.dat','lists.py','lists.pyc','nflodds_money_11379108554.dat','nflodds_money_11379109625.dat','nflodds_money_11379111424.dat','nflodds_money_21380641440.dat','nflodds_money_21380643245.dat','nflodds_money_21380645040.dat','nflodds_spread_11379108532.dat','nflodds_spread_11379109602.dat','nflodds_spread_11379111401.dat','nflodds_spread_11379629802.dat','nflodds_spread_11379631602 copy.html','nflodds_spread_11379631602.dat','nflodds_spread_11380643202.dat','nflodds_spread_11380645001.dat','offshore_money_11379108548.dat','offshore_money_11379109620.dat','offshore_money_21380645035.dat','offshore_spread_11379108538.dat','offshore_spread_11379109609.dat','offshore_spread_11379111408.dat','offshore_spread_21380643224.dat','offshore_spread_21380645013.dat']

	
    # [ ] find all files conatining the NFL Spreads 
    def testListAllNFLSpreadFiles(self):
        finder = FileFinder(testFileList = self.fixtureFileList)
		#should return a list of only spread file
        results = ['nflodds_spread_11379108532.dat', 'nflodds_spread_11379109602.dat', 'nflodds_spread_11379111401.dat', 'nflodds_spread_11379629802.dat', 'nflodds_spread_11379631602.dat', 'nflodds_spread_11380643202.dat', 'nflodds_spread_11380645001.dat']
        self.assertItemsEqual(finder.getNFLSpreadFiles(), results )

    def testFileFinderNeedsDirectoryOrTest(self):
		#finder needs either :dir or :testFileList
        self.assertRaises(AttributeError, FileFinder)



			#self.assertRaises(ExpectedException, afunction, arg1, arg2)



if __name__ == '__main__':
        unittest.main()