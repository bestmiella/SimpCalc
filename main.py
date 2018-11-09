#Simple Python Calculator
class SimpPyCalc:

  def __init__(self, curr_num, new_num, reset):
    self.curr_num = curr_num
    self.new_num = new_num
    self.reset = reset
    print("""Add, substract, multiply, or divide by entering
    the operator followed by the number
    (Example: enter '+4' to add 4)""")

    def add(curr_num, new_num):
      new_num = float(us_in.lstrip('+'))
      print(curr_num + new_num)
      curr_num = float(curr_num + new_num)
      return curr_num

    def sub(curr_num, new_num):
      new_num = float(us_in.lstrip('-'))
      print(curr_num - new_num)
      curr_num = float(curr_num - new_num)
      return curr_num

    def mult(curr_num, new_num):
      new_num = float(us_in.lstrip('*'))
      print(curr_num * new_num)
      curr_num = float(curr_num * new_num)
      return curr_num

    def div(curr_num, new_num):
      new_num = float(us_in.lstrip('/'))
      print(curr_num / new_num)
      curr_num = float(curr_num / new_num)
      return curr_num
    
    def get_input():
      get_input = input(curr_num)
      return get_input

    while reset == False:
      us_in = get_input()

      if us_in[0] == "+":
        curr_num = add(curr_num, new_num)

      elif us_in[0] == "-":
        curr_num = sub(curr_num, new_num)

      elif us_in[0] == "*":
        curr_num = mult(curr_num, new_num)

      elif us_in[0] == "/":
        curr_num = div(curr_num, new_num)

      else:
        print("Error: Invalid. A valid operator would be '+', '-', '*', or '/'")

calc_session = SimpPyCalc(0, 0, False)
