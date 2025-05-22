from django.shortcuts import render
from cmanager.models import Contact
from django.http import HttpResponseRedirect

# Create your views here.

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'index.html',{'contacts':contacts})

def contact_delete(request, id):
    contacts = Contact.objects.get(id=id)
    contacts.delete()
    return HttpResponseRedirect('/')

def contact_update(request, id):
    contact = Contact.objects.get(id=id)
    
    if request.method == "GET":
        return render(request, "contact_update.html", {"contact": contact})
    
    else:
        contact.name = request.POST["name"]
        contact.email = request.POST["email"]
        contact.phone = request.POST["phone"]
        contact.save()
        return HttpResponseRedirect("/")

    

def contact_create(request):
    if request.method == "GET":
        return render(request, "create_contact.html")
    else:
        Contact.objects.create(name = request.POST["name"],
                               phone = request.POST["phone"],
                               email = request.POST["email"])
        return HttpResponseRedirect("/")