import re

patterns = ['term1','term2']

text = 'This is a string with term1, but not the other!'
text2 = 'term1'
split_term = '@'

email = 'user@gmail.com'

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern,text):
        print("Match!")
    else:
        print("No match!")

match = re.search('term1',text)
print(match.start())

match2 = re.search('term1',text2)
print(match2.start())

print(re.split(split_term,email))

print(re.findall('match','test phrase match in match middle'))

# There are five ways to express repetition in a pattern:
#
#     1.) A pattern followed by the meta-character * is repeated zero or more times.
#     2.) Replace the * with + and the pattern must appear at least once.
#     3.) Using ? means the pattern appears zero or one time.
#     4.) For a specific number of occurrences, use {m} after the pattern, where
#         m is replaced with the number of times the pattern should repeat.
#     5.) Use {m,n} where m is the minimum number of repetitions and n is the
#         maximum. Leaving out n ({m,}) means the value appears at least m times,
#         with no maximum.

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd*']
# S followed by 0 or more Ds
multi_re_find(test_patterns,test_phrase)

test_patterns2 = ['sd+']
# S followed by 1 or more Ds
multi_re_find(test_patterns2,test_phrase)

test_patterns3 = ['sd?']
# S followed by 0 or 1 Ds
multi_re_find(test_patterns3,test_phrase)

test_patterns4 = ['sd{3}']
# S followed by 3 Ds
multi_re_find(test_patterns4,test_phrase)

test_patterns5 = ['sd{1,3}']
# S followed by 1 to 3 D's
multi_re_find(test_patterns5,test_phrase)

test_patterns6 = ['sd{2,3}']
# S followed by 2 to 3 D's
multi_re_find(test_patterns6,test_phrase)

# Character sets are used when you wish to match any one of a group of
# characters at a point in the input. Brackets are used to construct character
# set inputs. For example: the input [ab] searches for occurrences of either a or b.

test_patterns6 = ['s[sd]+']
# one or more Ss or Ds
multi_re_find(test_patterns6,test_phrase)

#########################################################################################

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns6 = ['[^!.?]+']
# Use [^!.? ] to check for matches that are not a !,.,?, or space. Add the +
# to check that the match appears at least once, this basically translate into
# finding the words.
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = ['[a-z]+']
# Return the sequence of lower case characters
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = ['[A-Z]+']
# Return the sequence of upper case characters
multi_re_find(test_patterns6,test_phrase)

#########################################################################################

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

test_patterns6 = [r'\d+']
# Return back a sequence of digits
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = [r'\D+']
# Return back a sequence of non-digits
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = [r'\s+']
# Return back a sequence of whitespace
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = [r'\S+']
# Return back a sequence of non-whitespace
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = [r'\w+']
# Return back a sequence of alphanumeric characters
multi_re_find(test_patterns6,test_phrase)

test_patterns6 = [r'\W+']
# Return back a sequence of non-alphanumeric characters
multi_re_find(test_patterns6,test_phrase)
