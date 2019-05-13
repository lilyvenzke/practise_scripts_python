"''drawing a circle with sqaure. A practise using turtle.resource: udacity python for beginners'"
import turtle

"""note to self: when i create a seperate function to create my window to draw on
i get a blank screen with no drawings even though i call the appropriate functions
WHY?"""

'''dont forget to add your parameters or your code
    will compile but you will get a blank/frozen screen the moment your
    broken function is called'''

def draw_square(my_turtle):
   for i in range(4):
      my_turtle.forward(100) #move forward for a 100 pixels
      my_turtle.right(90) #turn 90 degrees right

    
   
def draw_art():
    window_to_draw_on = turtle.Screen()
    window_to_draw_on.bgcolor("light blue")
    
    square_to_draw = turtle.Turtle()
    for i in range(1, 36):
        draw_square(square_to_draw)
        square_to_draw.right(10)
   #circle_to_draw = turtle.Turtle()
    #circle_to_draw.circle(100)

    #triangle_to_draw =turtle.Turtle()
    #triangle_to_draw.right(180)
    #triangle_to_draw.forward(100)
    #triangle_to_draw.right(90)
    #triangle_to_draw.forward(100)
    #triangle_to_draw.home()'''
   
    window_to_draw_on.exitonclick()
    
 

draw_art()


    
