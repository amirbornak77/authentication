from django.db import models
from account.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

class IdentityDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='identity_documents')
    document_type = models.CharField(max_length=50)  # type of document that should be considered for identity like passport or identity card
    document_number = models.CharField(max_length=50)
    document_image = models.ImageField(upload_to='identity_documents/')

class VerificationVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_videos')
    video = models.FileField(upload_to='verification_videos/')

class IdentityVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='identity_verification')
    verified = models.BooleanField(default=False)