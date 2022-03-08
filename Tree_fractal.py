# With help for link:
# https://www.geeksforgeeks.org/y-fractal-tree-in-python-using-turtle/

# 1. Import
import turtle

# 2. Variables
interactions, length, shorting_length, angle = 10, 90, 0.7, 20


# 3. Functions
def tree(interactions, length, shorting_length, angle):
    if interactions > 0:
        turtle.forward(length)
        #turtle.dot()
        turtle.left(angle)
        tree(interactions - 1, shorting_length * length, shorting_length, angle)
        turtle.right(2 * angle)
        tree(interactions - 1, shorting_length * length, shorting_length, angle)
        turtle.left(angle)
        turtle.back(length)


# 4. Run
turtle.Turtle()
turtle.right(-90)
turtle.hideturtle()
tree(interactions, length, shorting_length, angle)
turtle.mainloop()
