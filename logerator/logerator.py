import logging
import inspect
import re
import jsonpickle
import os
import datetime
from logentries import LogentriesHandler

def time_write(f):
    def wrapper(*args, **kwargs):
        print ('I am executing {} at {}'.format(f.__name__, datetime.datetime.now()))
        rslt = f(*args, **kwargs)
        return rslt
    return wrapper
'''
A decorator that logs before and after event information to a Logentries
log.

:param f: the function being wrapped by the decorator
'''

def before_and_after(f):
    def wrapper(*args, **kwargs):
        #Set up the logger
        log = logging.getLogger('logentries')
        log.setLevel(logging.INFO)
        #Get the token for the log
        log.addHandler(LogentriesHandler(os.environ['LOGENTRIES_TOKEN']))

        #build the before event data object that we'll log
        data = {}
        data['event'] = 'before'
        data['function'] = f.__name__
        data['filename'] = inspect.getsourcefile(f)

        line_num = get_function_line_number(data['function'], data['filename'])
        data['line_number'] = line_num

        data['args'] = args
        data['kwarg'] = kwargs

        #Deserialize the data object and log it
        log.info(jsonpickle.encode(data))
        if(os.environ['PRINT_BEFORE_AND_AFTER']):
            print(jsonpickle.encode(data))

        #Call the method that is being decorated
        rslt = f(*args, **kwargs)

        #Add the after event data
        data['event'] = 'after'
        data['result'] = rslt

        # Deserialize the data object and log it
        log.info(jsonpickle.encode(data))
        if (os.environ['PRINT_BEFORE_AND_AFTER']):
            print(jsonpickle.encode(data))
        #return the result of the decorated function
        return rslt
    return wrapper


def get_function_line_number(function_name, function_filespec):
    with open(function_filespec, 'r') as f:
        pattern = re.compile('\s*def\s* ' + function_name)

        for i, line in enumerate(f):
            if (pattern.match(line)):
                return i + 1




