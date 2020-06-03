def quick_sort(unsorted):
    size = len(unsorted)
    if size <= 1:
        return unsorted

    mid_idx = size//2+size%2

    mid = unsorted[mid_idx]
    left,right = [], []
    unsorted.remove(mid)
    for num in unsorted:
        if num > mid:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [mid] + quick_sort(right)
if __name__ == '__main__':
    
    unsort_array = [1,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    print(quick_sort(unsort_array))
'''
    Output:
    [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]
'''