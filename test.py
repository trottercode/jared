
pythonforbeginners.com

    Home
    Learn Python
    Basics
    Lists
    Dictionary
    Code Snippets
    Modules

Home >> Magic 8-ball written in Python
Apr. 14, 2013

      Code
      Code snippets

Magic 8-ball written in Python
Overview

The Magic 8 Ball is a toy used for fortune-telling or seeking advice.

Magic 8-ball written in Python

In this script I'm using 8 possible answers, but please feel free to add more as
you wish. 

There are 20 answers inside the Magic 8 Ball, and you can find them all
here

# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "It is certain"
    
    elif answers == 2:
        print "Outlook good"
    
    elif answers == 3:
        print "You may rely on it"
    
    elif answers == 4:
        print "Ask again later"
    
    elif answers == 5:
        print "Concentrate and ask again"
    
    elif answers == 6:
        print "Reply hazy, try again"
    
    elif answers == 7:
        print "My reply is no"
    
    elif answers == 8:
        print "My sources say no"

Exercise:
Is there a way to replace all elif answers with something else?

Recommended Python Training – DataCamp

For Python training, our top recommendation is DataCamp.

Datacamp provides online interactive courses that combine interactive coding challenges with videos from top instructors in the field.

Datacamp has beginner to advanced Python training that programmers of all levels benefit from.

 


Read more about:

      Code
      Code snippets

Disclosure of Material Connection: Some of the links in the post above are “affiliate links.” This means if you click on the link and purchase the item, I will receive an affiliate commission. Regardless, PythonForBeginners.com only recommend products or services that we try personally and believe will add value to our readers.
Categories

    Basics
    Cheatsheet
    Code snippets
    Development
    Dictionary
    Error Handling
    Lists
    Loops
    Modules
    Strings
    System & OS
    Web & Internet

© Python For Beginners 2012-2019 | Privacy Policy | Write For Us | Contact Us
Learn Beginner or Advanced Python at DataCamp Free Trial