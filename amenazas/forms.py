from django import forms
from .models import  AssetValuation, Active,Incident,Process,Procedure,ProcessProcedure,CriticalityAssessment,RiskAssessment

from betterforms.multiform import MultiModelForm


class ActiveForm(forms.ModelForm):
    class Meta:
        model = Active 
        fields = ('id','name','description','activeType','state')
        labels = { 
            'name': ('Nombre'), 
            'description': ('Descripción'), 
            'activeType': ('Tipo de Activo'), 
            'state': ('Estado'), 
        }
class AssetValuationForm(forms.ModelForm):
    class Meta:
        model = AssetValuation
        fields = ('id','processProcedure','safetyFactor','valoration')
        labels = { 
            'processProcedure': ('Proceso-Procedimiento'), 
            'safetyFactor': ('Factor de Seguridad'), 
            'valoration': ('Valoración'), 
        }

class ActiveAssetValuationForm(MultiModelForm):
    form_classes = {
        'assetValuation': AssetValuationForm,
        'active': ActiveForm,
    }




class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident 
        fields = ('id','name','active','threat','date','interruptTime','description')
        labels = { 
            'name': ('Nombre'), 
            'active': ('Activo'), 
            'threat': ('Amenaza'), 
            'date': ('Fecha'), 
            'interruptTime': ('Tiempo de interrupcion'), 
            'description': ('descripción'), 
        }
        widgets ={
            'date':forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                    'type': 'date'
                    }),
            'interruptTime':forms.DateInput(
                    attrs={'class': 'form-control', 
                    'type': 'time'
                    }), 
        }

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('id','description','processType')
        labels = {
            'name': ('Nombre'),
            'description':  ('Descripción'),
            'processType': ('Tipo de Proceso')
        }
    
class ProcedureForm(forms.ModelForm):
    class Meta:
        model=Procedure
        fields = ('id','description')
        labels = {
            'description': ('Descripción'),
        }

class ProcessProcedureForm(forms.ModelForm):
    class Meta:
        model = ProcessProcedure
        fields = ('id','process','procedure')
        labels = {
            'process':'Proceso',
            'procedure':'Procedimiento'
        }

class CriticalyForm(forms.ModelForm):
    class Meta:
        model=CriticalityAssessment
        fields = ('id','processProcedure','rangeFactor','active')
        labels = {
            'processProcedure': ('Procesos-Procedimiento'),
            'rangeFactor': ('Rango'),
            'active': ('Activo'),
        }

class RiskForm(forms.ModelForm):
    class Meta:
        model=RiskAssessment
        fields = ('id','incident','rangeFactor')
        labels = {
            'incident': ('Incidente'),
            'rangeFactor': ('Rango'),
        }



