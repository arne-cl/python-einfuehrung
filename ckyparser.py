'''
Created on May 3, 2011

@author: koller
'''

import nltk
import itertools

# Input
words = ["I", "shot", "an", "elephant", "in", "my", "pajamas"]
n = len(words)

grammar = nltk.parse_cfg("""
 S -> NP VP
 PP -> P NP
 NP -> Det N | 'I' | NP PP
 VP -> V NP | VP PP
 Det -> 'an' | 'my'
 N -> 'elephant' | 'pajamas'
 V -> 'shot'
 P -> 'in'
 """)


class Item:
    def __init__(self, nonterminal, start, end):
        self.nonterminal = nonterminal
        self.start = start
        self.end = end
        
    def __repr__(self):
        return "{0}:{1}:{2}".format(self.nonterminal, self.start, self.end)
    

# leere Chart bauen
chart = []
for i in range(n+1):
    row = []
    for j in range(n+1):
        row.append({})
    chart.append(row)

# Zugriff auf Chart-Eintraege
def get_nonterminals_in_cell(i, k):
    return chart[i][k].keys()

def get_items(i, k, nonterminal):
    return chart[i][k].get(nonterminal, [])
    
def add_entry(i, k, nonterminal, childItems):
    if not chart[i][k].has_key(nonterminal):
        chart[i][k][nonterminal] = []
        
    chart[i][k][nonterminal].append(childItems)
        
# Terminalproduktionen
for i in range(n):
    for prod in grammar.productions(rhs=words[i]):
        add_entry(i, i+1, prod.lhs(), [words[i]])

# Bottom-up
for width in range(2, n+1):
    for i in range(0, n-width+1): # i + width <= n
        for j in range(1, width): # 1 <= j <= width-1
            nts1 = get_nonterminals_in_cell(i, i+j)
            nts2 = get_nonterminals_in_cell(i+j, i+width)
            for nt1 in nts1:
                productions = grammar.productions(rhs=nt1)
                for production in productions:
                    for nt2 in nts2:
                        if nt2 == production.rhs()[1]:
                            add_entry(i, i+width, production.lhs(), [Item(nt1,i, i+j), Item(nt2, i+j, i+width)])


# Parsebaeume
def extract_parsetrees(start, end, nonterminal):
    ret = []
    for childItems in get_items(start, end, nonterminal):
        if len(childItems) == 1:
            ret.append("{0}({1})".format(nonterminal, childItems[0]))
        else:
            leftTrees = extract_parsetrees(childItems[0].start, childItems[0].end, childItems[0].nonterminal)
            rightTrees = extract_parsetrees(childItems[1].start, childItems[1].end, childItems[1].nonterminal) 
            for (left, right) in itertools.product(leftTrees, rightTrees):
                ret.append("{0}({1},{2})".format(nonterminal, left, right))
    return ret


print "\nChart:"
for row in chart:
    print row

print "\nParse trees:"
for tree in extract_parsetrees(0, n, nltk.grammar.Nonterminal("S")):
    print tree


            
            
            
            
            

