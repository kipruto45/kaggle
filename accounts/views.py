
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from .models import OTP, User
import random

# Simulate sending OTP (replace with SMS/email integration)
def send_otp(user, method='phone'):
	code = str(random.randint(100000, 999999))
	OTP.objects.create(user=user, code=code)
	# In production, send via SMS or email
	print(f"OTP for {user.username}: {code}")
	return code

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			send_otp(user, method='phone')
			return redirect('accounts:verify_otp', user_id=user.id)
	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

def verify_otp(request, user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		code = request.POST.get('otp')
		otp = OTP.objects.filter(user=user, code=code, is_used=False).first()
		if otp:
			otp.is_used = True
			otp.save()
			user.is_active = True
			user.is_phone_verified = True
			user.save()
			login(request, user)
			return redirect('datasets:list')
	return render(request, 'accounts/verify_otp.html', {'user': user})
