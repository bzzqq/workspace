import random
for _ in range(1, 30):
    a = random.randint(1, 9)
    b = random.randint(1, 5)
    c = random.randint(1, 20)
    d = random.randint(100, 200)
    operator = random.randint(1, 2)
    if operator == 1:
        op = ("+")
    else:
        op = ("-")
    if a > b:
        print(f"{a}x {op} {b}(x {op} {c}) = {d}")
