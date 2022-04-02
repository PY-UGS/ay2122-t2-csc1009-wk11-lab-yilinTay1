class calculator: 
    def __init__(self):
        self.input1 = input1
        self.input2 = input2
    def adder(self,input1,input2):
        return input1 + input2
    def subtractor(self,input1,input2):
        return input1 - input2
    def multiplier(self,input1,input2):
        return input1 * input2
    def divider(self,input1,input2):
        return input1 / input2
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        return self.input1,self.input2
result = 0
input1 = int(input('Enter 1st number: '))
input2 = int(input('Enter 2nd number: '))

object_calculator = calculator()

print("adder()"+str(object_calculator.adder(input1,input2)))
print("subtractor()"+str(object_calculator.subtractor(input1,input2)))
print("multiplier()"+str(object_calculator.multiplier(input1,input2)))
print("divider()"+str(object_calculator.divider(input1,input2)))
print("clear()"+str(object_calculator.clear()))