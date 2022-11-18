def selectionSort(lst):
    for i in range(len(lst) - 1):
        imin = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[imin]:
                imin = j
        temp = lst[i]
        lst[i] = lst[imin]
        lst[imin] = temp
    return


if __name__ == '__main__':
    unsorted_list = [2, 7, 4, 1, 5, 3]
    print('unsorted list is: {}'.format(unsorted_list))
    selectionSort(unsorted_list)
    print('sorted list is: {}'.format(unsorted_list))
