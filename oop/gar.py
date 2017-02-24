"""
THE REMOTE GARAGE DOOR
You just got a new garage door installed.
Your son (obviously when you are not home) is having a lot of fun playing with the remote clicker,
opening and closing the door, scaring your pet dog Siba and annoying the neighbors.
The clicker is a one-button remote that works like this:
If the door is OPEN or CLOSED, clicking the button will cause the door to move,
until it completes the cycle of opening or closing.
    Door: Closed -> Button clicked -> Door: Opening -> Cycle complete -> Door: Open.
If the door is currently opening or closing, clicking the button will make the door stop where it is.
When clicked again, the door will go the opposite direction, until complete or the button is clicked again.
We will assume the initial state of the door is CLOSED.
"""



# YOUR CODE HERE

class GarageDoor():
    def transition(self,button_clicked):
        self.state = ""
        change = self.button_clicked()
        switch = change.next()
        if bool(switch) is True:
            self.state = "OPEN"
        elif bool(switch) is False:
            self.state = "CLOSED"
    def button_clicked(self):
        while True:
            yield 0
            yield 1        
    def cycle_complete(self,button_clicked):
        pass
##        self.state = ""
##        if bool(switch) is True:
##            self.state = "CLOSING"
##        elif bool(switch) is False:
##            self.state = "OPENING"
##        print "Action: button_clicked\n"
##        print "Door: %s" % self.state




'''
Given some test cases the output should resemble the output in the picture
'''

# Test case 1 Output(https://github.com/tunapanda/Python-advance-tracks/blob/master/images/output1.png)
# Your son just open and closed the door on day1 and left it closed
door_on_day1 = GarageDoor()
door_on_day1.transition(GarageDoor.button_clicked) # Note button_clicked is a function
door_on_day1.transition(GarageDoor.cycle_complete) #  Note cycle_complete is a function
door_on_day1.transition(GarageDoor.button_clicked)
door_on_day1.transition(GarageDoor.cycle_complete)
print "The final state of the door is " + door_on_day1.state # # Note state is not a function 


# Test case 2 Output(https://github.com/tunapanda/Python-advance-tracks/blob/master/images/output2.png)
# The next day, he just had to do more experiments with the door. He clicked clicked a lot.
# The list below is the sequence of actions to the garage door
action_sequence = [GarageDoor.button_clicked, GarageDoor.cycle_complete, GarageDoor.button_clicked,
                   GarageDoor.button_clicked, GarageDoor.button_clicked, GarageDoor.button_clicked,
                   GarageDoor.button_clicked, GarageDoor.cycle_complete]

door_on_day2 = GarageDoor()
   
for action in action_sequence:
    door_on_day2.transition(action)

print "The final state of the door is " + door_on_day2.state
