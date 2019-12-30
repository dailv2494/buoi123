from django.shortcuts import render,redirect
from . import db
from django.core.files.storage import FileSystemStorage #new
import os
import time
def saveFile(studentNo,file):
    path = 'static/image/' + studentNo + '.jpg'
    if os.path.exists(path):
        os.remove(path)
    fs = FileSystemStorage()
    fs.save(path,file)


def index(request):
    context = {'students' : db.getAllStudent(),'time':time}
    return render(request, 'index.html', context)


def createStudent(request):
    if request.method == 'POST':
        studentNo = request.POST.get('studentNo')
        name = request.POST.get('name')
        db.createStudent(studentNo, name)
        file = request.FILES.get('image')
        if file and file.name :
            saveFile(studentNo,file)
        return redirect('home')
    else:
        return render(request, 'student_form.html')


def updateStudent(request,id):
    if request.method == 'POST':
        studentNo = request.POST.get('studentNo')
        name = request.POST.get('name')
        db.updateStudent(id, studentNo, name)
        file = request.FILES.get('image')
        if file and file.name :
            saveFile(studentNo,file)
        return redirect('home')
    else:
        st = db.getStudentById(id)
        studentNo = st.studentNo
        name = st.name
        context ={'studentNo':studentNo,'name':name}
        return render(request, 'student_form.html', context)

    

def deleteStudent(request,id):
    db.deleteStudent(id)
    return redirect('home')


