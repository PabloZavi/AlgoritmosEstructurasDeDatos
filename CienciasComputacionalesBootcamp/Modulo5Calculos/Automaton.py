# This code defines a finite state automaton (FSA) that processes a
# string to determine if it is accepted based on certain rules.
# such as a regexp evaluator 
# 1. The first letter has to be 'a'
# 2. The following letters have to be 'b' or 'c' (at least one, and they can be repeated)
# 3. The last letter has to be 'd'
# For example, the words 'abcd' | 'abcbcccbbcd' are accepted,
# but the words 'abc' | 'abcbcccdbb' are rejected

class automaton:
    def __init__(self):
        self.state = 0
               
    def transition(self, character):
        if self.state == 0 and character == 'a':
            self.state = 1
        elif self.state == 1 and (character == 'b' or character == 'c'):
            self.state = 1
        elif self.state == 1 and character == 'd':
            self.state = 2
        else:
            self.state = -1
            
        
    def accept(self):
        return self.state == 2
    
    def process(self, string):
        for character in string:
            self.transition(character)
            if self.state == -1:
                break
        return self.accept()
    

autom = automaton()
word = "abcbcccbbcd"
print("The word", word, "is", "accepted" if autom.process(word) else "rejected")
    
    
    
            