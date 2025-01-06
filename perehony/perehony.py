import turtle
import random

# Функція для початку гри
def start_game(x, y):
    global num_players
    num_players = int(screen.textinput("Кількість гравців", "Введіть кількість гравців (1-4):"))
    print(f"Кількість гравців: {num_players}")
    
    # Малювання меж поля
    pen.speed(0)
    pen.clear()
    pen.penup()
    pen.goto(-350, -250)  # Нижній лівий кут
    pen.pendown()
    pen.color("black")
    pen.pensize(3)
    for _ in range(2):
        pen.forward(700)  # Довжина поля
        pen.left(90)
        pen.forward(500)  # Висота поля
        pen.left(90)

    start_x, start_y = -350, -200

    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color("blue")
    pen.forward(700)

    finish_x, finish_y = -350, 200

    pen.penup()
    pen.goto(finish_x, finish_y)
    pen.pendown()
    pen.color("red")
    pen.forward(700)

    pen.penup()
    pen.goto(start_x - 40, start_y - 20)
    pen.color("blue")
    pen.write("Старт", font=("Arial", 16, "bold"))
    pen.goto(finish_x - 40, finish_y + 20)
    pen.color("red")
    pen.write("Фініш", font=("Arial", 16, "bold"))

    pen.hideturtle()

    # Розміщення черепашок на стартовій лінії
    turtles = []
    colors = ["red", "blue", "green", "yellow"]
    for i in range(num_players):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape("turtle")
        t.penup()
        t.goto(start_x + (700 / (num_players + 1)) * (i + 1), start_y)
        t.setheading(90)
        t.pendown()
        turtles.append(t)

    #Інтерфейс користувача
    status_pen = turtle.Turtle()
    status_pen.penup()
    status_pen.hideturtle()
    status_pen.goto(0, 220)

    def update_status():
        leader = max(turtles, key= lambda t: t.ycor())
        leader_color = leader.color()[0]
        distance_to_finish = finish_y - leader.ycor()
        status_pen.clear()
        status_pen.write(f'Лідирує: {leader_color}. Дистанція до фінішу: {distance_to_finish}', align='center', font=("Arial", 16, "bold"))

    #РУХ ЧЕРЕПАХ
    race_in_progress = True
    while race_in_progress:
        for t in turtles:
            distance = random.randint(1, 10) #випадкова відстань від 1 до 10 пікселів
            t.forward(distance)
            if t.ycor() >= finish_y:
                race_in_progress = False
                winner = t.color()[0]
                print(f'winner color: {winner}')
                break
        update_status()


# Створюємо об'єкт екрану та черепашки
screen = turtle.Screen()
pen = turtle.Turtle()

# Створюємо кнопку
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
pen.end_fill()

# Додаємо текст на кнопку
pen.penup()
pen.goto(0, -20)
pen.color("white")
pen.write("Почати гру", align="center", font=("Arial", 16, "bold"))
pen.hideturtle()

# Відслідковування натискання на кнопку
screen.onscreenclick(start_game, 1)

# Тримаємо вікно відкритим
screen.mainloop()
