from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout



@login_required
def index_view(request):
    return redirect('risk:index')
    
@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')

def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        redirect("administracion:index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('risk:index')
            else:
                return render(request, 'app/login.html', {'error': 'Usuario o contraseña invalidos'})

        return render(request, 'app/login.html')



