from django.db import models

class Question(models.Model):
    """
    Django model representing a question.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns a string representation of the question.

        Returns:
            str: The text of the question.
        """
        return self.question_text

class Choice(models.Model):
    """
    Django model representing a choice for a question.

    Attributes:
        question (Question): The question associated with the choice.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received for the choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Note: The 'Question' and 'Choice' models are grouped together for admin site organization
