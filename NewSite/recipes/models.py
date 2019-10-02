from django.db import models

class Account(models.Model):
    firstName = models.CharField(max_length=20, help_text='Enter firstname')
    lastName = models.CharField(max_length=20, help_text='Enter lastname')
    dateOfBirth = models.CharField(max_length=20, help_text='Enter date of birth')
    email = models.CharField(max_length=20, help_text='Enter email')   
    userName = models.CharField(max_length=20, help_text='Enter username')
    passWord = models.CharField(max_length=20, help_text='Enter password')
    retypePassWord = models.CharField(max_length=20, help_text='Retype Password') 

    def __str__(self):
        return self.lastName + " " + self.firstName
