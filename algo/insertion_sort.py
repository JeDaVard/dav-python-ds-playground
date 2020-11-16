from algo.swap import swap
from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def insertion_sort(list_to_sort):
    lst = list_to_sort

    for i in range(len(lst)):
        key = lst[i]

        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

    return lst


print(insertion_sort(list_to_sort0))
print(insertion_sort(list_to_sort1))
print(insertion_sort(list_to_sort2))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('insertion_sort(long_list_to_sort)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.insertion_sort import insertion_sort;'
                       'from algo.swap import swap'))
