def derivative(f):
  vars = f.strip(" ").split('+')
  t = []
  for var in vars:
    if "x^" in var:
      if var[0].isdigit():
        newValue = int(var[0])*int(var[3])



derivative("5x^2")