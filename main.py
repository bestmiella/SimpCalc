# Simple Python Calculator
class SimpPyCalc:

    def __init__(self, curr_num, new_num):

        # 'curr_num' is the current value stored in the calculator
        self.curr_num = curr_num
        # 'new_num' is the number that the user chooses to add, subtract, multiply, or divide from the 'curr_num'
        self.new_num = new_num

        print("""Add, substract, multiply, or divide by entering
the operator followed by the number. (Ex. '+4')

To reset the calculator, enter 'reset'
""")

        # method for addition
        def add(curr_num, new_num):
            new_num = float(us_in.lstrip('+'))
            print(curr_num + new_num)
            curr_num = float(curr_num + new_num)
            return curr_num

        # method for subtraction
        def sub(curr_num, new_num):
            new_num = float(us_in.lstrip('-'))
            print(curr_num - new_num)
            curr_num = float(curr_num - new_num)
            return curr_num

        # method for multiplication
        def mult(curr_num, new_num):
            new_num = float(us_in.lstrip('*'))
            print(curr_num * new_num)
            curr_num = float(curr_num * new_num)
            return curr_num

        # method for division
        def div(curr_num, new_num):
            new_num = float(us_in.lstrip('/'))
            print(curr_num / new_num)
            curr_num = float(curr_num / new_num)
            return curr_num

        # method for user input
        def get_input():
            get_input = input()
            return get_input

        # calculator constantly runs
        while True:
            # 'us_in' is for storing user input
            us_in = get_input()

            # following determines whether the user is adding, subtracting, multiplying, dividing, or resetting
            if us_in[0] == "+":
                curr_num = add(curr_num, new_num)        

            elif us_in[0] == "-":
                curr_num = sub(curr_num, new_num)        

            elif us_in[0] == "*":
                curr_num = mult(curr_num, new_num)    

            elif us_in[0] == "/":
                curr_num = div(curr_num, new_num)

            elif us_in == "reset":
                curr_num = 0
                print("[Successfully reset]")

            # runs when the user's input is invalid
            else:
                print("Error: Invalid. A valid operator would be '+', '-', '*', or '/'")

# calculator object
calc_session = SimpPyCalc(0, 0)
