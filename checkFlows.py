import time
from threading import Thread
from datetime import datetime


def read_file(max_time: int, write_interval: int, original_file, new_file):
    """Copy the contents of a file and append it to a different file."""
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        with open(original_file) as hello:
            new_mad_lib = hello.read()

        with open(new_file, 'a') as new:
            new.write('Time: ' + str(datetime.utcnow()) + '\n' + new_mad_lib + '\n\n')
        print(new_mad_lib)
        time.sleep(write_interval)


test_num = int(input('How many files would you like to check?'))
for i in range(test_num):
    orig_file = input('Which file are you reading from?')
    dest_file = input('Which file are appending to?')
    timer = int(input('Enter the amount of seconds you want to run this: '))
    interval = int(input('Enter the seconds you would like between each write to the new file: '))
    t = Thread(target=read_file, args=(timer, interval, orig_file, dest_file,))
    t.start()
