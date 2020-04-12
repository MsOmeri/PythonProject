sayi=int((input('sayi giriniz:')))
fak = 1
while int(sayi) > 0:
  fak *= sayi
  sayi = sayi-1
print(fak)


def rec_fac(r):
    if r==1 or r==0:
        return 1

    return rec_fac(r-1)*r
