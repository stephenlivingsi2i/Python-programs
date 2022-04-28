
def selection_sort(input_list):
    for i in range(1, len(input_list)):
        for j in range(0, i):
            if input_list[i] < input_list[j]:
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp
    return input_list


input_list = [19, 2, 31, 45, 6, 11, 121, 27]
print(selection_sort(input_list))
