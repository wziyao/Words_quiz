import sys
import codecs
import random


# base class

# the class for a single word and its quiz
class Word():

  def __init__(self, inputStr, dilimiter):

    w = inputStr.strip().split(dilimiter)

    if len(w):
      self.english_name = w[0]
      self.chinese_name = w[1]

    return

  def generate_quiz(self):

    self.quiz = self.english_name[0]

    for i in range(len(self.english_name)-2):
        self.quiz += ' _'

    self.quiz += ' '+self.english_name[-1]

    self.quiz += ' ' + self.chinese_name

    return

  def print_quiz(self, outputf):
    
    print >> outputf, self.quiz

    return

# the class for a list of words that stored in a plain txt file
class Words():

    def __init__(self, name=None):

      if name:

        self.name = name
        self.total = 0
        self.quiz_count = 0
        self.card_count = 0
        self.words = []

        file_name = 'lists/' + name + '.txt'
        #inputf = codecs.open(u'lists/b.txt', 'r', encoding='utf-8')
        input_file = codecs.open(file_name, 'r', encoding='utf-8')

        for line in input_file:
          if line.strip():
            w = Word(line, ' ')
            self.words.append(w)
            self.total += 1

        input_file.close()

        self.total = len(self.words)

        #print self.name, self.total, self.count

      return

    

