






def Insertion_Sort(list_items):
    # Indexing_length = range(1, len(list_items))

    for i in range(1, len(list_items)):
        # list_sorted = list_items[i]
        while list_items[i - 1] > list_items[i] and i > 0:
            list_items[i - 1], list_items[i] = list_items[i], list_items[i - 1]
            i = i - 1
    return list_items


if __name__ == "__Main__":
    Insertion_Sort()

list1 = [2, 4, 5, 45, 3, 88, 99, 64, 47, 6, 89, 34, 65, 23, 65, -1, 39, 49, 78, 96]
list2 = [4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6, 100]
list3 = (list1 + list2)
print(Insertion_Sort(list3))
print(Insertion_Sort(list2))
print(Insertion_Sort(list1))
