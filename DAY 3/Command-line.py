def interactive_calculator():
    print("簡易計算機 (輸入 'q' 退出)")
    while True:
        try:
            expr = input("請輸入算式 (例如 2 + 3): ")
            if expr.lower() == 'q':
                break
            a, op, b = expr.split()
            a, b = float(a), float(b)
            
            if op == '+':
                print(f"結果: {a + b}")
            elif op == '-':
                print(f"結果: {a - b}")
            elif op == '*':
                print(f"結果: {a * b}")
            elif op == '/':
                print(f"結果: {a / b if b != 0 else '錯誤：除數不能為零！'}")
            else:
                print("不支援的運算符！")
        except ValueError:
            print("輸入格式錯誤！請用空格分隔數字與運算符。")

interactive_calculator()