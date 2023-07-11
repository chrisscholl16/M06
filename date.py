import datetime
today = datetime.date.today()
file_ptr = open('today.txt', 'w')
file_ptr.write(str(today))
file_ptr.close()

file_ptr = open('today.txt', 'r')
today_date = file_ptr.read()
file_ptr.close()

today = datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print('Today is: ', today)


import multiprocessing
from datetime import datetime
import time
import random

def print_time():
    now = datetime.now()
    print("Today's date and time is: ",format(now))
    time.sleep(random.random())
    
if __name__ == '__main__':
    proc1 = multiprocessing.Process(target=print_time())
    proc2 = multiprocessing.Process(target=print_time())
    proc3 = multiprocessing.Process(target=print_time())
    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()
    
    print('Completed')