class SimpleCalculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "錯誤：除數不能為零！"
        return a / b

# 使用範例
calc = SimpleCalculator()
print("5 + 3 =", calc.add(5, 3))          # 輸出: 8
print("5 - 3 =", calc.subtract(5, 3))     # 輸出: 2
print("5 * 3 =", calc.multiply(5, 3))     # 輸出: 15
print("5 / 3 =", calc.divide(5, 3))       # 輸出: 1.666...
print("5 / 0 =", calc.divide(5, 0))       # 輸出: 錯誤：除數不能為零！