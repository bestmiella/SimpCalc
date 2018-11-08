#Simple Python Calculator
class SimpPyCalc:

  def __init__(self, curr_num, op, reset):
    self.curr_num = curr_num
    self.op = op
    self.reset = reset

    while reset == False:
      get_input = SimpPyCalc.get_input()

  def add():
    return 0

  def sub():
    return 0

  def mult():
    return 0

  def div():
    return 0
  
  def get_input():
    us_in = input("""add, substract, multiply, or divide by entering
the opperator followed by the number
(Example: enter '+4' to add 4)""")
    return us_in

calc_session = SimpPyCalc(0, "none", False)



