def counting_sort(input):
    maximum = max(input)
    count_arr = [0] * (maximum + 1)

    for i in input:
        count_arr[i] += 1
    
    for i in range(1, maximum + 1):
        count_arr[i] += count_arr[i - 1]
    
    output = [0] * len(input)

    for i in range(len(input) - 1, -1, -1):
        output[count_arr[input[i]] - 1] = input[i]
        count_arr[input[i]] -= 1
    
    return output