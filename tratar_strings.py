import re
from collections import Counter

def consoante(string):
    count=0
    c = Counter(re.sub('[^bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ]', '', string))
    for i in c:
       count=count+c[i] 
    return count

def vogal(string):
    count=0
    v = Counter(re.sub('[^aeiouAEIOUâãàáêéèîíìõôóòûúùÂÃÀÁÊÉÈÎÌÍÔÕÓÒÛÚÙ]', '', string))
    for i in v:
       count=count+v[i] 
    return count


def chars(string):
    count=0
    v = Counter(re.sub('[^aeiouAEIOUbcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ âãàáêéèîíìõôóòûúùÂÃÀÁÊÉÈÎÌÍÔÕÓÒÛÚÙ|\<,>.:;?//^~`´/{/}/[/]/]', '', string))
    for i in v:
       count=count+v[i] 
    return count

def inverso(string):
    i=string[::-1]
    return i

def tratar(clientMsg):
    return vogal(clientMsg),consoante(clientMsg),inverso(clientMsg),chars(clientMsg)

def remove_b(s):
    s =  s[2:-1]
    return s
