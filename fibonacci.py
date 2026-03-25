import time

# 1. Rekurzioni Naiv
def fib_naiv(n):
    if n <= 1:
        return n
    return fib_naiv(n - 1) + fib_naiv(n - 2)

# 2. Rekurzioni me Memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result

# 3. Iterative (O(1) hapësirë)
def fib_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def benchmark(n):
    print(f"--- Krahasimi për Fibonacci({n}) ---")
    
    start = time.time()
    res_iter = fib_iter(n)
    end = time.time()
    print(f"[Iterative] Rezultati: {res_iter}, Koha: {end-start:.6f} s")

    start = time.time()
    res_memo = fib_memo(n)
    end = time.time()
    print(f"[Memoization] Rezultati: {res_memo}, Koha: {end-start:.6f} s")

    if n > 35:
        print("[Naiv] do të marrë shumë kohë. Anulohet.")
    else:
        start = time.time()
        res_naiv = fib_naiv(n)
        end = time.time()
        print(f"[Naiv] Rezultati: {res_naiv}, Koha: {end-start:.6f} s")

if __name__ == "__main__":
    benchmark(10)
    print("\n")
    benchmark(30)
    print("\n")
    benchmark(40)
