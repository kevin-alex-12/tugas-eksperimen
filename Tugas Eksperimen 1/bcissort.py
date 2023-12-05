def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def is_equal(arr, sl, sr):
    for k in range(sl + 1, sr):
        if(arr[k] != arr[sl]):
            swap(arr, k, sl)
            return k
    return -1

def ins_right(arr, cur_item, sr, right):
    j = sr
    while(j <= right and cur_item > arr[j]):
        arr[j - 1] = arr[j]
        j += 1
    arr[j - 1] = cur_item

def ins_left(arr, cur_item, sl, left):
    j = sl
    while(j >= left and cur_item < arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = cur_item

def bcis_sort(input, left, right):
    sl = left
    sr = right

    while(sl < sr):
        swap(input, sr, sl + ((sr - sl)//2))

        if(input[sl] == input[sr]):
            if(is_equal(input, sl, sr) == -1):
                return None
        
        if(input[sl] > input[sr]):
            swap(input, sl, sr)

        if(sl - sr >= 100):
            for i in range((sl + 1), ((sr - sl)**0.5) + 1):
                if(input[sr] < input[i]):
                    swap(input, sr, i)
                elif(input[sl] > input[i]):
                    swap(input, sl, i)
        else:
            i = sl + 1

        lc = input[sl]
        rc = input[sr]

        while(i < sr):
            cur_item = input[i]

            if(cur_item >= rc):
                input[i] = input[sr - 1]
                ins_right(input, cur_item, sr, right)
                sr = sr - 1

            elif(cur_item <= lc):
                input[i] = input[sl + 1]
                ins_left(input, cur_item, sl, left)
                sl += 1
                i += 1
            else:
                i += 1
        sl += 1
        sr -= 1