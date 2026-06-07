(course use a person class builder as example) 
# the telescopic constructor problem

readability, extensively, error prompt, how far will you go

# the builder solution 

# tools
building dedicated class
+ mutators for each situation (setters or access methods)
=› code widget non chained example

## build() return the product 
=> code widget with a builder returning product 

## chaining technique 
each chain element method returns a reference to the builder 
=> snippet of chaining methods

## what if we need to return smart pointer
=> code snippet with pointer example 


# Exercise: Sandwich shop
Refactor a sandwich shop with telescopics constructor (class has content() method listing properly 
1. replace constructor with accessors, test
2. make a build() method 
2. make a builder class using mutators
3. create chain methods for each situation (box, bread, sauces,etc.)
4. close the constructor making it private, to let the builder the only path to constuct sandwiches)
5. encapsulate the build stereotypes in public methods

sources :
