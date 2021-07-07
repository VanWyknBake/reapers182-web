from django.shortcuts import render
from .models import Books, Home, About, Profile, Category, Skills, Portfolio, News


def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()
    books = Books.objects.all()
    news = News.objects.latest('desc')

    context = {
        'home': home,
        'news': news,
        'about': about,
        
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'books': books,
    }


    return render(request, 'index.html', context)
