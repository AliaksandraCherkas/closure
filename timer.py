from datetime import datetime
from time import perf_counter, sleep
def timer():
    # start  = datetime.now()
    start = perf_counter()
    def inner():
        # return datetime.now() - start
        return perf_counter() - start
    return inner

t1 = timer()
sleep(1)
print(round(t1(),2))
sleep(2)
print(t1())