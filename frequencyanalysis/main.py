# This is code designed to count the frequency of the letters in a text.

inputtext = "NGYUJRWCQNMROONANWLNKNCFNNWVXWXJUYQJKNCRLJWMYXUHJUYQJKNCRLLRYQNABJWMFQJCRVYJLCCQJCQJBXWCQNRWMNGXOLXRWLRMNWLNRRWHXDANGYUJWJCRXWYUNJBNLXENAFQHCQNHJANMROONANWC"

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
total = 0
for char in inputtext.lower():
    alphabet[char] += 1
    total += 1
print("Total number of letters: ", total)
print("Letter - count (percentage)")
for item in sorted(alphabet.items(), key=lambda x: x[1], reverse=True):
    print("%c - %3d (%d%%)" % (item[0], item[1], (100 * item[1]) / total))
