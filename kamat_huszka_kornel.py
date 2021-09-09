import math

c=int(input('Add meg az alaptőkét:'))
r=int(input('Éves névleges kamatláb:'))
m=12
t=int(input('Az évek száma:'))

FV=c*math.pow((1+r/m), m*t)
print('A betét értéke a futamidő végén:', FV)

# Mivel nem értek hozzá, így nem tudom megmondani, hogy az eredmény reális, így azt se tudom megmondani, hogy jól csináltam-e meg.

