# # # import timeit
# # # from time import perf_counter

# # # lst1 = [x for x in range(100000)]
# # # lst2 = [x for x in range(100000)]

# # # def fct1(l):
# # #     for i in range(10000):
# # #         l.pop()

# # # def fct2(l):
# # #     for i in range(10000):
# # #         l.pop(0)

# # # # temps1 = timeit.repeat(
# # # #     lambda: fct1(lst1),
# # # #     number=1,
# # # #     repeat=5
# # # # )

# # # # print("pop() : ", temps1)
# # # # print("***********************")
# # # # print(min(temps1))

# # # # print("***********************")
# # # # print("***********************")
# # # # print("***********************")

# # # # temps2 = timeit.repeat(
# # # #     lambda: fct2(lst2),
# # # #     number=1,
# # # #     repeat=5
# # # # )

# # # # print("pop(0) : ", temps2)
# # # # print("***********************")
# # # # print(min(temps2))

# # # lst1 = [x for x in range(100000)]
# # # lst2 = [x for x in range(100000)]

# # # # print("***********************************************")
# # # # print("Chronometre avec perf_counter (ancien)")
# # # # print("***********************************************")

# # # # start = perf_counter()

# # # # fct1(lst1)

# # # # print("pop(), ", perf_counter() - start)

# # # # start = perf_counter()

# # # # fct2(lst2)

# # # # print("pop(0), ", perf_counter() - start)

# # # import tracemalloc

# # # def fct3():
# # #     for i in range(100):
# # #         lst = [x for x in range(10000)]
# # #         my_set = set(lst)
 
# # # # tracemalloc.start()
# # # # fct3()
# # # # actuel, pic = tracemalloc.get_traced_memory()
# # # # tracemalloc.stop()

# # # # Fonction reutilisable pour memoire
# # # def get_memory(fct: function):
# # #     tracemalloc.start()
# # #     fct()
# # #     actuel, pic = tracemalloc.get_traced_memory()
# # #     tracemalloc.stop()
# # #     return actuel, pic


# # # actuel, pic = get_memory(fct3)
# # # print(f"pic : {pic / 1024:.0f} Kio")
 
# # # # print(f"pic : {pic / 1024:.0f} Kio")

# # import random

# # lst = [random.randint(0, 15) for _ in range(15)]

# # def somme(l):
# #     return sum(l)

# # def est_dedans(elem, l):
# #     return elem in l

# # def tri(l):
# #     return sorted(l)

# # def main():
# #     total = somme(lst)
# #     print(est_dedans(50, lst))
# #     tried_list = tri(lst)


# # main()


# from collections import deque

# mon_deque = deque(maxlen=3)

# ma_list = [1, 2, 3, 4, 5]

# for i in ma_list:
#     mon_deque.append(i)

# # [3, 4, 5]

# # print(mon_deque)


# # import heapq

# # taches = []

# # heapq.heappush(taches, (5, 'Sortir les poubelles'))
# # heapq.heappush(taches, (3, 'Faire à manger'))
# # heapq.heappush(taches, (10, 'Balayer le sol'))
# # heapq.heappush(taches, (1, 'Faire le café'))

# # print(heapq.heappop(taches))

# # heapq.heappush(taches, (2, 'Faire les exo du cours de Davit'))
# # heapq.heappush(taches, (1, 'Sortir le chien'))

# # print(heapq.heappop(taches))

# # print(heapq.nlargest(3, [1, 5, 4, 6, 8, 10, 0, 5]))
# # print(heapq.nsmallest(3, [1, 5, 4, 6, 8, 10, 0, 5]))

# import bisect

# # list_pas_trie = [1, 5, 2, 81, 6, 7, 4] => bisect ne fonctionne pas
 
# seuils = [10, 12, 14, 16]            # triés
# seuils_doublons = [10, 12, 12, 12, 14, 16]            # triés avec doublons
# mentions = ["échec", "satisfaction", "distinction",
#             "grande distinction",
#             "plus grande distinction"]
 
# def mention(note):
#     return mentions[bisect.bisect_right(seuils, note)]

# print(bisect.bisect_left(seuils, 11)) # renvoie position de 11 dans la lsite -> index

# print(bisect.bisect_left(seuils_doublons, 12)) # => renvoie 1 (12 à gauche car doublons)
# print(bisect.bisect_right(seuils_doublons, 12)) # => renvoie 4 (12 à droite car doublons)
 
# # mention(13.5)    # 'distinction'
 
# bisect.insort(seuils, 15)   # garde l'ordre, O(n)

# print(seuils)


# elem = {2, 3, True}

# print(elem)

# print(True == 2)


# def my_sum(a, b):
#     return a + b
