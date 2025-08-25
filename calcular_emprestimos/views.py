from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def resultado(request):
    montante_final = None
    juros = None
    
    if request.method == "POST":
        
        capital_inicial = float(request.POST.get('capital_inicial'))
        taxa_de_juros_por_periodo = float(request.POST.get('taxa_de_juros_por_periodo'))
        num_de_periodos = float(request.POST.get('num_de_periodos'))
        
        montante_final = capital_inicial * (1 + taxa_de_juros_por_periodo) ** num_de_periodos
        juros = montante_final - capital_inicial
    
    return render(request, "resultado.html", {
        "montante_final": montante_final,
        "juros":juros
    })