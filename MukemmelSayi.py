sayi = int(input("Sayiyi giriniz: "))
i=1
toplam=0
while i < sayi:
    if sayi%i == 0:
        toplam += i
        i += 1

if toplam == sayi:
    print('Sayi mukemmel sayidir')

print('Sayi mukemmel sayi degildir')

    
