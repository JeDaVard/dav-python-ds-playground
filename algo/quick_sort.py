from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def quick_sort(list_to_sort, start, end):
    lst = list_to_sort
    if start >= end:
        return

    p = partition(lst, start, end)
    quick_sort(lst, start, p-1)
    quick_sort(lst, p+1, end)

    return lst


def partition(lst, start, end):
    pivot = lst[start]
    low = start + 1
    high = end

    while True:
        while low <= high and lst[high] >= pivot:
            high = high - 1

        while low <= high and lst[low] <= pivot:
            low = low + 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
        else:
            break

    lst[start], lst[high] = lst[high], lst[start]

    return high


print(quick_sort(list_to_sort0, 0, len(list_to_sort0) - 1))
print(quick_sort(list_to_sort1, 0, len(list_to_sort1) - 1))
print(quick_sort(list_to_sort2, 0, len(list_to_sort2) - 1))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('quick_sort(long_list_to_sort, 0, len(long_list_to_sort) - 1)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.quick_sort import quick_sort;'
                       'from algo.swap import swap'))
