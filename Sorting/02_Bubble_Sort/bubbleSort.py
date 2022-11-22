def bubbleSort(lst):
    length_of_list = len(lst)
    for i in range(0, length_of_list - 2):
        flag = 0
        for j in range(0, length_of_list - i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return


if __name__ == '__main__':
    unsorted_list = [2, 7, 4, 1, 5, 3]
    print('unsorted list is: {}'.format(unsorted_list))
    bubbleSort(unsorted_list)
    print('sorted list is: {}'.format(unsorted_list))
