from django.db import models


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    choice_1 = models.CharField(max_length=50)
    choice_2 = models.CharField(max_length=50)
    choice_3 = models.CharField(max_length=50)
    choice_4 = models.CharField(max_length=50)
    answer = models.IntegerField()
    explain = models.TextField()
    Management_id = models.ForeignKey('Management', on_delete=models.CASCADE)

    class Meta:
        ordering = ('quiz_id',)


class Wrongnote(models.Model):
    wrong_id = models.AutoField(primary_key=True)
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image-folder', blank=True, null=True, max_length=1000)
    title = models.TextField()
    text = models.TextField()
    Management_id = models.ForeignKey('Management', on_delete=models.CASCADE)

    class Meta:
        ordering = ('wrong_id',)


class Management(models.Model):
    title = models.CharField(max_length=100)
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
