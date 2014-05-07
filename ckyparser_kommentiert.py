'''
Created on May 3, 2011

@author: koller
'''

import nltk

def print_chart(chart, num_of_tabs=1):
    """nicht notwendige, selbstgebastelte Funktion zum Drucken von Charts"""
    tabstring = '\t' * num_of_tabs
    for row in chart:
        print tabstring+"\t".join([str(list(element)) for element in row])

# Input
words = ["I", "shot", "an", "elephant", "in", "my", "pajamas"]
print "Text to be parsed:\n\t{}".format(words)
n = len(words)


# Grammatik aus String lesen und in 'grammar' repraesentieren
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

print "\nGrammar rules:"
for prod in grammar.productions():
    print "\t", prod
print "\n"

# leere Chart bauen
chart = []
for i in range(n+1):
    # Erzeuge eine leere Zeile
    row = []
    # Haenge n+1 leere Mengen (set()) an
    for j in range(n+1):
        row.append(set())
    # Haenge die neue Zeile an die Chart an
    chart.append(row)

print "Initial chart:"
print_chart(chart)

## Zugriff auf Chart-Eintraege
#def get_entries(i, k):
#    return chart[i][k]
#
#def add_entry(i, k, item):
#    if( not (item in chart[i][k])):
#        chart[i][k].append(item)

# Terminalproduktionen
# Iteriere ueber alle Positionen des Eingabesatzes
for i in range(n):
    # Iteriere ueber alle Regeln der Grammatik, die das Wort words[i] als rechte Seite haben
    # z.B. words[4] = 'elephant' und N -> 'elephant'
    print "productions for terminal '{}':".format(words[i])
    for prod in grammar.productions(rhs=words[i]):
        print "\t", prod
        # Fuege in die Zelle fuer die Spanne von i bis i+1 die linke Regel (z.B. N)
        # in die Menge ein (.add())
        chart[i][i+1].add(prod.lhs())
        print "\t{0} added to chart[{1}][{2}]\n".format(prod.lhs(), i, i+1)

print "Chart after filling it with terminal productions:"
print_chart(chart)

# Bottom-up
# Iteriere ueber alle Spannen ab Laenge 2
for width in range(2, n+1):
    # Iteriere ueber alle moeglichen Anfaenge einer Spanne
    for i in range(0, n-width+1): # i + width <= n
        # Iteriere ueber alle moeglichen Teilungspunkte dieser Spanne
        for j in range(1, width): # 1 <= j <= width-1
            # Jetzt wollen wir Nichtterminale aus 2 gegebenen Chartzellen kombinieren
            # Wir speichern beide erst mal in jeweils einer Variablen
            nts1 = chart[i][i+j]
            # j ist der Teilungspunkt: eine Spanne geht von i bis i+j, die andere von
            # i+j bis i+width
            nts2 = chart[i+j][i+width]
            if nts1 and nts2:
                print ("\ntry to combine nonterminals from [{0}][{1}] ({2})"
                      " and [{3}][{4}] ({5})".format(i, i+j, list(nts1), i+j, i+width, list(nts2)))
                # Iteriere nun ueber alle Nichtterminale der ersten Zelle
                for nt1 in nts1:
                    # Bestimme die Kandidatenregeln, die ein Nichtterminal aus nts1 als
                    # erstes Element auf ihrer rechten Regelseite haben
                    # Beispiel: nts1 enthaelt NP => suche alle Regeln der Form X => NP Y,
                    # z.B. S -> NP VP
                    productions = grammar.productions(rhs=nt1)
                    if productions:
                        print "\tproductions for nonterminal '{}' (1st element of RHS)".format(nt1)
                    else:
                        print "\tNO productions where nonterminal '{}' is the 1st element of RHS!".format(nt1)
                    # Gehe nun diese Kandidatenregeln durch
                    for production in productions:
                        # Pruefe, ob das 2. Element der rechten Regelseite (production.rhs()[1]),
                        # (also im Beispiel oben VP) im anderen Kaestchen enthalten ist
                        if production.rhs()[1] in nts2:
                            # ok, fuege dann die rechte Regelseite (also S) in das Zielkaestchen
                            # chart[i][i+width] ein. Dieses enthaelt alle Nichtterminale, die die
                            # Eingabe zwischen den Positionen i und i+width ableitet.
                            print ("\t\t2nd element of production RHS '{0}' is also in '{1}'"
                                  "\n\t\tLHS will be added to [{2}][{3}]".format(production, list(nts2), i, i+width))
                            chart[i][i+width].add(production.lhs())
                            print_chart(chart, 2)
                        else:
                            print "\t\t2nd element of production RHS '{0}' NOT in '{1}'!".format(production, list(nts2))
            else: # if either 'nts1' or 'nts2' is empty
                continue # don't try to combine empty sets, continue with next iteration

# Gib nun die Chart aus
print "\nResulting chart:"
print "================"
print_chart(chart)
