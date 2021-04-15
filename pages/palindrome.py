def palindrome(str):
    for i in range(0,int(len(str)/2)):
        if (str[i] != str[len(str)-i-1]):
            return False
    return True

w= "mmalayalam"
result = palindrome(w)

if (result):
    print("Palindrome")
else:
    print("Not palindrome")
