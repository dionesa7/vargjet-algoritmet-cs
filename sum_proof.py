import time

# 1. Algoritmi i zakonshëm (Kompleksiteti O(n))
def shuma_me_cikel(n):
    shuma = 0
    for i in range(1, n + 1):
        shuma += i
    return shuma

# 2. Formula Matematikore e vërtetuar me Induksion (Kompleksiteti O(1))
def shuma_me_formule(n):
    return n * (n + 1) // 2

# Funksioni për të demonstruar vërtetësinë
def vërteto_korrektesine(max_n):
    print(f"--- Duke testuar korrektësinë për numrat nga 1 deri në {max_n} ---")
    te_gjitha_sakte = True
    
    # Këtu po simulojmë testimin për çdo 'n' (si hapi induktiv)
    for k in range(1, max_n + 1):
        rez_cikli = shuma_me_cikel(k)
        rez_formula = shuma_me_formule(k)
        
        if rez_cikli != rez_formula:
            print(f"Gabim te n={k}! Cikli: {rez_cikli}, Formula: {rez_formula}")
            te_gjitha_sakte = False
            break
            
    if te_gjitha_sakte:
        print("Sukses! Për çdo 'n', algoritmi dhe formula japin të njëjtin rezultat.")
        print("Induksioni matematik na jep garancinë që kjo vlen deri në pafundësi!\n")

# Funksioni për të krahasuar shpejtësinë
def krahaso_performancen(n):
    print(f"--- Krahasimi i performancës për një numër të madh (n = {n:,}) ---")
    
    start = time.time()
    res_cikli = shuma_me_cikel(n)
    end = time.time()
    print(f"[Cikli For - O(n)] Rezultati: {res_cikli}, Koha: {end-start:.6f} sekonda")

    start = time.time()
    res_form = shuma_me_formule(n)
    end = time.time()
    print(f"[Formula - O(1)] Rezultati: {res_form}, Koha: {end-start:.6f} sekonda")

if __name__ == "__main__":
    # 1. Vërtetojmë që kodi dhe formula janë e njëjta gjë
    vërteto_korrektesine(100)
    
    # 2. Tregojmë pse vërtetimi matematikor na bën inxhinierë më të mirë
    # Po e testojmë me 100 milionë!
    krahaso_performancen(100000000)
