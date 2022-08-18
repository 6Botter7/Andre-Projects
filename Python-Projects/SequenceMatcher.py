from difflib import SequenceMatcher
s_1 = 'Botter'
s_2 = 'Bter'
print(SequenceMatcher(a=s_1, b=s_2).ratio())
