a=int(input("digite un numero"))
div=0
i=0
while i<a:
    i=i+1
    if a%i==0:
        div=div+1
if div>2:
    print("el numero es primo")
else:
    print("el numero no es primo")
