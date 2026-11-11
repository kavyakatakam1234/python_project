print('STUDENT RECORD MANAGEMENT')
print('1. Add Student')
print('2. View All Students')
print('3. Search Student')
print('4. Update Student')
print('5. Delete Student')
print('6. Exit')

choice=int(input('Enter Your Choice:'))

if choice==1:
      id=input('Enter Student ID:')
      name=input('Enter Name:')
      age=input('Enter Age:')
      course=input('Enter course:')
      marks=input('Enter marks:')
      with open('std.txt','a') as s:
            s.write(id + "," + name + "," + age + "," + course + "," + marks + "\n")
      print('Student Added Successfully!')
elif choice==2:
      with open('std.txt','r') as s:
            records=s.readlines()
            if len(records)==0:
                  print('No student records found')
            else:
                  print('student details')
                  for record in records:
                        data=record.strip().split(",")
                        print('\nID',data[0])
                        print('name',data[1])
                        print('age',data[2])
                        print('course',data[3])
                        print('marks',data[4])
elif choice==3:
      search_id=input('Enter Student ID:')
      with open('std.txt','r') as s:
            for record in s:
                  data=record.strip().split(",")
                  if data[0]==search_id:
                        print('\nStudent Found!')
                        print('ID',data[0])
                        print('name',data[1])
                        print('age',data[2])
                        print('course',data[3])
                        print('marks',data[4])
                        found=True
                        break
                  else:
                        print('Student Not Found')
elif choice==4:
      update_id=input('Enter Student ID to Update:')
      students=[]
      found=False
      with open('std.txt','r') as s:
            for record in s:
                  data=record.strip().split(",")
                  if data[0]==update_id:
                         print('Enter updated Details')
                         marks=input('Enter Marks:')
                         data[4]=marks
                         students.append(",".join(data) + "\n")
                         found=True
                  else:
                         students.append(record)
      with open('std.txt','w') as s:
            s.writelines(students)
      if found:
            print('Marks Updated Successfully!')
      else:
            print('Student Not Found')
elif choice==5:
      delete_id=input('Enter Student ID to Delete:')
      students=[]
      found=False
      with open('std.txt','r') as s:
             for record in s:
                  data=record.strip().split(",")
                  if data[0]==delete_id:
                        found=True
                  else:
                        students.append(record)
      with open('std.txt','w') as s:
            s.writelines(students)
      if found:
            print('Student Deleted Successfully!')
      else:
            print('Student Not Found')
elif choice==6:
     print('Thank you for using Student Record Management System!')
            

