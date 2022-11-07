# What is oztils?
oztils is just a small "module", that has a ton of random features!
# Functions
### nonIndexedRange
nonIndexedRange takes an input of an int, and returns a range type. 
When you use range(3), it makes a list of [0,1,2], but when you use nonIndexedRange(3), it returns [1,2,3]
### invert
Takes a single input (preferrably a string, but can be anything) and returns what it is reversed.
For example, "Hello" would return "olleH".
### removeStart
removeStart is a universal version function, meaning that it will work in both Python 2.X and Python 3.X.
For example, removeStart("www.","www.ozzy.fun") would return "ozzy.fun".
### removeEnd
removeEnd is a universal version function, meaning that it will work in both Python 2.X and Python 3.X.
For example, removeEnd(".fun","www.ozzy.fun") would return "www.ozzy".
### isPalindrome
isPalindrome takes one input and checks if it is a palindrome - or if it can be reversable and be the same thing!
Example: isPalindrome("racecar") would return true, because "racecar" reversed is "racecar"
### reverseList
reverseList does exactly what it says, it reverses a list.
Example: reverseList([1,5,2]) would return [2,5,1].
### listToString
listToString takes one input, a list. It then concatenates it into a single string!
Example: listToString(["Hello","there"]) would return "Hellothere".
### slowprint
slowprint is something I stole from my friend ultra bob, where it takes 2 inputs, the text and the time.
It prints out the text over the span of how much time you inputted (in seconds).
Example: slowprint("hello, world!", 5.3) would type "hello, world!" over the span of 5.3 seconds.
