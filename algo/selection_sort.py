from algo.swap import swap
from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def selection_sort(list_to_sort):
    lst = list_to_sort

    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if lst[i] > lst[min_index]:
            swap(i, min_index, lst)

    return lst


print(selection_sort(list_to_sort0))
print(selection_sort(list_to_sort1))
print(selection_sort(list_to_sort2))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('selection_sort(long_list_to_sort)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.selection_sort import selection_sort;'
                       'from algo.swap import swap'))
