from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm

def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirecionar para a página desejada após salvar o cliente
    else:
        form = ClienteForm()
    return render(request, 'add_cliente.html', {'form': form})