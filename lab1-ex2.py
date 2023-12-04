bool1 = bool(int(input("boolean 1:")))
bool2 = bool(int(input("boolean 2:")))

result = int((bool1 and bool2) or (not bool1 and not bool2))
print("XNOR operation result:", result)
