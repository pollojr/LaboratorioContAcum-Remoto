a=int(input("digite un numero"))
div=0
for i in range(1,a+1):
    if a%i==0:
        div=div+1
if div>2:
    print("el numero no es primo")
else:
    print("el numero es primo")

    
