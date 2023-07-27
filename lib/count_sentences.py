#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
       self.value = value
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if(isinstance(value, str)):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False
    
    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False
    
    def count_sentences(self):
        sentences = 0
        prev_character = None
        for character in self._value:
          if(character in ('.', '!','?') and prev_character != character):
              sentences+=1
          prev_character = character
        return sentences
    
    value = property(get_value, set_value)

  

