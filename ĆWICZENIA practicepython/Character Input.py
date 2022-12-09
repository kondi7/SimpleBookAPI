#CEL: WYŚWIETL ROK, W KTORYM UZYTKOWNIK BEDZIE MIAL 100 LAT

import datetime

nazwa = input("Wpisz swoje imie: ")

while not nazwa.isalpha():
    print("Tylko litery są dozwolone!")
    nazwa = input("Wpisz swoje imie: ")

while True:
    try:
        wiek = int(input("Wpisz swoj wiek: "))
        break
    except ValueError:
        print("to nie liczba, wpisz swoj wiek ponownie.")

dzis = datetime.date.today()
rok = dzis.year

wiek_uzytkownika = 100-wiek+rok

print("Nazywasz się", nazwa.capitalize(), "i bedzięsz miał 100 lat w roku", wiek_uzytkownika)
