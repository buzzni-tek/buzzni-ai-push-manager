from django.db import models


STATUS_TYPE = (
        ('BEFORESTART', 'BEFORESTART'),
        ('ING', 'ING'),
        ('ERROR', 'ERROR'),
        ('COMPLETE', 'COMPLETE')
    )


class Extract(models.Model):
    id = models.BigAutoField(primary_key=True)
    promotion = models.BigIntegerField('프로모션', null=False, db_index=True)
    start_date = models.DateTimeField('시작날짜', default=None, null=True)
    end_date = models.DateTimeField('종료날짜', default=None, null=True)
    status = models.CharField('상태', max_length=255, choices=STATUS_TYPE, default='PENDING')
    created_at = models.DateTimeField('생성시간', auto_now_add=True)


class ExtractProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    extract = models.ForeignKey(Extract, on_delete=models.CASCADE)
    entity_id = models.IntegerField(null=True, db_index=True)
    user_count = models.IntegerField(default=0)
    user_extract_status = models.CharField('유저 추출 상태', max_length=255, choices=STATUS_TYPE, default='BEFORESTART')
    created_at = models.DateTimeField('생성시간', auto_now_add=True)


class ExtarctUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    extract_product = models.ForeignKey(ExtractProduct, on_delete=models.CASCADE)
    entity_id = models.BigIntegerField(null=False, db_index=True)
    xid = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
