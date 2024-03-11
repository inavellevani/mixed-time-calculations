import time
import random
import concurrent
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from Classes import Trapezoid, Rectangle, Square
from threading import Thread


def trapezoid_area(trap_data):
    sh_base, lng_base, height = trap_data
    trap = Trapezoid(sh_base, lng_base, height)
    trap.area_calculator()
    return trap.area


def rectangle_area(rec_data):
    length, width = rec_data
    rec = Rectangle(length, width)
    rec.area_calculator()
    return rec.area


def square_area(sq_data):
    side = sq_data
    sq = Square(side[0])
    sq.area_calculator()
    return sq.area


def calculate_areas_sequential(arr, function):
    start = time.perf_counter()

    for data in arr:
        function(data)

    finish = time.perf_counter()
    print(f"Execution time:{round(finish - start, 2)}")  # Return execution time


def threaded_execution(arr, num_threads, function):
    start = time.perf_counter()

    threads = []
    for data in arr:
        thread = Thread(target=function, args=(data,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'With Threads ({num_threads} threads): {round(finish - start, 2)} seconds')


def concurrent_futures(arr, function):
    start = time.perf_counter()

    with ProcessPoolExecutor(max_workers=5) as executor:
        with ThreadPoolExecutor(max_workers=20) as threads:
            future_to_thread = {executor.submit(function, data): data for data in arr}
            for future in concurrent.futures.as_completed(future_to_thread):
                trap_data = future_to_thread[future]
                area = future.result()

    finish = time.perf_counter()
    print(f'With Concurrent Futures (5 processes, 20 threads each): {round(finish - start, 2)} seconds')


def calculator(arr, function):
    calculate_areas_sequential(arr.copy(), function)
    threaded_execution(arr.copy(), 100, function)
    concurrent_futures(arr.copy(), function)


def main():
    tr_arr = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for _ in range(100000)]
    rc_arr = [[random.randint(1, 200), random.randint(1, 200)] for _ in range(100000)]
    sq_arr = [[random.randint(1, 200)] for _ in range(100000)]

    print("Results for Trapezoid:")
    calculator(tr_arr, trapezoid_area)
    print("Results for Rectangle:")
    calculator(rc_arr, rectangle_area)
    print("Results for Square:")
    calculator(sq_arr, square_area)


if __name__ == '__main__':
    main()


''' Best results:

Results for Trapezoid:
Regular execution time:0.02
With Threads: 6.45 seconds
With Concurrent Futures: 40.32 seconds

Results for Rectangle:
Regular execution time:0.03
With Threads: 6.4 seconds
With Concurrent Futures: 40.48 seconds

Results for Square:
Regular execution time:0.04
With Threads: 6.36 seconds
With Concurrent Futures: 40.59 seconds


'''