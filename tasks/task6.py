# tasks/task6.py

def solve():
# Ниже пишите решение задачи
  a, b, c = map(int, input().split())
  a, b, c = sorted([a, b, c])
  print(c * c == a * a + b * b)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()