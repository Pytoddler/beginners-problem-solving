import sys

# sys.stdin 會自動讀取所有系統輸入的文字，直到結束（EOF）
for line in sys.stdin:
    # 假設輸入是一行兩個數字，用空白隔開
    a, b = map(int, line.split())
    print(a + b)
