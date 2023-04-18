import time

nazwa_zespolu = "KoderMaster"
czlonkowie_zespolu = "Jan Kowalski, Anna Nowak, Piotr Wiśniewski"
specjalizacje = "programowanie gier, tworzenie aplikacji webowych, uczenie maszynowe"
uzasadnienie = "chcemy poszerzyć swoje umiejętności i rozwijać się w otoczeniu najlepszych #SuperKoderów"


def literuj_tekst(tekst, opoznienie=0.1):
    for litera in tekst:
        if litera == ' ':
            print(' ', end='', flush=True)
        else:
            print(litera, end='', flush=True)
            time.sleep(opoznienie)
    print()


print("Twoje zaproszenie brzmi:")

literuj_tekst("Zapraszamy #SuperKoderów do naszej szkoły, gdzie działa zespół", opoznienie=0.1)
print()
literuj_tekst(nazwa_zespolu, opoznienie=0.2)
print()
literuj_tekst("składający się z uczniów:", opoznienie=0.1)
print()
literuj_tekst(czlonkowie_zespolu, opoznienie=0.2)
print()
literuj_tekst("specjalizujących się w:", opoznienie=0.1)
print()
literuj_tekst(specjalizacje, opoznienie=0.2)
print()
literuj_tekst("i chcemy dołączyć do Waszego programu, ponieważ", opoznienie=0.1)
print()
literuj_tekst(uzasadnienie, opoznienie=0.2)
print()
