s="tenget"

person1=0
person2=len(s)-1
while person1<person2:
    if s[person1]==s[person2]:
        person1+=1
        person2-=1
else:
    # print(s[person1], s[person2])
    if s[person1] != s[person2]:
        print("not a palindrome")
        
print('is a palindrome')
    

