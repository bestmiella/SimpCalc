#Simple Python Calculator
class SimpPyCalc:

  def __init__(self, curr_num, new_num, reset):
    self.curr_num = curr_num
    self.new_num = new_num
    self.reset = reset
    print("""add, substract, multiply, or divide by entering
the operator followed by the number
(Example: enter '+4' to add 4)""")

    def add():
      return curr_num + new_num

    def sub():
      return curr_num - new_num

    def mult():
      return curr_num * new_num

    def div():
      return curr_num / new_num
    
    def get_input():
      get_input = input()
      return get_input

    while reset == False:
      us_in = get_input()
      if us_in[0] == "+":
        add()
      elif us_in[0] == "-":
        sub()
      elif us_in[0] == "*":
        mult()
      elif us_in[0] == "/":
        div()
      else:
        print("Error: Invalid. A valid operator would be '+', '-', '*', or '/'")

calc_session = SimpPyCalc(0, 0, False)
