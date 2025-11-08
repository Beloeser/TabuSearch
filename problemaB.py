import numpy as np
from TS.TS import TS
artistas = [
    "Taylor Swift", "Beyoncé", "Tardezinha c/ Thiaguinho", "Jorge & Mateus",
    "Anitta", "Luísa Sonza", "Billie Eilish", "Avenged Sevenfold",
    "Nando Reis", "Gilberto Gil", "Zeca Pagodinho", "Joelma",
    "Numanice (Ludmila)", "Adele", "Paramore", "The Weeknd"
]

precos = [1200, 1100, 300, 250, 350, 280, 800, 700, 200, 220, 240, 180, 200, 1000, 900, 950]
valores = [9.5, 9.5, 7.0, 6.0, 6.0, 6.5, 7.5, 6.5, 7.5, 7.5, 7.0, 5.5, 5.0, 8.0, 6.5, 8.5]

# Função objetivo
def funcao_objetivo(x):
    x_bin = np.round(x).astype(int)
    x_bin = np.clip(x_bin, 0, 1)
    custo = np.sum(x_bin * precos)
    
    if custo > 3000:
        return 10000 
    
    qtd = np.sum(x_bin)
    gosto = np.sum(x_bin * valores)
    return -(qtd * 100 + gosto)

# 0 ou 1 para cada artista
bounds = [(0, 1) for _ in range(16)]

# parâmetros padrão
print("Teste 1 – parâmetros padrão")
p_inicial1 = np.random.uniform(0, 1, 16)
res1 = TS(funcao_objetivo, 100, 20, bounds, 0.3, 10, 0.8, 15, [0.1]*16, p_inicial1, False)

x1 = np.round(res1.x).astype(int)
x1 = np.clip(x1, 0, 1)
shows1 = [artistas[i] for i in range(16) if x1[i] == 1]
custo1 = sum(precos[i] for i in range(16) if x1[i])
gosto1 = sum(valores[i] for i in range(16) if x1[i])

print(f"Qtd shows: {len(shows1)} | Custo total: R$ {custo1} | Gosto: {gosto1:.1f}")
print("Selecionados:", ", ".join(shows1))
print()

# mais iterações
print("Teste 2 – mais iterações")
p_inicial2 = np.random.uniform(0, 1, 16)
res2 = TS(funcao_objetivo, 200, 30, bounds, 0.3, 10, 0.8, 15, [0.1]*16, p_inicial2, False)

x2 = np.round(res2.x).astype(int)
x2 = np.clip(x2, 0, 1)
shows2 = [artistas[i] for i in range(16) if x2[i] == 1]
custo2 = sum(precos[i] for i in range(16) if x2[i])
gosto2 = sum(valores[i] for i in range(16) if x2[i])

print(f"Qtd shows: {len(shows2)} | Custo total: R$ {custo2} | Gosto: {gosto2:.1f}")
print("Selecionados:", ", ".join(shows2))
print()

# raio maior
print("Teste 3 – raio maior")
p_inicial3 = np.random.uniform(0, 1, 16)
res3 = TS(funcao_objetivo, 100, 20, bounds, 0.5, 10, 0.8, 15, [0.1]*16, p_inicial3, False)

x3 = np.round(res3.x).astype(int)
x3 = np.clip(x3, 0, 1)
shows3 = [artistas[i] for i in range(16) if x3[i] == 1]
custo3 = sum(precos[i] for i in range(16) if x3[i])
gosto3 = sum(valores[i] for i in range(16) if x3[i])

print(f"Qtd shows: {len(shows3)} | Custo total: R$ {custo3} | Gosto: {gosto3:.1f}")
print("Selecionados:", ", ".join(shows3))
print()

# lista tabu maior
print("Teste 4 – lista tabu maior")
p_inicial4 = np.random.uniform(0, 1, 16)
res4 = TS(funcao_objetivo, 100, 20, bounds, 0.3, 10, 0.8, 30, [0.1]*16, p_inicial4, False)

x4 = np.round(res4.x).astype(int)
x4 = np.clip(x4, 0, 1)
shows4 = [artistas[i] for i in range(16) if x4[i] == 1]
custo4 = sum(precos[i] for i in range(16) if x4[i])
gosto4 = sum(valores[i] for i in range(16) if x4[i])

print(f"Qtd shows: {len(shows4)} | Custo total: R$ {custo4} | Gosto: {gosto4:.1f}")
print("Selecionados:", ", ".join(shows4))
print()
