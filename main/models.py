from django.db import models


class Team(models.Model):
    captain = models.TextField()
    name = models.TextField()
    position = models.TextField()
    valid_steps = models.TextField()
    add_steps = models.TextField()
    hints = models.TextField()

    def __str__(self):
       return self.captain, self.name, self.position, self.valid_steps, self.add_steps, self.hints
