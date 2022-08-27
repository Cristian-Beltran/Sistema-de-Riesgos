from inspect import classify_class_attrs
from django.contrib import admin

# Modelos
from .models import ThreatType,Threat,ParValuesValuation,SafetyFactor,ActiveType,Active,Incident,RangeFactor,RiskAssessment,Procedure,ProcessType,Process,ProcessProcedure,AssetValuation,CriticalityAssessment

@admin.register(ThreatType)
class ThreatTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_display_links = ('description','id')
    search_fields = ('description',)

@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','availability','integrity','confidentiality', 'threatType']
    list_display_links = ('name','id')
    search_fields = ('name',)

@admin.register(ParValuesValuation)
class ParValuesValuationAdmin(admin.ModelAdmin):
    list_display = ['code', 'valor','probability','occurrence','color' ]
    list_display_links = ('code',)

@admin.register(SafetyFactor)
class SafetyFactorAdmin(admin.ModelAdmin):
    list_display = ['code', 'description' ]
    list_display_links = ('description','code')

@admin.register(ActiveType)
class ActiveTypeAdmin(admin.ModelAdmin):
    list_display = ['id','description']
    list_display_links = ('description','id')

@admin.register(Active)  
class ActiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description','activeType','state']
    list_display_links = ('name','description','id')
    search_fields = ('name',)

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','active','threat','date','description']
    list_display_links = ('name','description')
    search_fields = ('name','description')

@admin.register(RangeFactor)
class RangeFactorAdmin(admin.ModelAdmin):
    list_display = ['id', 'minValor','maxValor']
    list_display_links = ('minValor','id')

@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'incident','rangeFactor']
    list_display_links = ('id',)

@admin.register(ProcessType)
class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ['id','code', 'name','description']
    list_display_links = ('code','name','id')

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['id','description','processType']
    list_display_links = ('id','description') 
    list_filter = ('processType',)
    search_fields = ('description',)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_display_links = ('description','id')
    search_fields = ('description',)

@admin.register(ProcessProcedure)
class ProcessProcedureAdmin(admin.ModelAdmin):
    list_display = ['id','process','procedure']
    list_display_links = ('id','procedure','process')
@admin.register(CriticalityAssessment)
class CriticalityAssessmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'processProcedure','rangeFactor','active']
    list_display_links = ('id',)
    list_filter = ('rangeFactor','active')

    
@admin.register(AssetValuation)
class AssetValuationAdmin(admin.ModelAdmin):
    list_display = ['id', 'processProcedure','active','safetyFactor','valoration']
    list_display_links = ('id',)
    list_filter = ('active',)

