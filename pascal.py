import functools

@functools.lru_cache(maxsize=None)
def Engset(a, V, N):
  if V == 0:
    return 1.0
  else:
    return (-a * (-N - V + 1) * Engset(a, V - 1, N)) / (V + -a * (-N - V + 1) * Engset(a, V - 1, N))
    #zamiana N na -N i a na -a we wzorze względem Engseta
ruch_uzytkownika = 0.05 *2
pojemnosc_systemu = 2 * 30
stopien_obciazenia = -ruch_uzytkownika / (-ruch_uzytkownika-1) #zmiana z Engseta na Pascala

prawdopodobienstwo_blokady = 0.005
V = pojemnosc_systemu
N = int(stopien_obciazenia * V)

while True:
  Pb = Engset(stopien_obciazenia, V, N)
  if Pb > prawdopodobienstwo_blokady:
    break
  N += 1

print("Liczba użytkowników:", N-1)

print("prawdopodobieństwo blokad: ",Engset(stopien_obciazenia,pojemnosc_systemu,N-1))