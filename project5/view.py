from django.shortcuts import render,redirect
from data.models import data,MyModel
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class RestrictedPageView(LoginRequiredMixin, TemplateView):
    template_name = 'userhome.html'



def home(request):
	return render(request,'home.html')

@login_required
def userhome(request):
	return render(request,'userhome.html')	

def login(request):
	error_message = ''
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST.get('password')
		try:
			user = MyModel.objects.get(email=email)
			if user and check_password(password, user.password):
				return render(request, 'userhome.html', {'user': user})
			else:
				error_message = 'Invalid email or password'
		except MyModel.DoesNotExist:
			error_message = 'User does not exist'				
	return render(request,'login.html',{'error': error_message})

def register(request):
	if request.method == "POST":
		fn = request.POST['fullname']
		nm = request.POST['username']
		em = request.POST['email']
		ps = request.POST['password']
		if MyModel.objects.filter(email=em).exists():
			error_message = 'Email Address Already Registered..'
		else:
			hashed_password = make_password(ps)
			user = MyModel(fullname=fn, username=nm,email=em, password=hashed_password)
			user.save()
			return redirect('login')
	return render(request,'register.html')
	return render(request,'register.html',{'error': error_message})

def terms(request):
	return render(request,'terms.html')

def Withdraw(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        balance = int(request.POST.get('balance'))
        requiset_amount = int(request.POST.get('requiset'))

        if requiset_amount > balance:
            return render(request, 'fab.html', {'username': username, 'balance': balance, 'error': 'Withdrawal amount exceeds balance!'})

        user = MyModel.objects.get(username=username)
        user.requiset = requiset_amount
        user.save()

        return render(request, 'fab.html', {'username': username, 'balance': balance, 'success': 'Request sent successfully!'})

    else:
        username = request.GET.get('username')
        balance = request.GET.get('balance')
        
        return render(request, 'fab.html', {'username': username, 'balance': balance})

def aboutus(request):
	return render(request,'aboutus.html')

def contactus(request):
	if request.method == "POST":
		fn = request.POST['fullname']
		nm = request.POST['phone_number']
		em = request.POST['email']
		ps = request.POST['subject']
		ms = request.POST['message']
		data1 = data(fullname=fn,phone_number=nm,email=em,subject=ps,message=ms)
		data1.save()
		return redirect('/home/')
	return render(request,'contactus.html')	
	return render(request,'contactus.html')
