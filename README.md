# PatientQueue
Opis
Program w Pythonie do zarządzania kolejką pacjentów z umówionymi wizytami. Umożliwia dodawanie zwykłych i priorytetowych pacjentów, usuwanie pacjentów oraz wyświetlanie aktualnej kolejki. System zapewnia, że wizyty są planowane w 15-minutowych blokach i odpowiednio dostosowuje terminy w przypadku pacjentów priorytetowych.

Funkcje
Dodawanie zwykłych pacjentów do kolejki
Dodawanie pacjentów priorytetowych (z preferencyjnym traktowaniem w harmonogramie)
Usuwanie pacjentów za pomocą numeru PESEL
Przeglądanie wszystkich pacjentów w kolejce z ich danymi
Automatyczna regulacja terminów dla pacjentów priorytetowych
Walidacja wprowadzanych danych
Walidacja danych

System sprawdza poprawność:
Imion i nazwisk (tylko litery)
Numerów PESEL (dokładnie 11 cyfr)
Wiek (wartość numeryczna)
Płci (k/m/i)
Godzin wizyt (muszą być w 15-minutowych blokach)

Jak używać
Uruchom program
Użyj menu, aby wybrać operację:

1: Dodaj zwykłego pacjenta
2: Dodaj pacjenta priorytetowego
3: Usuń pacjenta
4: Wyświetl wszystkich pacjentów
5: Wyjdź

Wymagania
Python 3.x
Brak zewnętrznych zależności

Uwagi
Pacjenci priorytetowi powodują przesunięcie terminów zwykłych pacjentów w przypadku konfliktu godzin
Wszystkie godziny wizyt muszą być w formacie HH:MM i w 15-minutowych odstępach (np. 09:00, 09:15, 09:30)
System automatycznie utrzymuje kolejkę w porządku chronologicznym
