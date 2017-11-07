from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):
    
    """ Image models """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

    creator = models.ForeignKey(user_models.User, null=True) 

class Comment(TimeStampedModel):

    """ Comment models """
    message = models.TextField()

    creator = models.ForeignKey(user_models.User, null=True) 
    image = models.ForeignKey(Image, null=True)


class Like(TimeStampedModel):
    
    """ Like models """
    creator = models.ForeignKey(user_models.User, null=True) 
    image = models.ForeignKey(Image, null=True)