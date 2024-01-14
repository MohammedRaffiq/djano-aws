from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class register(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']





class Topic(models.Model):

    do =  [
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('c++', 'C++'),
        ('php', 'PHP'),
        ('ruby', 'Ruby'),
        ('swift', 'Swift'),
        ('typescript', 'TypeScript'),
        ('aws', 'aws'),
    ]
    name = models.CharField(max_length=50, choices = do)


    # name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:20]
    

class Profile(models.Model):
    connect = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default ='2.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.connect.username} Profile"



