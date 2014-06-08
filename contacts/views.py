from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse



#from contacts.models import Person
from .models import Person, ExtraDetail
from .form import ContactForm, DeleteForm


# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request, 
                  'index.html', 
                  {'persons' : persons } )


def new_contact(request):
    if request.method == "GET":
        # render form
        return render(request,
                      'new_contact.html',
                      {'form' : ContactForm} )

    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            p = Person.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
            )
            ExtraDetail.objects.create(
                person = p,
                notes = form.cleaned_data['notes'],
                website = form.cleaned_data['website'],
                relationship = form.cleaned_data['relationship'],
                birthday = form.cleaned_data['birthday'],
            )
            # redirect to index page
            return redirect(reverse('index'))
        return render(request,
                      'new_contact.html',
                      {'form' : form})


def edit_contact(request, contact_id):
    contact = Person.objects.get(pk=contact_id)
    if request.method == "GET":
        form = ContactForm(
                initial = {
                    'first_name' : contact.first_name,
                    'last_name' : contact.last_name,
                    'phone_no' : contact.phone_no,
                    'address' : contact.address,
                    'website' : contact.extradetail.website,
                    'notes' : contact.extradetail.notes,
                    'birthday' : contact.extradetail.birthday,
                    'relationship' : contact.extradetail.relationship,
                } 
        )
        return render(request,
                      'new_contact.html',
                      {'form' : form})
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.phone_no = form.cleaned_data['phone_no']
            contact.address = form.cleaned_data['address']
            contact.extradetail.website = form.cleaned_data['website']
            contact.save()
            return redirect(reverse('index'))
        else:
            return render(request,
                          'new_contact.html',
                          {'form' : form} )
               


def delete_contact(request, contact_id):
    contact = Person.objects.get(pk=contact_id)
    if request.method == "GET":
        return render(request,
                      'confirm_delete.html',
                      {'form' : DeleteForm})
    elif request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            contact.delete()
            return redirect(reverse('index'))
        else:
            return render(request,
                          'confirm_delete.html',
                          {'form' : DeleteForm} )
                
