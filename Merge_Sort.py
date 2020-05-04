from random import randint


# Merge Sort:

# This divide and conquer algorithm splits a list in half, and keeps splitting the list by 2 until it only has singular elements.
# Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well.
# This process continues until we get a sorted list with all the elements of the unsorted input list.

#
def create_array(min = -100, max = 50, size = 10):
    return [randint(min,max) for _ in range(size)]

def Merge_part(left_item_list, right_item_list):
    Sorted_items = []  # Create an empty list for sorted items
    left_item_index, right_item_index = 0, 0  # Initially set the index of lists to "0"

    # initialize condition for While loop until we get the list items split to single items

    # until this condition is false the iteration continues
    while left_item_index < len(left_item_list) and right_item_index < len(right_item_list):
        # checking if the value in the left list item is less than the right list item
        if left_item_list[left_item_index] < right_item_list[right_item_index]:
            # appending the less value to the sorted list
            Sorted_items.append(left_item_list[left_item_index])
            # Incrementing the value with 1
            left_item_index += 1
        else:
            # appending the less value to the sorted list
            Sorted_items.append(right_item_list[right_item_index])
            # Incrementing the value with 1
            right_item_index += 1

    # if after iteration last value remains in any list
    if left_item_index == len(left_item_list):
        # Extend the value to right list
        Sorted_items.extend(right_item_list[right_item_index:])
    else:
        # extend the values to left list
        Sorted_items.extend(left_item_list[left_item_index:])
    return Sorted_items


def Merge_sort(item_list):
    # the list has 0 or 1 element/item
    if len(item_list) <= 1:
        return item_list
    left, right = Merge_sort(item_list[:len(item_list) // 2]), Merge_sort(item_list[len(item_list) // 2:])
    return Merge_part(left, right)


if __name__ == "__Main__":
    Merge_sort()

# list1 = [randint(-100, 100) for _ in range(0, 5)]
list1 = create_array()
print("list1 : {}".format(list1))
# list2 = [randint(-100, 100) for _ in range(0, 10)]
# print("list2 : {}".format(list2))
# list3 = (list1 + list2)
print("Final List: {}".format(Merge_sort(list1)))
# print(Merge_part(list1, list2))
# print(Merge_part(list2))s
# print(Merge_part(list1))
