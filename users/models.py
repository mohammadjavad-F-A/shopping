from django.db import models

class more_users(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    image = models.ImageField(upload_to="users")
    phone = models.IntegerField()

    def __str__(self):
        return self.user_name



