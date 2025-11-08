import numpy as np
from TS.TS import TS

# Lista de artistas e seus dados
artistas = [
    "Taylor Swift", "Beyoncé", "Tardezinha c/ Thiaguinho", "Jorge & Mateus",
    "Anitta", "Luísa Sonza", "Billie Eilish", "Avenged Sevenfold",
    "Nando Reis", "Gilberto Gil", "Zeca Pagodinho", "Joelma",
    "Numanice (Ludmila)", "Adele", "Paramore", "The Weeknd"
]

precos = [1200, 1100, 300, 250, 350, 280, 800, 700, 200, 220, 240, 180, 200, 1000, 900, 950]
valores = [9.5, 9.5, 7.0, 6.0, 6.0, 6.5, 7.5, 6.5, 7.5, 7.5, 7.0, 5.5, 5.0, 8.0, 6.5, 8.5]

# Função objetivo (sem restrição)
def objetivo_basico(x):
    x_bin = np.round(x).astype(int)
    x_bin = np.clip(x_bin, 0, 1)
    
    custo = np.sum(x_bin * precos)
    if custo > 3000:
        return 10000 + (custo - 3000)  
    
    qtd = np.sum(x_bin)
    gosto = np.sum(x_bin * valores)
    return -(qtd * 100 + gosto)

# Função com restrição (precisa Taylor ou Beyoncé)
def objetivo_com_restricao(x):
    x_bin = np.round(x).astype(int)
    x_bin = np.clip(x_bin, 0, 1)
    
    # Se não tiver Taylor (0) nem Beyoncé (1), punição forte
    if x_bin[0] == 0 and x_bin[1] == 0:
        return 99999

    custo = np.sum(x_bin * precos)
    if custo > 3000:
        return 99999
    
    qtd = np.sum(x_bin)
    gosto = np.sum(x_bin * valores)
    return -(qtd * 100 + gosto)

# Limites (cada artista pode ser 0 ou 1)
bounds = [(0, 1) for _ in range(16)]

# Rodando o primeiro caso (sem restrição)
p_ini = np.random.uniform(0, 1, 16)
res1 = TS(objetivo_basico, 100, 20, bounds, 0.3, 10, 0.8, 15, [0.1]*16, p_ini, False)

x1 = np.round(res1.x).astype(int)
x1 = np.clip(x1, 0, 1)

shows1 = [artistas[i] for i in range(16) if x1[i] == 1]
custo1 = sum(precos[i] for i in range(16) if x1[i])
gosto1 = sum(valores[i] for i in range(16) if x1[i])

print("==== SEM RESTRIÇÃO ====")
print(f"Total de shows: {len(shows1)} | Custo: R$ {custo1} | Gosto total: {gosto1:.1f}")
print("Escolhidos:", ", ".join(shows1))
print()

#com restrição
p_ini2 = np.random.uniform(0, 1, 16)
p_ini2[0] = 1  # começa com Taylor escolhida
res2 = TS(objetivo_com_restricao, 100, 20, bounds, 0.3, 10, 0.8, 15, [0.1]*16, p_ini2, False)

x2 = np.round(res2.x).astype(int)
x2 = np.clip(x2, 0, 1)

shows2 = [artistas[i] for i in range(16) if x2[i] == 1]
custo2 = sum(precos[i] for i in range(16) if x2[i])
gosto2 = sum(valores[i] for i in range(16) if x2[i])

print("==== COM RESTRIÇÃO (Taylor OU Beyoncé) ====")
print(f"Total de shows: {len(shows2)} | Custo: R$ {custo2} | Gosto total: {gosto2:.1f}")
print("Escolhidos:", ", ".join(shows2))
print()

