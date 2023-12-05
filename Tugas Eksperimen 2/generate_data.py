import random

def buatData(vertex, filename):
    check = 0

    adjList = [[] for i in range(vertex)]

    for i in range(vertex):
        if i == 0:
            awal = 1
        else:
            awal = 0
        
        edge = []
        j = random.randint(awal, 15)
        for k in range(j):
            check += 1
            edge.append(check)

            if check >= vertex - 1:
                break
        
        adjList[i] = edge

        if check >= vertex - 1:
            break

    idx = 0

    file = open(f"input\data_{filename}.txt", "w+")
    for i in adjList:
        file.write(str(idx) + " ")
        for j in i:
            file.write(str(j) + " ")
        file.write("\n")
        idx += 1
    file.close()

if __name__ == "__main__":

    size_data = [[10000, "kecil_dp"], [100000, "sedang_dp"], [1000000, "besar_dp"]]

    for size in size_data:
        buatData(size[0], size[1])

    print("Generating data is completed")