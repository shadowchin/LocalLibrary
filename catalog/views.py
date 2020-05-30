from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre, Language

def dashboard(request):
    return render(request, 'catalog/dashboard.html', {})

def test(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1Ijoic2hhZG93Y2hpbiIsImEiOiJja2FxbXUwdjgwYmw1MnlsZ3M5eXg4NDQ0In0.aP5N1o59VTKaX_jJlKRcyQ'
    return render(request, 'catalog/test.html', { 'mapbox_access_token': mapbox_access_token } )

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of Genre
    num_genres = Genre.objects.all().count()

    # Books that contain the word 'money'
    num_books_money = Book.objects.filter(title__contains='Money').count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Create a python dictionary 'context'
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_money' : num_books_money,    
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

