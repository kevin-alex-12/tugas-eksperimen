import random

def sorted_data(size, name):
    file = open(f"sorted_{name}.txt", "w+")
    for i in range(size):
        file.write(str(i) + "\n")
    file.close()

def random_data(size, name):
    file = open(f"random_{name}.txt", "w+")
    for i in range(size):
        file.write(str(random.randint(1, size)) + "\n")
    file.close()

def reversed_data(size, name):
    file = open(f"reversed_{name}.txt", "w+")
    for i in range(size-1, -1, -1):
        file.write(str(i) + "\n")
    file.close()

if __name__ == "__main__":

    size_data = [[500, "kecil"], [5000, "sedang"], [50000, "besar"]]

    for size in size_data:
        sorted_data(size[0], size[1])
        random_data(size[0], size[1])
        reversed_data(size[0], size[1])

    print("Generating data is completed")