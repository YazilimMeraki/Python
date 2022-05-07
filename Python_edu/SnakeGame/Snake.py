import turtle
import time
import random
""" 
    1- Turtle modülü içindeki hazır fonksiyonlarla çizim yapmaya yarar.
    2- Bir ekran oluşturduk ve ona arka plan rengi yükseklik verdik.
    3- Tracer ile gğncellemeyi kapattık.
    4- Sayfanın kapanmaması ve güncellenmesi için update kullandık.
   -------------------------------------------------------------------
    5- Turtle sınıfından head denen bir nesne oluşturduk.
    6- Kendimiz haraket ettirmek için hız vermedik.
    7- Şeklini kare belirledik.
    8- Rengini siyah yaptık.
    9- Kafa haraket ederken yazı çıkmayacağı için penup kullandık.
    10- Başlangıç koordinatını seçtik.
    11- Direction ile yön ekledik.
    -------------------------------------------------------------------
    12- Hız değişkeni oluşturduk ve değer atadık.
    13- Programın yavaş çalışması için time modülübü çağırdık ve time sleep yaparak programı yavaşlattık.
    14- Yön metodu oluşturduk ve değerlerini atadık.
    15- Yön methoduna haraketleri tanımladık.
    16- Ekranın tuşları dinlemesini sağladık ve yönlere göre haraket etmesini sağladık.
    -------------------------------------------------------------------
    17- Yemek özelliklerini belirledik.
    18- Yemek ilk çıkma koordinatını yazdık.
    --------------------------------------------------------------------
    19- Bir tails arrayi oluşturduk.
    20- Yemek yendikten sonra kuyruk oluşması için kuyruk nesnesi oluşturduk ve kuyruklar array'ine gönderdik.
    21- For döngüsü kullaranak kuyruklar array'indeki her eleman için bir kuyruk oluşturmasını söyledik.
    22- Array'in eleman sayısı 0 dan büyükse her kuyruğun kordinatının bir eksiğini bir sonraki kuyruğa verdik.
    --------------------------------------------------------------------
"""

hiz=0.1

window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0 , 100)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0 , 0)
food.shapesize(0.80 ,0.80)

tails = []
point =0

write= turtle.Turtle()
write.speed(0)
write.shape('square')
write.color('white')
write.penup()
write.goto(0 ,260)
write.hideturtle()
write.write('Point:{}'.format(point),align='center',font=('Courier',24,'normal'))

def move():
    if head.direction=='up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x = head.xcor()
        head.setx(x-20)

def goUp():
    if head.direction!='down':
        head.direction='up'
def goDown():
    if head.direction!='up':
        head.direction='down'
def goRight():
    if head.direction!='left':
        head.direction='right'
def goLeft():
    if head.direction!='right':
        head.direction='left'

window.listen()
window.onkey(goUp,'Up')
window.onkey(goDown,'Down')
window.onkey(goRight,'Right')
window.onkey(goLeft,'Left')

while True:
    window.update()

    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        for tail in tails:
            tail.goto(1000,1000)

        tails=[]

        hiz=0.15

        write.clear()
        point=0

        write.write('Point:{}'.format(point), align='center', font=('Courier', 24, 'normal'))

    if head.distance(food)<20:
        x =random.randint(-250,250)
        y = random.randint(-250, 250)
        food.goto(x,y)

        newTail= turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('white')
        newTail.penup()
        tails.append(newTail)

        point=point+10
        write.clear()
        write.write('Point:{}'.format(point), align='center', font=('Courier', 24, 'normal'))

    for i in range(len(tails)-1,0,-1):
        x=tails[i-1].xcor()
        y=tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails)>0:
        x=head.xcor()
        y=head.ycor()
        tails[0].goto(x,y)

    move()
    time.sleep(hiz)