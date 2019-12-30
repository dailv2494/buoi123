from .models import Student
# Create your tests here.
def getAllStudent():
    return Student.objects.all()
#students = getAllStudnet()
def createStudent(studentNo,name):
    return Student.objects.create(
        studentNo = studentNo,
        name = name
    )
# st1 = createStudent('1001','Nguyen Son Tung')
# st2 = createStudent('1002','Nguyen Son Tung 2')

def getStudentById(id):
    return Student.objects.get(pk=id)

# st1 = getStudentById(1)

def updateStudent(id,studentNo,name):
    st = getStudentById(id)
    st.studentNo = studentNo
    st.name = name
    st.save()
    return st 

# updateStudent('1','1111','Update')

def deleteStudent(id):
    st = getStudentById(id)
    if st:
        st.delete()
# deleteStudent(2)
