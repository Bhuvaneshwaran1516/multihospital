from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Hospitalavail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    availability=models.CharField(max_length=50,null=True)
    info=models.TextField(null=True)
    CATEGORY_CHOICES = [
        ('cylinder', 'Cylinder'),
        ('blood', 'Blood'),
        ('organ', 'Organ'),
    ]
    availabilitylist = models.CharField(max_length=10, choices=CATEGORY_CHOICES,null=True)
    image = models.ImageField(upload_to='hospital_images/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name


class HospitalRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    hospital_avail = models.ForeignKey(Hospitalavail, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='pending')
    message = models.TextField(null=True, blank=True)
    response_message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Request from {self.from_user} to {self.to_user} for {self.hospital_avail.name}"


class HospitalDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.BigIntegerField(null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Hospital Details"