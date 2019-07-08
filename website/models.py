from django.db import models

# Create your models here.

class GetInTouch(models.Model):
    class Meta:
        verbose_name_plural = 'get in touches'
        ordering = ['email']

    email = models.EmailField()
    contacted = models.BooleanField(default=False)
    language = models.CharField(max_length=4, default="en")

    def __str__(self):
        if self.contacted:
            return f'done {self.language} {self.email}'
        else:
            return f'not contacted {self.language} {self.email}'
    