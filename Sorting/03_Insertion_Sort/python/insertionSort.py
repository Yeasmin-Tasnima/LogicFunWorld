def insertionSort(lst):
    length_of_list = len(lst)
    for i in range(1, length_of_list):
        value = lst[i]
        hole = i
        while hole > 0 and lst[hole - 1] > value:
            lst[hole] = lst[hole - 1]
            hole = hole - 1
        lst[hole] = value
    return


if __name__ == '__main__':
    unsorted_list = [2, 7, 4, 1, 5, 3]
    print('unsorted list is: {}'.format(unsorted_list))
    insertionSort(unsorted_list)
    print('sorted list is: {}'.format(unsorted_list))
