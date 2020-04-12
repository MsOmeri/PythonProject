sayi=int(input("sayigir: "))

fibbo=[1,1]
i=2
while i < sayi:
  siradaki=fibbo[i-1]+fibbo[i-2]
  fibbo.append(siradaki)
  i += 1
print(fibbo)


def rec_fibbo()
