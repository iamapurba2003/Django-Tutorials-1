from django.shortcuts import render
from .forms import ReviewForms
from .models import ReviewModel

# Create your views here.

def reviews(request):
    forms = ReviewForms()
    render(request, 'reviews/reviews.html', args={
       "form": forms})
    if reuqest.method == "POST":
        if forms.is_valid():
            stored_data = forms.cleaned_data
            modelInsert = ReviewModel(user_name=stored_data['user_name'], review_Text=stored_data['review_Text'], rating=stored_data['rating'])
            modelInsert.save()
            return HttpResponseRedirect('thank-you/')

def thank_you(request):
    render(request, "reviews/thank-you.html")
