class AdvancedCalculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self
    
    def subtract(self, num):
        self.result -= num
        return self
    
    def multiply(self, num):
        self.result *= num
        return self
    
    def divide(self, num):
        if num == 0:
            raise ValueError("除數不能為零！")
        self.result /= num
        return self

# 使用範例 (鏈式呼叫)
calc = AdvancedCalculator()
result = calc.add(5).multiply(3).subtract(2).divide(2).result
print("(5 + 0) * 3 - 2 / 2 =", result)  # 輸出: 6.5