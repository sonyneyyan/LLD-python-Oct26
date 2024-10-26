from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.TimeField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)






# CharField  -> small sized text
# textField  -> large sized text
# intField  -> int values
# FloatField  ->float values
# BooleanField  -> boolean values
# DateField  -> for date teime format

# cardinality
# foriegn keys are used for 1:M relation

# once the aboe models are created run the command python3 manage.py makemigrations
#python3 manage.py makemigrations
#igrations for 'tryhello':
# tryhello/migrations/0001_initial.py
#   + Create model Course
#   + Create model Student
#   + Create model Enrollment


#Then run the command - > python3 manage.py migrate -> this will create the table.
#Operations to perform:
#  Apply all migrations: admin, auth, contenttypes, sessions, tryhello
#Running migrations:
#  Applying contenttypes.0001_initial... OK
#  Applying auth.0001_initial... OK
#  Applying admin.0001_initial... OK
#  Applying admin.0002_logentry_remove_auto_add... OK
#  Applying admin.0003_logentry_add_action_flag_choices... OK
#  Applying contenttypes.0002_remove_content_type_name... OK
#  Applying auth.0002_alter_permission_name_max_length... OK
#  Applying auth.0003_alter_user_email_max_length... OK
#  Applying auth.0004_alter_user_username_opts... OK
#  Applying auth.0005_alter_user_last_login_null... OK
#  Applying auth.0006_require_contenttypes_0002... OK
#  Applying auth.0007_alter_validators_add_error_messages... OK
#  Applying auth.0008_alter_user_username_max_length... OK
#  Applying auth.0009_alter_user_last_name_max_length... OK
#  Applying auth.0010_alter_group_name_max_length... OK
#  Applying auth.0011_update_proxy_permissions... OK
#  Applying auth.0012_alter_user_first_name_max_length... OK
#  Applying sessions.0001_initial... OK
#  Applying tryhello.0001_initial... OK

# once we updated one of the field in the models we need to run the migarion steps again
# here we are adding the field is_active to enrollment model

#python3 manage.py makemigrations
#Migrations for 'tryhello':
#  tryhello/migrations/0002_enrollment_is_active.py
#    + Add field is_active to enrollment
#
# python3 manage.py migrate
#Operations to perform:
#  Apply all migrations: admin, auth, contenttypes, sessions, tryhello
#Running migrations:
#  Applying tryhello.0002_enrollment_is_active... OK