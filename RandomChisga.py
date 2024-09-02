import random

#Clases 
class Musicos():
    musicos = [1,2,3,4,5,6,7,8,9,10]
    
class Instrumentos():
    instrumentos = ['Guitarra', 'Piano', 'Violín', 'Flauta', 'Batería', 'Bajo', 'Saxofón', 'Trompeta', 'Teclado', 'Clarinete']

#Funcion random
def randomizar(lista):
    num = random.randrange(0, len(lista))
    return lista[num]

#main
def main():
    
    print('---GENERADOR CHIZGA ALEATORIA---\n')
    
    #Objetos
    musicians = Musicos()
    instruments = Instrumentos()
    
    aux=1
    
    op = 1
    while op!=0:

        print('CHIZGA NUMERO: ',aux,'\n')
        num_musicos = randomizar(musicians.musicos)
        
        print(f'El numero de musicos para su banda es: {num_musicos} \n')
        
        for i in range(1,num_musicos+1):
            print(f'Musico numero: {i} Instrumento: {randomizar(instruments.instrumentos)} ')
        
        aux+=1
        op=int(input('\nSeleccone: \n0. cerrar \n1. reiniciar\n'))
        
    print('GRACIAS POR USAR NUESTRO PROGRAMA')
          
if __name__=='__main__':
    main()
