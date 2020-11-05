#!/usr/bin/env python
# coding: utf-8

# In[ ]:


opcion = 0

def menu():
    opc = int(input("Menu Principal \n" +
                    "1. Numero par o impar \n" +
                    "2. Factorial \n" +
                    "3. Numero primo o no \n" +
                    "4. Raiz cuadrada \n" +
                    "5. multiplicacion \n" +
                    "6. Finalizar  \n" +
                    "Elija una Opcion :) \n")) 
    return opc
#fin funcion menu

def numeroPar_o_Impar(numero):
    if numero % 2 == 0:
        print('El número', numero, 'es par.')
    else:
        print('El número', numero, 'es impar.')    
#fin funcion numero para o impar
        
def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):  
        fact = fact * i 
      
    print ("el factorial de ", numero ," es: ", fact) 
#fin funcion factorial

def esPrimo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True                    
 #fin funcion esPrimo    
    
def numeroPrimo_o_No(numero):
    if esPrimo(numero) == True:
        print('es primo el: ', numero)  #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, ...
    else:
        print('no es primo: ', numero)  #4, 6, 8, 9, 10 ...
#fin funcion numero primo o no        
        
def raizCuadrada(numero):
    if numero >= 0:
        resultado = numero ** (1/2)  #con la biblioteca math se puede math.sqrt() debe import math 
        print("la raiz cuadrada es: ", resultado)   
 #fin funcion raiz cuadrada

        
def multiplicacion(numero1, numero2):
     return numero1 * numero2

    
while opcion != 6:
    opcion = menu()
    if opcion == 1:
        numero = int(input("digite un numero: \n"))
        numeroPar_o_Impar(numero)
        
    if opcion == 2:
        numero = int(input("digite un numero: \n"))
        factorial(numero)
         
    if opcion == 3:
        numero = int(input("digite un numero: \n"))
        numeroPrimo_o_No(numero)
        
    if opcion == 4:
        numero = int(input("digite un numero: \n"))
        raizCuadrada(numero)
        
    if opcion == 5:
        numero1 = int(input("digite un numero: \n"))  
        numero2 = int(input("digite un numero: \n"))
        resultado = multiplicacion(numero1, numero2)
        print("el resultado de la multiplicacion es: ", resultado)
        
    if opcion == 6:    
        print("Programa terminado")
        
    if opcion > 6:
        print("opcion invalida") 


# In[ ]:




