from django.db import models

# Create your models here.

#If 'CHOICES' is given, the default form widget will be a select box with these choices instead of the standard text field.
#the first element in each tuple is the actual value to be stored, and the second element is the human-readable name.

MODELS = [
    ('R33B', 'OX-J'),
    ('F31', 'SC-E'),
    ('F32', 'SC-F'),
    ('F33', 'SC-J'),
    ('F34', 'SC-P'),
]

PROCESSES = [
    ('UDT', 'UpDown'),
    ('APS', 'APS'),
    ('DCR', 'DCR'),
]

class Fail(models.Model):
    fail_code = models.PositiveSmallIntegerField(primary_key=True)
    fail_name = models.CharField(max_length=50)
    process = models.CharField(max_length=3, choices=PROCESSES)

    def __str__(self):
        return f"{self.fail_name} ({self.fail_code})"

class Config(models.Model):
    config_name = models.CharField(primary_key=True, max_length=10)
    model = models.CharField(max_length=4, choices=MODELS)

    def __str__(self):
        return f"{self.model} - {self.config_name}"


class Lot(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=12)
    config = models.ForeignKey(Config, on_delete=models.CASCADE)
    process = models.CharField(max_length=3, choices=PROCESSES)
    input = models.PositiveSmallIntegerField()
    pass_qty = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.lot_id} - {self.pass_qty}/{self.input}"

class NG(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, null=True)
    fail = models.ForeignKey(Fail, on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.lot.lot_id} - {self.fail.fail_name} ({self.qty}ea)"

    # def save(self, *args, **kwargs):
    #     self.