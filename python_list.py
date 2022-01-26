# Tworzymy pustą listę
myList = []

# Tworzymy przykładową listę zawierającą dane
# Zwróć uwagę na fakt, iż lista mozę zawierać różne typy danych. Elementem listy może być inna lista

myList = [133, 2, 'XYZ', [3, 4, 'ABC']]

# Dostęp do elementów listy uzyskujemy poprzez podanie jego indeksu w nawiasach kwadratowych.

print("Elementy listy indeksujemy od zera, więc pierwszy element ma numer 0, drugi 1, i tak dalej.")
print(f"Cała lista: {myList}")
print(f"Czwarty element listy jest listą: {myList[3]}")
print(f"Czwarty element listy i jego trzecia pozycja: {myList[3][2]}")

# zamiast liczb dodatnich możemy także użyć ujemnych
# nazywa się to negative indexing i pozwala uzyskać dostęp do elementów listy licząc od końca

print(f"Ostatni element naszej listy ma indeks -1 {myList[-1]}")

# Każdą listę można pokroić na plasterki, to działanie nazywa się slicing
# Możemy wyciągnąć fragment naszej listy jak poniżej
# W nawiasach kwadratowych podajemy pierwszy lelement fragmentu i po dwukropku ostatni
# UWAGA!
# Ostatni element nie będzie zawarty w nowej liście
# Oznacza to, ze jeżeli chcemy pobrać 2 elementy, poczynając od drugiego, musimy poprosić o indeksy [1:3]
# Zwrócone zostaną indeksy 1 i 2, indeks numer 3 nie zostanie zwrócony

print(f"Zwracamy 2 elementy listy, poczynając od drugiego: {myList[1:3]}")

# Elementy listy można zmieniać
# Zmieniamy pierwszy element listy

myList[0] = 521
print(f"Nowa lista po zmianie pierwszego elementu na 521: {myList}")

# Tak jak w przypadku slicingu, możemy zmienić fragment listy

myList[1:3] = ['CSS', [9, 8, 7, 'DDD']]
print(myList)

# Do listy możemy dodawać nowe elementy. Metody append i extend
# Dodajemy jedną pozycję

myList.append(11)
print(f"Lsta po dodaniu nowego elementu: {myList}")

# I jeszcze jedną

myList.append('ZXC')
print(f"Lsta po dodaniu nowego elementu: {myList}")

# Aby dodać do listy klilka elementów używamy metody extend

myList.extend([11, '11', 234])
print(f"Nowa lista po dodaniu kliku elementów: {myList}")

# Dodawanie elementów do listy można wykonać za pomocą operacji zwanej konkatenacją, z operatorem +

myList = myList + [55, 'ESD', 1234]
print(f"Nowa lista po konkatenacji: {myList}")

# Elementy można dodawać do lity nie tylko na końcu. Możemy dodać nowe lementy w dowolnym miejscu.

myList.insert(1, 100)
print(f"Dodane 100 na pozycji 2: {myList}")

# Możemy także wstrzelić w listę elementy na wskazanej pozycji.

myList[3:3] = [999, 998, 997, 996]
print(f"Dodane 4 pozycje od pozycji 3: {myList}")

# Kopiowanie, shallowcopy i deepcopy

print()
print(f"Lista przed zmianą: {myList}")
shallowCopy = myList
deepCopy = myList.copy()
myList.append('LAST ELEMENT')
print(f"Oryginalna lista:   {myList}")
print(f"Płytka kopia:       {shallowCopy}")
print(f"Głęboka kopia:      {deepCopy}")
# print(id(myList))
# print(id(shallowCopy))
# print(id(deepCopy))
print()

# Usuwanie elementów listy
# Metoda pop usuwa jeden indeks z listy i zwraca jesgo wartość. Argumentem jest indeks.
# Metoda remove uzuwa jeden element z listy. Argumentem jest wartość.
# Słowo kluczowe del. Indeks jako argument. Usuwa wiele pozycji lub całą listę.

myList.pop()
print(f"Usunięty ostatni element listy - pop bez argumentu: {myList}")
myList.pop(0)
#myList.remove(12)
print(f"Usunięty pierwszy element listy - pop(0):           {myList}")
del myList[1:3]
print(f"Usunięty dwa element listy - del:                   {myList}")
myList.clear()
print(myList)
del myList
# print(myList)
