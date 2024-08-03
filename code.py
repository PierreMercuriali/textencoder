"""
    Python Language Encoder
    https://github.com/vgaj/ple highlighted a very important thing in cryptography: if people (or machines)
    do not know there is a hidden message, they won't try to decode it.
    Input :
    I suggest using the "Lorem ipsum" dictionary
    because people have now been trained to gloss over and ignore latin-looking text. 
    This could probably be verified with a cognitive survey but I don't have the funding for that!
    usage : python code.py <option> <dictionary> <input> <output>

"""
import sys
OPTION              = sys.argv[1]
FILENAME_DICTIONARY = sys.argv[2]
FILENAME_INPUT      = sys.argv[3]
FILENAME_OUTPUT     = sys.argv[4]
WORDS               = []
with open(FILENAME_DICTIONARY, 'r') as f:
    WORDS = f.read()[:-3].split('\n')


def encode(text, dictionary):
    res = []
    for c in text:
        num = ord(c)
        try:
            res.append(dictionary[num])
        except:
            res.append(c)
    return ' '.join(res)
def decode(text, dictionary):
    res = []
    for word in text.split(' '):
        if word in dictionary:
            res.append(chr(dictionary.index(word)))
        else:
            res.append(word)
    return ''.join(res)

with open(FILENAME_INPUT, 'r') as f:
    text = f.read()
out = text
if OPTION in ['e', 'encode', 'encoding']:
    out_ = encode(text, WORDS)
if OPTION in ['d', 'decode', 'decoding']:
    out_ = decode(text, WORDS)
with open(FILENAME_OUTPUT, 'w') as f:
    f.write(out_)
