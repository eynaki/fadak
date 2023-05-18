from django.db import models


class UsersRegister(models.Model):
    user_name = models.TextField(max_length=50)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user_name} , {self.phone_number}"