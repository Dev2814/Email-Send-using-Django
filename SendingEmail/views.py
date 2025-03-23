from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.

def Sending_login_email(request, email, username):
    subject = "🔐 Login Successful - Welcome Back to SendingEmail App!"
    from_email = "Sending Email Support <support@SendingEmailApp.com>"
    to_email = [email]
    message = f"""
    <p>Dear {username},</p>

    <p>We noticed a successful login to your <b>SendingEmail App</b> account. If this was you, no further action is required. ✅</p>

    <p>If you didn't log in, please contact us immediately for assistance.</p>

    <p><b>Need Help?</b></p>
    <ul>
        <li>📧 Contact Support: <a href="mailto:support@SendingEmailApp.com">support@SendingEmailApp.com</a></li>
        <li>📖 Visit Help Center: <a href="http://localhost:2814/contact">SendingEmailApp.com/help</a></li>
    </ul>

    <p>Stay safe and secure!</p>

    <p>Best Regards,<br>
    <b>The SendingEmail App Team</b></p>
    """

    sending_login_email = EmailMultiAlternatives(subject, message, from_email, to_email)
    sending_login_email.content_subtype = "html"
    sending_login_email.send()

def Sending_signup_email(request, email, firstname):
        subject = "🎉 Welcome to SendingEmial App! Your Signup is Successful"
        from_email = "Sending Email Support"
        to_email = [email]

        message = f"""
        <p>Dear {firstname},</p>

        <p>Welcome to <b>SendingEmail App</b>! We are thrilled to have you on board. 🚀</p>

        <p>Your account has been successfully created, and you can now access all our services.</p>

        <p><b>Need Help?</b></p>
        <ul>
            <li>📧 Contact Support: <a href="mailto:support@SendingEmail App.com">support@SendingEmail App.com</a></li>
            <li>📖 Visit Help Center: <a href="http:/localhost:2814/contact">SendingEmail App.com/help</a></li>
        </ul>

        <p>Thank you for joining us!</p>

        <p>Best Regards,<br>
        <b>The SendingEmail App Team</b></p>
        """
        semail = EmailMultiAlternatives(subject, message, from_email, to_email)
        semail.content_subtype = "html"
        semail.send()


def index(request):
    return render(request, "index.html")

def signup_user(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Server-side validations
        if not all([first_name, last_name, username, email, password, confirm_password]):
            messages.error(request, "All fields are required!")
            return redirect('signup_user')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup_user')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup_user')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup_user')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long!")
            return redirect('signup_user')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        Sending_signup_email(request, user.email, user.first_name)
        return redirect('Login_user')

    return render(request, "Signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both fields are required!")
            return redirect('Login_user')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Login successful! { username }")
            Sending_login_email(request, user.email, user.username)
            return redirect('home') 
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('Login_user')

    return render(request, 'Login.html') 

def logout_user(request):
    logout(request)
    return redirect("Login_user")

