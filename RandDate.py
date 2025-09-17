import time
import random

def random_date(start, end):
    format = '%m/%d/%y'
    randomgen = random.random()
    start_time = time.mktime(time.strptime(start, format))
    end_time = time.mktime(time.strptime(end, format))
    random_time = start_time + randomgen * (end_time - start_time)
    random_date = time.strftime(format, time.localtime(random_time))
    return random_date
print("Random date between 1/1/20 and 1/1/22 is ", "\n", random_date("1/1/20", "1/1/22"), "\n")
