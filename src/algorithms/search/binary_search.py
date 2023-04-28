def binary_search(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    myList = [2, 4, 6, 8, 10, 11, 13, 15, 17]
    print(binary_search(myList, 15))
