import numpy as np
from TS.TS import TS

artistas = ["Taylor Swift", "Beyoncé", "Tardezinha c/ Thiaguinho", "Jorge & Mateus",
           "Anitta", "Luísa Sonza", "Billie Eilish", "Avenged Sevenfold",
           "Nando Reis", "Gilberto Gil", "Zeca Pagodinho", "Joelma",
           "Numanice (Ludmila)", "Adele", "Paramore", "The Weeknd"]

precos = [1200, 1100, 300, 250, 350, 280, 800, 700, 200, 220, 240, 180, 200, 1000, 900, 950]
valores = [9.5, 9.5, 7.0, 6.0, 6.0, 6.5, 7.5, 6.5, 7.5, 7.5, 7.0, 5.5, 5.0, 8.0, 6.5, 8.5]

def funcaoObjetivo(x):
    xBin = np.round(x).astype(int)
    xBin = np.clip(xBin, 0, 1)
    custo = np.sum(xBin * precos)
    if custo > 3000:
        return 1000 + (custo - 3000)
    numShows = np.sum(xBin)
    valorGosto = np.sum(xBin * valores)
    return -(numShows * 100 + valorGosto)

def funcaoComRestricao(x):
    xBin = np.round(x).astype(int)
    xBin = np.clip(xBin, 0, 1)
    if xBin[0] == 0 and xBin[1] == 0:
        return 2000
    custo = np.sum(xBin * precos)
    if custo > 3000:
        return 1000 + (custo - 3000)
    numShows = np.sum(xBin)
    valorGosto = np.sum(xBin * valores)
    return -(numShows * 100 + valorGosto)

bounds = [(0, 1) for _ in range(16)]
pInit = np.random.uniform(0, 1, 16)
resultado1 = TS(funcaoObjetivo, 100, 20, bounds, 0.3, 10, 0.8, 15, [0.1]*16, pInit, False)

xOtimo1 = np.round(resultado1.x).astype(int)
xOtimo1 = np.clip(xOtimo1, 0, 1)
shows1 = [artistas[i] for i in range(16) if xOtimo1[i] == 1]
custo1 = sum(precos[i] for i in range(16) if xOtimo1[i] == 1)
gosto1 = sum(valores[i] for i in range(16) if xOtimo1[i] == 1)

print("PROBLEMA ORIGINAL:")
print(f"Shows: {len(shows1)} | Custo: R$ {custo1} | Gosto: {gosto1:.1f}")
print(f"Selecionados: {', '.join(shows1)}")
print()

pInit2 = np.random.uniform(0, 1, 16)
pInit2[0] = 1
resultado2 = TS(funcaoComRestricao, 100, 20, bounds, 0.3, 10, 0.8, 15, [0.1]*16, pInit2, False)

xOtimo2 = np.round(resultado2.x).astype(int)
xOtimo2 = np.clip(xOtimo2, 0, 1)
shows2 = [artistas[i] for i in range(16) if xOtimo2[i] == 1]
custo2 = sum(precos[i] for i in range(16) if xOtimo2[i] == 1)
gosto2 = sum(valores[i] for i in range(16) if xOtimo2[i] == 1)

print("COM RESTRIÇÃO (Taylor Swift OU Beyoncé):")
print(f"Shows: {len(shows2)} | Custo: R$ {custo2} | Gosto: {gosto2:.1f}")
print(f"Selecionados: {', '.join(shows2)}")
print()

print(f"Diferença de shows: {len(shows2) - len(shows1)}")
print(f"Diferença de custo: R$ {custo2 - custo1}")
print(f"Diferença de gosto: {gosto2 - gosto1:.1f}")