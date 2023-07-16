from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
# Create your views here.
from django.urls import reverse

monthly_challenges = {
    'january':'Eat meat',
    'february':'Eat apple',
    'march':'Eat pie',
    'april':'Eat nothing',
    'may':'Eat something',
    'june':'Eat anything',
    'july':'Eat ice',
    'august':'Eat bubble',
    'september':'Eat carrot',
    'october':'Eat mayoneese',
    'november':'Eat sausage',
    'december':'Eat potatpop',

}


def monthly_challenge(request, month):

    try:
        text = monthly_challenges[month]
        response_data = f"<h1 style=color:red;background-color:blue;>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('This month is not supported!')


def monthly_challenge_by_number(request, month):

    months_by_name = list(monthly_challenges)
    if month > len(months_by_name):
        return HttpResponseNotFound('Invalid month')

    m = months_by_name[month-1]
    redirected_path = reverse('month-challenge',args=[m])

    return HttpResponseRedirect(redirected_path)


def month_list(request):
    lista = list(monthly_challenges)
    data = [f"<li><a href='{month}'>{month}</a></li>" for month in lista]

    ul = f"<ul>{' '.join(str(x) for x in data)}</ul>"
    return HttpResponse(ul)

