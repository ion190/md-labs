# You are given a string str. You can convert str to a palindrome by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.

s = input("Enter string: ")
# Find the longest palindrome
for i in range(len(s), 0, -1):
    if s[:i] == s[:i][::-1]:
        # Add the remaining characters in reverse order to the beginning
        print(s[i:][::-1] + s)
        break
