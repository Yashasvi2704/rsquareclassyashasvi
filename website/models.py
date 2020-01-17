from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings

ROLE_CHOICES = (
    ('OWNER', 'Owner'),
    ('BRANCHMANAGER', 'Branch Manager'),
    ('ACCOUNTANT', 'Accountant'),
    ('TEACHER', 'Teacher'),
    ('STUDENT', 'Student')
)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phone_no = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class RsquareUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='OWNER')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    def is_owner(self):
        return self.role == 'OWNER'
    def is_branch_manager(self):
        return self.role == 'BRANCHMANAGER'
    def is_student(self):
        return self.role == 'STUDENT'
    def is_teacher(self):
        return self.role == 'TEACHER'
    def is_accountant(self):
        return self.role == 'ACCOUNTANT'

    def __str__(self):
        return self.first_name + " " + self.last_name


class SubjectGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    fee = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    duration_type = models.CharField(max_length=20)
    no_of_installments = models.PositiveIntegerField()
    days_between_two_installments = models.PositiveIntegerField()
    installment_duration_type = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CourseSubject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rel')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='rel')

    def __str__(self):
        return str(self.course) + " | " + str(self.subject)
class AcademicYear(models.Model):
    year = models.CharField(max_length = 20)
    def __str__(self):
        return self.year


class Batch(models.Model):
    batch_name = models.CharField(max_length=200)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='related_1')
    def __str__(self):
        return self.batch_name
class BatchSubjects(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='related')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='related_1')
    def __str__(self):
        return self.batch.batch_name +" "+ self.subject.name
