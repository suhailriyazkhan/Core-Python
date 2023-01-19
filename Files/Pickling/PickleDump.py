import pickle
from Files.Pickling import Student
f=open("student.dat","wb")
s=Student.Student(123,"king",90)
pickle.dump(s,f)
f.close()
