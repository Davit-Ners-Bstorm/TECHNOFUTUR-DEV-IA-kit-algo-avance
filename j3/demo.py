# # import sys
# # # sys.setrecursionlimit(1000000) Pas une super idée hein!

# # pile = []

# # def compte_a_rebours(n):
# #     if n == 0:
# #         print('BOOM')
# #         return n
# #     print('Descente --- ', n)
# #     remonte =  compte_a_rebours(n - 1)
# #     print('ça remonte', n)
# #     return remonte

# # compte_a_rebours(10)

# # def compter_valeurs(obj) -> int:
# #     """Nombre de valeurs simples dans un JSON imbriqué."""
# #     total = 0
# #     pile = [obj]
# #     while pile:
# #         x = pile.pop()
# #         if isinstance(x, dict):
# #             pile.extend(x.values())
# #         elif isinstance(x, list):
# #             pile.extend(x)
# #         else:
# #             total += 1
# #     return total


# lettres = ['A', 'B', 'C']

# resultat = []

# for l in lettres:
#     if l not in resultat:
#         resultat.append(l)

# # Resolution ? => len(lettres) == len(resultat)

# # De base, [] de resultat est vide

# def backtracking(result = []):
#     if len(result) == len(lettres):
#         print(result)
#         return

#     for l in lettres:
#         if l not in result:
#             result.append(l)
#             # print(f'APPEND {l} DANS RESULT : ', result)
#             backtracking(result)
#             result.pop()
#             # print('BACKTRACK ***********************', result)

# backtracking()

# fib(n) = fib(n - 1) + fib(n - 2)
# 0 : 0
# 1 : 1
# 2 : 1
# 3 : 2
# 4 : 3
# 5 : 5
i = 0
def fib(n):
    global i
    print(i)
    i += 1
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

# print(fib(50))

memo = {}

def fib_memo(n):
    if n < 2:
        return n

    if n in memo:
        return memo[n]

    resultat = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = resultat

    return resultat

# print(fib_memo(300))

from functools import cache
import unicodedata

@cache
def fib_cache_natif(n):
    if n < 2:
        return n

    return fib_cache_natif(n - 1) + fib_cache_natif(n - 2)

# print(fib_cache_natif(900))

def fib_tab(n):
    a = 0 # 1
    b = 1 # 2

    for _ in range(n):
        a, b = b, a + b

    return a

# print(fib_tab(50))
# print(fib_cache_natif(50))

# A : 2kg - 3e
# B : 3kg - 4e
# C : 4kg - 5e

# sac : 5kg
