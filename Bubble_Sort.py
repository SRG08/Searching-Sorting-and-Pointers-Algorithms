# Bubble Sort - Compare and swapping two elements like small soap bubbles and hence the name given as bubble sort.

# This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list, and the smaller elements stay at the "bottom".

def bubble(list_item):
    index_len = len(list_item) - 1
    sorted_list = False

    while not sorted_list:
        sorted_list = True
        for i in range(0, index_len):
            if list_item[i] > list_item[i + 1]:
                sorted_list = False
                list_item[i], list_item[i + 1] = list_item[i + 1], list_item[i]
    return list_item

if __name__ == '__Main__':
    bubble()

list1 = [2, 4, 5, 45, 3, 88, 99, 64, 47, 6, 89, 34, 65, 23, 65, 87, 39, 49, 78, 96]
list2 = [4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6, 100]
list3 = (list1 + list2)
print(bubble(list3))
print(bubble(list2))
print(bubble(list1))

