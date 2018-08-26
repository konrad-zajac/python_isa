import unittest
import is_div_357
import ttto
import seasons
import temp_conv_fc

class TestDay3(unittest.TestCase):

    def setUp(self):
        print('---su---')

    def tearDown(self):
        print('---td---')

    def test_357_ok(self):
        print('test case #1a OK is_div_357(105) == True')
        self.assertTrue(is_div_357.div_357(105))
        print('test case #1b OK b is_div_357(210) == True')
        self.assertTrue(is_div_357.div_357(210))
        print('test case #1c OK c is_div_357(315) == True')
        self.assertTrue(is_div_357.div_357(315))

    def test_357_nok(self):
        print('test case #1a N_OK is_div_357(10) == False')
        self.assertFalse(is_div_357.div_357(10))
        print('test case #1b N_OK is_div_357(10) == False')
        self.assertFalse(is_div_357.div_357(21))
        print('test case #1c N_OK is_div_357(\'a\') == False')
        self.assertRaises(ValueError, is_div_357.div_357, 'a')

    def test_ttto_ok(self):
        print('test case #3a OK ttto(\'xoooxooox\') == x wins diagonally')
        self.assertEqual(ttto.ttto('xoooxooox'), 'x wins - diagonally' )
        print('test case #3b OK ttto(\'oxxxoxxxo\') == o wins diagonally')
        self.assertEqual(ttto.ttto('oxxxoxxxo'), 'o wins - diagonally' )
        print('test case #3b OK ttto(\'oxxxoxxxn\') == the house wins')
        self.assertEqual(ttto.ttto('oxxxoxxxn'), 'the house wins' )

    def test_ttto_nok(self):
        print('test case #3d N_OK ttto(\'a\') == Raises ValueEror')
        self.assertRaises(ValueError, ttto.ttto, 'a')

    def test_season_ok(self):
        print('test case #4a OK seasons(1,1) == Season is winter')
        self.assertTrue(seasons.seasons(1,1))
        print('test case #4b OK seasons(5,1) == Season is spring')
        self.assertTrue(seasons.seasons(5,1))
        print('test case #4c OK seasons(8,1) == Season is summer')
        self.assertTrue(seasons.seasons(8,1))
        print('test case #4d OK seasons(11,1) == Season is autumn')
        self.assertTrue(seasons.seasons(11,1))

   
    def test_season_nok(self):
        print('test case #4e N_OK season(\'a\',\'c\') == Raises ValueEror')
        self.assertRaises(ValueError, seasons.seasons, 'a','c')

    def test_temp_ok(self):
        self.assertIn(temp_conv_fc.temp_conv_fc('32F'), '0C')

    def test_temp_nok(self):
        self.assertRaises(ValueError, temp_conv_fc.temp_conv_fc, 'a')


if __name__ == '__main__':
    unittest.main()

