from django import forms

class ReviewForms(forms.Form):
    user_name = forms.CharField(max_length=100, label="Your Name")
    review_Text = forms.CharField(label="Your Feedback", widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5, label='Your Rating')
