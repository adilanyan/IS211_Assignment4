#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def binary_search_iterative(a_list, item):
    start_time = time.time()
    merged_list = reduce(lambda x, y: x+y, a_list)
    merged_list.sort()
    first = 0
    last = len(merged_list)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if merged_list[midpoint] == item:
            found = True
        else:
            if item < merged_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    end_time = time.time()
    exec_time = end_time - start_time
    result = [found, '{:f}'.format(exec_time)]
    return result


def binary_search_recursive(arr, item):
    start_time = time.time()
    merged_list = reduce(lambda x, y: x + y, arr)
    merged_list.sort()

    def binary_search(item, first, last, merged_list):
        if last < first:
            return False
        if last == first:
            return merged_list[last] == item
        mid = (first + last) // 2
        if merged_list[mid] > item:
            last = mid
            return binary_search(item, first, last, merged_list)
        elif arr[mid] < item:
            first = mid + 1
            return binary_search(item, first, last, merged_list)
        else:
            return merged_list[mid] == item
    end_time = time.time()
    exec_time = end_time - start_time
    return [binary_search(item, 0, len(merged_list) - 1, merged_list), '{:f}'.format(exec_time)]


def python_search():
    sequential_search_execution_time = sequential_search(generate_lists(), -1)
    ordered_sequential_search_exec_time = ordered_sequential_search(generate_lists(), -1)
    binary_search_exec_time = binary_search_iterative(generate_lists(), -1)
    binary_search_recursive_exec_time = binary_search_recursive(generate_lists(), -1)

    def math():
        result = (float(sequential_search_execution_time[1]) +
                  float(ordered_sequential_search_exec_time[1]) +
                  float(binary_search_exec_time[1]) +
                  float(binary_search_recursive_exec_time[1])
                  )
        sequential = float(sequential_search_execution_time[1])*100/result
        ordered = float(ordered_sequential_search_exec_time[1])*100/result
        binary_iterative = float(binary_search_exec_time[1])*100/result
        binary_recursive = float(binary_search_recursive_exec_time[1])*100/result

        print("Sequential Search took %{} seconds to run, on average".format(round(sequential, 2)))
        print("Ordered Search took %{} seconds to run, on average".format(round(ordered, 2)))
        print("Binary iterative Search took %{} seconds to run, on average".format(round(binary_iterative, 2)))
        print("Binary recursive Search took %{} seconds to run, on average".format(round(binary_recursive, 2)))

    math()
    
python_search()

