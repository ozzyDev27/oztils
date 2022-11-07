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
### remove
Instead of doing text.replace("~","") over and over again to remove the characters from a string you don't like, use remove!
remove takes two arguments, text and toRemove - both strings. Every single character in toRemove gets removed from text!
Example: remove("Hello, world! How are you doing today?", ",!?d") removes all commas, exclamation marks, question marks, and letter "d"'s from the string, returning "Hello worl How are you oing toay"
### fileAppend
fileAppend takes two arguments, file, and toWrite. It proceeds to add the text "toWrite" to the end of the file.
Example: fileAppend("hello.txt","Hello, world!") adds "Hello, world!" to the end of "hello.txt".
### fileErase
fileErase does not delete the file, it instead erases everything within it. It takes one argument, the file name.
Example: fileErase("hello.txt") would remove everyting within "hello.txt"
### fileDelete
fileDelete does exactly what it says on the tin - deletes the file! It takes one argument, the file name!
Example: fileDelete("hello.txt") would simply delete "hello.txt"
### fileRename
fileRename does exactly what it says, renames the file. It takes two inputs, the file, and what you are renaming it to.
Example: fileRename("hello.txt","world.txt") would rename "hello.txt" to "world.txt"
### isRound
isRound takes an input of a number, and checks if it is round.
Example: isRound(6.3) would return false, because it has a decimal.
### intput
Takes an input that must be an integer!
### simplify
Simplifies a fraction as much as possible! Takes two inputs of integers, the numerator and denominator!
Example: simplify(2,6) returns [1,3], as a list, because 2 over 6 can be simplified to 1 over 3.
