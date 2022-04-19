# turtle time ve random kütüphanelerini import ettik

import  turtle,time,random

# window oluşturduk ve özelliklerini belirttik
window =turtle.Screen()
window.title('RaceGame')
window.bgcolor('gray')
window.setup(height=700,width=500)
window.tracer(0)

# Araç ve arka plan giflerini koyduk
window.register_shape('racingback.gif')
window.register_shape('racingcar.gif')

# Araba nesnesi oluşturduk ve özelliklerini belirttik
car = turtle.Turtle()
car.speed(0)
car.shape('racingcar.gif')
car.shapesize(2)
car.color('red')
car.setheading(90)
car.penup()
car.goto(0,-200)

# Arkaplan için nesne oluşturduk ve özelliklerini belirledik
back = turtle.Turtle()
back.speed(0)
back.pensize(3)
back.shape('square')
back.color('white')
back.penup()
back.hideturtle()
back.goto(0, 0)

# Kamera özelliklerini tanımladık.
camera_dy=0
camera_y =0

# Sola gitmesi için oluşturulan methot
# Buradaki amaç x kordinatının -170px ten fazla gitmesini engellemek  her başışta -10 px sola gider.
def left():
    #x i arabanın x kordinatına eşitledik ve 10px çıkardık
    x = car.xcor()
    x = x-10
    # Eğer x < -170 ten x koordinatı -170
    if x < -170:
        x = -170
    # x kordinatını arabanın x kordinatına verdik
    car.setx(x)


# Sağa gitmesi için oluşturulan methot
# Buradaki amaç x kordinatının 170px ten fazla gitmesini engellemek  her başışta -10 px sağa gider.
def right():
    x = car.xcor()
    x = x+10
    if x > 170:
        x = 170
    car.setx(x)

# engeller için oluşturulan barriers arrayı
barriers = []

# for döngüsü 10 kere çalışacak
for i in range(10):
    # engel nesnesinin temel özelliklerini tanımladık.
    barrier = turtle.Turtle()
    barrier.speed(0)
    barrier.shape('square')
    barrier.shapesize(3, 6)
    barrier.color('red')
    barrier.setheading(90)
    barrier.penup()
    barrier.dx = random.randint(-170, 170)
    barrier.dy = 500
    barrier.goto(barrier.dx, barrier.dy)
    barriers.append(barrier)

# Window'u dinlemesini söyledik.
window.listen()
# Eğer sol oka basılırsa sola gitmesi için
window.onkeypress(left, "Left")
# Eğer sağ oka basılırsa sağa gitmesi için
window.onkeypress(right, "Right")
# Başlangıç zamanı için
start_time= time.time()
i = -1



# Main loop kısmı oyunun çalışması esnasında dönecek
while True:
    # Kameranın takibi için gereken kodlar
    camera_dy = -2
    camera_y = camera_y + camera_dy
    camera_y = camera_y % 700
    # Arka planın kamera takibi be oynatılacak resim
    back.goto(0, camera_y-700)
    back.shape('racingback.gif')
    back.stamp()
    # Arabanın görseli ekran haraketinde arka planda kaybolmaması için
    car.shape('racingcar.gif')
    car.stamp()

    # arka planın kendini yenilemesi için
    back.goto(0,camera_y)
    back.shape('racingback.gif')
    back.stamp()
    # arka plana bağlı aracın haraketi için
    car.shape('racingcar.gif')
    car.stamp()

    # Eğer şuanki zamandan başlangıç zamanı çıktığında > rastgele sayı oluşturdu
    if time.time()-start_time>random.randint(3, 6):
        # Başlangıç zamanı şuanki zamana eşitledik böylece döngü olmuş oldu devam ettiği sürece
        start_time = time.time()
        # i her döngüde 1  artar
        i = i+1
        # eğer i 9 olursa
        if i == 9:
            # i'yi -1 e eşitle
            i = -1
            # bariyer döngüsü
            for barrier in barriers:
                # sağ ve soldan kordinatı random şekilde verdik.
                barrier.dx = random.randint(-170, 170)
                # bariyer hep 500den başladı oluşma yeri
                barrier.dy = 500
                # bariyerin tam konumu için iki değişkenide atadık koordinatlara.
                barrier.goto(barrier.dx, barrier.dy)


    y = barriers[i].ycor()
    y = y-2
    barriers[i].sety(y)

    # Engele Takılma kısmı
    if barriers[i].distance(car)<30:
        print('Game Over')
        back.clear()
        car.clear()
        time.sleep(1)
    # ekranı güncelle
    window.update()

    #araba ve arka planı temizle
    back.clear()
    car.clear()