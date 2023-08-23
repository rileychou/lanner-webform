from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.template import loader

from .models import FormEntry, FilesEntry
from .forms import EntryForm, EntryFilesForm

import datetime, csv

# Create your views here.
def index(request):
    date = datetime.datetime.now().replace(microsecond=0)
    case_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    # case_num = FormEntry(case_num=case_id)
    form_entry = EntryForm(request.POST or None)
    files_entry = EntryFilesForm(request.POST, request.FILES or None)
    files= request.FILES.getlist('file')
    
    if form_entry.is_valid() and files_entry.is_valid():
        form_instance = form_entry.save(commit=False)
        form_instance.case_num = case_id
        form_instance.date = date
        form_instance.save()
        for f in files:
            file_instance = FilesEntry(file=f, associated_entry=form_instance)
            file_instance.save()
            
        return render(request, 'submitted.html')

    return render(request, 'index.html', {'form_entry': form_entry, 'files_entry': files_entry})

def submissions(request):
    form_entries = FormEntry.objects.all()
    return render(request, 'submissions.html', {'form_entries' : form_entries})

def submission(request, cn):
    form_entry = FormEntry.objects.get(case_num=cn)
    return render(request, 'submission.html', {'form_entry' : form_entry})

def export_to_csv(request):
    form_entries = FormEntry.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=form_responses.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','Inspector','Supplier','Model','Part_No','Nc_Qty','Size','Order_No','SNs','Result','NCMR','Report if Rejected'])
    form_entry_fields = form_entries.values_list('case_num','inspector','customer_supplier','model_partname','lanner_part_no','nonconf_quantity','tot_lot_size','wo_po_number','serial_nums','inspection_result','insp_report_if_rej')
    for entry in form_entry_fields:
        writer.writerow(entry)

    return response

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exosts.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords must match.')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/submissions')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')


def edit(request, cn):
    submission = FormEntry.objects.get(case_num=cn)

    if request.method == 'GET':
        form = EntryForm(instance=submission)
        files_entry = EntryFilesForm(instance=submission)
        if not request.user.is_superuser:
            form.fields["inspection_result"].disabled = True
            form.fields["insp_report_if_rej"].disabled = True


        # TODO: deal with associated files
        return render(request, 'edit.html', {'form': form, 'files_entry':files_entry})

    elif request.method == 'POST':
        form = EntryForm(request.POST, instance=submission)
        files_entry = EntryFilesForm(request.POST, request.FILES or None, instance=submission)
        files= request.FILES.getlist('file')

        if form.is_valid() and files_entry.is_valid():
            form.save()
            for f in files:
                file_instance = FilesEntry(file=f, associated_entry=form)
                file_instance.save()
            messages.success(request, 'Form entry updated successfully')
            return redirect('submissions')
        else:
            messages.error(request, 'Please correct errors')
            return render(request, 'edit.html', {'form': form, 'files_entry':files_entry})

    
