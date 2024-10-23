import turtle
import math
import time
import random

wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger by Li")
wn.setup(600, 800)
wn.bgcolor("black")
wn.bgpic(r"bg.gif")
wn.tracer(0)

# Register shapes (ensure paths are correct)
wn.register_shape(r"frogger.gif")
wn.register_shape(r"car_left.gif")
wn.register_shape(r"car_right.gif")
wn.register_shape(r"log.gif")
wn.register_shape(r"turtles_right.gif")
wn.register_shape(r"turtles_left.gif")
wn.register_shape(r"turtles_right_half.gif")
wn.register_shape(r"turtles_left_half.gif")
wn.register_shape(r"turtles_submerged.gif")
wn.register_shape(r"goal.gif")
wn.register_shape(r"frog_small.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
# Define a global speed modifier
global_speed_modifier = 1.0  # 1.0 is normal speed, increase to speed up

# Create base Sprite class
class Sprite:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def update(self):
        pass

    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return x_collision and y_collision

# Create Player class
class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.frogs_home = 0
        self.max_time = 60
        self.time_remaining = 60
        self.start_time =time.time()
        self.lives = 3

    # Movement methods
    def up(self):
        self.y += 50

    def down(self):
        self.y -= 50

    def right(self):
        self.x += 50

    def left(self):
        self.x -= 50

    def update(self):
        self.x += self.dx

        #update the timer
        self.time_remaining =self.max_time - round(time.time() - self.start_time)

        # Boundary checking
        if self.x < -300 or self.x > 300:
            self.x = 0
            self.y = -300
        if self.y < -300:
            self.y = -300

        #out of time
        if self.time_remaining <= 0:
            player.lives -= 1
            self.go_home()

    def go_home(self):
        self.dx =0
        self.y = -300
        self.x = 0

    def game_over(self):
        pen.clear()
        self.pen.goto(0,0)
        self.pen.color("red")
        self.pen.write("Game Over", align="center", font=("Arial", 36,"bold"))
        self.pen.write("Press 'R' to Restart", align="center", font=("Arial", 24, "normal"))
        turtle.update()
    def reset_game():
        global game_over
        game_over = False
        player.lives = 3
        player.frogs_home = 0        
        player.time_remaining = player.max_time
        player.start_time = time.time()

        for home in homes:
            home.is_occupied = False
        pen.clear()
        wn.update()
    wn.onkeypress(reset_game, "r")

# Create Car class
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx * global_speed_modifier
        # Boundary checking
        if self.x < -400:
            self.x = 400
        if self.x > 400:
            self.x = -400

# Create Log class
class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx * global_speed_modifier
        # Boundary checking
        if self.x < -400:
            self.x = 400
        if self.x > 400:
            self.x = -400

# Create Turtle class
class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full"  # full, half, submerge
        self.full_time = random.randint(8,12)
        self.half_time = random.randint(4,6)
        self.submerged_time = random.randint(4,6)
        self.start_time = time.time()

    def update(self):
        self.x += self.dx * global_speed_modifier
        # Boundary checking
        if self.x < -400:
            self.x = 400
        if self.x > 400:
            self.x = -400

        # Update image based on state
        if self.state == "full":
            if self.dx > 0:
                self.image = r"turtles_right.gif"
            else:
                self.image = r"turtles_left.gif"
        elif self.state == "half_up" or self.state == "half_down":
            if self.dx > 0:
                self.image = r"turtles_right_half.gif"
            else:
                self.image = r"turtles_left_half.gif"
        elif self.state == "submerged":
            self.image = r"turtles_submerged.gif"

        # State transitions based on timer
        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half_down"
            self.start_time = time.time()
        elif self.state == "half_down" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "half_up"
            self.start_time = time.time()
        elif self.state == "half_up" and time.time() - self.start_time > self.submerged_time:
            self.state = "full"
            self.start_time = time.time()

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.is_occupied = False

    def occupy(self):
        if not self.is_occupied:
            self.is_occupied = True

# Create a separate pen for the timer
timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.hideturtle()
timer_pen.penup()

class Timer:
    def __init__(self, max_time):
        self.x = 100  # Starting X position
        self.y = -375  # Starting Y position
        self.max_time = max_time
        self.width = 200  # Total width for the timer bar

    def render(self, time_remaining):
        # Clear only the timer drawing
        timer_pen.clear()

        percent = time_remaining / self.max_time
        dx = percent * self.width
        
        # Move to the start position for the timer bar
        timer_pen.goto(self.x, self.y)
        timer_pen.setheading(0)  # Set heading to right
        timer_pen.pendown()

        # Draw the timer bar
        timer_pen.pensize(5)
        
        # Draw the green part of the timer
        timer_pen.color("green")
        timer_pen.forward(dx)

        # Draw the remaining red part
        timer_pen.color("red")
        timer_pen.forward(self.width - dx)

        pen.goto(self.x-100, self.y-10)
        pen.color("white")
        pen.write(f"Time Left: {time_remaining}s", align="center", font=("Arial", 16, "normal"))
        pen.penup()


# Create player and other sprites
player = Player(0, -300, 40, 40, r"frogger.gif")
timer = Timer(60)

level_1= [
    Car(0, -250, 80, 40, r"car_left.gif", -0.25),
    Car(180, -250, 80, 40, r"car_left.gif", -0.25),

    Car(0, -200, 80, 40, r"car_right.gif", +0.25),
    Car(180, -200, 80, 40, r"car_right.gif", +0.25),

    Car(0, -150, 80, 40, r"car_left.gif", -0.1),
    Car(180, -150, 80, 40, r"car_left.gif", -0.1),

    Car(0, -100, 80, 40, r"car_right.gif", +0.1),
    Car(180, -100, 80, 40, r"car_right.gif", +0.1),

    Car(0, -50, 80, 40, r"car_left.gif", -0.1),
    Car(180, -50, 80, 40, r"car_left.gif", -0.1),

    Log(0, 50, 160, 40, r"log.gif", +0.2),
    Log(260, 50, 160, 40, r"log.gif", +0.2),

    Log(0, 100, 160, 40, r"log.gif", -0.2),
    Log(260, 100, 160, 40, r"log.gif", -0.2),

    Turtle(0, 150, 150, 40, r"turtles_right.gif", +0.2),
    Turtle(250, 150, 150, 40, r"turtles_right.gif", +0.2),

    Turtle(0, 200, 160, 40, r"turtles_left.gif", -0.2),
    Turtle(260, 200, 160, 40, r"turtles_left.gif", -0.2),

    Log(0, 250, 160, 40, r"log.gif", +0.2),
    Log(260, 250, 160, 40, r"log.gif", +0.2)
    ]

homes =[
   Home(0,300, 40, 40,  r"goal.gif"),
   Home(-150,300, 40, 40,  r"goal.gif"),
   Home(-250,300, 40, 40,  r"goal.gif"),
   Home(150,300, 40, 40,  r"goal.gif"),
   Home(250,300, 40, 40,  r"goal.gif")
   ]


# Create a list of sprites
sprites = level_1 + homes
sprites.append(player)

# Key bindings
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

# Create function to adjust speed
def change_speed(factor):
    global global_speed_modifier
    global_speed_modifier *= factor

# Key bindings to increase or decrease speed (optional)
wn.onkeypress(lambda: change_speed(1.1), "plus")     # Increase speed by 10%
wn.onkeypress(lambda: change_speed(0.9), "minus")    # Decrease speed by 10%

game_over = False

while True:
    if game_over:
        continue

    # Clear the pen stamps (but not text)
    pen.clearstamps()

    # Render and update each sprite
    for sprite in sprites:
        sprite.render()
        sprite.update()

    #render the lives
    pen.goto(-290, -375) 
    pen.shape(r"frog_small.gif")  
    for life in range(player.lives):
        pen.goto(-280 +(life *30), -375)
        pen.stamp()   

    # Handle player movement on logs and turtles
    player.dx = 0
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                player.go_home()
                break
            elif isinstance(sprite, Log):
                # Move player with the log or turtle
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home) and not sprite.is_occupied:
                # Player reaches an unoccupied home
                sprite.occupy()
                player.frogs_home += 1  # Increment frogs_home correctly
                player.go_home()  # Move player back to the starting position
                break

    # Check if player is in the water area but hasn't collided with logs/turtles
    if player.y > 0 and not player.collision:
        player.lives -= 1       
        player.go_home()

        sprites = level_1 + homes
        sprites.append(player)

    # Render timer after all sprites have been rendered
    timer.render(player.time_remaining)

    # Display frogs in home
    for sprite in sprites:
        if isinstance(sprite, Home) and sprite.is_occupied:
            pen.goto(sprite.x, sprite.y)
            pen.shape(r"frogger.gif")
            pen.stamp()

    # When player loses all lives or after placing all frogs:
    if player.lives == 0 or player.frogs_home == 5:
        player.go_home()
        player.frogs_home = 0
    
        for home in homes:
            home.is_occupied = False  # Reset occupied state for all homes
            home.render()  # Make sure to render updated state

        if player.lives == 0:
            player.lives = 3  # Reset lives
            player.max_time = 60
            player.time_remaining = player.max_time
            player.start_time = time.time()  # Reset timer
        

        player.lives = 3
        player.max_time = 60
        player.time_remaining = player.max_time
        player.start_time = time.time()

    player.time_remaining = player.max_time -round(time.time()-player.start_time) 
    timer.render(player.time_remaining)   

    # Update the screen
    wn.update()
    
    pen.clear()


