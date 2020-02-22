from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="问题_文字")
    pub_date = models.DateTimeField('发表时间')
    class Meta:
        # 复数形式，如果只设置verbose_name，在Admin会显示为“产品信息s”
        verbose_name_plural = "问题"
        verbose_name = "问题"
        
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问题")
    choice_text = models.CharField(max_length=200, verbose_name="选项_文字")
    votes = models.IntegerField(default=0, verbose_name="数")
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = '选择'
        verbose_name_plural = '选择'
