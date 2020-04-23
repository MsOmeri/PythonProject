i=1
j=1

while i <= 10:
    while j <= 10:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    j = 1
    i += 1
    print('--------------------------')
