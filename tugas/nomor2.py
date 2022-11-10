from numpy import matrix, linalg

def f(x,y):
  return (x**2+y-11)**2 + (x+y**2-7)**2

def f_dx(x,y):
  return 4*x*(x**2+y-11) + 2*(x+y**2-7)

def f_dy(x,y):
  return 2*(y+x**2-11) + 4*y*(y**2+x-7) 

def f_dx_dx(x,y):
  return 12*x**2 + 4*y - 42

def f_dx_dy(x,y):
  return 4*(x+y)

def f_dy_dx(x,y):
  return 4*(x+y)

def f_dy_dy(x,y):
  return 12*y**2 + 4*x - 26

def newton(x, y, n):
  print(f"x0 = ({x,y})")
  for i in range(0, n):
    vct = matrix([[x], [y]])

    df = matrix([ [f_dx(x,y)], [f_dy(x,y)] ])

    h = matrix([ [f_dx_dx(x,y), f_dx_dy(x,y)], [f_dy_dx(x,y), f_dy_dy(x,y)] ])

    inversH = linalg.inv(h)

    vctN = vct - inversH * df

    x = vctN[0,0]
    y = vctN[1,0]

    print(f"x{(i+1)} = ({x},{y})")
  
  print(f"Nilai maksimum = {f(x,y)}")

# newton(5,5,3)

def steepest(x, y, t, n):
  print(f"x0 = ({x,y})")
  for i in range(n):
    vectorX = matrix([ [x], [y]] )

    df = matrix([ [f_dx(x,y)], [f_dy(x,y)] ])
    # print(t*df[1,0])
    t_x_df = matrix([ [t*df[0,0]], [t*df[1,0]]  ])

    vectorX = vectorX - t_x_df

  print(vectorX)
  
newton(5,5,3)
steepest(5,5,1/2,1)