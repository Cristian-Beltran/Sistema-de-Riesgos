from threading import Thread
from django.urls import path
from . import views

app_name= "risk"
urlpatterns = [
    path("", views.ActiveListView.as_view(), name="index"),

    path("activos", views.ActiveListView.as_view(), name="activeList"),
    path("crearActivo",views.ActiveCreateView.as_view(),name="activeCreate"),
    path("actualizarActivo/<int:pk>", views.ActiveUpdateView.as_view(), name="activeUpdate"),
    path("desactivarActivo/<int:pk>",views.activeDesactive_view,name = "activeDesactive"),

    path("amenazas",views.ThreatListView.as_view(),name="threatList"),

    path("incidentes",views.IncidentListView.as_view(),name="incidentList"),
    path("crearIncidente",views.IncidentCreateView.as_view(),name="incidentCreate"),
    path("actualizarIncidente/<int:pk>", views.IncidentUpdateView.as_view(), name="incidentUpdate"),

    path("TiposdeProcesos",views.ProcessTypeListView.as_view(),name="processTypeList"),

    path("procesos",views.ProcessListView.as_view(),name="processList"),
    path("crearProcesos",views.ProcessCreateView.as_view(),name="processCreate"),
    path("actualizarProcesos/<int:pk>", views.ProcessUpdateView.as_view(), name="processUpdate"),

    path("procedimientos",views.ProcedureListView.as_view(),name="procedureList"),
    path("crearProcedimiento",views.ProcedureCreateView.as_view(),name="procedureCreate"),
    path("actualizarProcedimiento/<int:pk>", views.ProcedureUpdateView.as_view(), name="procedureUpdate"),

    path("p-p",views.ProcessProcedureListView.as_view(),name="processProcedureList"),
    path("crearP-P",views.ProcessProcedureCreateView.as_view(),name="processProcedureCreate"),
    path("actualizarP-P/<int:pk>", views.ProcessProcedureUpdateView.as_view(), name="processProcedureUpdate"),

    path("valoracionRiesgos",views.RiskListView.as_view(),name="riskList"),
    path("crearriesgos",views.RiskCreateView.as_view(),name="riskCreate"),
    path("actualizarRiesgos/<int:pk>", views.RiskUpdateView.as_view(), name="riskUpdate"),

    path("valoracionCriticidad",views.CriticalyListView.as_view(),name="criticalyList"),
    path("crearCriticidad",views.CriticalyCreateView.as_view(),name="criticalyCreate"),
    path("actualizarCriticad/<int:pk>", views.CriticalyUpdateView.as_view(), name="criticalyUpdate"),

    path("report",views.ReportListView.as_view(),name="report"),
    path("valuation",views.ValuationListView.as_view(),name="valuation"),
    path("reportPDF",views.ReportPDF.as_view(),name="reportPDF")
]