import time


def check_flows(max_time: int, write_interval: int, original_file, new_file):
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        with open(original_file) as hello:
            new_mad_lib = hello.read()

        with open(new_file, 'a') as new:
            new.write('Time: ' + str(time.time()) + '\n' + new_mad_lib + '\n\n')
        print(new_mad_lib)
        time.sleep(write_interval)


orig_file = input('Which file are you reading from?')
dest_file = input('Which file are writing to?')
timer = int(input('Enter the amount of seconds you want to run this: '))
interval = int(input('Enter the seconds you would like between each write to the new file: '))
check_flows(timer, interval, orig_file, dest_file,)

