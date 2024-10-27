from django.db import models

# Create your models here.
from django.db import models

class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ('suggestion', 'Suggestion'),
        ('compliment', 'Compliment'),
        ('complaint', 'Complaint'),
    ]
    
    SERVICE_CHOICES = [
        ('enquiries', 'Enquiries/Information'),
        ('complaint_handling', 'Complaint handling/dispute resolution'),
        ('home_building', 'Home building licenses'),
        ('business_licenses', 'Business licenses'),
        ('inspections', 'Inspections/Investigations'),
        ('transport_bonds', 'Transport/Travel bonds'),
        ('strata_mediation', 'Strata/State mediation'),
        ('cooperatives', 'Co-operatives/Associations'),
        ('asbestos', 'Loose-fill asbestos implementation taskforce'),
        ('other', 'Other'),
    ]
    
    ISSUE_CHOICES = [
        ('fair_trading', 'Fair Trading decision, policy or procedure'),
        ('administration', 'Administration of legislation'),
        ('information', 'Information accuracy'),
        ('timeliness', 'Timeliness of service'),
        ('staff', 'Staff actions/Customer service'),
        ('accessibility', 'Accessibility of service'),
        ('fees', 'Fees/Charges'),
        ('website', 'Website'),
        ('other', 'Other'),
    ]
    
    rating = models.IntegerField(default=0)
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    about_service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    about_issue = models.CharField(max_length=50, choices=ISSUE_CHOICES)
    other_service = models.CharField(max_length=100, blank=True, null=True)
    other_issue = models.CharField(max_length=100, blank=True, null=True)
    how_provided = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    fair_trading_officer = models.CharField(max_length=100, blank=True, null=True)
    date_of_service = models.DateField(blank=True, null=True)
    time_of_service = models.TimeField(blank=True, null=True)
    trader_or_consumer = models.CharField(max_length=50)
    feedback_details = models.TextField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    daytime_phone = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name