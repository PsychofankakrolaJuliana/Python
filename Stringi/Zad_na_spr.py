# Stringi/Zad_na_spr.py

# Zad.1
# n=input("Napisz napis: ")
# m=list(n)
# y=m.pop()
# x=m[0]
# print(x," ",y)

# Zad.2
# napis=input("Napisz napis: ")
# n=list(napis)
# for i in range(1,len(n)-1):
#   print(n[i])

# Zad.3
# napis=input("Napisz napis: ")
# n=list(napis)
# x=n.reverse()
# for i in range(0,4):
#   print(x[i])

# Zad.4
# napis=input("Napisz napis: ")
# suma=0
# T=list(napis)
# for i in range(len(T)):
#   suma=suma+ord(T[i])
# print(suma)

# Zad.5
# ilo=0
# ilo2=0
# napis=input("Napisz napis: ")
# T=list(napis)
# x=""
# for i in range(len(T)):
#   for j in range(len(T)):
#     if T[i]==T[j]:
#       ilo+=1
#     if ilo>ilo2:
#       ilo2=ilo
#       x=T[i]
# print(x)