import numbers

def calcularTipoTriangulo(numeros_ingresados):
    a = numeros_ingresados.pop()
    b = numeros_ingresados.pop()
    c =numeros_ingresados.pop()
    if a == b == c: 	
        print("Triangulo equilateral") 
        return
    if (a==b) or (b==c) or (c==a): 	
        print("Triangulo isosceles") 
        return
    else: 	
        print("Triangulo escaleno") 


numbers = []
cont = 0
contador = 0 
bandera = True

while bandera:
    print("Ingresa valores de A, B y C: ") 
    x = input("Entrada: ")
    try:
        val = int(x)
        if (val == None) or (val == 0) or (1 > val) or (val > 200):
            print("Dato invalido")
        elif (1 <= val):
            if (val <= 200):
                    numbers.insert(cont, val)
                    cont+=1
                    if (cont == 3):
                        calcularTipoTriangulo(numbers)
                        bandera = False
    except ValueError:
        print("Dato invalido")