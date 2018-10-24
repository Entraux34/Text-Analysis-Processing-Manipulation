import pickle
import argparse

parser = argparse.ArgumentParser(description='Word to display features of')

parser.add_argument('Word', metavar='N', type=str, nargs='+', help='The word you are looking to find out about')

args = parser.parse_args()

class Word():
    def __init__(self,a,b,c,d):
        self.Word = a
        self.Occurances = b
        self.Common = c
        self.Followers = d

file = open('relate.dat','rb')
x = pickle.load(file)
file.close()

print(x[args.Word[0]].Common)
