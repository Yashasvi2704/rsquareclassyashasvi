from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from . import models


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    messages = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_owner():
                request.session["curr_branch"] = models.Branch.objects.all()[0].name
            elif user.is_branch_manager():
                request.session['curr_branch'] = request.user.branch.name
            return redirect('dashboard')
        messages['alert'] = 'Failed to authenticate!'
    return render(request, 'login/login.html', {'messages': messages})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def change_branch(request):
    if request.method == 'POST':
        branch_name = request.POST['branch']
        request.session["curr_branch"] = branch_name
        print(request.session['curr_branch'])
        return redirect('dashboard')
    else:
        return redirect('dashboard')


@login_required
def view_branches(request):
    branches = models.Branch.objects.all()
    return render(request, 'branch/branch_viewall.html', {'branches': branches})


@login_required
def view_courses(request):
    courses = models.Course.objects.filter(branch__name=request.session['curr_branch'])
    if not (request.user.is_owner() or request.user.is_branch_manager()):
        return redirect('dashboard')
    subject_groups = models.SubjectGroup.objects.all()
    if request.method == 'GET':
        return render(request, 'course/course_viewall.html', {
            'courses': courses,
            'subject_groups': subject_groups
        })
    else:
        name = request.POST['name']
        fee = request.POST['fee']
        duration = request.POST['duration']
        duration_type = request.POST['duration_type']
        no_of_installments = request.POST['no_of_installments']
        installments_duration_type = request.POST['installments_duration_type']
        days_between_two_installments = request.POST['days_between_two_installments']
        if  request.user.is_owner():
            add_to_all = request.POST['add_to_all'];
            if add_to_all=='true':
                for branch in models.Branch.objects.all():
                    course = models.Course.objects.create(name=name, fee=fee,
                    duration=duration, no_of_installments=no_of_installments,
                    days_between_two_installments=days_between_two_installments,
                    duration_type=duration_type, installment_duration_type=installment_duration_type,
                    branch=branch)
                    for subject_id in request.POST.getlist('subjects[]'):
                        courseSubject = models.CourseSubject.objects.create(course=course, subject_id=subject_id)
            else:
                course = models.Course.objects.create(name=name, fee=fee,
                duration=duration, no_of_installments=no_of_installments,
                days_between_two_installments=days_between_two_installments,
                duration_type=duration_type, installment_duration_type=installment_duration_type,
                branch=models.Branch.objects.get(name=request.session['curr_branch']))
                for subject_id in request.POST.getlist('subjects[]'):
                    courseSubject = models.CourseSubject.objects.create(course=course, subject_id=subject_id)
        elif request.user.is_branch_manager():
            course = models.Course.objects.create(name=name, fee=fee, duration=duration, no_of_installments=no_of_installments, days_between_two_installments=days_between_two_installments, branch=request.user.branch
            , duration_type=duration_type, installment_duration_type=installment_duration_type)
            for subject_id in request.POST.getlist('subjects[]'):
                courseSubject = models.CourseSubject.objects.create(course=course, subject_id=subject_id)

        return redirect('course-viewall')

@login_required
def calendar(request):
    return render(request, 'calendar/calendar.html')


@login_required
def student(request):
    if not (request.user.is_owner() or request.user.is_branch_manager()):
        return redirect('dashboard')
    students = models.RsquareUser.objects.filter(role='STUDENT')
    courses = models.Course.objects.filter(branch__name=request.session['curr_branch'])
    return render(request, 'student/student_viewall.html', {'students': students, 'courses': courses})


@login_required
def student_add(request):
    if not (request.user.is_owner() or request.user.is_branch_manager()):
        return redirect('dashboard')
    courses = models.Course.objects.filter(branch__name=request.session['curr_branch'])
    return render(request, 'student/student_add.html', {'courses': courses})


@login_required
def dark_mode(request):
    if request.session.get("dark", None):
        request.session["dark"] = False
    else:
        request.session["dark"] = True
    return redirect('dashboard')


@login_required
def settings(request):
    if request.method == 'POST':
        if request.POST.get('dark-mode-switch', 'off') == 'on':
            request.session["dark"] = True;
        else:
            request.session["dark"] = False;
        return redirect('settings')
    return render(request, 'settings.html')

def batch(request):
    if request.method == 'GET':
        batch = models.Batch.objects.all()
        bsubject = models.BatchSubjects.objects.all()
        #sgroup = {}
        #for subject in bsubject:
        #    sgroup.append(subject.group.name)
        #    print(subject.group.name)
        args = {'batch':batch,'bsubject':bsubject}
        return render(request, 'batch/batch.html',args)
def batch_add(request):
    subject_groups = models.SubjectGroup.objects.all()
    academic_year = models.AcademicYear.objects.all()
    args =  {'subject_groups': subject_groups,'academic_year':academic_year}
    if request.method == 'GET':
        return render(request, 'batch/batch_add.html',args)
    else:
        name = request.POST['name']
        academic_year = request.POST['academic_year']
        year = models.AcademicYear.objects.get(pk = academic_year)
        batch = models.Batch.objects.create(batch_name = name,academic_year = year)
        for subject_id in request.POST.getlist('subjects[]'):
            batchsubject = models.BatchSubjects.objects.create(batch=batch, subject_id=subject_id)
        arr = [1,2,3,4]
        return redirect('batch-view')



def batch_edit(request,pk):
    batch = models.Batch.objects.get(pk = pk)
    bsubject = models.BatchSubjects.objects.select_related().filter(batch = batch)
    batchsubject = []
    for subject in bsubject:
        batchsubject.append(subject.subject)
    subject_groups = models.SubjectGroup.objects.all()
    academic_year = models.AcademicYear.objects.all()

    if request.method == 'GET':
        args = {'batch':batch,'batchsubject':batchsubject,'subject_groups':subject_groups,"academic_year":academic_year,}
        return render(request, 'batch/batch_edit.html',args)
    else:

        academic_year = request.POST['academic_year']

        year = models.AcademicYear.objects.get(pk = academic_year)
        batch.batch_name = request.POST['name']
        batch.academic_year = year
        batch.save()
        for subject in bsubject:
            note = get_object_or_404(models.BatchSubjects,pk=subject.pk).delete()
        for subject_id in request.POST.getlist('subjects[]'):
            batchsubject = models.BatchSubjects.objects.create(batch=batch, subject_id=subject_id)
        arr = [1,2,3,4]
        return redirect('batch-view')
