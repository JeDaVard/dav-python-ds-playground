list1 = ['a'] * 999
list1.append('c')

list2 = ['b'] * 999
list2.append('c')


def has_common_a_multiply_b(l1, l2):
    for i in range(len(l1)):

        for j in range(len(l2)):

            if l1[i] == l2[j]:
                return True

    return False


def has_common_a_plus_b(l1, l2):
    dic = {}

    for i in range(len(l1)):
        dic[i] = True

    for j in range(len(l2)):
        if dic[j]:
            return True

    return False


if __name__ == '__main__':
    from timeit import timeit

    print(timeit('has_common_a_multiply_b(list1, list2)', number=1, setup='from __main__ import has_common_a_multiply_b, list1, list2'))
    print(timeit('has_common_a_plus_b(list1, list2)', number=1, setup='from __main__ import has_common_a_plus_b, list1, list2'))
