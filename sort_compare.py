import time
import random

def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    begin = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
    end = time.time()

def shell_sort(a_list):
    begin = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        print("After increments of size", sublist_count, "The list is", a_list)

        sublist_count = sublist_count // 2

def gap_insertion_sort (a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    return sorted(a_list)

if __name__ == "__main__":
# Insertion Sort Execution Time Averages
    total_time_insertion_sort500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = insertion_sort(mylist)
        time_spent = time.time() - start
        total_time_insertion_sort500 += time_spent
    avg_time = total_time_insertion_sort500 / 100
    print(f"Insertion Sort with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_insertion_sort1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = insertion_sort(mylist)
        time_spent = time.time() - start
        total_time_insertion_sort1000 += time_spent
    avg_time = total_time_insertion_sort1000 / 100
    print(f"Insertion Sort with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_insertion_sort5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = insertion_sort(mylist)
        time_spent = time.time() - start
        total_time_insertion_sort5000 += time_spent
    avg_time = total_time_insertion_sort1000 / 100
    print(f"Insertion Sort with 5000 elements took {avg_time:10.7f} seconds to run, on average")


# Shell Sort Execution Time Averages
    total_time_shell_sort500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = shell_sort(mylist)
        time_spent = time.time() - start
        total_time_shell_sort500 += time_spent
    avg_time = total_time_shell_sort500 / 100
    print(f"Shell Sort with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_shell_sort1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = shell_sort(mylist)
        time_spent = time.time() - start
        total_time_shell_sort1000 += time_spent
    avg_time = total_time_shell_sort1000 / 100
    print(f"Shell Sort with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_shell_sort5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = shell_sort(mylist)
        time_spent = time.time() - start
        total_time_shell_sort5000 += time_spent
    avg_time = total_time_shell_sort1000 / 100
    print(f"Shell Sort with 5000 elements took {avg_time:10.7f} seconds to run, on average")


# Python Sort Execution Time Averages
    total_time_python_sort500 = 0
    for i in range(100):
        mylist = get_me_random_list(500)
        start = time.time()
        sorted_list = python_sort(mylist)
        time_spent = time.time() - start
        total_time_python_sort500 += time_spent
    avg_time = total_time_python_sort500 / 100
    print(f"Python Sort with 500 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_python_sort1000 = 0
    for i in range(100):
        mylist = get_me_random_list(1000)
        start = time.time()
        sorted_list = python_sort(mylist)
        time_spent = time.time() - start
        total_time_python_sort1000 += time_spent
    avg_time = total_time_python_sort1000 / 100
    print(f"Python Sort with 1000 elements took {avg_time:10.7f} seconds to run, on average")

    total_time_python_sort5000 = 0
    for i in range(100):
        mylist = get_me_random_list(5000)
        start = time.time()
        sorted_list = python_sort(mylist)
        time_spent = time.time() - start
        total_time_python_sort5000 += time_spent
    avg_time = total_time_python_sort5000 / 100
    print(f"Python Sort with 5000 elements took {avg_time:10.7f} seconds to run, on average")



# list_sizes = [500, 1000, 5000]
#    for the_size in list_sizes:
#        for i in range(100):
#            count = 0
#            mylist = get_me_random_list(the_size)
#            start = time.time()
#            sorted_list = python_sort(mylist)
#            time_spent = time.time() - start
#            total_time += time_spent
#        avg_time = total_time / the_size
#        print(f"Python Sort took {avg_time:10.7f} seconds to run, on average for {list_sizes}")
