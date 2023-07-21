from django.shortcuts import render,redirect
from .import views
from studentapp.models import Student

# Create your views here.
def addstudent(request):
    return render(request,'student.html')
def addstudentdetails(request):
    if request.method=='POST':
        s_name=request.POST['StudentName']
        address=request.POST['Address']
        age=request.POST['Age']
        email=request.POST['EmailID']
        joindate=request.POST['JoiningDate']
        qualification=request.POST['Qualification']
        gender=request.POST['Gender']
        mobile=request.POST['MobileNumber']
        student=Student(StudentName=s_name,Address=address,Age=age,EmailID=email,JoiningDate=joindate,Qualification=qualification,Gender=gender,MobileNumber=mobile)
        student.save()

        return redirect('showstudent')
def showstudent(request):
    student=Student.objects.all()
    return render(request,'showstudent.html',{'students':student})
def showstudentdetails(request,pk):
    student=Student.objects.get(id=pk)
    return render(request,'showstudentdetails.html',{'students':student})
def editstudentpage(request,pk):
    student=Student.objects.get(id=pk)
    qualification=Student.objects.values('Qualification').distinct()
    return render(request,'editstudent.html',{'students':student,'q':qualification})
def editstudentdetails(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.StudentName=request.POST.get('sname')
        student.Address=request.POST.get('address')
        student.Age=request.POST.get('age')
        student.EmailID=request.POST.get('emailid')
        student.JoiningDate=request.POST.get('joiningdate')
        student.Qualification=request.POST.get('qualification')
        student.Gender=request.POST.get('gender')
        student.MobileNumber=request.POST.get('mobilenumber')
        student.save()
        return redirect('showstudent')
    return render(request,"editstudent.html")
def deletepage(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('showstudent')
def studentcard(request,pk):
    student=Student.objects.get(id=pk)
    return render(request,"showstudentdetails.html",{'students':student})