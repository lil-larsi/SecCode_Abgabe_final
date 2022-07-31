import re
import random
from typing import List

HEX_GRAMMAR= {
'<start>': ['x<SINGLE_BIT>'],
'<NUMBER>':  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
'<HEX_LETTERS>' : ['A', 'B', 'C', 'D', 'E', 'F'],
'<SINGLE_BIT>' : ['<HEX_LETTERS><NUMBER>', '<HEX_LETTERS><HEX_LETTERS>', '<NUMBER><HEX_LETTERS>', '<NUMBER><NUMBER>']
}

RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
START_SYMBOL = '<start>'
def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_NONTERMINAL, expansion)


def is_nonterminal(s):
    return re.match(RE_NONTERMINAL, s)





class ExpansionError(Exception):
    pass

def simple_grammar_fuzzer(grammar, start_symbol=START_SYMBOL,
                          max_nonterminals=10, max_expansion_trials=100,
                          log=False):
    term = start_symbol
    expansion_trials = 0

    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))

    return term

#trys finding good input for seeds

#z = "b'BM\\xf6\\xd4\\x01\\x00\\x00\\x00\\x00\\x006\\x00\\x00\\x00(\\x00\\x00\\x00\\xc8\\x00\\x00\\x00\\xc8\\x00\\x00\\x00\\x01\\x00\\x18\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\vx00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00v\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00\\xff\\x00\\x00"
#d="sd\asd\asdh\da\"
#d = d.replace("\","\\")
# z = ''
# for i in range(29900):
#    if i == 0:
#        z = z + simple_grammar_fuzzer(grammar= SIMPLE_ABC_GRAMMAR) 
#    else:
#        z = z + "\\" + simple_grammar_fuzzer(grammar= SIMPLE_ABC_GRAMMAR)
# z = z + "'"
# print(len(z))
# with open('/home/lars/Projektobjekt/Fuzzingffjpeg/src/inputbmp/test_erzeugt.bmp', 'wb') as f:

with open('XXXX/Fuzzingffjpeg/src/inputbmp/test.bmp', 'rb') as f:
    x = f.read()
    print(type(x))
    print(type(x[0]))
    print(x[0])
    print(len(x))
    hex_string = "0xFF"
    an_integer = int(hex_string, 16)
    print(an_integer)
    hex_value = hex(an_integer)
    print(hex_value)
    print(type(an_integer))
    fileheader = x[1]
    test="xf6"
    test2 = bytes(an_integer)
    print(test2)
    print(test[0])
    print(fileheader)
