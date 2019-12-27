
from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def challenge(request):
    return render(request, 'challenge.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()


    #Counting most viewed words
    word_dic = {}

    for word in wordlist:
        if word in word_dic:
            #increase
            word_dic[word] += 1
        else:
            #add the word to the dic
            word_dic[word] = 1

    sorted_words = sorted(word_dic.items(), key = operator.itemgetter(1), reverse=True)



    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sorted':sorted_words})
