from django.db import models

# Create your models here.


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    del_article = models.BooleanField()
    edit_article = models.BooleanField()
    can_mange_role = models.BooleanField()
    can_mange_user = models.BooleanField()
    can_mange_article = models.BooleanField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['-date_time']
