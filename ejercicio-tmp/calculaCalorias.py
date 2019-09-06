bandera = True

while bandera:
    print("Sistema para medir TMB------------------------------------------------")
    entrada = input("Ingresa su peso (en kilogramos): ")
    try:
        peso = int(entrada)
        if (peso > 400) or (peso < 1) or (peso == None):
            print("El valor que ingresaste como PESO es incorrecto.")
        else:
            entrada = input("Ingresa su altura (en centimetros): ")
            altura = int(entrada)
            if (altura > 300) or (altura < 1) or (altura == None):
                print("El valor que ingresaste como ALTURA es incorrecto.")
            else:
                actividad = input("Ingresa tu nivel de actividad (Ingrese 'A' para alto, 'M' para medio y 'B' para bajo):    ").upper()
                if actividad == "A":
                    actividad = "Alta"
                elif actividad == "M":
                    actividad = "Media"
                elif actividad == "B":
                    actividad = "Baja"
                else: 
                    print("Haz ingresado un nivel de actividad inválido")
                genero = input("Ingrese su género: (Ingrese 'M' para másculino 'F' para femenino) ").upper()
                if genero == "M":
                    genero = "Masculino"
                elif genero == "F":
                    genero = "Femenino"
                else: 
                    print("Has ingresado un género inválido")
                entrada = input("Ingrese el número de días que ejercita a la semana:  ").upper()
                dias = int(entrada)
                if (dias > 7) or (dias < 1) or (dias == None):
                    print("El valor que ingresaste como días de actividad es incorrecto.")
                else: 
                    print("Corre función")
    except ValueError:
            print("Dato ingresado no es valido")