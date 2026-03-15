import random
import threading
import time


def sleep_sort(nums):
    sorted_array = []

    def sleep_and_append(num):
        time.sleep(num)
        sorted_array.append(num)

    # 记录开始时间
    start_time = time.time()

    threads = []
    for num in nums:
        thread = threading.Thread(target=sleep_and_append, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("排序后的数组:", sorted_array)
    # 计算时间差
    print("排序耗时（秒）:", time.time() - start_time)


if __name__ == "__main__":
    input_array = [random.randint(1, 10) for _ in range(5)]
    print("原始数组:", input_array)
    sleep_sort(input_array)
