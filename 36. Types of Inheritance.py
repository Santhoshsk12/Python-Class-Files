# 1. Multilevel Inheritance (Generations) = A child inherits from a parent, who in turn inherited from a grandparent.

    #  ** Eg: Think of a family tree: Grandparent --> Parent --> Child.
            # The Child inherits traits from the Parent.
            # The Parent inherited traits from the Grandparent.
            # Therefore, the Child gets traits from both!
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Grandparent
class OldPhone:
    def call(self):
        print("Can able to make Voice Call")

# 2. Parent (inherits OldPhone)
class FeaturePhone(OldPhone):
    def text(self):
        print("Can able to send SMS Text")

# 3. Child (inherits FeaturePhone, which already has OldPhone)
class SmartPhone(FeaturePhone):
    def browsing(self):
        print("Can able to do Internet Browsing")



ob = SmartPhone()

# It gets all 3 abilities through the chain of generations:
ob.call()
ob.text()
ob.browsing()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. Multiple Inheritance (Two or More Direct Parents) = A child inherits from more than one parent at the same time

    #  Eg: In real life, a child has two parents (Mother and Father) and inherits traits from both.
        # ** It was like 'Mixing two separate things' -> Parent 1 + Parent 2 ----> Child


# Parent 1
class OldWatch:
    def time(self):
        print("It tells Time")


# Parent 2 
class FitnessTrackerWatch:
    def count_steps(self):
        print("It counts no. of steps walked")

# Child (lists BOTH parents inside the parentheses separated by a comma)
class SmartWatch(OldWatch, FitnessTrackerWatch):
    pass  # Has all abilities of OldWatch AND FitnessTrackerWatch


obj = SmartWatch()

# Can do actions from Parent 1:
obj.time()

# Can do actions from Parent 2:
obj.count_steps
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. What if Both Parents Have the Same Skill/Method? (MRO) --> Method Resolution Order
    # Eg: Imagine a child has two parents:
            # Dad speaks English.
            # Mom speaks Tamil.
        # -- Both have a method called speak(). Which language does the child speak by default?


class Dad:
    def speak(self):
        print("Speaking English ")

class Mom:
    def speak(self):
        print("Speaking Tamil")

# Dad is written FIRST (that is on the left):
class Child(Dad, Mom):
    pass

o = Child()
o.speak()   # Output: Speaking English





    # If you swap the order and put Mom first:

# Mom is written FIRST (that is on the left):
class Child(Mom, Dad):
  pass

o = Child()
o.speak()  # Output: Speaking Tamil



'''     The Rule:
                 Python reads the parents left to right. 
                    Whichever parent is listed first (that is on the left) wins any tie. 
                        This is called MRO (Method Resolution Order).'''



