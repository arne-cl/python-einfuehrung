import nltk

words = ["I", "shot", "an", "elephant", "in", "my", "pajamas"]

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

nltk.app.chartparser_app.ChartParserApp(grammar, words)
