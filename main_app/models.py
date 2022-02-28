from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

EVENTS = (
    ('I', 'Indoor'),
    ('O', 'Outdoor'),
    ('R', 'Remote')
)

# Main_model(Many) to Star_model(another model with full CRUD --Many) Relationship
class Star(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('stars_detail', kwargs={'pk': self.id})

# Main Model.
class View(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  occassion = models.CharField(max_length=250)
  credit = models.CharField(max_length=50)
  stars = models.ManyToManyField(Star)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'view_id': self.id})
  
  def event_for_today(self):
    return self.event_set.filter(date=date.today()).count() >= len(EVENTS)
  
  # Main_model(One) to Event_model(Many) Relationship
class Event(models.Model):
  # date = models.DateField()
  date = models.DateField('event date')
  event = models.CharField(max_length=1, choices=EVENTS, default=EVENTS[0][0])
  view = models.ForeignKey(View, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_event_display()} on {self.date}"
  
    # change the default sort
  class Meta:
    ordering = ['-date']


