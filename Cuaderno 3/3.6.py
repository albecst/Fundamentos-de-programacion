a = 3
b = 2
c = 1

if a < b < c:
    print(f"{c} > {b} > {a}")
if a < c < b:
    print(f"{b} > {c} > {a}")
if b < c < a:
    print(f"{a} > {c} > {b}")
if b < a < c:
    print(f"{c} > {a} > {b}")
if c < a < b:
    print(f"{b} > {a} > {c}")
if c < b < a:
    print(f"{a} > {b} > {c}")

