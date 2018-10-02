from scipy.optimize import linprog


ca = [0, 0, 0, 0, 0, 1, 1, 1]
Aa = [[0.2, 0.5, 0.4, -1, 0, 1, 0, 0], [0.6, 0.4, 0.4, 0, -1, 0, 1, 0], [1, 1, 1, 0, 0, 0, 0, 1]]
ba = [0.3, 0.5, 1]
xa_bnds = []

for i in range(len(ca)):
    xa_bnds.append((0,None))

res = linprog(ca, Aa, ba, bounds=xa_bnds)
print(res)

# c = [0.56, 0.81, 0.46, 0, 0]
# A = [[0.2, 0.5, 0.4, -1, 0], [0.6, 0.4, 0.4, 0, -1], [1, 1, 1, 0, 0]]
# b = [0.3, 0.5, 1]
# x_bnds = []

# for i in range(len(c)):
#     x_bnds.append((0,None))

# res = linprog(c, A, b, bounds=x_bnds)

# print(res)