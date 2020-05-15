TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

oddelovac = "-" * 30

members = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

print(oddelovac)
user = input("Dobry den, zadejte jmeno uzivatele: ")

if user not in members.keys():
    print("takovy uzivatel neexistuje")
    exit()
else:
    print(f"USER: {user}")
    print(f"PASS: {members[user]}")

print(oddelovac)

vyber_textu = int(input("vyberte k anylyze ze tri textu, zadejde cislo 1, 2 nebo 3: "))

print(oddelovac)

vybrany_text = TEXTS[vyber_textu - 1]

cisty_text = [slovo.strip(",.") for slovo in vybrany_text.split()]

#cisty_text =['Situated', 'about', '10', 'miles', 'west', 'of', 'Kemmerer', 'Fossil', 'Butte', 'is', 'a', 'ruggedly', 'impressive', 'topographic', 'feature', 'that', 'rises', 'sharply', 'some', '1000', 'feet', 'above', 'Twin', 'Creek', 'Valley', 'to', 'an', 'elevation', 'of', 'more', 'than', '7500', 'feet', 'above', 'sea', 'level', 'The', 'butte', 'is', 'located', 'just', 'north', 'of', 'US', '30N', 'and', 'the', 'Union', 'Pacific', 'Railroad', 'which', 'traverse', 'the', 'valley']

pocet_slov = 0
pocet_titlecase = 0
pocet_uppercase = 0
pocet_lowercase = 0
pocet_cisel = 0

for slovo in cisty_text:
    if slovo.isalpha():
        pocet_slov +=1
    if slovo.istitle():
        pocet_titlecase += 1
    if slovo.isupper():
        pocet_uppercase += 1
    if slovo.islower():
        pocet_lowercase +=1
    if slovo.isdigit():
        pocet_cisel += 1


print(f"V textu se nachazi: {pocet_slov} slov" ,
      f"V textu se nachazi: {pocet_titlecase} velkych pismen na zacatku",
      f"V textu se nachazi: {pocet_uppercase} slov psanych velkymi pismeny",
      f"V textu se nachazi: {pocet_lowercase} slov psanych malymi pismeny",
      f"V textu se nachazi: {pocet_cisel} cisel",
      sep = "\n"
    )

print(oddelovac)

jen_slova = []
for slovo in cisty_text:
    if slovo.isalpha():
        jen_slova.append(slovo)

#jen_slova = ['Situated', 'about', 'miles', 'west', 'of', 'Kemmerer', 'Fossil', 'Butte', 'is', 'a', 'ruggedly', 'impressive', 'topographic', 'feature', 'that', 'rises', 'sharply', 'some', 'feet', 'above', 'Twin', 'Creek', 'Valley', 'to', 'an', 'elevation', 'of', 'more', 'than', 'feet', 'above', 'sea', 'level', 'The', 'butte', 'is', 'located', 'just', 'north', 'of', 'US', 'and', 'the', 'Union', 'Pacific', 'Railroad', 'which', 'traverse', 'the', 'valley']


slovnik_cetnosti ={}
for slovo in jen_slova:
    slovnik_cetnosti[len(slovo)] = slovnik_cetnosti.setdefault(len(slovo),0) +1     #jako klic beru pocet pismen, jako hodnotu do klice cetnost_vyskytu tech poctu pismen


sor = sorted(slovnik_cetnosti.items())   # list obsahujici tuply v poradi (pocet_pismen , cetnost_vyskytu)


serazeny_slovnik = dict(sor)


for key in serazeny_slovnik:
    print(f"{key} {'*' * serazeny_slovnik[key]} {serazeny_slovnik[key]}")

print(oddelovac)

jen_cisla = []
for prvek in cisty_text:
    if prvek.isdigit():
        jen_cisla.append(int(prvek))

soucet_cisel = sum(jen_cisla)

print(f"Soucet vsech cisel v textu je celkem: {soucet_cisel}")


print(oddelovac)