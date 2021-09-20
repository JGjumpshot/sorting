import random

SEED_VALUE = int(100 * random.random())
lyst = random.sample(range(1000000), k=SEED_VALUE)
print(lyst)
def selection_sort(my_list):
    for i in range(len(my_list)):
        select_min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[select_min]:
                select_min = j
        if select_min != i:
            my_list[i], my_list[select_min] = my_list[select_min], my_list[i]
    return my_list

def main():
    print(selection_sort(lyst))

if __name__ == "__main__":    
    main()

