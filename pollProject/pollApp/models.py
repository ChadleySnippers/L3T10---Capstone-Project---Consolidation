from django.db import models

# Define a Django model 'Question' with a text field and a publication date field
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# Define a Django model 'Choice' with a foreign key to 'Question', a text field, and a vote count field
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Note: The 'Question' and 'Choice' models are grouped together for admin site organization

