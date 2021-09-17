#!/usr/bin/python3

from datetime import datetime
from multiprocessing import Process

def func1():
  print('func1: starting')
  for i in range(1000):
    xmla = i * 3453456
    print('func1: finishing')

def func2():
  print('func2: starting')
  for i in range(1000):

    xmla = i**2 * 345
    print(f'func2: finishing {xmla}')




def main():
    start_time = datetime.now()

    # allDomains = getDomain()

    print(f"The time as started at {start_time.strftime('%I:%M:%S')}...")

    for i in range(1000):
        func1()

    # func1()
    for i in range(1000):
        p1 = Process(target=func1)
        p1.start()
        # p2 = Process(target=func1)
        # p2.start()
        # p3 = Process(target=func1)
        # p3.start()
        p1.join()
        # p2.join()
        # p3.join()

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'The total time was {total_time}')


if __name__ == '__main__':
    main()
