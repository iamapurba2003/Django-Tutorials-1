from django.shortcuts import render

# Create your views here.

def reviews(request):
   render(request, 'reviews/reviews.html')

def thank_you(request):
    render(request, "reviews/thank-you.html")
