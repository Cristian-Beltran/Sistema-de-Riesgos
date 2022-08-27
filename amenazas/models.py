from django.db import models
from django.db.models import Sum,Avg
# Create your models here.



class ThreatType(models.Model):
    description = models.TextField(default="")
    def __str__(self):
        return self.description

class Threat(models.Model):
    name = models.CharField(max_length=255)
    availability = models.BooleanField(default=False)
    integrity = models.BooleanField(default= False)
    confidentiality = models.BooleanField(default=False)
    threatType = models.ForeignKey(ThreatType,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ParValuesValuation(models.Model):
    code =models.CharField(max_length=25,default="")
    valor = models.CharField(max_length=50)
    probability = models.CharField(max_length=50)
    occurrence = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.code

class SafetyFactor(models.Model):
    code = models.CharField(max_length=25,default="")
    description = models.TextField(default="")
    def __str__(self):
        return self.code


class ActiveType(models.Model):
    description = models.TextField(default="")
    def __str__(self):
        return self.description

class Active(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    activeType = models.ForeignKey(ActiveType,on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    def criticalys(self):
        criticaly = CriticalityAssessment.objects.filter(active=self.id).aggregate(Avg('rangeFactor__maxValor'))
        avg = criticaly['rangeFactor__maxValor__avg']
        return avg
    def risks(self):
        criticaly = RiskAssessment.objects.filter(incident__active=self.id).aggregate(Avg('rangeFactor__maxValor'))
        avg = criticaly['rangeFactor__maxValor__avg']
        return avg

class Incident(models.Model):
    name = models.CharField(max_length=255)
    active = models.ForeignKey(Active,on_delete=models.CASCADE)
    threat = models.ForeignKey(Threat,on_delete=models.CASCADE)
    date = models.DateField()
    interruptTime = models.TimeField()
    description = models.TextField(default="")
    def __str__(self):
        return self.name

class RangeFactor(models.Model):
    minValor = models.IntegerField()
    maxValor = models.IntegerField()
    def __str__(self):
        return f'{self.minValor}-{self.maxValor}'

class RiskAssessment(models.Model):
    incident = models.ForeignKey(Incident,on_delete=models.CASCADE)
    rangeFactor = models.ForeignKey(RangeFactor,on_delete=models.CASCADE)

class ProcessType(models.Model):
    code = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    def __str__(self):
        return self.code


class Process(models.Model):
    description = models.TextField(default="")
    processType = models.ForeignKey(ProcessType,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.description

class Procedure(models.Model):
    description = models.TextField(default="")
    def __str__(self):
        return self.description

class ProcessProcedure(models.Model):
    process = models.ForeignKey(Process,on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.process}-{self.procedure}'


class AssetValuation(models.Model):
    processProcedure = models.ForeignKey(ProcessProcedure,on_delete=models.CASCADE)
    active = models.ForeignKey(Active,on_delete=models.CASCADE,null=True)
    safetyFactor = models.ForeignKey(SafetyFactor,on_delete=models.CASCADE)
    valoration = models.ForeignKey(ParValuesValuation,on_delete=models.CASCADE)

class CriticalityAssessment(models.Model):
    processProcedure = models.ForeignKey(ProcessProcedure,on_delete=models.CASCADE)
    rangeFactor = models.ForeignKey(RangeFactor,on_delete=models.CASCADE)
    active = models.ForeignKey(Active,on_delete=models.CASCADE)


