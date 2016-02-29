from django.shortcuts import render
from .apps import Utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings




def landing_page(request):

    movie_list = Utils.MyData
    query = request.GET.get("q")
    if query:
        movie_list = Utils.search_data(query)

    #Pagination handled here:    
    paginator = Paginator(movie_list, 10)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)

    #end pagination    
    
    context = {
        "movies": movies
    }

    return render(request, "starter/landing_page.html", context)

def movie_detail(request, id):

    movie_list = Utils.MyData

    for movie in movie_list:

        if movie['id'] == id:
            context = {
                "movie": movie
            }



    return render(request, "starter/movie_detail.html", context)
