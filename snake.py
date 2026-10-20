
import turtle 
import time
import random
#ritardo per velocizzare la velocità di gioco
ritardo = 0.1

#configurazione schermo
finestra = turtle.Screen()
finestra.title("Gioco di Snake in Python")
finestra.bgcolor("black")
finestra.setup(width=600, heigth=600)
finestra.tracer(0) #disattiva aggiornamenti automatici per evitare scatti

#testa del serpente
testa= turtle.Turtle()
testa.speed(0)
testa.shape("square")
testa.color("green")
testa.penup()
testa.goto(0, 0)
testa.direzione = "stop"

#funzioni di movimento
def vai_su():
    if testa.direzione != "down"

                