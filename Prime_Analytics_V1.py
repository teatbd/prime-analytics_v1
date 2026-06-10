# Prime Analytics v1

import time
import math
import matplotlib.pyplot as plt


# =========================
# 1. NAIVE METHOD
# =========================
def es_primo_v1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# =========================
# 2. OPTIMIZED (SQRT)
# =========================
def es_primo_v2(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# =========================
# 3. SIEVE OF ERATOSTHENES
# =========================
def criba(n):
    es_primo = [True] * (n + 1)
    es_primo[0] = False
    es_primo[1] = False

    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            for j in range(i*i, n + 1, i):
                es_primo[j] = False

    return [i for i in range(2, n + 1) if es_primo[i]]


# =========================
# 4. BENCHMARK
# =========================
rangos = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000]

tiempo_ingenuo = []
tiempo_opt = []
tiempo_criba = []

speedup_sqrt = []
speedup_sieve = []

for r in rangos:
    print(f"\nRango: {r}")

    # naive
    inicio = time.time()
    primos1 = [n for n in range(1, r) if es_primo_v1(n)]
    t1 = time.time() - inicio
    tiempo_ingenuo.append(t1)

    # sqrt
    inicio = time.time()
    primos2 = [n for n in range(1, r) if es_primo_v2(n)]
    t2 = time.time() - inicio
    tiempo_opt.append(t2)

    # sieve
    inicio = time.time()
    primos3 = criba(r)
    t3 = time.time() - inicio
    tiempo_criba.append(t3)

    # speedups
    speedup_sqrt.append(t1 / t2)
    speedup_sieve.append(t1 / t3)

    print("Ingenuo:", t1)
    print("Raiz:", t2)
    print("Criba:", t3)
    print("Speedup sqrt:", t1 / t2)
    print("Speedup sieve:", t1 / t3)


# =========================
# 5. PLOTS
# =========================

# 5.1 Time comparison
plt.plot(rangos, tiempo_ingenuo, label="Naive")
plt.plot(rangos, tiempo_opt, label="Sqrt")
plt.plot(rangos, tiempo_criba, label="Sieve")
plt.xlabel("Range")
plt.ylabel("Time (seconds)")
plt.title("Algorithm Performance")
plt.legend()
plt.show()

# 5.2 Speedup log-log (naive vs sqrt)
plt.plot(rangos, speedup_sqrt, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Range")
plt.ylabel("Speedup (Naive / Sqrt)")
plt.title("Scaling Behaviour (log-log)")
plt.show()

# 5.3 Speedup comparison
plt.plot(rangos, speedup_sqrt, label="Naive vs Sqrt")
plt.plot(rangos, speedup_sieve, label="Naive vs Sieve")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Range")
plt.ylabel("Speedup")
plt.title("Speedup Comparison")
plt.legend()
plt.show()


# =========================
# 6. PRIME DENSITY
# =========================

rangos_densidad = [10, 100, 1000, 10000, 100000, 1000000]

densidad_real = []
densidad_teorica = []

for r in rangos_densidad:
    primos = criba(r)
    dens = len(primos) / r
    densidad_real.append(dens)

    teorica = 1 / math.log(r)
    densidad_teorica.append(teorica)

# Density plot
plt.plot(rangos_densidad, densidad_real, marker='o', label="Real")
plt.plot(rangos_densidad, densidad_teorica, marker='x', label="1/log(n)")
plt.xscale('log')
plt.xlabel("Range")
plt.ylabel("Density")
plt.title("Prime Density vs Theory")
plt.legend()
plt.show()

plt.savefig("performance.png")
