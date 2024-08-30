from django.shortcuts import render, redirect
from .forms import EmailForm
from .tasks import send_email_task


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [form.cleaned_data['recipient_list']]
            # call Celery task
            send_email_task.delay(subject, message, recipient_list)
            return redirect('email_success')
    else:
        form = EmailForm()

    return render(request, 'emailapp/send_email.html', {'form': form})


def email_success(request):
    return render(request, 'emailapp/email_success.html')

