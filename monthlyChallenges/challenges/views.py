from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, response
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no snacks this month!",
    "february": "Learn nothing this month!",
    "march": "Learn everything this month!",
    "april": "Beat the shit out of everyone!",
    "may": "Learn everything this month!",
    "june": "Learn everything this month!",
    "july": "Learn Python and master Django!",
    "august": "Beat the shit out of everyone!",
    "september": "Respect Everyone!",
    "october": "Master GK",
    "november": "Learn how to live",
    "december": "Do nothing",
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "monthsList":months
    })



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h2>Invalid Month</h2>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "monthName" : month
        })
    except:
        return HttpResponseNotFound("<h2>This month is not supported</h2>")
