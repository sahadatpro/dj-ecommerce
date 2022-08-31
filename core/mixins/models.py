from django_userforeignkey.models.fields import UserForeignKey
from django.db import models

class UserForeignKeyMixin(models.Model):
       created_by  = UserForeignKey(auto_user_add=True, verbose_name="Created By", related_name="%(app_label)s_%(class)s_created_by_related")
       updated_by  = UserForeignKey(auto_user=True, verbose_name="Update By", related_name="%(app_label)s_%(class)s_updated_by_related")
       
       class Meta:
              abstract = True 
       
class TimeStampMixin(models.Model):
       created = models.DateTimeField(auto_now_add=True)
       updated = models.DateTimeField(auto_now=True)
       class Meta:
              abstract = True
              
class AuthorWithTimeMixin(UserForeignKey, TimeStampMixin):
       pass 

       class Meta:
              abstract = True