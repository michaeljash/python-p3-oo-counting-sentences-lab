#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self.value = value if isinstance(value, str) else ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            self._value = ''
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
    
        clean_value = re.sub(r'[.!?]+', '.', self.value)
    
        sentences = clean_value.split('.')
      
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())