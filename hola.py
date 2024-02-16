while True:
    try:
        n=int(input("Ingresa un numero entero: "))
        if n < 2:
            print( "no es primo")
            break
        for i in range(2, n):
            if n % i == 0:
                print( "no es primo",i,"es divisor")
                break
        print("es primo")
        break
    except:
        print("Debes ingresar un numero entero")
        
    

