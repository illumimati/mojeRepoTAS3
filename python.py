while True:
    try:
        wiek = input("Podaj ile masz lat jesli chcesz kupic papierosy: ")
        wiek = int(wiek)
        break
    except ValueError:
        print('wprowadz cyfre')
if wiek<18:
    print("Jestes za mlody na papierosy")
else:
    print("Proszę, dla Ciebie pierwsza paczka gratis")


