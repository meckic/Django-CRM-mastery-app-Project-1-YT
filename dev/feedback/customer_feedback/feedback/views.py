from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def feedback_form(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        feedback_type = request.POST.get('feedback_type')
        about_service = request.POST.get('about_service')
        about_issue = request.POST.get('about_issue')
        other_service = request.POST.get('other_service')
        other_issue = request.POST.get('other_issue')
        how_provided = request.POST.get('how_provided')
        phone_number = request.POST.get('phone_number')
        fair_trading_officer = request.POST.get('fair_trading_officer')
        date_of_service = request.POST.get('date_of_service')
        time_of_service = request.POST.get('time_of_service')
        trader_or_consumer = request.POST.get('trader_or_consumer')
        feedback_details = request.POST.get('feedback_details')
        name = request.POST.get('name')
        address = request.POST.get('address')
        organisation = request.POST.get('organisation')
        daytime_phone = request.POST.get('daytime_phone')
        email_address = request.POST.get('email_address')

        # Validations
        errors = []
        if not feedback_type:
            errors.append("Feedback type is required.")
        if not about_service:
            errors.append("Service type is required.")
        if not about_issue:
            errors.append("Issue type is required.")
        if not how_provided:
            errors.append("How the service was provided is required.")
        if not feedback_details:
            errors.append("Feedback details are required.")
        if not name:
            errors.append("Name is required.")
        if email_address:
            try:
                validate_email(email_address)
            except ValidationError:
                errors.append("Enter a valid email address.")

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            feedback = Feedback(
                rating = rating,
                feedback_type=feedback_type,
                about_service=about_service,
                about_issue=about_issue,
                other_service=other_service,
                other_issue=other_issue,
                how_provided=how_provided,
                phone_number=phone_number,
                fair_trading_officer=fair_trading_officer,
                date_of_service=date_of_service,
                time_of_service=time_of_service,
                trader_or_consumer=trader_or_consumer,
                feedback_details=feedback_details,
                name=name,
                address=address,
                organisation=organisation,
                daytime_phone=daytime_phone,
                email_address=email_address,
            )
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback_form')

    return render(request, 'feedback/feedback_form.html')