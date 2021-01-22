from django.shortcuts import render
from contacts.models import Contact
from . import views
# from contacts import navigation

# Create your views here.

def contact(request):
          contacts = Contact.objects.all()

          context = {
            'contacts': contacts,
          }

          return render(request, 'contacts/contacts.html', context)
