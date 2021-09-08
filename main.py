def get_firstOccurrence(l, x):
    l.sort()
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if x < l[mid]:
            right = mid - 1
        elif x > l[mid]:
            left = mid + 1
        elif l[mid] == x:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                right = mid - 1

    return -1


def get_lastOccurrence(l, x):
    l.sort()
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if x < l[mid]:
            right = mid - 1
        elif x > l[mid]:
            left = mid + 1
        elif l[mid] == x:
            if l[mid + 1] == len(l) or l[mid + 1] != l[mid]:
                return mid
            else:
                left = mid + 1

    return -1

def get_countOccurrence(l, x):
    first_occurrence = get_firstOccurrence(l,x)
    last_occurrence = get_lastOccurrence(l,x)
    if first_occurrence <= last_occurrence and first_occurrence >=0 and last_occurrence >= 0:
        return last_occurrence-first_occurrence+1
    else:
        return 0

if __name__ == '__main__':
    lst = [100,1000,30,20,50,10,120,20,30]
    print(get_countOccurrence(lst, 20))
