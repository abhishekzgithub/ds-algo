"""
Vowel =['a',]
"""

def get_winner(s):
    vowel='aeiou'
    last_winner="chris"
    winner=[]
    while len(s)>0:
        ele =s.pop(0)
        if set(ele)-set(vowel)!=set(ele):
            for index,subele in enumerate(ele):
                if subele in vowel:
                    if index %2==0:
                        last_winner="alex"
                        winner.append(last_winner)
                    else:
                        last_winner="chris"
                        winner.append(last_winner)
        else:
            winner.append(last_winner)
    return winner


s=["llc",'cbi','qwt',"cde"]
print(s)
print(get_winner(s))