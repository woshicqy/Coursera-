def merge_sort(unsorted):
    size = len(unsorted)
    if size == 1:
        return unsorted
    middle = int(size/2 + size%2)

    a = unsorted[:middle]
    b = unsorted[middle:]

    a = merge_sort(a)
    b = merge_sort(b)


    ### process of merging the sorted list ###
    re = []
    while a != [] and b != []:
        # print('a:',a)
        # print('b:',b)
        if a[0] < b[0]:
            re.append(a[0])
            a.pop(0)
            # print('a_pop:',a)
        else:
            re.append(b[0])
            b.pop(0)
            # print('b_pop:',b)
    # print('-'*100)
    # print('a_now:',a)
    # print('b_now:',b)
    # print('1st re:',re)
    re += a
    # print('a + re:',re)
    re += b
    # print('b + re:',re)
    # print('re:',re)
    # print('One is done !')
    # print('='*100)
    return re

if __name__ == '__main__':
    # exit()
    a = [1,4,3,2,-10,4,56]
    sorted_list = merge_sort(a)
    print('result:',sorted_list)

