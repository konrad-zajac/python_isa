import unittest
import tree_foo
import uncommon_list

class TestDay3(unittest.TestCase):

    def setUp(self):
        print('---su---')

    def tearDown(self):
        print('---td---')

    def test_tree_foo_nok(self):
        print('test case #d4_1a N_OK tree_foo(\'a\') == Raises ValueEror')
        self.assertRaises(ValueError, tree_foo.tree_foo, 'a')

    def test_tree_foo_ok(self):
        print('test case #d4_2b OK tree_foo(\'1\') ==\'+\' ')
        self.assertEqual(tree_foo.tree_foo(3), '  +  \n +++ \n+++++\n' )
        print('test case #d4_3b OK tree_foo(\'3\') ==\'  +  \n +++ \n+++++\n\' ')
        self.assertEqual(tree_foo.tree_foo(3), '  +  \n +++ \n+++++\n' )

    def test_uncommon_list_nok(self):
        print('test case #d4_2a N_OK uncommon_list(\'a\') == Raises ValueEror')
        self.assertRaises(ValueError, uncommon_list.uncommon_list, 'a')

    def test_uncommon_list_ok(self):
        print('test case #d4_2b OK uncommon_list([1,2,3]) == [1,2,3]')
        self.assertEqual( uncommon_list.uncommon_list([1,2,3]), [1, 2, 3])

    def test_uncommon_list_ok(self):
        print('test case #d4_2c OK uncommon_list([1,2,1]) == [2]')
        self.assertEqual( uncommon_list.uncommon_list([1,2,1]), [2])

    def test_uncommon_list_ok(self):
        print('test case #d4_2d OK uncommon_list([1,2,1,2) == []')
        self.assertEqual( uncommon_list.uncommon_list([1,2,1,2]), [])

    def test_uncommon_list_ok(self):
        print('test case #d4_2e OK uncommon_list([1,2,1,2,1,2) == [1,2] ')
        self.assertEqual(uncommon_list.uncommon_list([1,2,1,2,1,2]), [1,2])




if __name__ == '__main__':
    unittest.main()

