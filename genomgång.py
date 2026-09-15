ålder=int(input("Hur gammal är du? "))

if ålder == 17:
    print("Du är lika gammal som de flesta i EE25")
else:
    print("Du är inte lika gammal som de flesta i EE25")

if ålder != 43:
    print("Du är inte lika gammal som Per")
else:
    print("Du är lika gammal som Per")

if ålder <= 13:
    print("Du är väldigt ung")
elif ålder < 18:
    print("Du får inte ta körkort")
elif ålder < 20:
    print("Du får ta kärkort")
else:
    print("Du får handdla på systembolaget")

namn = input("Vad är dit namn? ")

if namn == "Adrian":
    print("King aså!")
elif namn == "Adriano":
    print("Wrong name buddy")
else:
    print("Should have been named Adrian")

if ålder == 17 and namn == "Adrian":
    print("Ej, so sigma my g that is my name and age too, wait... might you be me?")
else:
    print("Aw hell naw!")