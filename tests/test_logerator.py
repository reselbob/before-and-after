from unittest import TestCase
from logerator import before_and_after
from logerator import time_write
from .simple_class import SimpleClass

@before_and_after
def turn_to_upper(strng):
    return str(strng).upper()

@time_write
def simple_add(num_one, num_two):
    return num_one + num_two


@before_and_after
def simple_function(num_one, num_two, signature="bob"):
    rslt = num_one + num_two
    print ('The result is: ' + str(rslt))
    print (signature)
    return rslt

class TestLogerator(TestCase):
    def test_simple(self):
        self.assertTrue(1 == 1)

    def test_logerator(self):
        rslt = simple_function(1,2)
        self.assertTrue(rslt == 3)

    def test_to_upper(self):
        reslt = turn_to_upper('some lower case data')

    def test_class(self):
        sc = SimpleClass('Bob', 'Reselman', 'Itchy', 'White Dog')
        sc.save()

    def test_time_write(self):
        rslt = simple_add(10, 200)
        print ('The result of calling simple_add is {}'.format(rslt))
        self.assertTrue(rslt == 210)
