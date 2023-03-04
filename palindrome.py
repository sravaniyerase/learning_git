def check_palindrome(string):
   first = 0
   last = len(string)-1
   isPalindrome=True
   while(first<last):
        if(string[first] == string[last]):
            first=first+1
            last=last-1
        else:
            isPalindrome=False
            break
   return isPalindrome
 
string="MADAM"
isPalindrome=check_palindrome(string)
if(isPalindrome):
   print("It is a palindrome ")
else:
    print('is palindrome')