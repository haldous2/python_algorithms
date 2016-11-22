"""
 Cracking the coding interview
 Practice questions
 Part 3. Stacks and Queues
"""

"""
 Helper Code
"""

"""
 3.1
 Create 3 stacks from one array
 Initial brute force thoughts - array list of array ? - array in an array... this wouldn't be one array though... maybe?
 brute force #2 - create large array and allocate space in thirds for three stacks

    ** issues might be when pop, array will shrink
       could just Null out space where pop occured to keep array the same length
    ** limit on stack space .. or double (triple) size of array
    ** shrinking would require checking all stacks for space constraints

    pop: [1,2,3|4,5,6|7,N,N] -> pop() second stack = 6 -> [1,2,3|4,5,N|7,N,N]
    grow: [1,2|3,4|5,6] -> grow, triple -> [1,2,N,N|3,4,N,N|5,6,N,N]

    assume: not allowed to grow - return error if adding to stack and full
            using a third of space only - not sharing space with other stacks

"""

class stackThreeContainer(object):

    def __init__(self):
        self.container = []         # array, list etc...
        self.stackLength = {}       # lengh to each stack
        self.stackLength[1] = 0
        self.stackLength[2] = 0
        self.stackLength[3] = 0
        self.numberOfStacks = 3
        self.numberOfElements = 5
        self.minValue = []
        self.create_container(self.numberOfStacks * self.numberOfElements)

    def create_container(self, n):
        if not n or type(n) is not int:
            raise ValueError('invalid integer passed to create array')
        self.container = [None] * n

    def print_container(self):
        print self.container

    def push(self, stack, value):

        if not stack or type(stack) is not int:
            raise ValueError('invalid stack value passed')
        if stack < 1 or stack > 3:
            raise ValueError('invalid stack number passed')
        if not value:
            raise ValueError('no value passed to push onto stack')

        stack_start = self.numberOfElements * (stack - 1)
        stack_end = stack_start + self.numberOfElements
        stackLength = self.stackLength[stack]

        if stackLength >= self.numberOfElements:
            raise ValueError('cannot push any more values onto stack')
        else:
            pushIndex = stackIndex = stack_start + stackLength
            self.setMin(value)
            self.container[pushIndex] = value
            self.stackLength[stack] += 1

    # Note - min only takes into account entire container for question #2
    def setMin(self, value):
        if self.minValue:
            if value < self.minValue[-1] and value != self.minValue[-1]:
                self.minValue.append(value)
        else:
            self.minValue.append(value)

    def popMin(self, value):
        if self.minValue:
            if value == self.minValue[-1]:
                self.minValue.pop()

    def getMin(self):
        return self.minValue[-1]

    def pop(self, stack):

        # Note stack starts @ 1 to number of stacks, not zero
        # note stack length from 0 to self.stackLength

        if not stack or type(stack) is not int:
            raise ValueError('invalid stack value passed')
        if stack < 1 or stack > 3:
            raise ValueError('invalid stack number passed')

        # stack 1 with length 5 (0,1,2,3,4)
        # stack 2 with length 5 (5,6,7,8,9) etc...
        #                        1 2 3 4 5  stack index

        stack_start = self.numberOfElements * (stack - 1)
        stack_end = stack_start + self.numberOfElements
        stackLength = self.stackLength[stack]

        if stackLength:
            # stackIndex @ stack 2 of length 5 and stackLength = 1
            #            stack_start = 5 + stackLegth = 1; -1 = 5 ... good to go!
            stackIndex = (stack_start + stackLength) - 1
            stackValue = self.container[stackIndex]
            self.popMin(stackValue)
            self.container[stackIndex] = None
            self.stackLength[stack] -= 1
            return stackValue
        else:
            # nothing in stack
            return None

    def peek(self, stack):

        # Note stack starts @ 1 to number of stacks, not zero
        # note stack length from 0 to self.stackLength

        if not stack or type(stack) is not int:
            raise ValueError('invalid stack value passed')
        if stack < 1 or stack > 3:
            raise ValueError('invalid stack number passed')

        # stack 1 with length 5 (0,1,2,3,4)
        # stack 2 with length 5 (5,6,7,8,9) etc...
        #                        1 2 3 4 5  stack index

        stack_start = self.numberOfElements * (stack - 1)
        stack_end = stack_start + self.numberOfElements
        stackLength = self.stackLength[stack]

        if stackLength:
            # stackIndex @ stack 2 of length 5 and stackLength = 1
            #            stack_start = 5 + stackLegth = 1; -1 = 5 ... good to go!
            stackIndex = (stack_start + stackLength) - 1
            stackValue = self.container[stackIndex]
            return stackValue
        else:
            # nothing in stack
            return None

# Test - 3 stacks in one array
# s = stackThreeContainer()
# #s.push(1, 'a')
# s.push(2, 'd')
# s.push(1, 'b')
# s.push(3, 'e')
# s.push(3, 'f')
# s.push(3, 'g')
# s.push(3, 'h')
# s.push(3, 'i')
# #s.push(3, 'j') # generate error
# s.push(1, 'c')
# s.print_container()
# print s.pop(1) # return c
# print s.pop(2) # return d
# print s.pop(2) # return None
# s.print_container()
# print s.peek(1) # print b
# print s.peek(2) # print None
# print s.peek(3) # print i

"""
 3.2
 Stack - return minimum element
 Notes: push, pop, peek & min should all run in O(1) time

 Brute force - store everything in a min heap. Problem in storage for min heap is avg. O(nlogn)time - no bueno
 Or - track smallest value that is pushed onto stack in another variable. Return on min call.

"""

# lazy integration into above 3 stack
#print "min",s.getMin()

"""
 3.3
 Stack of plates - don't let them get too high! - create a new stack, etc.. as they are stacked
 allow pop to pop top from any stack if defined, else from last stack

 |||||||  |||||||| |||||| - don't break any!

 ** unlimited stacks, pop from last stack
 ** thinking I can store stacks in a stack (list of lists) [0:[],1:[],2:[]]
 ** this data structure doesn't clean up empty stacks if popAt removes all plates from stack
 ** need to know if any under filled stacks should be filled first - if plates, yes ... if data that needed order then no
    since this analogy is plates, just fill in non full stacks first.
    plates are too heavy and valuable to move over so leave empty sub-stack spaces empty
"""

class setOfStacks(object):

    def __init__(self):

        self.stackHeight = 10
        self.mainStack = []
        self.subStackLength = {}    # dict container for sub-stack size e.g., 0:10, 1:8 etc...
        self.lastStack = None       # last sub-stack in list ... not sure if I'll need this... integer value

        #self.minStack = {None:None} # stack with minimum number of plates key:val
        #self.maxStack = {None:None} # stack with maximum number of plates key:val

    def print_container(self):
        print self.mainStack
        print self.subStackLength

    def peek(self):
        pass

    def pop(self):

        # pop from last available stack ? - easiest (going with easy)
        # pop from stack with most plates ? - keep track of max

        pop = None

        # pop from last stack
        if self.lastStack is None:
            return None
        # index exits in mainStack
        print "lastStack:{} len.mainStack:{}".format(self.lastStack, len(self.mainStack))
        if self.lastStack > len(self.mainStack) - 1:
            return None
        # sub-stack has something to pop off
        if len(self.mainStack[self.lastStack]) == 0:
            return None

        pop = self.mainStack[self.lastStack].pop()
        self.subStackLength[self.lastStack] -= 1

        if pop is not None:

            # sub-list cleanup
            if len(self.mainStack[self.lastStack]) == 0:
                # remove empty main-stack slot
                self.mainStack.pop(self.lastStack)
                # reset lastStack
                if self.lastStack == 0:
                    self.lastStack = None
                else:
                    self.lastStack -= 1

        return pop

    def popAt(self, stack=None):

        # of course one would have to know how many stacks there were for this to work right
        # let's just assume that is the case

        pop = None

        # pop defined stack
        if stack is None:
            return None
        if type(stack) is not int:
            return None
        # index exits in mainStack
        if stack > len(self.mainStack) - 1:
            return None
        # sub-stack has something to pop off
        if len(self.mainStack[stack]) == 0:
            return None

        pop = self.mainStack[stack].pop()
        self.subStackLength[stack] -= 1

        if pop is not None:

            # sub-list cleanup
            if len(self.mainStack[stack]) == 0:
                # remove empty main-stack slot
                self.mainStack.pop(stack)
                # reset lastStack
                if self.lastStack == 0:
                    self.lastStack = None
                else:
                    self.lastStack -= 1

        return pop

    def createStack(self):
        # append a sub-stack to the main stack and return
        self.mainStack.append([])
        stackIndex = len(self.mainStack) - 1
        #print "=========stackIndex:",stackIndex
        self.subStackLength[stackIndex] = 0
        return stackIndex

    def firstAvailableStack(self):
        # return first available (has room to grow) stack index
        # walk through subStackLength (dict) key:len
        for l in self.subStackLength:
            # compare stacklength to class max stack height
            if self.subStackLength[l] < self.stackHeight:
                # return mainStack index
                return l
        # no available stacks
        return None

    def lastAvailableStack(self):
        # return last available stack index
        # walk through subStackLength (dict) key:len
        for l in self.subStackLength:
            #print "lastAvailableStack l:{} subStackLength[l]:{} stackHeight:{}".format(l, self.subStackLength[l], self.stackHeight)
            # compare stacklength to class max stack height
            if self.subStackLength[l] < self.stackHeight:
                # return mainStack index
                #print "returning l:",l
                return l
        # no available stacks
        return None

    # def getNextMax(self):
    #     # find next max value in stack lengths
    #     for l in self.subStackLength:
    #         pass

    def push(self, value):

        # need to know
        # 1. any stack built yet
        # 2. first stack with room

        if self.mainStack:

            # has at least one sub-stack
            # let's find that stack

            # index of last stack in mainStack -> stackIndex
            stackIndex = self.firstAvailableStack()
            #print "stackIndex from firstAvailableStack...",stackIndex
            if stackIndex is None:
                stackIndex = self.createStack()
                #print "stackIndex from createStack...",stackIndex

            # append value to
            self.mainStack[stackIndex].append(value)
            self.subStackLength[stackIndex] += 1
            self.lastStack = stackIndex

        else:

            # no sub-stacks built yet
            self.mainStack.append([value])
            self.subStackLength[0] = 1
            self.lastStack = 0              # last sub-stack in main-stack
            #self.maxStack[0] = 1            # stack with the most plates (so far)

# Tests - stacks in array
# plates = setOfStacks()
# plates.pop()
# plates.push(1)
# plates.push(2)
# plates.push(3)
# plates.push(4)
# plates.push(5)
# plates.push(6)
# plates.push(7)
# plates.push(8)
# plates.push(9)
# plates.push(10)
# plates.push('a')
# plates.push('b')
# plates.push('c')
# plates.push('d')
# plates.push('e')
# plates.push('f')
# plates.push('g')
# plates.push('h')
# plates.push('i')
# plates.push('j')
# plates.push('k')
# plates.print_container()
# print "pop:",plates.pop()
# plates.print_container()
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "popAt:",plates.popAt(0)
# print "pop:",plates.pop()
# plates.print_container()

"""
 3.4
 Queue from two Stacks

 push into stack 1, pop stack 1, push into stack 2 - now stack pop will act like a queue
"""

class queueStacks(object):

    def __init__(self):

        self.stack_fwd = []
        self.stack_rev = []

    def printQueue(self):
        print "fwd:",self.stack_fwd
        print "rev:",self.stack_rev

    def push(self, val):

        # add rev back to fwd
        # pop:  fwd:[1,2,3,4] pop to -> rev:[4,3,2,1]
        # push: add 5,6... first pop rev to fwd -> [1,2,3,4] ... push 5,6 fwd:[1,2,3,4,5,6]
        # repeat
        while self.stack_rev:
            pop = self.stack_rev.pop()
            self.stack_fwd.append(pop)

        # push new value onto stack
        self.stack_fwd.append(val)

    def pop(self):

        # add fwd back to rev
        while self.stack_fwd:
            pop = self.stack_fwd.pop()
            self.stack_rev.append(pop)
        if self.stack_rev:
            return self.stack_rev.pop()
        else:
            return None

    def peek(self):

        # like pop - just don't remove anything from rev
        # add fwd back to rev
        while self.stack_fwd:
            pop = self.stack_fwd.pop()
            self.stack_rev.append(pop)
        if self.stack_rev:
            return self.stack_rev[-1]
        else:
            return None

# Tests - Queue from two stacks

# queue = queueStacks()
# print "queue.pop:",queue.pop()
# print "queue.peek:",queue.peek()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# queue.push(4)
# queue.printQueue()
# print "queue.pop:",queue.pop()
# queue.printQueue()
# print "queue.pop:",queue.pop()
# queue.printQueue()
# queue.push(5)
# queue.push(6)
# queue.printQueue()
# print "queue.pop:",queue.pop()
# queue.printQueue()
# print "queue.peek:",queue.peek()
# print "queue.peek:",queue.peek()

"""
 3.5
 Stack - order from min to max - assuming this means on push
 pop will always return the min
 No mention of time complexity
"""

class stackMin(object):

    def __init__(self):

        self.stack_fwd = []
        self.stack_rev = []

    def printQueue(self):
        print "fwd:",self.stack_fwd
        print "rev:",self.stack_rev

    def is_empty(self):
        if len(self.stack_fwd) > 0:
            return False
        else:
            return True

    def push(self, val):

        #print "========== push-ing...", val

        # add rev back to fwd
        # pop:  fwd:[1,2,3,4] pop to -> rev:[4,3,2,1] - pop out -> 1
        # push: add 5,6... first pop rev to fwd -> [1,2,3,4] ... push 5,6 fwd:[1,2,3,4,5,6]
        # repeat

        # move rev back to fwd

        #print ".fwd:", self.stack_fwd
        #print ".rev:", self.stack_rev
        while self.stack_rev:
            self.stack_fwd.append(self.stack_rev.pop())
        #print "..fwd:", self.stack_fwd
        #print "..rev:", self.stack_rev

        push_val = False

        # insert val in order
        #for v in self.stack_fwd:
        while self.stack_fwd:
            if val >= self.stack_fwd[-1]:       # peek stack
                #print "{} >= {}".format(val, self.stack_fwd[-1])
                push_val = True
                self.stack_fwd.append(val)
                break
            else:
                # store in rev as temp storage
                pop = self.stack_fwd.pop()
                #print "pop stack @ ", pop
                #self.stack_rev.append(self.stack_fwd.pop())
                self.stack_rev.append(pop)
        #print "....fwd:", self.stack_fwd
        #print "....rev:", self.stack_rev

        if not push_val:
            self.stack_fwd.append(val)

        # move temp back to fwd
        while self.stack_rev:
            self.stack_fwd.append(self.stack_rev.pop())

        #print ".....fwd:", self.stack_fwd
        #print ".....rev:", self.stack_rev

    def pop(self):

        # add fwd back to rev
        while self.stack_fwd:
            self.stack_rev.append(self.stack_fwd.pop())

        if self.stack_rev:
            return self.stack_rev.pop()
        else:
            return None

    def peek(self):

        # like pop - just don't remove anything from rev
        # add fwd back to rev
        while self.stack_fwd:
            self.stack_rev.append(self.stack_fwd.pop())

        if self.stack_rev:
            return self.stack_rev[-1]
        else:
            return None

# Tests - Min Stack

# minstack = stackMin()
# print "queue.pop:",minstack.pop()
# print "queue.peek:",minstack.peek()
# minstack.push(4)
# minstack.push(7)
# minstack.push(9)
# minstack.push(3)
# print "queue.pop:",minstack.pop()
# print "queue.pop:",minstack.pop()
# minstack.printQueue()
# minstack.push(20)
# minstack.push(1)
# minstack.printQueue()
# print minstack.peek()
# print minstack.peek()
# minstack.printQueue()

"""
 3.6
 Queue - Animal Shelter

 methods:
  enqueue
  dequeue
  dequeueCat
  dequeueDog

 Note: using a single list to store cats and dogs results on O(c+d) time
       using two lists and itering through both at the same time would give (c or d) time depending on the longer list
       the more efficient algorithm (data structure) would be to use two lists

"""

class Animal(object):

     def __init__(self, name='', age=0, species=None):
         self.name = name
         self.age = age
         self.species = species

class queueAnimalShelter(object):

    def __init__(self):
        self.inventory = []

    def printInventory(self):

        if not self.inventory:
            print "inventory: None"
            return

        for animal in self.inventory:
            print "inventory:", animal.species, animal.name, animal.age

    def printAnimal(self, animal):

        if animal and type(animal) is Animal:

            print "requested info:", animal.species, animal.name, animal.age

        else:

            print "requested info: none found"

    def enqueue(self, name='', age=0, species=None):

        # when queueing up, shoudl I check for dups ?
        # assuming the animal is already processed with a tag - no need to dup check
        if not name or not age or (species is not 'dog' and species is not 'cat'):
            raise ValueError('please enter a name, age and species:dog or cat')

        self.inventory.append(Animal(name, age, species))

    def dequeue(self):

        # dequeue first animal - species doesn't matter
        pass
        if len(self.inventory) > 0:
            return self.inventory.pop(0)
        else:
            return None

    def dequeueCat(self):

        # dequeue first cat in list
        for k in range(len(self.inventory)):
            if self.inventory[k].species == 'cat':
                return self.inventory.pop(k)

    def dequeueDog(self):

        # dequeue first dog in list
        for k in range(len(self.inventory)):
            if self.inventory[k].species == 'dog':
                return self.inventory.pop(k)

# Tests - Queue - Animal Shelter

# shelterpets = queueAnimalShelter()
# shelterpets.enqueue('Fluffy', 8, 'dog')
# shelterpets.enqueue('Snipper', 2, 'dog')
# shelterpets.enqueue('Poopy', 7, 'cat')
# shelterpets.enqueue('Jughead', 3, 'dog')
# shelterpets.enqueue('Scrappy', 4, 'dog')
# shelterpets.enqueue('Tunces', 5, 'cat')
#
# shelterpets.printInventory()
#
# shelterpets.printAnimal(shelterpets.dequeue())
# #shelterpets.printAnimal(shelterpets.dequeue())
# #shelterpets.printAnimal(shelterpets.dequeue())
# shelterpets.printAnimal(shelterpets.dequeueCat())
# #shelterpets.printAnimal(shelterpets.dequeueCat())
# shelterpets.printAnimal(shelterpets.dequeueDog())
# shelterpets.printInventory()
