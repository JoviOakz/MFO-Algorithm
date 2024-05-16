import numpy as np
from mealpy import FloatVar, MFO
import statistics
import math

global contagem
contagem = 0

def Rosenbrock(solution):
    global contagem
    contagem += 1
    f = []
    for i in range(len(solution) - 1):
        f.append(100 * (solution[i] ** 2 - solution[i + 1]) ** 2 + (solution[i] - 1) ** 2)
    return np.sum(f)

def Rastrigin(solution):
    global contagem
    contagem += 1
    f = []
    for i in range(len(solution)):
        f.append(solution[i] ** 2 - 10 * math.cos(2 * math.pi * solution[i]) + 10)
    return 10 * len(solution) + np.sum(f)

def Weierstrass(solution):
    global contagem
    contagem += 1
    res1, res2 = 0, 0
    a, b, kmax = 0.5, 3, 20
    for i in range(len(solution)):
        for k in range(kmax + 1):
            res1 += a ** k * math.cos(2 * math.pi * b ** k * (solution[i] + 0.5))
    for k in range(kmax + 1):
        res2 += a ** k * math.cos(2 * math.pi * b ** k * 0.5)
    return res1 - len(solution) * res2

problem_dict = {
    "bounds": FloatVar(lb=(-100.,) * 10, ub=(100.,) * 10, name="delta"),
    "minmax": "min",
    "obj_func": Weierstrass
}
term_dist = {
    "max_fe": 100000
}

a = []
b = []

for i in range(51):
    contagem = 0
    model = MFO.OriginalMFO(epoch=200, pop_size=200)
    g_best = model.solve(problem_dict, termination=term_dist)
    a.append(g_best.target.fitness)
    b.append(contagem)

print(a)
print(b)

melhor0 = [0 if n < 10e-8 else n for n in a]

menor_numero = min(melhor0)
media = statistics.mean(melhor0)
mediana = statistics.median(melhor0)
maior_numero = max(melhor0)
desvio_padrao = statistics.stdev(melhor0)

print("Melhor: ", menor_numero)
print("Média: ", media)
print("Mediana ", mediana)
print("Maior ", maior_numero)
print("Desvio padrão: ", desvio_padrao)