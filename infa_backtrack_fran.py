"""ova verzija programa radi tako da pokusava zavrsiti
tablicu pokusavanjem jednog tip pomaka i kada ne uspije
vrati se za jedan korak natrag i proba drugi tip pomaka
a.k.a. Backtracking"""

import random
print("rjesenje problema za \"knight\'s tour\"")

# liste za sva polja i posjecena polja
polja = []
posjecena_polja = []

# generira 81 integer i stavlja ga u listu polja
for i in range(1, 82):
    polja.append(i)

p = random.choice(polja)  # odabire random polje s kojeg krece
posjecena_polja.append(p)  # stavlja pocetno polje u listu posjecena_polja
polja.remove(p)				# brise pocetno polje iz liste polja
# odabire random polje s kojeg krece

# tipovi pomaka:
a = p + 17  # dolje_lijevo_dugo
b = p + 7  # dolje_lijevo_dugo
c = p + 19  # dolje_desno_dugo
d = p + 11  # dolje_desno_kratko
e = p - 19  # gore_lijevo_dugo
f = p - 11  # gore_lijevo_kratko
g = p - 17  # gore_desno_dugo
h = p - 7  # gore_desno_katko
