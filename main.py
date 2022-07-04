import nltk


def print_tree(input_trees):
    for i in range(len(input_trees)):
        print(input_trees[i], end="")


def run_parsers(input_grammar, input_sentence):
    print("Top-down parser: ", end="")
    print_tree(list(nltk.RecursiveDescentParser(input_grammar).parse(input_sentence)))
    print()

    print("Bottom-up parser: ", end="")
    print_tree(list(nltk.ShiftReduceParser(input_grammar).parse(input_sentence)))
    print()

    print("Top-down + Bottom-up parser: ", end="")
    print_tree(list(nltk.LeftCornerChartParser(input_grammar).parse(input_sentence)))
    print()


grammar = nltk.CFG.fromstring("""
    S -> VP
    VP -> Verb NP
    NP -> Det Nominal
    Nominal -> Noun
    Verb -> 'book'
    Det -> 'that'
    Noun -> 'flight'
  """)
sentence = ['book', 'that', 'flight']
print("sentence : book that flight")

run_parsers(grammar, sentence)
print()

grammar = nltk.CFG.fromstring("""
    S -> Aux NP VP
    NP -> Pronoun
    VP -> Verb NP
    NP -> Nominal
    Nominal -> Proper-Noun Nominal
    Nominal -> Noun
    Aux -> 'can'
    Pronoun -> 'you'
    Verb -> 'book'
    Proper-Noun -> 'TWA'
    Noun -> 'flights'
  """)
sentence = ['can', 'you', 'book', 'TWA', 'flights']
print("sentence : can you book TWA flights")

run_parsers(grammar, sentence)
