# to run this script, please use Python's interactive mode, i.e.
# python -i nltk_tree_drawing.py


from nltk.tree import *
from nltk.draw import tree

num_tree = Tree(1, [2, 3, 4])

print num_tree
num_tree.draw()

s = Tree('S', [Tree('NP', ['I']),
           Tree('VP', [Tree('V', ['saw']),
               Tree('NP', ['him'])])])

print s
s.draw()
