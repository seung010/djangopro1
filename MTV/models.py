
from django.db import models



class Answer(models.Model):
  # question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
      return self.content