class ScoreRange:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return 'Nombre: ' + self.name + ', Puntuacion: ' + str(self.score)


puntuacion1 = ScoreRange('Pepe',140)
puntuacion2 = ScoreRange('Juan',100)
puntuacion3 = ScoreRange('Mario',80)

arrayObjetos = [puntuacion1,puntuacion2,puntuacion3]

#for i in arrayObjetos:
   # print (i)
    
class Board:
    def __init__ (self):
        self.contain = []
    
    def add (self,record):
        self.contain.append(record)
        
    def __str__(self):
        if len(self.contain) == 0:
            return 'No hay puntajes'
        else:
            result = ''
            for i in self.contain:
                result+= str(i) + '\n'
            return result
    

board_1 = Board()

board_1.add(puntuacion1)
board_1.add(puntuacion2)
board_1.add(puntuacion3)

print(board_1) 
    

   

    
    
