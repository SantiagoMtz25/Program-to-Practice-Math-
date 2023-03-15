import random
from statistics import mean, median
from fractions import Fraction


def validar_input(mensaje):
    entrada = ""
    while True: 
        try: 
            entrada = eval(input(mensaje))
            break
        except: 
            print("Por favor introduce un número válido. ")
            continue 
    
    return entrada


def main():
    puntos = 0 
    p = 0
    a, b, c, d = 0, 0, 0, 0
    print("Bienvenido a tu página de repaso de matématicas")
    print("Nota: Introduzca sus respuestas dentro de los menus como números. ") 

    while True:
        print("Teclea el tema que deseas practicar: ")
        print("1-Arítmetica")
        print("2-Fracciones")
        print("3-Probabilidad y estadística")
        print("4-Conversiones de unidades")
        print("5-Salir")
        while True: 
            try: 
                n = int(input("Introduce una opción del menú: "))
                if n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
                    break   
                print("Las opciones válidas son 1, 2, 3, 4 o 5. ")
            except: 
                print("Error: Introduce un número válido. ")

        if n == 1:
            p = ej1()
            a = p 
            puntos += p
        elif n == 2: 
            p = ej2()
            b = p 
            puntos += p
        elif n == 3:
            p = ej3()
            c = p 
            puntos += p
        elif n == 4: 
            p = ej4()
            d = p
            puntos += p
        elif n == 5: 
            print("Gracias por participar. ")
            matriz(a, b, c, d, puntos)
            return


def suma_fun(a):
    corr = 0 
    puntos = 0 
    for i in range(10):
        n1 = random.randint(1,a)
        n2 = random.randint(1,a)
        suma = n1 + n2 
        bien = False
        
        for j in range(2):
            print("Cuál es la suma de",n1,"+",n2,":")
            resp = validar_input("Teclee la respuesta: ")
                    
            if resp == suma:  
                bien = True
                print("Correcto.")
                break
            else:
                print("Incorrecto. ")
    
        if bien:
            corr += 1 
        else: 
            print("Agotaste todos los intentos. ")

        if corr == 3:
            puntos += 1
        elif corr == 7:
            puntos += 1 
        elif corr == 10:
            puntos += 2

    return puntos


def resta_fun(a):
    corr = 0 
    puntos = 0 
    for i in range(10):
        n1 = random.randint(1,a)
        n2 = random.randint(1,a)
        resta = n1 - n2 
        bien = False
        
        for j in range(2):
            print("Cuál es la suma de",n1,"-",n2,":")
            resp = validar_input("Teclee la respuesta: ")
                    
            if resp == resta:  
                bien = True
                print("Correcto.")
                break
            else:
                print("Incorrecto. ")

        if bien:
            corr += 1 
        else: 
            print("Agotaste todos los intentos. ")

        if corr == 3:
            puntos += 1
        elif corr == 7:
            puntos += 1 
        elif corr == 10:
            puntos += 2

    return puntos


def mult_fun(a):
    corr = 0 
    puntos = 0 
    for i in range(10):
        n1 = random.randint(1,a)
        n2 = random.randint(1,a)
        multiplicacion = n1 * n2
        bien = False

        for j in range(2):
            print("Cuál es la multiplicación de",n1,"x",n2,":")
            resp = validar_input("Teclee la respuesta: ")

            if resp == multiplicacion:  
                bien = True
                print("Correcto.")
                break
            else:
                print("Incorrecto. ")

        if bien:
            corr += 1 
        else: 
            print("Agotaste todos los intentos. ")

        if corr == 3:
            puntos += 1
        elif corr == 7:
            puntos += 1 
        elif corr == 10:
            puntos += 2
        
    return puntos


def div_fun(a,b):
    corr = 0 
    puntos = 0 
    for i in range(10):
        n1 = random.randint(1,a)
        n2 = random.randint(1,b)
        division = n1 / n2
        bien = False

        for j in range(2):
            print("Cuál es la division de",n1,"%",n2,":")
            resp = validar_input("Teclee la respuesta (redonde su resultado a dos decimales): ")

            if resp == round(division,2):  
                bien = True
                print("Correcto.")
                break
            else:
                print("Incorrecto. ")

        if bien:
            corr += 1 
        else: 
            print("Agotaste todos los intentos. ")

        if corr == 3:
            puntos += 1
        elif corr == 7:
            puntos += 1 
        elif corr == 10:
            puntos += 2  

    return puntos


def mode(lista):
    frequency = {}

    for valor in lista:
        frequency[valor] = frequency.get(valor, 0) + 1

    most_frequent = max(frequency.values())

    moda = [llave for llave, valor in frequency.items() if valor == most_frequent]

    return moda


def esta_fun(a,b):
    puntos = 0 
    l2= []
    for i in range(a):
        lista = []
        for j in range(a):
            lista.append(random.randint(1,b))

        l2.append(lista)

    print("Analiza la siguiente serie de datos y obten la media, mediana y moda. ")
    print("Si la moda se repite escribe los dos número que se repiten en orden ascendente ¡Con un solo espacio entre ellos! ")
    print(*l2, sep="\n")

    ll = []

    for i in l2:
        for j in i:
            ll.append(j)

    media = round(mean(ll), 2)
    mediana = round(median(ll), 2)
    moda = mode(ll)
    moda.sort()
    l = " ".join([str(f) for f in moda])

    
    for i in range(2):
        r1 = validar_input("Cuál es la media (redondea tu respuesta a dos decimales): ")
        if r1 == media:
            puntos += 1 
            print("Correcto. ")
            break 
        else: 
            print("Incorrecto. ")

    for i in range(2):
        r2 = validar_input("Cuál es la mediana: ")
        if r2 == mediana:
            puntos += 1 
            print("Correcto. ")
            break
        else:
            print("Incorrecto. ")

    for i in range(2):
        r3 = str(input("Cuál es la moda: "))
        if r3.strip() == l:
            puntos += 1 
            print("Correcto. ")
            break
        else:
            print("Incorrecto. ")

    return puntos


def ej1():
    puntos = 0
    p = 0
    print("""
Bienvenido a aritmética obtendras 1 puntos por 3 respuetas correctas y 1 más por 7 respuetas correctas, 
y obtendrás 2 más si tienes 10 respuestas correctas. 

Tendrás dos oportunidades por respuesta. 
""")
    while True:
        print("Qué deseas practicar 1-Sumas, 2-Restas, 3-Multiplicaciones, 4-Divisiones")
        while True: 
            n = validar_input("Introduce una opción del menú: ")
            if n == 1 or n == 2 or n == 3 or n == 4: 
                break
            print("Las opciones válidas son 1, 2, 3 o 4. ")

        if n == 1: 
            print("Suma")
            while True: 
                r = validar_input("Que dificultad desea obtener: 1-fácil, 2-intermedio, 3-difícil: ")
                if r == 1 or r == 2 or r == 3:                             
                    break
                print("Las opciones válidas son 1, 2, o 3. ")

            if r == 1: 
                ran = 10
                p = suma_fun(ran)
                puntos += p 

            elif r == 2: 
                ran = 100
                p = suma_fun(ran)
                puntos += p 

            elif r == 3: 
                ran = 1000
                p = suma_fun(ran)
                puntos += p 

        elif n == 2:
            print("Resta")
            while True: 
                r = validar_input("Que dificultad desea obtener: 1-fácil, 2-intermedio, 3-difícil: ")
                if r == 1 or r == 2 or r == 3:                             
                    break
                print("Las opciones válidas son 1, 2, o 3. ")
            
            if r == 1: 
                ran = 10
                p = resta_fun(ran)
                puntos += p 

            elif r == 2: 
                ran = 100
                p = resta_fun(ran)
                puntos += p 

            elif r == 3: 
                ran = 1000
                p = resta_fun(ran)
                puntos += p 

        elif n == 3: 
            print("Multiplicación")
            while True: 
                r = validar_input("Que dificultad desea obtener: 1-fácil, 2-intermedio, 3-difícil: ")
                if r == 1 or r == 2 or r == 3:                             
                    break
                print("Las opciones válidas son 1, 2, o 3. ")
            
            if r == 1: 
                ran = 10 
                p = mult_fun(ran)
                puntos += p 

            elif r == 2: 
                ran = 50 
                p = mult_fun(ran)
                puntos += p 
        
            elif r == 3: 
                ran = 100
                p = mult_fun(ran)
                puntos += p 

        elif n == 4: 
            print("Division")
            while True: 
                r = validar_input("Que dificultad desea obtener: 1-fácil, 2-intermedio, 3-difícil: ")
                if r == 1 or r == 2 or r == 3:                             
                    break
                print("Las opciones válidas son 1, 2, o 3. ")

            if r == 1: 
                ran = 20 
                ran2 = 5 
                p = div_fun(ran, ran2)
                puntos += p 

            elif r == 2: 
                ran = 50
                ran2 = 10 
                p = div_fun(ran, ran2)
                puntos += p 

            elif r == 3: 
                ran = 100
                ran2 = 10
                p = div_fun(ran, ran2) 
                puntos += p 

        respuesta = str(input("Désea practicar de nuevo u practicar otro ejercicio [Si/No]: ")).lower().strip()
        if respuesta[0] == "s":
            continue
        else: 
            break
            
    return puntos


def ej2():
    puntos = 0
    print("Bienvenido a fracciones. ")
    print("""
Si obtienes tres respuestas correctas sumaras un punto, si obtienes cinco correctas sumarás otro. 
Tendrás dos oportunidades por respuesta. 
    """)
    while True: 
        print("""Qué deseas practicar: 
1-suma de fracciones 
2-resta de fracciones 
3-multiplicación de fracciones
4-división de fracciones
5-comparar fracciones
    """)
        while True: 
            n = validar_input("Introduce una opción del menú: ")
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5: 
                break
            print("Las opciones válidas son 1, 2, 3, 4 o 5. ")

        if n == 1: 
            corr = 0  
            for i in range(5):
                bien = False
                num1, num2, den1, den2 = [random.randint(2, 9) for i in range(4)]
                sign = "+"
                print(f"{num1}   {num2}\n- {sign} - = \n{den1}   {den2}\n")

                a = Fraction(num1,den1)
                b = Fraction(num2,den2)
                suma = a + b 
                
                for i in range(2):
                    respuesta = input("Introduce tu respuesta en formato a/b: ")
                    respuesta = Fraction(respuesta.strip())
                    if respuesta == suma:
                        bien = True
                        print("Correcto. ")
                        break
                    else:
                        print("Incorrecto, vuelve a intentar. ")

                if bien: 
                    corr += 1
                else: 
                    print("Agotaste todos los intentos disponibles. ")

                if corr == 3: 
                    puntos += 1 
                elif corr == 5: 
                    puntos += 1

        if n == 2: 
            corr = 0 
            for i in range(5):
                bien = False
                num1, num2, den1, den2 = [random.randint(2, 9) for i in range(4)]
                sign = "-"
                print(f"{num1}   {num2}\n- {sign} - = \n{den1}   {den2}\n")

                a = Fraction(num1,den1)
                b = Fraction(num2,den2)
                resta = a - b 

                for i in range(2):
                    respuesta = input("Introduce tu respuesta en formato a/b: ")
                    respuesta = Fraction(respuesta.strip())
                    if respuesta == resta:
                        bien = True
                        print("Correcto. ")
                        break
                    else:
                        print("Incorrecto, vuelve a intentar. ")

                if bien: 
                    corr += 1
                else: 
                    print("Agotaste todos los intentos disponibles. ")

                if corr == 3: 
                    puntos += 1 
                elif corr == 5: 
                    puntos += 1

        if n == 3: 
            corr = 0
            for i in range(5):
                bien = False
                num1, num2, den1, den2 = [random.randint(2, 9) for i in range(4)]
                sign = "x"
                print(f"{num1}   {num2}\n- {sign} - = \n{den1}   {den2}\n")

                r = [str(num1 * num2), str(den1 * den2)]

                for i in range(2):
                    respuesta = input("Introduce tu respuesta en formato a/b: ")
                    respuesta = respuesta.strip().split("/")
                    if respuesta == r:
                        bien = True 
                        print("Correcto!")
                        break
                    else: 
                        print("Incorrecto, vuelve a intentar. ")

                if bien: 
                    corr += 1
                else: 
                    print("Agotaste todos los intentos disponibles. ")

                if corr == 3: 
                    puntos += 1 
                elif corr == 5: 
                    puntos += 1

        if n == 4:
            corr = 0  
            for i in range(5):
                bien = False
                num1, num2, den1, den2 = [random.randint(2, 9) for i in range(4)]
                sign = "÷"
                print(f"{num1}   {num2}\n- {sign} - = \n{den1}   {den2}\n")

                r = [str(num1 * den2), str(num2 * den1)]

                for i in range(2):
                    respuesta = input("Introduce tu respuesta en formato a/b: ")
                    respuesta = respuesta.strip().split("/")
                    if respuesta == r:
                        bien = True 
                        print("Correcto!")
                        break
                    else: 
                        print("Incorrecto, vuelve a intentar. ")

                if bien: 
                    corr += 1
                else: 
                    print("Agotaste todos los intentos disponibles. ")

                if corr == 3: 
                    puntos += 1 
                elif corr == 5: 
                    puntos += 1

        if n == 5: 
            corr = 0 
            for i in range(5):
                bien = False
                num1, num2, den1, den2 = [random.randint(2, 9) for i in range(4)]
                sign = ["<",">"]
                sign_elegido = random.choice(sign)
                print(f"{num1}   {num2}\n- {sign_elegido} - = \n{den1}   {den2}\n")

                a = Fraction(num1,den1)
                b = Fraction(num2,den2)

                while True: 
                    respuesta = input("Introduce tu respuesta en formato (verdadero/falso): ").lower()
                    if not respuesta in ["verdadero", "falso"]:
                        print("Escribe una opción válida. ")
                        continue 
                    else: 
                        break

                if sign_elegido == "<":
                    if (respuesta == "verdadero") == (a<b):
                        bien = True 
                        print("Correcto. ")
                    else: 
                        print("Incorrecto. ")
                elif sign_elegido == ">":
                    if (respuesta == "verdadero") == (a>b):
                        bien = True 
                        print("Correcto. ")
                    else: 
                        print("Incorrecto. ")

                if bien:
                    corr += 1 
                else:
                    ("Agotaste todos los intentos")
                
                if corr == 3: 
                    puntos += 1 
                elif corr == 3: 
                    puntos += 1 

        respuesta = str(input("Désea practicar de nuevo u practicar otro ejercicio [Si/No]: ")).lower().strip()
        if respuesta[0] == "s":
            continue
        else: 
            break

    return puntos
            

def ej3():  
    puntos = 0 
    p = 0 
    print("Probabilidad y estadística")
    print("""
        
    Para resumir un conjunto de datos numéricos podemos utilizar la media aritmética, la mediana o la moda. 
    En esta aplicación vamos a conocer un poco mejor la media aritmética y la mediana de conjunto de datos.

    La media es el valor que correspondería a cada uno de los datos de la distribución si su suma total se repartiera por igual.
    Si se ordenan todos los datos, de menor a mayor, la mediana es el valor que ocupa la posición central. 
    Si el número de datos es par, la mediana es la media aritmética de los dos centrales.
    La moda es el valor que más se repite o, lo que es lo mismo.
        """)
    print("""
En estos ejercicios sumarás un punto por cada respuesta correcta. 
Tendrás dos oportunidades por respuesta. 

        """)
    while True: 
        while True: 
            r = validar_input("Que dificultad desea obtener: 1-fácil, 2-intermedio, 3-difícil: ")
            if r == 1 or r == 2 or r == 3:                             
                break
            print("Las opciones válidas son 1, 2, o 3. ")

        if r == 1: 
            ran = 3 
            ran2 = 10
            p = esta_fun(ran,ran2)
            puntos += p

        elif r == 2: 
            ran = 4 
            ran2 = 100
            p = esta_fun(ran,ran2)
            puntos += p 

        elif r == 3:
            ran = 5 
            ran2 = 1000
            p = esta_fun(ran,ran2) 
            puntos += p

        resp = str(input("Quierer realizar otro ejercicio [Si/No]: ")).lower().strip()
        if resp[0] == "s":
            continue
        else: 
            break

    return puntos


def conv_unidades(num, unidad1, unidad2, sistema = 0, resp = 0): 

    print(f"Convierte {num} {unidad1} a {unidad2}:")

    if resp == 0: 
        resp = obtener_conversion(sistema, num, unidad1, unidad2)

    bien = False
    for i in range(2):
        respuesta = validar_input("Cúal es la respuesta (redondea tu respuesta a 6 decimales): ")
        if respuesta == round(resp, 6): 
            bien = True  
            print("Correcto. ")
            break 
        else: 
            print("Incorrecto. ")

    return bien


def obtener_conversion(sistema, num, unidad1, unidad2):
    if unidad1 == unidad2: 
        return num

    return num * (sistema[unidad1]/sistema[unidad2])


def ej4():
    print("Sistema métrico y sistema imperial")
    print("""
Bienvenido obtendras 1 puntos por 3 respuetas correctas y 1 más por 7 respuetas correctas, 
y obtendrás 2 más si tienes 10 respuestas correctas. 

Tendrás dos oportunidades por respuesta. 

    """)
    puntos = 0
    while True: 
        while True: 
            r = validar_input("Que quiere practicar 1-Sistema Métrico, 2-Sistema Imperial, 3-Conversión entre sistemas: ")
            if r == 1 or r == 2 or r == 3:                             
                break
            print("Las opciones válidas son 1, 2, o 3. ")

        metrico = {'mm':0.001, 'cm': 0.01, 'm': 1, 'km':1000}
        imperial = {'pulgadas': 1, 'pies': 12, 'yardas': 36, 'millas': 63360}

        if r == 1:
            corr = 0 
            for i in range(10):
                n = random.randint(1,100) 
                unidades = random.sample(list(metrico),2)
                n1 = conv_unidades(n, unidades[0], unidades[1], metrico)
                if n1:
                    corr += 1 
                
            if corr == 3: 
                puntos += 1
            elif corr == 7: 
                puntos += 1
            elif corr == 10: 
                puntos += 2 

        elif r == 2: 
            corr = 0 
            for i in range(10):
                n = random.randint(1,100)
                unidades = random.sample(list(imperial),2)
                n1 = conv_unidades(n, unidades[0], unidades[1], imperial)
                if n1:
                    corr += 1 
                
            if corr == 3: 
                puntos += 1
            elif corr == 7: 
                puntos += 1
            elif corr == 10: 
                puntos += 1 

        elif r == 3: 
            corr = 0 
            for i in range(10):
                n = random.randint(1,100)
                unidad_m = random.choice(list(metrico))
                unidad_i = random.choice(list(imperial))
                
                resp = obtener_conversion(imperial, obtener_conversion(metrico, n, unidad_m, 'cm')/2.54, 'pulgadas', unidad_i)
                n1 = conv_unidades(n, unidad_m, unidad_i, resp = resp)
                if n1:
                    corr += 1
                
            if corr == 3: 
                puntos += 1
            elif corr == 7: 
                puntos += 1
            elif corr == 10: 
                puntos += 1 

        resp = str(input("Quiere realizar otro ejercicio [Si/No]:")).lower().strip()
        if resp[0] == "s":
            continue 
        else: 
            break
    
    return puntos 

    
def matriz(a, b, c, d, puntos):
    lista = [["Participante 1", "Puntos"],
             ["Sección 1:       ", a],
             ["Sección 2:       ", b],
             ["Sección 3:       ", c],
             ["Sección 4:       ", d],
             ["Total puntos:    ", puntos]]

    print(*lista, sep="\n")


main()