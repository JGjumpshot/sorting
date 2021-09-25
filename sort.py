import random
import time

SEED_VALUE = int(100 * random.random())
lyst = random.sample(range(1000000), k=SEED_VALUE)
selection_copy = lyst.copy()
insertion_copy = lyst.copy()
merge_copy = lyst.copy()
quick_copy = lyst.copy()
tim_copy = lyst.copy()

def is_sorted(my_list):
    """Is the list sorted?"""
    if type(my_list).__name__ == 'list':
        for i in range(len(my_list) - 1):
            if type(my_list[i]).__name__ == 'int' and my_list[i] < my_list[i+1]:
                continue
            else:
                return False
        return True
    else:
        return False


def selection_sort(my_list):
    """Sorting by selection"""
    for i in range(len(my_list)):
        select_min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[select_min]:
                select_min = j
        if select_min != i:
            my_list[i], my_list[select_min] = my_list[select_min], my_list[i]
    return my_list


def insertion_sort(my_list):
    """Sorting by insertion"""
    for i in range(1, len(my_list)):
        j = i
        while j >= 1 and my_list[j - 1] > my_list[j]:
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            j = j - 1
    return my_list


def mergesort(my_list):
    """Sorting by breaking down and combining things into a new list"""
    try:
        middle = len(my_list) // 2 - 1
        split_left = my_list[:middle + 1]
        split_right = my_list[middle + 1:]
        if len(my_list) > 1:
            list_a = mergesort(split_left)
            list_b = mergesort(split_right)
            a_test = 0
            b_test = 0
            new_list = []
            while b_test < len(list_b) and a_test < len(list_a):
                if list_a[a_test] > list_b[b_test]:
                    new_list.append(list_b[b_test])
                    b_test += 1
                elif list_a[a_test] <= list_b[b_test]:
                    new_list.append(list_a[a_test])
                    a_test += 1
            while a_test < len(list_a):
                new_list.append(list_a[a_test])
                a_test += 1
            while b_test < len(list_b):
                new_list.append(list_b[b_test])
                b_test += 1
            return new_list
        else:
            return my_list
    except:
        return False


def quicksort(lyst):
    """Quick sorting by picking a pivot point and appending lower values than pivot to lower array and greater values to greater array"""
    length = len(lyst)
    if length <= 1:
        return lyst
    else:
        pivot = lyst.pop()
    items_greater = []
    items_lower = []

    for item in lyst:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

def stopwatch(function, my_list, target):
    """stopwatch function"""
    start = time.perf_counter()
    function(my_list, target)
    stop = time.perf_counter()
    print(f"tarting {function.__name__}\n  {function.__name__} duration: {stop - start}")

def main():
    """Main function"""
    if is_sorted(lyst) == True:

    
if __name__ == "__main__":
    main()
