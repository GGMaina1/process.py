# python -m venv name1
#name1\Scripts\activate
#pip install django
#django-admin startproject name2
#cd name2
#python manage.py startapp name3
#python manage.py runserver


#settings.py > add the app at installed app
#copy urls.py to apps
#configure it in project urls.py + add  import include__(from django.urls import path, include)
           # __(path('',include('name3.urls') ),)
#create a folder-Templates at root directory
#configure it at settings.py__('DIRS': ['Templates'],)
#create a html file at Templates___(index.html)
#add a function at views.py__(def home(request):
#                                                          return render(request,'index.html'))
#in app urls.py link url to its function
            #first import views.py__(from cartapp import views)
            #add the line __(path('home/', views.home),)

#commands to run the website---terminal
#python -m venv name1
#cart\Scripts\activate
#pip install django
#python manage.py runserver (8000-)


#configuring static files--go to settings at static_url--write
        #STATICFILES_DIRS=[
#              BASE_DIR, 'static',
 #          ]
 #using static having images at assets file in html
#       write(__{% load static %})btwn the head tags
#       at ther line to display the image__(<img src="{% static 'assets/img.png' %}" alt="">)


# using inheritance in html files
# in the parent page
#    write   (    {% block content %}

 #                      {% endblock %}   )
 #   btwn the text that will be different

 #at the page to inherit...
 # write(   {% extends 'starter-page.html' %}
#                {% load static %}
#                {% block content %}   )
# place the content here---
#close-----{%endblock%}

###step to be an admin
#in terminal---
#python manage.py migrate
#python manage.py createsuperuser
#follow the steps---



#DATABASE
#start at models.py
#   class patient(models.Model)

#   >if text   use
#                 name= models.CharField(max_length=x)
#   others-
#                  age = models.IntegerField()
#                  email = models.EmailField()
#                  message = models.TextField()
# to display the name of the patient
#---in models.py
#                   def __str__(self):
#                         return self.fullname


#command to run the model
# python manage.py makemigrations
# python manage.py migrate


#registering migrations
#go to admin.py
#import models
#---admin.site.register(patient)

##CONNECTING THE DATA FROM FRONTEND TO BACKEND
#1         <form method="post" >
 #2           {% csrf_token %}
#3    have a name attribute for all inputs
#4   <button type="submit">Make an Appointment</button></div>
#5  at views.py---change the line    return render(request,'departments.html')

#--  to        if request.method == "POST":
 #                    myappointments=Appointment(    ---Appointment is the name of the model
 #                          name=request.POST['name'],
 #                          email=request.POST['email'],
 #                          others____
#                     )

#time to save
#                    myappointments.save()
 #                   return redirect('/appointment/')
 #               else:
  #                  return render(request,'appointment.html')
#               


###DISPLAY DATA
#in views.py
#def show (request):
#   all = Appointment.objects.all()
#   return render(request,'show.html',{'all':all})

#in urls.py
#path('show/', views.show, name='show'),

#in show.html
#  {% for x in all %}
#      <div class="card w-30">
#      <p class="text-primary fw-bold">{{ x.name }}</p>
#      <p><strong>Email :</strong> {{ x.email }}</p>
#      <p><strong>Phone :</strong> {{ x.phone }}</p>
#      <p><strong>Date :</strong> {{ x.date }}</p>
#      <p><strong>Department :</strong> {{ x.department }}</p>

#      </div>
#  {% endfor %}

#deleting an appointment
#define id---
#in views.py
#def delete (request,id):
#    deleteappointment = Appointment.objects.get(id=id)
#    deleteappointment.delete()
#    return redirect('/show/')

#in urls.py
#path('delete/<int:id>', views.delete),

#in the html page
#<a href="/delete/{{ x.id }}" class="text-danger">
#    <i class="bi bi-trash"></i>Delete
#</a>










