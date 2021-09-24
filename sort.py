import random

SEED_VALUE = int(100 * random.random())
lyst = random.sample(range(1000000), k=SEED_VALUE)

def selection_sort(my_list):
    for i in range(len(my_list)):
        select_min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[select_min]:
                select_min = j
        if select_min != i:
            my_list[i], my_list[select_min] = my_list[select_min], my_list[i]
    return my_list


def insertion_sort(my_list):    
    for i in range(1, len(my_list)):
        j = i
        while j >= 1 and my_list[j - 1] > my_list[j]:
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            j = j - 1
    return my_list

def is_sorted(my_list):
    if type(my_list).__name__ == 'list':
        for i in range(len(my_list) - 1):
            if type(my_list[i]).__name__ == 'int' and my_list[i] < my_list[i+1]:
                continue
            else:
                return False
        return True
    else:
        return False
def main():
    print(is_sorted(selection_sort(lyst)))
    print(is_sorted(insertion_sort(lyst)))


if __name__ == "__main__":
    main()
