birler = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
def yazilis(sayi):
    print(onlar[int(sayi[0])-1],birler[int(sayi[1])-1])
sayi = input("Sayı:")
yazilis(sayi)