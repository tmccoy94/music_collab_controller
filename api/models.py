from django.db import models
import string, random

def generate_unique_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # k is length for this function
        if Room.objects.filter(code=code).count() == 0: # query and check if there are any codes equal to this one
            break # if code is unique break the loop
        
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # unique ID
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # can add methods - make it PHAT lol