
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
    if testa.direzione != "down":
       testa.direzione = "up"

def vai_giu() :
    if testa.direzione != "up":
       testa.direzione = "down"

def vai_sinistra():
    if testa.direzione != "right" :
        testa.direzione = "left"

def vai_destra():
    if testa.direzione != "left" :
        testa.direzione = "rigt"

def muovi():
    if testa.direzione == "up":
        y = testa.ycor()
        testa.sety( y + 20)
    if testa.direzione == "down":
        y = testa.ycor()
        testa.sety(y - 20)
    if testa.direzione == "left":
        x = testa.ycor()
        testa.setx(x - 20)
    if testa.direzione == " rigth" :
        x= testa.ycor()
        testa.setx(x + 20)

        #collegamento tasti
        





        
       


                