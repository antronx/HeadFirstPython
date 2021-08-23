from functools import wraps
import time

def execution_time(func):
    @wraps(func)
    def wrapper (*args, ** kwargs):
        time_before_millis = current_time_in_millis()
        foo = func(*args, **kwargs)
        time_after_millis = current_time_in_millis()
        print("Execution time in milliseconds: " + str(round(time_after_millis - time_before_millis)))
        return foo
    return wrapper
    


def current_time_in_millis() -> float:
    time_m = time.time()*1000
    return time_m

@execution_time
def foo():
    print("Boooyaa!!!")

foo()
