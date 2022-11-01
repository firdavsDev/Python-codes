
import turtle

def funk1():
    tosh.pencolor(ranglar[rang])
    tosh.forward(50)

def funk2():
    tosh.left(45)

def funk3():
    tosh.right(45)

def funk4():
    wn.bye()

def funk5():
    global pensz
    pensz += 1
    tosh.pensize(pensz)

def funk6():
    global pensz
    pensz -= 1
    if pensz > 0:
        tosh.pensize(pensz)
    else:
        pensz = 1
        tosh.pensize(pensz)

def funk7():
    global ruchka
    if ruchka == 1:
        tosh.penup()
        ruchka = 0
    else:
        tosh.pendown()
        ruchka = 1

def funk8():
    tosh.pencolor("green")
    tosh.back(50)

def funk9():
    global rang
    if rang > 2:
        rang = 0
    else:
        rang += 1
    print(rang)
    tosh.pencolor(ranglar[rang])

def funk10(tekst, x, y):
    tanish = turtle.Turtle()
    tanish.hideturtle()
    tanish.penup()
    tanish.goto(x, y)
    tanish.write(tekst, font=10)

def main():
    global tosh
    global wn
    global pensz
    global ruchka
    global rang
    global ranglar
    rang = 0
    pensz = 1
    ruchka = 1
    ranglar = ["yellow", "orange", "red", "white"]

    wn = turtle.Screen()
    wn.setup(700, 500)
    wn.title("Toshbaqa")
    wn.bgcolor("green")

    tosh = turtle.Turtle()
    tosh.pensize(pensz)

    funk10("'↑' - oldiga yurish", 450, 300)
    funk10("'↓' - o'chirish", 450, 275)
    funk10("'→' - o'ngga burilish", 450, 250)
    funk10("'←' - chapga burilish", 450, 225)
    funk10("'probel' - ruchkani ko'tarish va qo'yish", 450, 200)
    funk10("'a' - shriftni kattalashtirish", 450, 175)
    funk10("'s' - shriftni kichraytirish", 450, 150)
    funk10("'d' - rangni o'zgartirish", 450, 125)


    wn.onkey(funk1, "Up")
    wn.onkey(funk2, "Left")
    wn.onkey(funk3, "Right")
    wn.onkey(funk4, "q")
    wn.onkey(funk5, "a")
    wn.onkey(funk6, "s")
    wn.onkey(funk7, "space")
    wn.onkey(funk8, "Down")
    wn.onkey(funk9, "d")


    wn.listen()
    wn.mainloop()

main()