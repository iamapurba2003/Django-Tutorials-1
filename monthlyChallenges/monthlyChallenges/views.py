from django.http.response import HttpResponse
from django.shortcuts import render

# Views created below

def emptyPage(request):
    return HttpResponse(f"""
    <title>Home</title>
    <ul>
        <li><a href="challenges/">Challenges</a></li>
        <li><a href="admin/">Admin</a></li>
    </ul>
    """)