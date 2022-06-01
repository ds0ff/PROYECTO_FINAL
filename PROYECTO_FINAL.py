import random as r
import numpy as np

def dado():
    a = r.randrange(1,7)
    return a

def juego(): 
    cant_j = int(input('Ingrese el numero de jugadores:\n '))
    apuesta = int(input('Ingrese el valor inicial de la apuesta:\n '))
    
    jugadores = list(np.arange(1,cant_j+1))
    l = {}
    for jugador in jugadores:
        n= 5000-apuesta
        l[jugador] = n 
        
    if apuesta < 100:
        int(input('El valor inicial debe ser mayor a 100, ingrese un nuevo valor inicial de la apuesta:\n '))
    
    pozo= cant_j * apuesta    
    
    casino = []
    turnos = 1
 
    while pozo>0:
        lan1 = dado()
        lan2 = dado()

        print(l)
        print(' ')
        
        if turnos>cant_j:
            turnos = 1
            print(' ')
        
        
        print('jugador',turnos)
        print('Primer lanzamiento: ',lan1)
        comision = 0.05
        

        if lan1 == 1:
            print("Perdiste la apuesta")
            pozo += apuesta
            print ('Pozo:',pozo)
            l[turnos] -= apuesta

        if lan1 == 6:
            print("Ganaste la apuesta")
            casino_alerta2 = apuesta*comision
            l[turnos] -= casino_alerta2
            l[turnos] += apuesta
            casino.append(casino_alerta2)
            casino = [sum(casino)]
            pozo -= apuesta
            print('Pozo', pozo)

        if 1<lan1<6:
            apuesta2 = int(input(f'Ingrese el valor a apostar que no sea mayor a {min(int(pozo),l[jugador])}: '))
            casino_alerta = apuesta2*comision
            print ('Segundo lanzamiento: ',lan2)
            
            if lan1<lan2:
                print("Ganaste la apuesta") 
                l[turnos] -= casino_alerta
                l[turnos] += apuesta2
                casino.append(casino_alerta)
                casino = [sum(casino)]
                pozo -= apuesta2
                print('Pozo:', pozo)

            elif pozo<apuesta:
                print('Error, la apuesta es mayor que pozo')
                print('Pozo:',pozo)
            
            if lan1>=lan2:
                print("Perdiste la apuesta")
                pozo = pozo+apuesta2
                print('Pozo:',pozo)
                l[turnos] -= apuesta2
                
        if l[turnos] <= 0:
            l.pop(turnos)
            print('Pozo:', int(pozo))
            print('Fin del juego')
            print('Ganancia de jugadores:',l)
            break

        if pozo <= 0:
            print('Pozo:', int(pozo))
            print('Fin del juego')
            
        turnos+=1

            
        print ('Casino: ',casino)
        print(' ') 

            


    return casino
