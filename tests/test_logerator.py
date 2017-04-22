from unittest import TestCase
from logerator import before_and_after
from .simple_class import SimpleClass

@before_and_after
def turn_to_upper(strng):
    return str(strng).upper()


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
        simple_function(1,2)

    def test_to_upper(self):
        turn_to_upper('some lower case data')

    def test_class(self):
        sc = SimpleClass('Bob', 'Reselman', 'Itchy', 'White Dog')
        sc.save()
