from django.db import models
from django.contrib.auth import models as mod_auth

class User(mod_auth.User):
    img = models.FileField(upload_to="users/imgs/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.img
