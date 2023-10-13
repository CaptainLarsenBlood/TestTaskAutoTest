import time


def assert_equal_time(val1, val2, time_wait, and_wait=0.5):
    start = time.time()
    stop = start + time_wait

    while time.time() < stop:
        if val1 == val2:
            return True
        else:
            time.sleep(and_wait)

    return False
