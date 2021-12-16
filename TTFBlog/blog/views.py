from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

postsData = [{
    "slug": "Programming-Himangshu",
    "title":"Programming",
    "author_name":
    "Himangshu De",
    "id":1,
    "content":
    """Web content is dominated by the "page" concept, its beginnings in an academic setting, and in a setting dominated by type-written pages, the idea of the web was to link directly from one academic paper to another academic paper. This was a completely revolutionary idea in the late 1980s and early 1990s .""",
}, {
    "slug": "Nature-Arunodaya",
    "title":"Nature",
    "author_name":
    "Arunodaya Biswas",
    "id":2,
    "content":
    "The Earth we live in abounds with wonders, mysteries and miracles. Out of these, the most spectacular, spontaneous and splendid is what we call “Nature”. Mother Nature with unending powers to protect life when it should or uproot life if it must. The given paragraphs will give us a better idea of the diverse elements and forms found in nature."
}, {
    "slug": "Philosophy-Apurba",
    "title":
    "Philosophy",
    "author_name":
    "Apurba Ghosh",
    "id":3,
    "content":
    """Philosophy is the study of humans and the world by thinking and asking questions. It is a science and an art. Philosophy tries to answer important questions by coming up with answers about real things and asking "why?" Sometimes, philosophy tries to answer the same questions as religion and science."""
}]


def index(request):
    return render(request, "index.html", {
        "posts": postsData
    })


def posts(request):
    return render(request,"post.html", {
        "posts":postsData
    })


def postDetail(request, id):
    for data in postsData:
        if data['id'] == id:
            return render(request, 'post-detail.html',
            {
                "post":data
            })