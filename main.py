def calculate(a, b, op):
    elif op == "x" or op == "×" or op == "*":
        ans = a * b
    
    return ans

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
op = input("Operation (Symbol): ")
print(calculate(num1, num2, op))
