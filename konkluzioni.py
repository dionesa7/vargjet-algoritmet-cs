import time

def pergjigja_per_profesorin():
    print("\n[SISTEMI] Duke analizuar pyetjen e pritshme të Profesorit...")
    time.sleep(1.5)
    print("[SISTEMI] Pyetja: 'A jeni të bindur që matematika ka ndikim në Shkenca Kompjuterike?'")
    time.sleep(2)
    
    print("\n[SISTEMI] Duke mbledhur provat nga ekzekutimi i sotëm...")
    time.sleep(1)
    print("  -> Prova 1 (Kodi Naiv pa matematikë): CPU u mbingarkua (Koha: E pafundme)")
    time.sleep(1)
    print("  -> Prova 2 (Kodi me Induksion Matematik): Kompleksitet O(1) (Koha: 0.000002s)")
    time.sleep(1)
    
    print("\n[SISTEMI] Duke llogaritur nivelin e bindjes së studentëve (Sufjan & Dionesa)...")
    time.sleep(1.5)
    
    # Këtu kodi kthen rezultatin vizual
    print("=====================================================")
    print(" REZULTATI: True (Të bindur 100%)")
    print(" STATUSI: Matematika nuk është thjesht numra. Është Shpejtësi!")
    print("=====================================================\n")

if __name__ == "__main__":
    pergjigja_per_profesorin()
