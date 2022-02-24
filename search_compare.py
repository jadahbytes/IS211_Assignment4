import time
import random

def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list,item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def ordered_sequential_search(a_list,item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

if __name__ == "__main__":
# Sequential Search Execution Time Averages
    total_time_sequential_search500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_sequential_search500 += time_spent
    avg_time = total_time_sequential_search500 / 100
    print(f"Sequential Search with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_sequential_search1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_sequential_search1000 += time_spent
    avg_time = total_time_sequential_search1000 / 100
    print(f"Sequential Search with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_sequential_search5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_sequential_search5000 += time_spent
    avg_time = total_time_sequential_search5000 / 100
    print(f"Sequential Search with 5000 elements took {avg_time:10.7f} seconds to run, on average")

    # Ordered Sequential Search Execution Time Averages
    total_time_ordered_sequential_search500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_ordered_sequential_search500 += time_spent
    avg_time = total_time_ordered_sequential_search500 / 100
    print(f"Ordered Sequential Search with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_ordered_sequential_search1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_ordered_sequential_search1000 += time_spent
    avg_time = total_time_ordered_sequential_search1000 / 100
    print(f"Ordered Sequential Search with 1000 elements took {avg_time:10.7f} seconds to run, on average")


    total_time_ordered_sequential_search5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time_ordered_sequential_search5000 += time_spent
    avg_time = total_time_ordered_sequential_search5000 / 100
    print(f"Ordered Sequential Search with 5000 elements took {avg_time:10.7f} seconds to run, on average")

    # Binary Search Iterative Execution Time Averages
    total_time_binary_search_iterative500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time_binary_search_iterative500 += time_spent
    avg_time = total_time_binary_search_iterative500 / 100
    print(f"Binary Search Iterative with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_binary_search_iterative1000= 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time_binary_search_iterative1000 += time_spent
    avg_time = total_time_binary_search_iterative1000 / 100
    print(f"Binary Search Iterative with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_binary_search_iterative5000= 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time_binary_search_iterative5000 += time_spent
    avg_time = total_time_binary_search_iterative5000 / 100
    print(f"Binary Search Iterative with 5000 elements took {avg_time:10.7f} seconds to run, on average")

    # Binary Search recursive Execution Time Averages
    total_time_binary_search_recursive500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = binary_search_recursive(mylist, 99999999)
        time_spent = time.time() - start
        total_time_binary_search_recursive500 += time_spent
    avg_time = total_time_binary_search_recursive500 / 100
    print(f"Binary Search Recursive with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_binary_search_recursive1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = binary_search_recursive(mylist, 99999999)
        time_spent = time.time() - start
        total_time_binary_search_recursive1000 += time_spent
    avg_time = total_time_binary_search_recursive1000 / 100
    print(f"Binary Search Recursive with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_binary_search_recursive5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = binary_search_recursive(mylist, -1)
        time_spent = time.time() - start
        total_time_binary_search_recursive5000 += time_spent
    avg_time = total_time_binary_search_recursive5000 / 100
    print(f"Binary Search Recursive with 5000 elements took {avg_time:10.7f} seconds to run, on average")
