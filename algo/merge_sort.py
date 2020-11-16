from algo.swap import swap
from algo.unsorted_lists import list_to_sort0, list_to_sort1, list_to_sort2


def merge_sort(list_to_sort):
    lst = list_to_sort
    length = len(list_to_sort)

    if length == 1:
        return list_to_sort

    half = length // 2
    left = list_to_sort[:half]
    right = list_to_sort[half:]

    return merge(
        merge_sort(left),
        merge_sort(right)
    )


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


print(merge_sort(list_to_sort0))
print(merge_sort(list_to_sort1))
print(merge_sort(list_to_sort2))

if __name__ == '__main__':
    from timeit import timeit

    print(timeit('merge_sort(long_list_to_sort)', number=1000,
                 setup='from algo.unsorted_lists import long_list_to_sort;'
                       'from algo.merge_sort import merge_sort;'
                       'from algo.swap import swap'))
