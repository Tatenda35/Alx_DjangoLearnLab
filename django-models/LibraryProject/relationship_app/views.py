from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library


# Function-based view
def list_books(request):
    books = Book.objects.all()  # explicitly use Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Explicit path
    context_object_name = 'library'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Log in the user after registration
            return redirect("login")  # or redirect to a dashboard/home
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


