"""
Cracking the coding interview
Practice questions
Part 14. Databases
"""

"""
Note: need to have sqlite installed. my case, brew install sqllite for mac
      could virtualenv all dependancies to share
"""
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

"""
Time for School
"""

# Create table(ulz)
c.execute("CREATE TABLE IF NOT EXISTS courses (courseID int, courseName text, teacherID int)")
c.execute("CREATE TABLE IF NOT EXISTS teachers (teacherID int, teacherName text)")
c.execute("CREATE TABLE IF NOT EXISTS students (studentID int, studentName text)")
c.execute("CREATE TABLE IF NOT EXISTS studentCourses (courseID int, studentID int)")
c.execute("CREATE TABLE IF NOT EXISTS studentTest (testID int, studentID int, points real)")

#c.execute("DROP TABLE students")

# Reset table
c.execute("DELETE FROM courses")
c.execute("DELETE FROM teachers")
c.execute("DELETE FROM students")
c.execute("DELETE FROM studentCourses")
c.execute("DELETE FROM studentTest")

# Insert a row of data
c.execute("INSERT INTO courses VALUES (1,'Algebra',1)")
c.execute("INSERT INTO courses VALUES (2,'Business',2)")
c.execute("INSERT INTO courses VALUES (3,'Statistics',1)")
c.execute("INSERT INTO courses VALUES (4,'English 1',3)")

c.execute("INSERT INTO teachers VALUES (1,'Simmons')")
c.execute("INSERT INTO teachers VALUES (2,'Applegate')")
c.execute("INSERT INTO teachers VALUES (3,'Jennings')")

c.execute("INSERT INTO students VALUES (1,'Dirk')")
c.execute("INSERT INTO students VALUES (2,'Stephanie')")
c.execute("INSERT INTO students VALUES (3,'Jake')")
c.execute("INSERT INTO students VALUES (4,'Khym')")

c.execute("INSERT INTO studentCourses VALUES (1,1)")
c.execute("INSERT INTO studentCourses VALUES (2,1)")
c.execute("INSERT INTO studentCourses VALUES (3,4)")
c.execute("INSERT INTO studentCourses VALUES (2,2)")
c.execute("INSERT INTO studentCourses VALUES (1,2)")
c.execute("INSERT INTO studentCourses VALUES (1,3)")

c.execute("INSERT INTO studentTest VALUES (1, 1, 80.0)")
c.execute("INSERT INTO studentTest VALUES (1, 2, 75.0)")
c.execute("INSERT INTO studentTest VALUES (1, 3, 82.0)")
c.execute("INSERT INTO studentTest VALUES (1, 4, 95.0)")
c.execute("INSERT INTO studentTest VALUES (2, 1, 89.0)")
c.execute("INSERT INTO studentTest VALUES (2, 2, 75.0)")
c.execute("INSERT INTO studentTest VALUES (2, 3, 82.0)")
c.execute("INSERT INTO studentTest VALUES (2, 4, 95.0)")
c.execute("INSERT INTO studentTest VALUES (3, 1, 92.0)")
c.execute("INSERT INTO studentTest VALUES (3, 2, 75.0)")
c.execute("INSERT INTO studentTest VALUES (3, 3, 82.0)")
c.execute("INSERT INTO studentTest VALUES (3, 4, 95.0)")

# Save (commit) the changes
conn.commit()

# for row in c.execute(''' select teacherID, count(*) as number_students from courses
#                          inner join studentCourses on studentCourses.courseID = courses.courseID
#                          group by teacherID
#                      '''):
#     print "teacher-students:", row

# for row in c.execute('''select teacherName, number_students from teachers
#                         left join(
#                          select teacherID, count(*) as number_students from courses
#                          inner join studentCourses on studentCourses.courseID = courses.courseID
#                          group by teacherID
#                         ) c1 on teachers.teacherID = c1.teacherID
#                      '''):
#     print "courses:", row

"""
Apartment Rental Agency
"""

# Create table(ulz)
c.execute("CREATE TABLE IF NOT EXISTS buildings (buildingID int, buildingName text)")
c.execute("CREATE TABLE IF NOT EXISTS apartments (apartmentID int, apartmentNumber text, buildingID int)")
c.execute("CREATE TABLE IF NOT EXISTS tenants (tenantID int, tenantName text)")
c.execute("CREATE TABLE IF NOT EXISTS apartmentTenant (apartmentID int, tenantID int)")
c.execute("CREATE TABLE IF NOT EXISTS apartmentRequest (requestID int, apartmentID int, status text, description text)")

#c.execute("DROP TABLE IF EXISTS buildings")
# Reset table
c.execute("DELETE FROM buildings")
c.execute("DELETE FROM apartments")
c.execute("DELETE FROM tenants")
c.execute("DELETE FROM apartmentTenant")
c.execute("DELETE FROM apartmentRequest")

c.execute("INSERT INTO buildings VALUES (1,'The Alexander')")
c.execute("INSERT INTO buildings VALUES (2,'The Victorian')")

c.execute("INSERT INTO apartments VALUES (1,'1A', 1)")
c.execute("INSERT INTO apartments VALUES (2,'1B', 1)")
c.execute("INSERT INTO apartments VALUES (3,'1C', 1)")
c.execute("INSERT INTO apartments VALUES (4,'1D', 1)")
c.execute("INSERT INTO apartments VALUES (5,'1E', 1)")
c.execute("INSERT INTO apartments VALUES (6,'1A', 2)")
c.execute("INSERT INTO apartments VALUES (7,'1B', 2)")
c.execute("INSERT INTO apartments VALUES (8,'1C', 2)")
c.execute("INSERT INTO apartments VALUES (9,'1D', 2)")
c.execute("INSERT INTO apartments VALUES (10,'1E', 2)")

c.execute("INSERT INTO tenants VALUES (1,'Eric')")
c.execute("INSERT INTO tenants VALUES (2,'Bob')")
c.execute("INSERT INTO tenants VALUES (3,'Allen')")
c.execute("INSERT INTO tenants VALUES (4,'Mindy')")
c.execute("INSERT INTO tenants VALUES (5,'Taco')")
c.execute("INSERT INTO tenants VALUES (6,'Dora')")
c.execute("INSERT INTO tenants VALUES (7,'Cyndi')")

c.execute("INSERT INTO apartmentTenant VALUES (1,1)")
c.execute("INSERT INTO apartmentTenant VALUES (7,1)")
c.execute("INSERT INTO apartmentTenant VALUES (2,2)")
c.execute("INSERT INTO apartmentTenant VALUES (6,3)")
c.execute("INSERT INTO apartmentTenant VALUES (7,4)")
c.execute("INSERT INTO apartmentTenant VALUES (8,5)")

c.execute("INSERT INTO apartmentRequest VALUES (1,3,'Open','Request for The Alexander, 1C')")
c.execute("INSERT INTO apartmentRequest VALUES (1,9,'Open','Request for The Victorian, 1D')")
c.execute("INSERT INTO apartmentRequest VALUES (1,10,'Open','Request for The Victorian, 1E')")
c.execute("INSERT INTO apartmentRequest VALUES (1,4,'Closed','Request for The Alexander, 1D')")

conn.commit()

# queries and junk

### List all tenants in table, building they are in - apartment number
# for row in c.execute('''select buildingName, apartmentNumber, tenants.tenantName from tenants
#                         left join(
#                             select buildings.buildingName, apartments.apartmentNumber, tenants.tenantID, tenants.tenantName from tenants
#                             join apartmentTenant on apartmentTenant.tenantID = tenants.tenantID
#                             join apartments on apartments.apartmentID = apartmentTenant.apartmentID
#                             join buildings on buildings.buildingID = apartments.buildingID
#                         ) t1 on tenants.tenantID = t1.tenantID
#                      '''):
#     print "courses:", row

### 14.1 ### List tenants who are renting more than one apartment (subletting ?)
# for row in c.execute('''select tenantName, apt_count from tenants
#                         inner join(
#                          select tenantID, count(*) as apt_count
#                          from apartmentTenant
#                          group by tenantID
#                          having apt_count > 1
#                         ) t1 on tenants.tenantID = t1.tenantID
#                      '''):
#     print "courses:", row

### 14.2 ### List buildings with open requests
# inner query
# query_string = '''
#                select apartments.apartmentID from apartmentRequest
#                inner join apartments on apartments.apartmentID = apartmentRequest.apartmentID
#                where apartmentRequest.status = 'Open'
#                '''
# outer and inner query - inner join only, only buildings that match inner query
# query_string = '''
#                select buildingName, request_count from buildings
#                inner join(
#                  select apartments.buildingID, count(*) as request_count from apartmentRequest
#                  inner join apartments on apartments.apartmentID = apartmentRequest.apartmentID
#                  where apartmentRequest.status = 'Open'
#                  group by apartments.buildingID
#                ) t1 on buildings.buildingID = t1.buildingID
#                '''
# for row in c.execute(query_string):
#     print "courses:", row

### 14.3 ### Close requests for a building
#
# building -> apartments -> apartmentRequest
# need list of apartment ID's from building ID
# query_string = '''
#                select apartments.apartmentID from apartments
#                where buildingID = 2
#                '''
# for row in c.execute(query_string):
#     print "apartmentID:", row

# aaaannnddd... update to cancelled
# query_string = '''
#                update apartmentRequest
#                set status = 'Cancelled'
#                where apartmentRequest.apartmentID in (
#                select apartments.apartmentID from apartments
#                where buildingID = 2
#                )
#                '''
# c.execute(query_string)

# requests status query
# query_string = '''
#                select buildings.buildingName from buildings
#                inner join apartments on apartments.buildingID = buildings.buildingID
#                inner join apartmentRequest on apartmentRequest.apartmentID = apartments.apartmentID
#                where apartmentRequest.status = 'Cancelled'
#                group by buildings.buildingID
#                '''
# query_string = '''
#                select * from apartmentRequest
#                '''
# for row in c.execute(query_string):
#     print "building requests:", row

### 14.4 ### Entity Diagram Company

### 14.5 ### Grade DB - return top 10% gpa
# note: workaround for lack of ceiling function adding .5 to int(round(x)) - not perfect but it works
# note: cannot use 'case' function since limit doesn't acknowlege aliases

"""
top 10% of grades
"""
for row in c.execute('''
                     select studentName, avg_points

                     from students
                     left join(
                       select studentID, avg(points) as avg_points from studentTest
                       group by studentID
                     ) p1 on students.studentID = p1.studentID
                     order by avg_points desc

                     limit cast(round(((select count(*) from students) * .5) + 0.5) as int)

                     '''):
    print "students:", row

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
