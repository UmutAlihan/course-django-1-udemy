from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": 'eat no meat for entire month',
    "february": 'walk for at least 20 mins a day',
    "march": 'march text is here',
    "april": 'april challenge',
    "may": 'may challenge',
    "june": 'june challenge',
    "july": 'july challenge',
    "august": 'august challenge',
    "september": 'september challenge',
    "october": 'october challenge is here',
    "november": 'november challenge',
    "december": None
}

# Create your views here

def index(request):
    #list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('monthly-challenge', args=[redirect_month])
    #builds a path: /challenge/january (january comes from args)
    # bu sayede urls.py içerisinde değiştirirsen buraya kendiliğinden yansıtılır
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    ## month -> is the identifier as defined in brackets from challenges/urls.py
    ## multiple <..> dynamic url parameters -> can be extracted simply by name as parameters in view function (as kywargs)
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month': month
        })
        ## template not found error verirse -> settings.py içerisinde template_dirs değişkeni eklenir
        return HttpResponse(response_data)
    except:
        raise Http404()