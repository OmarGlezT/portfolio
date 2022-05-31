from django.db import models
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField

class Project(models.Model):
    image = models.ImageField(upload_to='images/', null=True) 
    description = models.TextField(max_length=200)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def delete(self, using=None,keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    message = models.TextField()

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email_address', 'message']