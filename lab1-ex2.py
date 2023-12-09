# Create a program that would ask for two boolean values (true or false, 0 or 1) and would output the result for the XNOR operation performed on them.
# You're allowed to use only `and`, `or` and `not` operations


bool1 = bool(int(input("boolean 1:")))
bool2 = bool(int(input("boolean 2:")))

result = int((bool1 and bool2) or (not bool1 and not bool2))
print("XNOR operation result:", result)
