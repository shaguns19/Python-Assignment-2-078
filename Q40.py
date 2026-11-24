start = int(input("Enter range start: ")); end = int(input("Enter range end: "))
for n in range(max(2, start), end + 1):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: prime = False; break
    if prime: print(n, end=" ")
print()
