from countingsort import counting_sort
from bcissort import bcis_sort
import time
import tracemalloc

name = ["sorted_", "random_", "reversed_"]
ukuran = ["kecil", "sedang", "besar"]

# Untuk waktu
for i in range(3):
    for j in range(3):
        filename = name[i] + ukuran[j]
        dataset = []

        with open(f"{filename}.txt", "r") as f:
            for data in f:
                dataset.append(int(data.strip()))
        
        start_counting = time.time() * 1000
        counting_sort(dataset)
        end_counting = time.time() * 1000

        start_bcis = time.time() * 1000
        bcis_sort(dataset, 0, len(dataset)-1)
        end_bcis = time.time() * 1000

        # Time Calculate
        time_counting = end_counting - start_counting
        time_bcis = end_bcis - start_bcis

        print(f"Dataset {filename}")
        print("Waktu counting adalah:", time_counting, "ms")
        print("Waktu bcis adalah:", time_bcis, "ms")
        print("")

# Untuk memori
for i in range(3):
    for j in range(3):
        filename = name[i] + ukuran[j]
        dataset = []

        with open(f"{filename}.txt", "r") as f:
            for data in f:
                dataset.append(int(data.strip()))
        
        tracemalloc.start()
        counting_sort(dataset)
        c_m = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tracemalloc.start()
        bcis_sort(dataset, 0, len(dataset)-1)
        b_m = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Dataset {filename}")
        print("Memori counting adalah:", c_m[1], "block")
        print("Memori bcis adalah:", b_m[1], "block")
        print("")