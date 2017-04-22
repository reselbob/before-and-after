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

def before_and_after(f):
    def wrapper(*args, **kwargs):
        log = logging.getLogger('logentries')
        log.setLevel(logging.INFO)
        log.addHandler(LogentriesHandler(os.environ['LOGENTRIES_ID']))
        #log.addHandler(LogentriesHandler('441de05d-e9ed-4a03-b157-d72449f86b59'))

        data = {}
        data['event'] = 'before'
        data['function'] = f.__name__
        data['filename'] = inspect.getsourcefile(f)
        data['line_number'] = get_function_line_number(data['function'], data['filename'])

        data['args'] = args
        data['kwarg'] = kwargs

        log.info(jsonpickle.encode(data))
        print(jsonpickle.encode(data))

        rslt = f(*args, **kwargs)

        result = f(*args, **kwargs)
        data['event'] = 'after'
        data['result'] = result

        log.info(jsonpickle.encode(data))
        print(jsonpickle.encode(data))
        return rslt
    return wrapper


def get_function_line_number(function_name, function_filespec):
    f = open(function_filespec, 'r')
    pattern = re.compile('\s*def\s* ' + function_name)
    line_num = 0

    for line in f.readlines():
        line_num += 1
        if (pattern.match(line)):
            return line_num




