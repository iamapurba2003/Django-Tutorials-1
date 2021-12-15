from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthDictionary = {
    'january':"Eat everything this month",
    'february':"Learn to code",
    'march':"Eat no snacks this month",
    'april':"Prepare for IIT-JEE",
    'may':"Have a relax",
    "june":"Do nothing",
    "july":"Grab orders for web dev",
    "august":"Make a routine",
    "september":"Eat each and every snacks",
    "october":"Eat no chicken this month",
    "november":"Learn nothing this month",
    "december":"Go to Gym"
}


def index(request):
    listMonths = list(monthDictionary.keys())
    return render(request, "./challenges/index.html", {
        "allMonth":listMonths,
    })




def challengeByNumber(request, month):
    try:
        monthList = list(monthDictionary.keys())
        redirectMonth = monthList[month-1]
        redirectPath = reverse("strMonth", args=[redirectMonth]) #This creates the path as /challenges/{month name}
        return HttpResponseRedirect(redirectPath)
    except Exception:
        return HttpResponse("Invalid Month")


def monthlyChallenge(request, month):
    chllngText = ""
    for i in monthDictionary:
        if i == month:
            chllngText = monthDictionary[i]
            return render(request, "challenges/challenge.html", {
                "text":chllngText,
                "curMonth": i
            })
    else:
        return HttpResponseNotFound("Invalid Month")