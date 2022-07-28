from django.db import models

# Create your models here.

status_choices = [
    (0,'In progress'),
    (1,'Finished')
]
class ToDo(models.Model):
    content = models.CharField(max_length=150)
    #user = models.ForeignKey(Usuario)
    status = models.IntegerField(choices=status_choices,default=0,)

    def __str__(self):
        return f'{self.content}'