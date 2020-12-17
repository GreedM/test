def spell(n):
    if n==1:
        return "one"
    elif n==2:
        return "two"
    else:
        return f"not implemented: spell({n:d})"

if __name__ == "__main__":
    s = input("Enter number: ")
    i = int(s)
    print(i, "is written:", spell(int(s)))

