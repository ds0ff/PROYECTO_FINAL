import random as r
def dado():
    a = r.randrange(1,7)
    return a

def juego(): 
    cant_j = int(input('Ingrese el numero de jugadores:\n '))
    apuesta = int(input('Ingrese el valor inicial de la apuesta:\n '))
    

    jugadores = list(range(1,cant_j+1))
    l = {}
    for jugador in jugadores:
        n= 5000-apuesta
        l[jugador] = n 
    
    pozo= cant_j * apuesta    
    turno = 1
    
    casino = []
    
    while pozo>0:
        lan1 = dado()
        lan2 = dado()
        
        print(l)
        print(' ')
        
        print('jugador',turno)
        print('Primer lanzamiento: ',lan1)
        comision = 0.05
 
        
        if lan1 == 1:
            print("Perdiste la apuesta")
            pozo += apuesta
            print ('Pozo:',pozo)
            l[turno] -= apuesta
            
        if lan1 == 6:
            print("Ganaste la apuesta")
            casino_alerta2 = apuesta*comision
            l[turno] -= casino_alerta2
            l[turno] += apuesta
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
                l[turno] -= casino_alerta
                l[turno] += apuesta2
                casino.append(casino_alerta)
                casino = [sum(casino)]
                pozo -= apuesta2
                print('Pozo', pozo)
            
            elif pozo<apuesta:
                print('Error, la apuesta es mayor que pozo')
                print('Pozo:',pozo)
                
            if lan1>=lan2:
                print("Perdiste la apuesta")
                pozo = pozo+apuesta2
                print('Pozo:',pozo)
                l[turno] -= apuesta2
                
            
        if turno>=cant_j:
            turno = 0
            print(' ')
            
        if pozo <= 0 :
            print('Pozo:', int(pozo))
            print('Fin del juego')
        
        turno+=1 
        
        print ('casino: ',casino)
        print(' ')
    
        if l[jugador] == 0:
            l.popitem()
            

