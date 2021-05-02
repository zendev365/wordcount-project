from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')

def aboutPage(request):
    return render(request, 'about.html')

def countPage(request):
    fullText = request.GET['fullText']
    # print(fulltext)
    wordList = fullText.split()

    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            # increase
            wordDictionary[word] += 1
        else:
            # add to the wordDictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',
    {
    'fullText':fullText,
    'count':len(wordList),
    'sortedWords':sortedWords,
    })
