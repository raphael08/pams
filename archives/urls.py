from . import views
from django.urls import path

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('', views.dashboard, name='home'),
    path('student',views.student,name='student'),
    path('student_od',views.student_od,name='student_od'),
    path('staff',views.staff,name='staff'),
    path('department',views.department,name='department'),
    path('login',views.login,name='login'),
    path('resetpassword/<str:pk>',views.reset_password,name='resetpassword'),
    path('logout/',views.logout,name='logout'),
    path('level/',views.level,name='level'),
    path('delete_level/<str:pk>',views.delete_level,name='delete_level'),
    path('update_level/<str:pk>',views.update_level,name='update_level'),
    path('project_type',views.project_type,name='project_type'),
    path('pdf_upload/',views.pdf_upload,name='pdf_upload'),
    path('preview_pdf/<str:pk>',views.preview_pdf,name='preview_pdf'),
    path('addstaff',views.addstaff,name='addstaff'), 
    path('editstaff/<str:pk>',views.editstaff,name='editstaff'),
    path('addprojecttype',views.addprojecttype,name='addprojecttype'),
    path('editprojecttype/<str:pk>',views.editprojecttype,name='editprojecttype'),
    path('deleteprojecttype/<str:pk>',views.deleteprojecttype,name='deleteprojecttype'),
    path('upload_addstaff',views.upload_addstaff,name='upload_addstaff'),
    path('subtime',views.submissionTime,name='subtime'),
    path('addlevel',views.addlevel,name='addlevel'),
    path('projects',views.projects,name='projects'),
    path('editstudent/<str:pk>',views.editstudent,name='editstudent'),
    path('editdepartment/<str:pk>',views.editdepartment,name='editdepartment'),
    path('deletedepartment/<str:pk>',views.deletedepartment,name='deletedepartment'),
    path('blockuser/<str:pk>',views.blockuser,name='blockuser'),
    path('upload', views.upload, name='upload'),
    path('editlevel/<str:pk>',views.editlevel,name='editlevel'),
    path('deletelevel/<str:pk>',views.deletelevel,name='deletelevel'),
    path('upload_student',views.upload_student,name='upload_student'),
    path('q',views.my_view,name='my_view'),
    path('get_project_types/<str:department>',views.get_project_types,name='get_project_types'),
    path('deletestudent/<str:pk>',views.deletestudent,name='deletestudent'),
    path('deletepdf/<str:pk>',views.deletepdf,name='deletepdf'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('manage_project',views.manage_project,name='manage_project'),
    path('changepassword',views.changepassword,name='changepassword'),
    # path('changedoctorpassword/<str:pk>',views.changedoctorpassword,name='changedoctorpassword'),
    path("manageroles",views.manageroles,name="manageroles"),
    path("addroles",views.addroles,name="addroles"),
    path("deleteroles/<str:pk>",views.deleteroles,name="deleteroles"),
    path("editroles/<str:pk>",views.editroles,name="editroles"),
    path('get_courses/', views.get_courses, name='get_courses'),
    # path("edit_speciality/<str:pk>",views.edit_speciality,name="edit_speciality"),
    # path("delete_speciality/<str:pk>",views.delete_speciality,name="delete_speciality"),
    path('save_pdf', views.save_pdf, name='save_pdf'),
    # path("deadline",views.deadline,name="deadline"),
    path("deadlines",views.deadlines,name="deadlines"),
    path("deletesub/<str:pk>",views.deletesub,name="deletesub"),
    path("assessment",views.assessment,name="assessment"),
    path("editsubtime/<str:pk>",views.editSubmittionTime,name="editsubtime"),
    path('progress',views.progress,name='progress'),
 
    # path('deletedoctorschedule/<str:pk>',views.deletedoctorschedule,name='deletedoctorschedule'),
    # path('editdoctorschedule/<str:pk>',views.editdoctorschedule,name='editdoctorschedule'),
    # path('makeappointment/<str:pk>',views.makeappointment,name='makeappointment'),
    # path('approve_appointment/<str:pk>',views.approve_appointment,name='approve_appointment'),
    # path('delete_appointment/<str:pk>',views.delete_appointment,name='delete_appointment'),
    # path('cancellappointment/<str:pk>',views.cancellappointment,name='cancellappointment'),
    
    # #doctor/////////////////////////////
    
    # path('doctordashboard',views.doctordashboard,name='doctordashboard'),
    # path('registerdoctor',views.registerdoctor,name='registerdoctor'),
    # path('doctorappointment',views.doctorappointment,name='doctorappointment'),
    # path('mypatient',views.mypatient,name='mypatient'),
    
    # path('doctorprofile',views.doctorprofile,name='doctorprofile'),
    # path('doctorchangepassword',views.doctorchangepassword,name='doctorchangepassword'),
     
    # #Patient //////////////////////////////////
    
    # path('patientdashboard',views.patientdashboard,name='patientdashboard'),
    # path('mydoctor',views.mydoctor,name='mydoctor'),
    # path('patient',views.patientprofile,name='patientprofile'),
    # path('patientprofile',views.patientprofile,name='patientprofile'),
    # path('patientchangepassword',views.patientchangepassword,name='patientchangepassword'),
    # path('booking',views.booking,name='booking'),
    # #  path('photopatient',views.photopatient,name='photopatient'),
    
     
     
]