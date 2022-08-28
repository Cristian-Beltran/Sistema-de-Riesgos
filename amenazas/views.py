# Library django
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,UpdateView,CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Sum,Avg

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime

# Models from amenazas
from .models import Active, Procedure, ProcessProcedure,Threat,Incident,Process,ProcessType,AssetValuation,CriticalityAssessment,RiskAssessment,ParValuesValuation
# Form from amenazas
from .forms import ActiveForm,IncidentForm,ProcedureForm,ProcessForm,ProcessProcedureForm,ActiveAssetValuationForm,CriticalyForm,RiskForm

from django.contrib.auth.mixins import LoginRequiredMixin





class ThreatListView(LoginRequiredMixin,ListView):
    model = Threat
    template_name = 'amenazas/threat_list.html'
    def get_queryset(self): 
        return Threat.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Amenazas"
        return context
 

class IncidentListView(LoginRequiredMixin,ListView):
    model =Incident 
    template_name = 'amenazas/incident_list.html'
    def get_queryset(self): 
        return Incident.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Incidentes"
        return context
 

class IncidentCreateView(LoginRequiredMixin,CreateView):
    model=Incident
    form_class = IncidentForm
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:incidentList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de Incidente"
        context['url_form'] = 'risk:incidentCreate' 
        return context


class IncidentUpdateView(LoginRequiredMixin,UpdateView):
    model =Incident 
    form_class = IncidentForm
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:incidentList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Incidente"
        context['url_form'] = 'risk:incidentUpdate' 
        return context

class ProcessTypeListView(LoginRequiredMixin,ListView):
    model =ProcessType
    template_name = 'amenazas/processType_list.html'

    def get_queryset(self): 
        return ProcessType.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Tipos de procesos"
        return context
 

class ProcessListView(LoginRequiredMixin,ListView):
    model =Process
    template_name = 'amenazas/process_list.html'
    def get_queryset(self): 
        return Process.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Procesos"
        return context
 

class ProcessCreateView(LoginRequiredMixin,CreateView):
    model=Process
    form_class =ProcessForm 
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:processList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de Procesos"
        context['url_form'] = 'risk:processCreate' 
        return context


class ProcessUpdateView(LoginRequiredMixin,UpdateView):
    model =Process
    form_class =ProcessForm 
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:processList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Proceso"
        context['url_form'] = 'risk:processUpdate' 
        return context



class ProcedureListView(LoginRequiredMixin,ListView):
    model =Procedure
    template_name = 'amenazas/procedure_list.html'
    def get_queryset(self): 
        return Procedure.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Procedimientos"
        return context
 

class ProcedureCreateView(LoginRequiredMixin,CreateView):
    model=Procedure
    form_class =ProcedureForm
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:procedureList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de Procedimientos"
        context['url_form'] = 'risk:procedureCreate' 
        return context


class ProcedureUpdateView(LoginRequiredMixin,UpdateView):
    model =Procedure
    form_class =ProcedureForm
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:procedureList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Procedimiento"
        context['url_form'] = 'risk:procedureUpdate' 
        return context



class ProcessProcedureListView(LoginRequiredMixin,ListView):
    model =ProcessProcedure
    template_name = 'amenazas/processProcedure_list.html'
    def get_queryset(self): 
        return ProcessProcedure.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Relacion Proceso-Procedimientos"
        return context
 

class ProcessProcedureCreateView(LoginRequiredMixin,CreateView):
    model =ProcessProcedure
    form_class =ProcessProcedureForm
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:processProcedureList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de P-P"
        context['url_form'] = 'risk:processProcedureCreate' 
        return context


class ProcessProcedureUpdateView(LoginRequiredMixin,UpdateView):
    model =ProcessProcedure
    form_class =ProcessProcedureForm
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:processProcedureList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de P-P"
        context['url_form'] = 'risk:processProcedureUpdate' 
        return context






def activeDesactive_view(request, pk):
    try:
        active= Active.objects.get(pk=pk)
    except Active.DoesNotExist:
        active= None
    if(active!=None):
        active.state = False
        active.save()
        return redirect('risk:activeList')
    return redirect('risk:activeList')

class ActiveListView(LoginRequiredMixin,ListView):
    model = Active
    template_name = 'amenazas/active_list.html'

    def get_queryset(self): 
        return AssetValuation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Activos"
        return context
    

class ActiveCreateView(LoginRequiredMixin,CreateView):
    model=Active
    form_class =ActiveAssetValuationForm 
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:activeList')

    def form_valid(self, form):
        active= form['active'].save()
        assetValuation= form['assetValuation'].save(commit=False)
        assetValuation.active=active 
        assetValuation.save()
        return super(ActiveCreateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Creacion de Activo"
        context['url_form'] = 'risk:activeCreate' 
        return context


class ActiveUpdateView(LoginRequiredMixin,UpdateView):
    model = AssetValuation 
    form_class =ActiveAssetValuationForm 
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:activeList')

    def get_form_kwargs(self):
        kwargs = super(ActiveUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'assetValuation': self.object,
            'active': self.object.active,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        assetValuation = AssetValuation.objects.get(id=pk)
        active= Active.objects.get(id=assetValuation.active.id)
        context['title'] = "Edicion de Activo"
        context['url_form'] = 'risk:activeUpdate' 
        return context


class CriticalyListView(LoginRequiredMixin,ListView):
    model =CriticalityAssessment
    template_name = 'amenazas/criticaly_list.html'
    def get_queryset(self): 
        return CriticalityAssessment.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Valoracion de Criticidad"
        return context
 

class CriticalyCreateView(LoginRequiredMixin,CreateView):
    model=CriticalityAssessment
    form_class =CriticalyForm
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:criticalyList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de Valoracion"
        context['url_form'] = 'risk:criticalyCreate' 
        return context


class CriticalyUpdateView(LoginRequiredMixin,UpdateView):
    model = CriticalityAssessment
    form_class = CriticalyForm
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:criticalyList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Valoracion"
        context['url_form'] = 'risk:criticalyUpdate' 
        return context



class RiskListView(LoginRequiredMixin,ListView):
    model =RiskAssessment
    template_name = 'amenazas/risk_list.html'
    def get_queryset(self): 
        return RiskAssessment.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Valoracion de Riesgos"
        return context
 

class RiskCreateView(LoginRequiredMixin,CreateView):
    model=RiskAssessment
    form_class =RiskForm
    template_name = 'amenazas/create.html'
    success_url = reverse_lazy('risk:riskList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Valoracion"
        context['url_form'] = 'risk:riskCreate' 
        return context


class RiskUpdateView(LoginRequiredMixin,UpdateView):
    model =RiskAssessment
    form_class =RiskForm
    template_name = 'amenazas/update.html'
    success_url=reverse_lazy('risk:riskList')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Valoracion"
        context['url_form'] = 'risk:riskUpdate' 
        return context



class ReportListView(LoginRequiredMixin,ListView):
    model = Active
    template_name = 'amenazas/report.html'
    def get_queryset(self): 
        return Active.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Valoracion de Riesgos"
        values = list(ParValuesValuation.objects.values('color'))
        context['color'] = values
        return context
 


class ValuationListView(LoginRequiredMixin,ListView):
    model =ParValuesValuation
    template_name = 'amenazas/valuation.html'

    def get_queryset(self): 
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Valores de valoracion"
        return context
 

class ReportPDF(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        template= get_template('amenazas/pdf.html')
        values = list(ParValuesValuation.objects.values('color'))
        active = Active.objects.all()
        valuation = ParValuesValuation.objects.all()

        context ={
            'titleData': "Reporte de valoraciones",
            'titleValuation': "Valores de valoracion",
            'color': values,
            'active': active,
            'valuation': valuation,
            'time': datetime.today()
        }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisaStatus = pisa.CreatePDF(
            html,dest=response
        )
        if pisaStatus.err:
            return HttpResponse('ERROR <pre>'+html+'</pre>')
        return response
 

class DetailCriticalityListView(LoginRequiredMixin,ListView):
    model = CriticalityAssessment
    template_name = 'amenazas/detailCriticality.html'

    def get_queryset(self): 
        return self.model.objects.filter(active=self.request.resolver_match.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Promedio de Criticidad"
        context['Promedio'] =  self.model.objects.filter(active=self.request.resolver_match.kwargs['pk']).aggregate(Avg('rangeFactor__minValor'))['rangeFactor__minValor__avg']
        return context
 

class DetailRiskListView(LoginRequiredMixin,ListView):
    model = RiskAssessment
    template_name = 'amenazas/detailRisk.html'

    def get_queryset(self): 
        return self.model.objects.filter(incident__active=self.request.resolver_match.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Promedio de Riesgo"
        context['Promedio'] =self.model.objects.filter(incident__active=self.request.resolver_match.kwargs['pk']).aggregate(Avg('rangeFactor__minValor'))['rangeFactor__minValor__avg']
        return context
 