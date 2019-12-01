'''
could you make a binary tree class where each node can have up to two children? To add in a higher-order aspect
(since there’s nothing actually higher order in your file so labeled): Could you write a binary tree method that takes a predicate over elements and
counts how many elements satisfy the predicate?
'''
import random

#This is a binary tree with pointers to a left and right branch. 
class tree:
    def __init__ (self, data):
        self.data = data
        self.right = None
        self.left = None
    def countPredicate (self, predicate):
        def keepCounting():
            if self.left and self.right:
                return self.left.countPredicate(predicate)+self.right.countPredicate(predicate)
            elif self.left:
                return self.left.countPredicate(predicate)
            elif self.right:
                return self.right.countPredicate(predicate)
            else:
                return 0 
        if self.data == None:
            return 0
        elif predicate(self.data):
            return (1+keepCounting())
        else:
            return (0+keepCounting())
    def read(self):
        print (self.data)
        if self.left:
            print ("l of ", self.data)
            self.left.read()
        if self.right:
            print ("r of ", self.data)
            self.right.read()


#recursive function that returns a tree with a number of nodes that store a random number in the range of 0 to rang. 
def genTree (rang, number):
    rang = abs(rang)
    number = abs (number)
    if number == 0:
        return None
    else:
        newTree = tree(random.randint(0, rang))
        number -=1
        if number > 0:
            newTree.right = genTree(rang, number//2)
            number =number-number//2
        if number > 0:
            newTree.left = genTree(rang, number)
        return newTree
    

        
#setup
newTree=genTree(5,10)
predicate = lambda x: x%2 ==0

#code
newTree.read()
count = newTree.countPredicate(predicate)
print ("")
print (count, "satisfy the condition")

