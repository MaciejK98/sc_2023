import functools

@functools.lru_cache(maxsize=None)
def Engset(a, V, N):
  if V == 0:
    return 1.0
  else:
    return (a * (N - V + 1) * Engset(a, V - 1, N)) / (V + a * (N - V + 1) * Engset(a, V - 1, N))

ruch_uzytkownika = 0.05 *2
pojemnosc_systemu = 2 * 30
stopien_obciazenia = ruch_uzytkownika / (1-ruch_uzytkownika)

prawdopodobienstwo_blokady = 0.005
V = pojemnosc_systemu
N = int(stopien_obciazenia * V)

while True:
  # print("N: ",N)
  Pb = Engset(stopien_obciazenia, V, N)
  if Pb > prawdopodobienstwo_blokady:
    break
  N += 1

print("Liczba użytkowników:", N-1)

print(Engset(stopien_obciazenia,60,N-1))