
def bubble_sort(input_list):
    for i in range(len(input_list)-1, 0, -1):
        for j in range(i):
            if input_list[j] < input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
    return input_list


input_list = [19, 2, 31, 45, 6, 11, 121, 27]
print(bubble_sort(input_list))
