# import sys
# # sys.setrecursionlimit(1000000) Pas une super idée hein!

# pile = []

# def compte_a_rebours(n):
#     if n == 0:
#         print('BOOM')
#         return n
#     print('Descente --- ', n)
#     remonte =  compte_a_rebours(n - 1)
#     print('ça remonte', n)
#     return remonte

# compte_a_rebours(10)

# def compter_valeurs(obj) -> int:
#     """Nombre de valeurs simples dans un JSON imbriqué."""
#     total = 0
#     pile = [obj]
#     while pile:
#         x = pile.pop()
#         if isinstance(x, dict):
#             pile.extend(x.values())
#         elif isinstance(x, list):
#             pile.extend(x)
#         else:
#             total += 1
#     return total


lettres = ['A', 'B', 'C']

resultat = []

for l in lettres:
    if l not in resultat:
        resultat.append(l)

# Resolution ? => len(lettres) == len(resultat)

# De base, [] de resultat est vide

def backtracking(result = []):
    if len(result) == len(lettres):
        print(result)
        return

    for l in lettres:
        if l not in result:
            result.append(l)
            # print(f'APPEND {l} DANS RESULT : ', result)
            backtracking(result)
            result.pop()
            # print('BACKTRACK ***********************', result)

backtracking()
