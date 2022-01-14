from django.db import models
from extract.models import ExtarctUser


PUSH_STATUS = (
    ('REGISTER', 'REGISTER'),
    ('SENDING', 'SENDING'),
    ('COMPLETE', 'COMPLETE'),
    ('ERROR', 'ERROR')
)


class PushCategory(models.Model):
    category = models.CharField('카테고리', max_length=255)

    def __str__(self):
        return self.category


class PushMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ExtarctUser, on_delete=models.CASCADE)
    category = models.ForeignKey(PushCategory, verbose_name='카테고리', db_index=True, on_delete=models.CASCADE)
    content = models.TextField('내용')
    status = models.CharField('전송상태', max_length=255, choices=PUSH_STATUS, default='REGISTER')
    sended_at = models.DateTimeField('전송시간', default=None, null=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
