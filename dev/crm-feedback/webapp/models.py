from django.db import models

class Venue(models.Model):                                     # 1st as no ref to other tables
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, verbose_name=("Phone (use international +1xx format):"))
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    upload = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name
    #upload = models.FileField(upload_to="media/", blank=True)
    #upload = models.FileField(upload_to="media/%Y/%m/%d/")

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, verbose_name=("Genre:"), choices=(('Pop', 'Pop'), ('Rock', 'Rock'), ('Country', 'Country'), ('Classical', 'Classical')), default='bull')
    date = models.DateTimeField(verbose_name=("Doors open:"))
    description = models.TextField(blank=True)
    webpage = models.URLField(default='https://')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)                         # one to many
    persons = models.ManyToManyField('Person', through='PersonEvent', blank=True)      # m2m ref to 2nd table, not def yet --> in '' !!!
    
    def __str__(self):
        return self.name

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, verbose_name=("Phone (use international +1xx format):"))
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    events = models.ManyToManyField(Event, through='PersonEvent', blank=True)            # m2m ref to table already defined

    def __str__(self):
        return self.first_name + "   " + self.last_name

class PersonEvent(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)   # same name as in pre classes
    event = models.ForeignKey(Event, on_delete=models.CASCADE)     # same name as in pre classes
    info = models.CharField(max_length=50)                         # Example: "Author", "Co-author"
    class Meta:
        unique_together = ('person', 'event')                      # Enforce composite + unique primary key

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, verbose_name=("Feedback Subject:"), choices=(('Venue', 'Venue'), ('Event', 'Event'), ('Person', 'Person'), ('General', 'General')), default='General')
    date = models.DateTimeField(verbose_name=("Time of incident:"))
    description = models.TextField(blank=True)
    urgency = models.CharField(max_length=100, verbose_name=("Incident Urgency:"), choices=(('Normal', 'Normal'), ('High', 'High'), ('Low', 'Low')), default='Normal')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.subject