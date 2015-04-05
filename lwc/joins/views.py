from django.shortcuts import render
from joins.forms import JoinForm
from joins.models import Join

# Create your views here.
def home(request):
    """
    Answers request to the index page
    """
    # This is using regular django form
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email = email)
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        old_join, created = Join.objects.get_or_create(email=email)
    template = "home.html"
    context = {"form": form}
    return render(request, template, context)
