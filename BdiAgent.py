from enum import Enum
class BdiMode(Enum):
 blind=0
 singleMinded=1
 openMinded=2

class BdiAgent():
    def __init__(self,beliefs,intentions,mode=BdiMode.blind):

        """In our example, Belief are the ontology and the reasoning and inference we can do on it"""
        self.beliefs=beliefs
        """Boolean functions with a priority"""
        self.intentions=intentions
        self.plan_buffer=[]
        self.mode=mode

    def belief_revision(self,percept):
        """Based on beliefs and the current percept"""
        """Needs to be overwritten"""
        """We can implement additional temporal rules based on the messages in the conversation"""
        """E.g. if the user is sad for a period of time with a specific number of messages and response time,
        they will be labeled as troll. A new feature based on these properties could be created to normalize them."""
        pass

    def desires(self):
        """Based on beliefs and intentions"""
        """In our case doesn't need to be overwritten"""
        pass

    def filter(self):
        """Based on beliefs, intentions and desires(all goals)"""
        """updates intentions"""
        """In our case doesn't need to be overwritten"""
        pass

    def plan(self):
        """Based on beliefs and intentions"""
        """updates the plan buffer"""
        """needs to be overwritten"""

    def execute(self):
        """Based on mode executes all the steps in the plan or just """
        """needs to be inherited"""
        if self.mode == BdiMode.blind:
            return self.plan_buffer
        else:
            return self.plan_buffer.pop()

    def impossible(self):
        """Based on beliefs and intentions"""
        return False

    def succeeded(self):
        """Based on beliefs and intentions"""
        return False

    def reconsider(self):
        """Based on beliefs and intentions"""
        return False

    def sound(self):
        """Based on beliefs and plan buffer"""
        return True

    def update(self,percept):
        """runs the agent in a single time-step"""
        """The percept could be the last two messages or the entire conversation, if we want to detect someone
        is stuck being a certain mood"""
        self.belief_revision(percept)
        if self.mode!=BdiMode.blind and self.plan_buffer:
            self.execute()
            if self.mode==BdiMode.openMinded and self.reconsider():
                self.filter()
            if not self.sound():
                self.plan_buffer=self.plan()
            return 0
        self.filter()
        self.plan()
        self.execute()

"""For simulating the message environment, lets have an array of objects, where each object is a message
with a time and the troll score that has been assigned to it."""

"""Dialouge actions could be implemented as triggers in the ontology"""







