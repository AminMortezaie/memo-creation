from django.db import models

class BaseModel(models.Model):
    name = models.CharField(max_length=250, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def soft_delete(self):
        if self.is_active:
            self.is_active = False
            self.save()

    class Meta:
        abstract = True


class Network(BaseModel):
    WEB3 = 'WB3'
    BTCFORK = 'BTC'
    API = 'API'
    TYPE_CHOICES = ((WEB3, 'Web3'),
                    (BTCFORK, 'BtcFork'),
                    (API, 'API'),)
    symbol = models.CharField(max_length=8, blank=False)
    deposit_enabled = models.BooleanField(default=False)
    withdrawal_enabled = models.BooleanField(default=False)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)


class Wallet(BaseModel):
    address = models.CharField(max_length=250)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)


class Memo(BaseModel):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    first_memo = models.IntegerField()
    last_memo = models.IntegerField()
    operation = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)



