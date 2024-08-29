from .models import signup
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobDescription
from .models import IT_Companies
from .models import Feedback
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import JobApplication
from django.urls import reverse
from .models import JobDescription, JobApplication
from .models import IT_Companies
from .models import ContactDetails


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        
        if name and email and password:
            rec = signup(name=name, email=email, password=password)
            rec.save()
        
             
    return render(request, "sign_up.html")

def login(request):
    if request.method == "GET":
        # Handle the sign-in form submission
        print("Its a POST request")
        email = request.GET.get("login_email")
        password = request.GET.get("login_password")
        print(email,"its an email")
        print(password,"its a password")

        if email and password:
            user = signup.objects.filter(email=email, password=password).first()
            
            if user:
                print("valid user",email,password)
                request.session['user_id'] = user.user_id
                print(user)

                return HttpResponseRedirect(reverse("homepage"))
            
            else:
                print("Invalid password",email,password)
        else:
            print("user or password is not found.",email,password) 
      
    return render(request, "sign_up.html")



def reset_password_confirm(request, uidb64, token):
    # This view handles the password reset confirmation form
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been successfully reset.')
            return redirect('login')  # Redirect to login page after successful password reset
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'reset_password_confirm.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')




def company_list(request):
    # Retrieve all IT companies from the database
    companies = IT_Companies.objects.all()
    
    # Pass the retrieved companies to the template for rendering
    return render(request, 'company_list.html', {'companies': companies})


def all_jobs(request):
    if request.method == 'GET':
        all_jobs = JobDescription.objects.all()
        return render(request, 'display_jobs.html', {'all_jobs': all_jobs})
    elif request.method == 'POST':
        company = request.POST.get('company')
        location = request.POST.get('location')
        title = request.POST.get('title')
        #print(company, location, title)
        
        # Initialize an empty query
        query = Q()
        
        # Add filters for each search parameter if it's not empty
        if company:
            query &= Q(company__company_name__icontains=company)
        if location:
            query &= Q(job_location__icontains=location)
        if title:
            query &= Q(job_title__icontains=title)
        
        # Filter based on the combined query
        search_results = JobDescription.objects.filter(query)
        
        return render(request, 'display_jobs.html', {'all_jobs': search_results})
    else:
        return render(request, 'display_jobs.html')


def feedback_view(request):
    msg = {}
    user = None
    if request.method == "POST":
        user_id = request.session.get('user_id')    # Assuming you have a way to get the user ID
        
        rating = request.POST.get("rating")
        feedback_text = request.POST.get("feedback_text")
        print(feedback_text)
        date = datetime.date.today()

        Feedback.objects.create(user_id=user_id, rating=rating, feedback_text=feedback_text, date=date)
        
        feedback_list = Feedback.objects.all()
        for feedbackObj in feedback_list:
            feedbackObj.user = get_object_or_404(signup, pk=feedbackObj.user_id)
            
            
        msg = {"msg": "Feedback submitted"}
        return render(request, "feedback.html", {"feedback_list": feedback_list, 'msg': msg, 'user': user})

    if request.method == "GET":
        feedback_list = Feedback.objects.all()
        for feedbackObj in feedback_list:
            #print(feedbackObj)
            feedbackObj.user = get_object_or_404(signup, pk=feedbackObj.user_id)
        return render(request, "feedback.html", {"feedback_list": feedback_list, 'user': user})



def apply_job(request, desc_id):
    if request.method == 'POST':
        # Parse the form data submitted by the user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        # Process the form data and save it to the database
        job = JobDescription.objects.get(pk=desc_id)
        company_name = job.company.company_name  # Get the company name associated with the job description
        application = JobApplication(name=name, email=email, phone=phone, cover_letter=cover_letter, resume=resume, job=job)
        application.save()
        

        # Redirect the user to the job_application.html page
        return redirect(reverse('thank_you_page'))

    # Render the job_application.html template with the company name
    job = JobDescription.objects.get(pk=desc_id)
    company_name = job.company.company_name
    return render(request, 'job_application.html', {'desc_id': desc_id, 'company_name': company_name})

def company_details(request, company_id):
    company = get_object_or_404(IT_Companies, pk=company_id)
    return render(request, 'company_details.html', {'company': company})






def contact_details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")
        domain = request.POST.get("domain")
        goals = request.POST.get("goals")
        
        # Correct the model instantiation
        contact_form = ContactDetails(name=name, email=email, role=role, domain=domain, goals=goals)
        contact_form.save()
        
        # Redirect to 'success' URL
        return redirect(reverse('success'))
        
    return render(request, 'contact_us.html')


def success(request):
    return render(request, 'success.html')      




def thank_you_page(request):
    return render(request, 'thank_you.html')



