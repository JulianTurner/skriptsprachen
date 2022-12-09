"""
nice docs
"""
import os
from functools import wraps

def log_to_file(func):
    """
    logs functionname, and other useless stuff to file
    """
    @wraps(func)
    def log(*args):
        print(func.__name__, args)
        result = func(*args)
        log_file = './.logs/logfile.txt'
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, 'a', encoding='utf-8', ) as file:
            file.write(f'func:{func.__name__}, args:{args}, result:{result}\n')

        return result

    return log

@log_to_file
def add(a:int,b:int) -> int:
    return a + b

@log_to_file
def subtract(a:int,b:int) -> int:
    return a - b

@log_to_file
def multiply(a:int,b:int) -> int:
    return a * b

if __name__ == '__main__':
    print(add(2,4))
    print(subtract(4,2))
    print(multiply(3,7))
