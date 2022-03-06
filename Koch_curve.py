# Based on Mr Dhanesh's code in:
# https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
# https://github.com/dbudhrani

# 1. Import

import turtle

# 2. Variables

number_faces, iterations, length, shortening_factor, angle, file_name = 3, 0, 200, 3, 60, 'Imagens/koch_curve'

# 3. Fuctions

def koch_curve(t, iterations, length, shortening_factor, angle):

  if iterations == 0:
    t.forward(length)
  else:
    iterations += - 1
    length = length / shortening_factor

    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle * 2)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)

def polygon(number_faces,t, iterations, length, shortening_factor, angle):
    for i in range(number_faces):
      koch_curve(t, iterations, length, shortening_factor, angle)
      t.right(360/number_faces)

def save_fig(file_name, number_faces, iterations, length, shortening_factor, angle):
    arquivo = file_name + \
              '_face_' + str(number_faces) + \
              '_Inter_' + str(iterations) + \
              '_leng_' + str(length) + \
              '_shorter_' + str(shortening_factor) + \
              '_Angle_' + str(angle) + \
              '.png'
    return arquivo

# 4. Run

t = turtle.Turtle()
t.hideturtle()
polygon(number_faces,t, iterations, length, shortening_factor, angle)
t.getscreen().getcanvas().postscript(file=save_fig(file_name, number_faces, iterations, length, shortening_factor, angle))
turtle.mainloop()