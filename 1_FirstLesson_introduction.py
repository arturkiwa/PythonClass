def dodawanie():
    liczba_pierwsza = input('First number')
    liczba_druga = input('Second number')
    if liczba_pierwsza.isnumeric() and liczba_druga.isnumeric():
        suma = int(liczba_pierwsza) + int(liczba_druga)
        return suma
    else:
        print('VALUE ERROR!')
        return False


sumaPierwsza = dodawanie()
sumaDruga = dodawanie()

print(f"Wyniki działań to: {sumaPierwsza} oraz: {sumaDruga}")
print("Wyniki działań to: "+str(sumaPierwsza)+" oraz: "+str(sumaDruga))

sumaDruga = ()
sumaTrzecia = {}
sumaCzwarta = []

print(type(sumaDruga))
print(type(sumaTrzecia))
print(type(sumaCzwarta))
