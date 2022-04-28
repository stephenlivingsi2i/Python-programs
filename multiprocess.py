import multiprocessing
import threading
import time


def first_function():
    first_list = []
    for i in range(1, 10000):
        first_list.append(i)
    print("first list: {}\n\n".format(first_list))


def second_function():
    second_list = []
    for i in range(10000, 20000):
        second_list.append(i)
    print("second list: {} ".format(second_list))


def multiprocessing_using_thread():
    process_one = multiprocessing.Process(target=perform_thread)
    start_time = time.time()
    process_one.start()
    process_one.join()
    end_time = time.time()
    print("time taken..", end_time-start_time)


def perform_thread():
    first_thread = threading.Thread(target=first_function)
    second_thread = threading.Thread(target=second_function)
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()


if __name__ == "__main__":
    multiprocessing_using_thread()



