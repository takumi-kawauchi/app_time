import time

def run_forward(object):
    print("オブジェクトに追加")
    object.set(time.perf_counter())

def get_result(start, finish):
    start_time = start.get()
    finish_time = finish.get()
    print(f"{finish_time-start_time:.2f}")
