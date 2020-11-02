from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags

# Create your models here.



class MetaInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='created_meta')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_meta')
      
    def __str__(self):
        return str(self.created_on)
 
 
class AnswerOption(MetaInfo):
    option_text = models.TextField()
    is_active = models.BooleanField(default=True)
    is_correct_ans = models.BooleanField(default=True)
    
    def __str__(self):
        return self.option_text


class Questions(MetaInfo):
    question = models.TextField(null=True, blank=True)
    answer_options = models.ManyToManyField(AnswerOption, blank=True)
    is_active = models.BooleanField(default=True)
    
    def get_answer_options(self):
        return self.answer_options.filter(is_active=True)
    
    def __str__(self):
        return strip_tags(self.question)
    

class QuizSubmission(MetaInfo):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerOption, blank=True, related_name='answer_option', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_correct = models.BooleanField(default=False)
    
    def is_valid(self):
        correct_ans = self.question.answer_options.filter(
            is_active=True, is_correct_ans=True).last()
        if correct_ans == self.answer:
            return True
        return False
    
    def save(self, *args, **kwargs):
        self.is_correct = self.is_valid()
        super(QuizSubmission, self).save(*args, **kwargs)
    
    def _str_(self):
        return self.user.get_full_name()


class QuizResult(MetaInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_user')
    submission = models.ManyToManyField(QuizSubmission, blank=True, related_name='user_submissions')
    no_of_questions = models.IntegerField()
    attended = models.IntegerField()
    correct_ans = models.IntegerField()
    incorrect_ans = models.IntegerField()
    total_score = models.FloatField()
    achieved_score = models.FloatField()
    is_active = models.BooleanField(default=True)
    
    def _str_(self):
        return self.user.get_full_name()
