import turtle
import time
import random

posponer = 0.1
marcador = 0
record = 0

#Ventana
window = turtle.Screen()
window.title('Serpiente')
window.bgcolor('#daa89b')
window.setup(width = 480, height = 480)
window.tracer(0)

#Serpiente cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('#52796f')

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(random.randint(-240, 240),random.randint(-240, 240))
comida.color('#169873')

#Serpiente cuerpo
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color('#ae847e')
texto.penup()
texto.hideturtle()
texto.goto(0, 205)
texto.write('Puntuacion: 0    Record: 0', align = 'center', font = ('Courier', 18, 'bold'))

#Funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    elif cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    elif cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    elif cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)   
        
#Teclado
window.listen()
window.onkeypress(arriba, 'Up')
window.onkeypress(abajo, 'Down')
window.onkeypress(izquierda, 'Left')
window.onkeypress(derecha, 'Right')                     

while True:
    window.update()
    #Colision comida
    if cabeza.distance(comida) < 20:
        comida.goto(random.randint(-230, 230),random.randint(-230, 230))
        
        newSegmento = turtle.Turtle()
        newSegmento.speed(0)
        newSegmento.shape('square')
        newSegmento.penup()
        newSegmento.color('#d4e09b')
        segmentos.append(newSegmento)
        
        marcador += 100
        if marcador > record:
            record = marcador
            
        texto.clear()    
        texto.write('Puntuacion: {}    Record: {}'.format(marcador, record), align = 'center', font = ('Courier', 18, 'bold'))        

    #Colision bordes
    if cabeza.xcor() > 240 or cabeza.xcor() < -240 or cabeza.ycor() > 240 or cabeza.ycor() < -240:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = 'stop'       
        
        #Limpiador de segmentos
        for i in segmentos:
            i.goto(1000,1000)
        segmentos = []
        marcador = 0
        texto.clear()    
        texto.write('Puntuacion: {}    Record: {}'.format(marcador, record), align = 'center', font = ('Courier', 18, 'bold')) 
                
    #mover segmento
    totalSegmentos = len(segmentos)
    for i in range(totalSegmentos -1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)
        
    if totalSegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
        
    mov()
    
    #Colisones con el cuerpo
    for i in segmentos:
        if i.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = 'stop'
            
            for i in segmentos:
                i.goto(1000, 1000)
        segmentos.clear()
    
    time.sleep(posponer)