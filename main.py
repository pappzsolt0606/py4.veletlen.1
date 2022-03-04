"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

szam = int(input("Kérek egy számot: "))

import random

random_szam = random.randint(1,3)

if szam == random_szam:
    print("Jól tippeltél")
else:
    print(f"ez volt a random szám: {random_szam}")
    print(f"ez volt a tipped: {szam}")
    print("nem jó")

