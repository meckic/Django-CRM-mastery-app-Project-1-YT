from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    #events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return self.first_name + "   " + self.last_name


class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    upload = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    webpage = models.URLField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Person, blank=True)
    
    def __str__(self):
        return self.name

#upload = models.FileField(upload_to="media/", blank=True)
#upload = models.FileField(upload_to="media/%Y/%m/%d/")













