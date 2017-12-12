from django.db import models

# Create your models here.


class User(models.Model):
    '''
    预订人
    '''
    name = models.CharField(max_length=32, null=True,unique=True)
    password = models.CharField(max_length=32, null=True)


class BoardRoom(models.Model):
    '''
    会议室
    '''
    title = models.CharField(max_length=32)
    max_num=models.IntegerField(default=10)



class Result(models.Model):
    '''
    结果
    '''
    day = models.DateField()
    choice_time = ((1, '08:00'),
                   (2, '09:00'),
                   (3, '10:00'),
                   (4, '11:00'),
                   (5, '12:00'),
                   (6, '13:00'),
                   (7, '14:00'),
                   (8, '15:00'),
                   (9, '16:00'),
                   (10, '17:00'),
                   (11, '18:00'),
                   (12, '19:00'),
                   (13, '20:00'),
                   )
    time = models.IntegerField(choices=choice_time)

    user=models.ForeignKey(to=User,null=True)
    room=models.ForeignKey(to=BoardRoom,null=True)

    class Meta:
        unique_together = ('day','time','user','room')

