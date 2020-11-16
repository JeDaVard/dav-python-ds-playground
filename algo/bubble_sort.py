from algo.swap import swap
from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def bubble_sort(list_to_sort):
    lst = list_to_sort

    for i in range(len(lst)):
        for j in range(len(lst) - i):
            if j < len(lst) - 1 and lst[j] > lst[j + 1]:
                swap(j, j + 1, lst)

    return lst


print(bubble_sort(list_to_sort0))
print(bubble_sort(list_to_sort1))
print(bubble_sort(list_to_sort2))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('bubble_sort(long_list_to_sort)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.bubble_sort import bubble_sort;'
                       'from algo.swap import swap'))
