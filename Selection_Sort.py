# Selection Sort Explanation:

# This algorithm segments the list into two parts: sorted and unsorted.
# We continuously remove the smallest element of the unsorted segment of the list and append it to the sorted segment.

# In practice, we don't need to create a new list for the sorted elements, what we do is treat the leftmost part of the list as the sorted segment. We then search the entire list for the smallest element, and swap it with the first element. Now we know that the first element of the list is sorted, we get the smallest element of the remaining items and swap it with the second element.This reiterates until the last item of the list is the remaining element to be examined.


def Selection_Sort(item_list):
    index_len = range(0, len(item_list) - 1)

    for i in index_len:
        min_value = i

        for j in (i + 1, len(index_len)):
            if item_list[j] < item_list[min_value]:
                min_value = j

        if min_value != i:
            item_list[min_value], item_list[i] = item_list[i], item_list[min_value]
    return item_list


if __name__ == "__Main__":
    Selection_Sort()

list1 = [2, 4, 5, 45, 3, 88, 99, 64, -5, 6, 89, 34, 65, 23, 65, -1, 39, 49, -6, 96]
list2 = [4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6, 100]
list3 = (list1 + list2)
print(Selection_Sort(list3))
print(Selection_Sort(list2))
print(Selection_Sort(list1))
