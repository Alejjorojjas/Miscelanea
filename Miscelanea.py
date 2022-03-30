'''Programa que tiene 3 menus con solucion a algoritmos de:
1. Operadores
2. Condicionales 
3. Ciclos  '''
import os

controlmenuinicio = 0
controlmenu1 = 0
controlmenu2 = 0
controlmenu3 = 0

while controlmenuinicio != 99:
    os.system('cls')
    try:
        menu = int(input('''Hola... \n\n'''  
            '''Por favor seleccciona una opción \n\n''' 
            '''Programa que da solucion a algoritmos de: \n'''
            '''1. Operadores. \n'''
            '''2. Condicionales. \n'''
            '''3. Ciclos. \n'''
            '''99. Oprima 99 para salir. \n'''))
        os.system('cls')
        

        if menu == 1:
                while controlmenu1 != 99:
                    submenu1 = int ( input ('''Menú Operadores:  \n\n'''
                        '''Por Favor seleccione una opción: \n''' 
                        '''1. Calcular el área de un triángulo.  \n'''
                        '''2. Ingresar dos números y sumarlos.  \n'''
                        '''3. Ingresar un número y visualizar el número elevado al cuadrado.  \n'''
                        '''4. Convertir Euros a Dolares.  \n'''
                        '''5. Calcular el área de un cuadrado y perimetro.  \n'''
                        '''6. Determinar el área y volumen de un cilindro.  \n'''
                        '''7. Leer el radio de una circunferencia y se calcula la longitud y el área.  \n'''
                        '''8. Calcular el promedio de 3 números ingresados. \n'''
                        '''99. Oprima 99 para volver al menú anterior.  \n'''))
                    os.system('cls')

                    if submenu1 == 1:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Calcular el area de un triángulo: \n')
                            x = 0
                            base = int ( input ('Digite la base del triángulo \n'))
                            altura = int ( input ('Digite la altura del triángulo \n'))
                            x = (base * altura)/2
                            print (f'El área del triángulo es de :', x, '\n')
                            retorno = input ('''Desea hacer otro cálculo de área de un triángulo? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')

                    if submenu1 == 2:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Ingresar dos números y sumarlos: \n')
                            x = 0
                            num1 = int ( input ('Digite el primer número \n'))
                            num2 = int ( input ('Digite el segundo número \n'))
                            x = num1 + num2
                            print (f'La Suma de los números es:', x, '\n')
                            retorno = input ('''Desea hacer otra suma de dos números? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')  


                    if submenu1 == 3:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Ingresar un número y visualizar el número al cuadrado: \n')
                            x = 0
                            num1 = int ( input ('Digite el número que quiere elevar al cuadrado: \n'))
                            x = num1**2
                            print (f'El número elevado al cuadrado es:', x, '\n')
                            retorno = input ('''Desea visualizar otro número al cuadrado? \n''' 
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')              

                    if submenu1 == 4:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Convertir Euros a Dólares (1 Euro = 1.10 Dólares US): \n')
                            x = 0
                            Euros = int ( input ('Digite la la cantidad de Euros a convertir \n'))
                            x = Euros*1.10
                            print (f'',Euros,'Euros son :', x , 'Dólares US' '\n')
                            retorno = input ('''Desea hacer otra conversión de Euros? \n''' 
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')        

                    if submenu1 == 5:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Calcular el área de un cuadrado y perimetro: \n')
                            area = 0
                            perimetro = 0
                            lado = int ( input ('Digite el lado del cuadrado. \n'))
                            area = lado**2
                            perimetro = lado*4
                            print (f'El área del cuadrado es:', area , 'y el perimetro es de:', perimetro, '\n')
                            retorno = input ('''Desea hacer otro cálculo de área de un cuadrado y perimetro? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                    if submenu1 == 6:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Calcular el area de la superficie y volumen de un cilindro: \n')
                            area = 0
                            volumen = 0
                            radio = int ( input ('Digite el radio del cilindro \n'))
                            altura = int ( input ('Digite la altura del cilindro \n'))
                            area = (3,141592*2*altura*radio)+((radio**2)*3,141592*2)
                            volumen = ((radio**2) * 3.141592) * altura
                            print (f'El área del cilindro es de :', area, 'y el volumen es :', volumen, '\n')
                            retorno = input ('''Desea hacer otro cálculo de área y volumen de un cilindro \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                    if submenu1 == 7:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Leer el radio de un circulo y se calcula la longitud de circunferencia y el área: \n')
                            circunferencia = 0
                            area = 0
                            radio = int ( input ('Digite el radio del circulo \n'))
                            circunferencia = 3.141592*(radio*2)
                            area = (3.141592*radio)**2
                            print (f'El área del triángulo es de:', area, 'y la longitud de circunferencia es de:', circunferencia, '\n')
                            retorno = input ('''Desea hacer otro cálculo de longitud de circunferencia y el área de un circulo? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                    if submenu1 == 8:
                        retorno = 's'
                        while retorno == 's':
                            os.system('cls')
                            print ('Calcular el promedio de tres números: \n')
                            x = 0
                            num1 = int ( input ('Digite el primer número: \n'))
                            num2 = int ( input ('Digite el segundo número: \n'))
                            num3 = int ( input ('Digite el tercer número: \n'))
                            x = (num1+num2+num3)/3
                            print (f'El promedio de los tres números ingresados es de :', x, '\n')
                            retorno = input ('''Desea hacer otro cálculo de área de un triángulo? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                    if submenu1 == 99:
                        controlmenu1 = 99

                    if (submenu1 != 1) & (submenu1 != 2) & (submenu1 != 3) & (submenu1 != 4) & (submenu1 != 5) & (submenu1 != 6) & (submenu1 != 7) & (submenu1 != 99):
                        input('''Opción no válida \n'''
                        '''Presione Enter para continuar...''')
                        os.system('cls')

                    

        if menu == 2:
            while controlmenu2 != 99:
                submenu2=int(input('''Menú Condicionales:  \n'''
                '''Por Favor seleccione una opción: \n'''
                '''1. Algoritmo para saber si el número ingresado es positivo o negativo. \n''' 
                '''2. Algoritmo que recibe dos números y calcula cuál número es mayor y cuál es menor. \n''' 
                '''3. Algoritmo que lee 3 números enteros positivos y calcula e imprime el menor y el mayor. \n''' 
                '''4. Digite dos números A y B, sumarlos si A es menor que B o si no restarlos. \n''' 
                '''5. Digite dos números A y B, encontrar el cociente entre A y B. La división entre cero no válida. \n''' 
                '''6. Digite dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos. \n''' 
                '''7. Algoritmo que determina si un año es bisiesto. \n''' 
                '''99. Oprima 99 para volver al menú anterior.  \n'''))

                if submenu2 == 1:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Calcular si el número ingresado por el usuario es positivo o negativo: \n')
                        x= int ( input ('Digite el número \n'))
                        if x >= 0:
                            print (f'El número digitado es positivo.', '\n')
                        
                        else:
                            print (f'El número digitado es negativo.', '\n')
                            
                        retorno = input ('''Desea hacer otro cálculo de área de un triángulo? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')

                if submenu2 == 2:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Ingresar dos números y mostrar el número mayor y el número menor: \n')
                        num1 = int ( input ('Digite el primer número \n'))
                        num2 = int ( input ('Digite el segundo número \n'))
                        if num1 > num2:
                            print (f'El número:', num1, 'es mayor que ', num2, '\n')
                        
                        else:
                            print (f'El número:', num2, 'es mayor que ', num1, '\n')
                        retorno = input ('''Desea hacer otra operación de número mayor y menor? \n'''
                            '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')  


                if submenu2 == 3:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Algoritmo que lee 3 números enteros positivos y calcula e imprime el menor y el mayor: \n')
                        num1 = int ( input ('Digite el primer número: \n'))
                        num2 = int ( input ('Digite el segundo número: \n'))
                        num3 = int ( input ('Digite el tercer número: \n'))
                        mayor = 0
                        menor = 0
                        if (num1 > num2) & (num1 > num3) :
                            mayor = num1

                        if (num2 > num1) & (num2 > num3) :
                            mayor = num2

                        if (num3 > num2) & (num3 > num1) :
                            mayor = num3

                        if (num1 < num2) & (num1 < num3) :
                            menor = num1

                        if (num2 < num1) & (num2 < num3) :
                            menor = num2

                        if (num3 < num2) & (num3 < num1) :
                            menor = num3

                        print (f'El número mayor es:', mayor, 'y el número menor es:', menor, '\n')
                        retorno = input ('''Desea calcular el valor mayor o menor? \n''' 
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')              

                if submenu2 == 4:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Ingresar dos numeros y sumarlos si A es menor que B o sino restarlos): \n')
                        Resultado = 0
                        A = int ( input ('Digite numero A: \n'))
                        B = int ( input ('Digite numero B: \n'))
                        if A < B :
                            resultado = A + B
                            print (f'A + B es igual a :', Resultado, '\n')
                        else:
                            resultado = A - B
                            print (f'A - B es igual a :', Resultado, '\n')
                        retorno = input ('''Desea ingresar dos numeros y sumarlos si A es menor que B o sino restarlos? \n''' 
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')        

                if submenu2 == 5:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Digite dos números A y B, encontrar el cociente entre A y B. La división entre cero no válida: \n')
                        cociente = 0
                        a= int ( input ('Digite el número A: \n'))
                        b= int ( input ('Digite el número B: \n'))

                        if b != 0:
                            cociente = a / b
                            print (f'El cociente entre A y B es:', cociente, '\n')

                        else:
                            print ('La división entre cero no es está definida. \n')

                        retorno = input ('''Desea calcular el cociente entre dos números? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                if submenu2 == 6:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Calcular el area de un triángulo: \n')
                        resultado = 0
                        A = int ( input ('Digite numero A: \n'))
                        B = int ( input ('Digite numero B: \n'))
                        if (A < 0) | (B < 0) :
                            resultado = A + B
                            print (f'A + B es igual a :', resultado, '\n')
                        else:
                            resultado = A * B
                            print (f'A * B es igual a :', resultado, '\n')

                        retorno = input ('''Desea ingresar dos números y sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos ? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                if submenu2 == 7:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Algoritmo que determina si un año es bisiesto: \n')
                        año = int ( input ('Digite el año para saber si es bisiesto: \n'))
                        if (año % 4) == 0 :
                            print (f'El año ingresado es bisiesto' '\n')
                        
                        else:
                            print (f'El año ingresado no es bisiesto' '\n')

                        retorno = input ('''Desea determinar si un año es bisiesto? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                if submenu2 == 99:
                        controlmenu2 = 99

                if (submenu2 != 1) & (submenu2 != 2) & (submenu2 != 3) & (submenu2 != 4) & (submenu2 != 5) & (submenu2 != 6) & (submenu2 != 7) & (submenu2 != 99):
                    input('''Opción no válida \n'''
                    '''Presione Enter para continuar...''')
                    os.system('cls')

        if menu == 3:
            while controlmenu3 != 99:
                submenu3=int(input('''Menú Ciclos:  \n''' 
                    '''Por Favor seleccione una opción: \n''' 
                    '''1. Imprimir todos los multiplos de 3 que hay entre 1 y 100. \n''' 
                    '''2. Imprimir los números impares entre 0 y 100. \n''' 
                    '''3. Imprimir los números pares del 1 al 100 \n''' 
                    '''4. Algoritmo que imprime los cuadrados de los números del 1 al 30. \n''' 
                    '''5. Algoritmo que suma los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla. \n''' 
                    '''6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los numeros comprendidos entre ellos en secuencia ascendente. \n''' 
                    '''7. Sumar todos los números que se dictan mientras no sea cero. \n''' 
                    '''99. Oprima 99 para volver al menú anterior.  \n'''))


                if submenu3 == 1:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Imprimir todos los múltiplos de 3 que hay entre 1 y 100. \n')
                        input ('Presione cualquier tecla para imprimir los múltiplos: \n')
                        for i in range (3,100,3):
                            print (f'',i,  '\n')
                        retorno = input ('''Desea imprimir nuevamente los múltiplos de 3? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')

                if submenu3 == 2:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Imprimir todos números impares entre 0 y 100. \n')
                        input ('Presione cualquier tecla para imprimir los números: \n')
                        for i in range (1,100,2):
                            print (f'',i,  '\n')
                        retorno = input ('''Desea imprimir nuevamente los números impares entre 0 y 100? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')  


                if submenu3 == 3:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Imprimir todos números pares entre 1 y 100. \n')
                        input ('Presione cualquier tecla para imprimir los números: \n')
                        for i in range (2,101,2):
                            print (f'',i,  '\n')
                        retorno = input ('''Desea imprimir nuevamente los números pares entre 1 y 100? \n''' 
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')              

                if submenu3 == 4:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Algoritmo que imprime los cuadrados de los números del 1 al 30. \n')
                        input ('Presione cualquier tecla para imprimir los números: \n')
                        for i in range (1,31):
                            print (f'',i*i,  '\n')
                        retorno = input ('''Desea hacer otra conversión de Euros? \n''' 
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')        

                if submenu3 == 5:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Algoritmo que suma los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla. \n')
                        input ('Presione cualquier tecla para imprimir los números: \n')
                        suma = 0                    
                        for i in range (1,101):
                            cuadrados = i*i
                            suma = suma + cuadrados

                        print (f'La suma de los cuadrados de los cien primeros números naturales es:',suma,  '\n')
                        retorno = input ('''Desea ver la suma de los cuadrados de los cien primeros números naturales? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                if submenu3 == 6:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Imprimir todos números pares entre 1 y 100. \n')
                        input ('Presione cualquier tecla para imprimir los números: \n')
                        for i in range (2,101,2):
                            print (f'',i,  '\n')
                        print (f'El área del triángulo es de :', x, '\n')
                        retorno = input ('''Desea hacer otro cálculo de área de un triángulo? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                    
                if submenu3 == 7:
                    retorno = 's'
                    while retorno == 's':
                        os.system('cls')
                        print ('Sumar todos los números que se dictan mientras no sea cero. \n')
                        num = 1
                        acumulado = 0                    
                        while num != 0:
                            num = 0
                            num = int ( input ('Ingrese un número para sumar y cero para terminar y mostrar el resultado:' '\n' ))
                            acumulado = acumulado + num
                        print (f'La suma de los numeros ingresados es :', acumulado, '\n')
                        retorno = input ('''Desea sumar otros números? \n'''
                        '''Digite s para si o cualquier tecla para volver al menú anterior. \n''')
                                    
                if submenu3 == 99:
                    controlmenu3 = 99

                if (submenu3 != 1) & (submenu3 != 2) & (submenu3 != 3) & (submenu3 != 4) & (submenu3 != 5) & (submenu3 != 6) & (submenu3 != 7) & (submenu3 != 99):
                    input('''Opción no válida \n'''
                    '''Presione Enter para continuar...''')
                    os.system('cls')

    
        if menu == 99:
            print('Nos Vemos ... ')
            controlmenuinicio = 99

            
        if (menu != 1) & (menu != 2) & (menu != 3) & (menu != 99) :
            input('''Opción no válida \n'''
            '''Presione Enter para continuar...''')
            os.system('cls')
    
    except:
        input('''Opción no válida \n'''
        '''Por favor digita un número. \n'''
        '''Presione Enter para continuar.....''')
        os.system('cls')


