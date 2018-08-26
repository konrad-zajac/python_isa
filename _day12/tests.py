from unittest import TestCase

import calculator

import employee


class TestCalculator(TestCase):

    def setUp(self):
        self.values_set = [(2, 3), (3, 8)]
        self.return_add = [5, 11]
        self.return_multi = [6, 24]
        self.return_divide = [0.6666666666666666, 0.375]
        print('jesteśmy w setup')

    def tearDown(self):
        self.values_set = None
        self.return_add = None
        self.return_multi = None
        self.return_divide = None
        print('jestesmy w teardown')

    def test_add(self):
        for values, returns in zip(self.values_set, self.return_add):
            self.assertEqual(returns, calculator.add(values[0], values[1]))

    def test_multi(self):
        for values, returns in zip(self.values_set, self.return_multi):
            self.assertEqual(returns, calculator.multi(values[0], values[1]))

    def test_divide(self):
        for values, returns in zip(self.values_set, self.return_divide):
            self.assertAlmostEqual(returns, calculator.divide(values[0], values[1]))


class TestEmployee(TestCase):

    def setUp(self):
        self.emp_position = employee.Employee('wiktor', 'rutka', position='sensei')
        self.emp_no_position = employee.Employee('wiktor', 'rutka')

    def test_init_employee(self):
        self.assertEqual(self.emp_position._Employee__name, 'wiktor')
        self.assertEqual(self.emp_position._Employee__second_name, 'rutka')
        self.assertEqual(self.emp_position._Employee__position, 'sensei')

    def test_position(self):
        self.assertIsNotNone(self.emp_position._Employee__position)
        self.assertEqual(self.emp_position.position, self.emp_position._Employee__position)
        self.assertEqual(self.emp_position.position, 'sensei')

    def test_position_is_none(self):
        self.assertIsNone(self.emp_no_position._Employee__position)
        test_position = self.emp_no_position.position
        self.assertIsNone(test_position)

    def test_position_setter(self):
        self.assertIsNone(self.emp_no_position._Employee__position)
        self.emp_no_position.position = '123123123'
        self.assertIsNone(self.emp_no_position._Employee__position)
        self.emp_no_position.position = 'ubersensei'
        self.assertIsNotNone(self.emp_no_position._Employee__position)

    def test_employee_counter(self):
        self.assertEqual(self.emp_position.employee_counter, 2)
        del(self.emp_no_position)
        self.assertEqual(self.emp_position.employee_counter, 1)
        emp3 = employee.Employee('a', 'b')
        emp4 = employee.Employee('a', 'b')
        emp5 = employee.Employee('a', 'b')
        self.assertEqual(emp3.employee_counter, 4)
