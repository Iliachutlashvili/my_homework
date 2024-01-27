# # დავალება 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         perimeter = 2 * self.radius
#         return perimeter

#     def area(self):
#         area = (self.radius ** 2)
#         return area
    
# radius = 5
# circle = Circle(radius)

# perimeter_result = circle.perimeter()
# area_result = circle.area()

# print(f"Circle with radius {radius}:")
# print(f"Perimeter: {perimeter_result:.2f}")
# print(f"Area: {area_result:.2f}")

# # --------------------------------------------------------------------

# # დავალება 2

num1 = int(input("Choose number 1: "))
num2 = int(input("Choose number 2: "))

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
        

calculator_instance = Calculator()

result_addition = calculator_instance.add(num1, num2)
result_subtraction = calculator_instance.subtract(num1, num2)
result_multiplication = calculator_instance.multiply(num1, num2)
result_division = calculator_instance.divide(num1, num2)

print(f"Addition: {result_addition}")
print(f"Subtraction: {result_subtraction}")
print(f"Multiplication: {result_multiplication}")
print(f"Division: {result_division}")