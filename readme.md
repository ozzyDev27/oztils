# What is oztils?
oztils is just a small "module", that has a ton of random features!
# Functions
### nonIndexedRange
The `nonIndexedRange` function takes an input of an int, and returns a list.  
When you use `range(3)`, it makes a list of `[0,1,2]`, but when you use `nonIndexedRange(3)`, it returns `[1,2,3]`  
Example: ```nonIndexedRange(4)``` returns a list of ```[1,2,3,4]```
### invert
The ```invert``` function takes a single input (anything) and returns what it is reversed.  
Example: ```invert("Hello")``` would return ```"olleH"```, and ```invert(7431)``` would return ```1347```
### removeStart
```removeStart``` is a universal version function, meaning that it will work in both Python 2.X and Python 3.X.   
It takes two arguments, both strings. The first is what you remove from the start, the second is the string.  
Example: ```removeStart("www.","www.ozzy.fun")``` would return ```"ozzy.fun"```.
### removeEnd
```removeEnd``` is a universal version function, meaning that it will work in both Python 2.X and Python 3.X.  
It takes two arguments, both strings. The first is what you remove from the end, the second is the string.  
Example: ```removeEnd(".fun","www.ozzy.fun")``` would return ```"www.ozzy"```.
### isPalindrome
The function ```isPalindrome``` takes one input and checks if it is a palindrome - or if it can be reversable and be the same thing!  
Example: ```isPalindrome("racecar")``` would return ```True```, because ```"racecar"``` reversed is ```"racecar"```
### listToString
```listToString``` takes one input, a list. It then concatenates it into a single string!  
Example: ```listToString(["Hello","there"])``` returns ```"Hellothere"```
### slowprint
The function ```slowprint``` is a function that takes two inputs, a string and a number.  
It prints out the text over the span of how much time you inputted (in seconds).  
Example: ```slowprint("hello, world!", 5.3)``` would type ```"hello, world!"``` over the span of ```5.3``` seconds.
### remove
Instead of doing ```text.replace("~","")``` over and over again to remove the characters from a string, use ```remove```!  
```remove``` takes two arguments, both strings. Every single character in the second string gets removed from text!   
Example: ```remove("Hello, world! How are you doing today?", ",!?d")``` removes all ```,```s, ```!```s, ```?```s, and ```d```s from the string, returning ```"Hello worl How are you oing toay"```
### fileAppend
```fileAppend``` takes two arguments both strings. The first string is a file path, and the second is any string.  
It then appends the string to the file.  
Example: ```fileAppend("test.txt","Hello, world!")``` adds ```"Hello, world!"``` to the end of ```"test.txt"```.
### fileErase
```fileErase``` does not delete the file, it instead erases everything within it. It takes one argument, the file path.  
Example: ```fileErase("hello.txt")``` would remove everyting within ```"hello.txt"```
### fileDelete
```fileDelete``` does exactly what it says on the tin - deletes the file! It takes one argument, the file path.  
Example: ```fileDelete("hello.txt")``` would simply delete ```"hello.txt"```
### fileRename
```fileRename``` does exactly what it says, renames the file. It takes two inputs, the file path, and what you are renaming it to.  
Example: ```fileRename("hello.txt","world.txt")``` would rename ```"hello.txt"``` to ```"world.txt"```
### isRound
```isRound``` takes an input of a number, and checks if it is round.  
Example: ```isRound(6.3)``` would return ```False```, because it has a decimal.
### simplify
The function ```simplify``` simplifies a fraction as much as possible!  
It takes two inputs of integers, the numerator and denominator!  
Example: ```simplify(2,6)``` returns ```[1,3]```, as a list, because ```2 over 6``` can be simplified to ```1 over 3```
### isPrime
The function ```isPrime``` does what it says - returns ```True``` if the number input (must be int) is prime!  
Example: ```isPrime(37)``` returns ```True```, because ```37``` is a prime number!
### deleteAllOf
```deleteAllOf``` takes two inputs - a list and something else (string, int - can be anything!) and returns the list, but removes every instance of the "something else"!  
Example: ```deleteAllOf(["hello","hi","hey","hi","how are you"],"hi")``` returns ```["hello,"hey","how are you"]```
### factorial
```factorial``` takes one input - an integer. It then returns the factorial of that number!
Example: ```factorial(5)``` returns ```120```, because ```5 factorial``` is ```120```.
### clamp
```clamp``` takes 3 inputs, all numbers.  
The first one is the value, the second is the minimum, and the third is the maximum.  
The minimum and maximum are practically the "walls", and makes sure the value doesn't go outside of it.  
Example: ```clamp(6,7,9)``` returns ```7```, because the value, ```6```, is less than the minimum, ```7```, so it pushes it back.
### getDifference
```getDifference``` gets the absolute difference of two numbers.  
Example: ```getDifference(7,9.3)``` returns ```2.3```, as the "distance" between the two numbers is ```2.3```.
### loop
The ```loop``` function is similar to the clamp function, but instead of maxing it out at the max value, it loops back down to the lowest!  
is similar to mod, but it keeps the loop within a certain range.  
Example: ```loop(7,4,6)``` returns ```5```, because ```7```, the value being inputted, is larger than the max of ```6```. This loops it over, and because it is ```1``` greater than the max, it returns ```1``` over the minimum.
### jumble
The ```jumble``` function takes one input - a list, and returns the same thing, but randomly sorted.  
Example: ```jumble([1,2,3])``` could return any assortment of the list, such as ```[3,1,2]```, or even ```[2,3,1]```.
### camelToUnder
```camelToUnder``` is a function takes a string as an argument, and converts it from camel case  
(```thisIsAnExampleOfCamelCase```) to underscored (```this_is_an_example_of_underscored```)   
Example: ```camelToUnder("helloWorldHowAreYou")``` returns ```"hello_world_how_are_you"```
### stripNot
The ```stripNot``` function takes two inputs, both strings.  
The first is everything you want to keep, and the second is the string.  
It then returns the second string, but gets rid of anything that is not in the first string.  
Example: ```stripNot('bda','abcdefgh')``` returns ```'abd'```, because it only keeps the letters ```b```, ```d``` and ```a```.
### percent
```percent``` is a function that takes a single input - a number. It then returns ```True``` that percent of the time, and ```False``` the other times.  
Example: ```percent(36)``` returns ```True``` 36% of the time.
### coinFlip
```coinFlip``` is a function that returns ```True``` half of the time, and ```False``` the other half.
Example: ```coinFlip()``` returns ```True``` half of the time.
### getFactors
```getFactors``` is a function that does what is says - it gets the factor of a number.  
It takes a single argument, an int, and returns a list of all of its factors.  
Example: ```getFactors(27)``` returns ```[1,3,9,27]```
### isUnique
```isUnique``` is a function that takes a single argument, a list.  
It then returns True if every item in the list is unique, meaning it has no duplicates.  
Example: ```isUnique([1,6,2,9,3,5,1])``` returns ```False``` because it has ```1``` twice.
### mean
```mean``` is a function that takes an input of a list, that contains numbers and returns the mean of the list.  
Example: ```mean([9,10,29])``` returns ```16```, because the mean of ```9, 10, 29``` is ```16```
### num
num is a function that converts the argument to either a float or an int, and will not add a ".0" or anything to the end
Example:
num("7") returns an int of 7, whereas num(7.3) returns a float of 7.3
### xor
what is says lol
### floor
The `floor` function rounds any number down. It takes a single argument, a number.  
Example: ```floor(17.561)``` returns ```17```
### ciel
pass
### mustInput
pass
### formatNumber
pass
### reciprocal
pass
### numberToBase
pass