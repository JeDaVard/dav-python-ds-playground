from algo.swap import swap
from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def quick_sort(list_to_sort):
    lst = list_to_sort

    return lst


print(quick_sort(list_to_sort0))
print(quick_sort(list_to_sort1))
print(quick_sort(list_to_sort2))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('quick_sort(long_list_to_sort)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.quick_sort import quick_sort;'
                       'from algo.swap import swap'))
