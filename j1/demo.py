import timeit
from time import perf_counter

lst1 = [x for x in range(100000)]
lst2 = [x for x in range(100000)]

def fct1(l):
    for i in range(10000):
        l.pop()

def fct2(l):
    for i in range(10000):
        l.pop(0)

# temps1 = timeit.repeat(
#     lambda: fct1(lst1),
#     number=1,
#     repeat=5
# )

# print("pop() : ", temps1)
# print("***********************")
# print(min(temps1))

# print("***********************")
# print("***********************")
# print("***********************")

# temps2 = timeit.repeat(
#     lambda: fct2(lst2),
#     number=1,
#     repeat=5
# )

# print("pop(0) : ", temps2)
# print("***********************")
# print(min(temps2))

lst1 = [x for x in range(100000)]
lst2 = [x for x in range(100000)]

# print("***********************************************")
# print("Chronometre avec perf_counter (ancien)")
# print("***********************************************")

# start = perf_counter()

# fct1(lst1)

# print("pop(), ", perf_counter() - start)

# start = perf_counter()

# fct2(lst2)

# print("pop(0), ", perf_counter() - start)

import tracemalloc

def fct3():
    for i in range(100):
        lst = [x for x in range(10000)]
        my_set = set(lst)
 
# tracemalloc.start()
# fct3()
# actuel, pic = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# Fonction reutilisable pour memoire
def get_memory(fct: function):
    tracemalloc.start()
    fct()
    actuel, pic = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return actuel, pic


actuel, pic = get_memory(fct3)
print(f"pic : {pic / 1024:.0f} Kio")
 
# print(f"pic : {pic / 1024:.0f} Kio")
