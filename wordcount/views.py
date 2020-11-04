from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    worddictionary= {}
    for word in wordslist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordslist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')