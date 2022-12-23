def Rice():
    print("List of Rice --> ")
    print(''' 1.Basmati Rice
2.Kaali Moonch
3.Kolam
4.HMT
5.Aambe Mohar
6.Masoori
7.Sugandhi Chinor
    ''')

def Multigrain():
    print("List of Multigrains --> ")
    print('''1.Whole Wheat
2.Chana Dal 
3.Jowar
4.Ragi
5.Oats
6.Maize
7.Soya bean
8.Bajra

''')

def DryFruits():
    print("List of Dry Fruits --> ")
    print('''1.Cashew
2.Badam
3.Khurma
4.Jaddalu
5.Anjir
6.Khismis
7.Lal Manuka
8.Kala Manuka
9.Godambi
10.Chilguja
11.Khobra
12.Pista
13.Charoli

''')

def Spices():
    print("List of Masalas -->")
    print('''1.Kalmi
2.Shahajire
3.Sunth
4.Mire
5.Lavang
6.Baaja
7.Dagad Ful
8.Tejpan
9.Bhendi Vilaychi
10.Vilaychi
11.Jayfal
12.Jaypatri
13.Trifala
14.Rampatri

''')




print("Enter R for List of Rice,M for List of Multigrains,D for List of Dryfruits,S for List of Spices")
a = input("Enter choice(R/M/D/S):")
match a:
    case "R" | "r":
        Rice()
    case 'M'|'m':
        Multigrain()
    case 'D'|'d':
        DryFruits()
    case 'S'|'s':
        Spices()
    case _:
        print("Enter a letter from given choices.................")
    
    
    
