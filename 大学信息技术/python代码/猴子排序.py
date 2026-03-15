import random
import time


def is_sorted(arr):
    # 检查数组是否已排序
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def monkey_sort(arr):
    attempts = 0
    start_time = time.time()

    while not is_sorted(arr):
        random.shuffle(arr)  # 随机打乱列表
        attempts += 1  # 尝试数+1
        print(f'第{attempts}次：' + str(arr))

    end_time = time.time()
    elapsed_time = end_time - start_time  # 耗时

    return arr, attempts, elapsed_time


if __name__ == "__main__":
    # 生成一个随机数组，作为排序的输入
    input_array = [random.randint(1, 100) for _ in range(9)]

    sorted_array, attempts, elapsed_time = monkey_sort(input_array)

    print("原始数组:", input_array)
    print("排序后的数组:", sorted_array)
    print("排序尝试次数:", attempts)
    print("排序耗时（秒）:", elapsed_time)
