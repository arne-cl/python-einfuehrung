Python-Einführung (für eilige Computerlinguisten)
=================================================

Dieses Repository enthält eine Python-Einführung für die Vorlesung
_Computerlinguistische Techniken_ (Sommersemester 2014, Universität Potsdam).

Installation und Benutzung
--------------------------

Die Einführung kann man am einfachsten [hier](http://nbviewer.ipython.org/github/arne-cl/python-einfuehrung/blob/master/python-intro.ipynb)
mit dem IPython Notebook Viewer betrachten. Bearbeiten und verändern lässt sie sich wie folgt:

```
git clone https://github.com/arne-cl/python-einfuehrung.git
cd python-einfuehrung
ipython notebook
```

Wer noch mehr computerlinguistische Themen mit Python und NLTK ausprobieren möchte, dem sei die Webseite [Natural Language Processing and Applications](http://nlpa.iupr.com/resources) der Uni Kaiserslautern ans Herz gelegt. Dort gibt es diverse IPython-Notebooks zu NLTK, regulären Ausdrücken, Hidden Markov Models, Unicode, POS-Tagging, Transduktoren und einigen Klassifikatoren.

Visualisierung von Programmabläufen
-----------------------------------

Mein Beispiel zur Visualisierung des CKY-Erkenners (Code: A. Koller/ T. Hanneforth)
könnt ihr euch zwar [online ansehen](http://nbviewer.ipython.org/github/arne-cl/python-einfuehrung/blob/master/cky-parser-visualization.ipynb),
sie funktioniert allerdings nur richtig, wenn ihr sie lokal auf eurem Rechner installiert (s.o.).
Hierfür muss zudem noch [ipythonblocks](http://ipythonblocks.org/) installiert werden.

Weitere Pakete installieren
---------------------------

Wie man Python-Pakete mit pip installiert, habe ich [hier](python-pakete-installieren.md) zusammengefasst.


Fehlersuche in Python-Programmen
--------------------------------

Zum Debuggen habe ich [pudb](https://pypi.python.org/pypi/pudb/) vorgestellt.
Das Paket lässt sich auch mit `pip` installieren, funktioniert aber
anscheinend nur unter Linux/Mac OS. Alternativ könnt ihr es mit
[winpdb](http://winpdb.org/download/) probieren (Windows/Linux/Mac OS).

Es gibt einen kostenlosen Online-Kurs zum Thema Debugging (in Python) bei
[Udacity](https://www.udacity.com/course/cs259) von Andreas Zeller (die
Videos sind thematisch gegliedert, man kann sie sich auch einzeln ansehen). 
Von ihm stammt auch das schöne Buch [Why Programs Fail](http://www.whyprogramsfail.com/).


System-Voraussetzungen
----------------------

Zum Bearbeiten des Notebooks benötigt man [git](http://git-scm.com/downloads) sowie [IPython](http://ipython.org/install.html).

Lizenz
------

Dieses Geschwurbel ist lizensiert unter der [Creative Commons Attribution-ShareAlike 4.0 International License]("http://creativecommons.org/licenses/by-sa/4.0/").

Autor
-----

Arne Neumann


