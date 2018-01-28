# Minion game
# Input: single line of input containing the string S that contain only uppercase letters: [A-Z]
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 
# Output: the name of the winner and their score separated by a space. print "Draw" if draw

# Optimization step: for a the substrings that start with s[i] are all scored to the same person, 
# it does not matter what the substrings are.


def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"  
