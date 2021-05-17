# Django Rest Framework

#### Django Rest Framework First Assignment<br />

#### CRUD functionality with Django REST Framework

Four main API requests are GET, POST, PUT, DELETE.<br />
1. GET —This request is made when we wanna request some data from the server. Eg: Fetching weather forecast from the weather API.<br />
2. POST — This request is made when we wanna add data to the server. Eg: User Registration and Login.<br />
3. PUT — This request is for changing any Existing information in the server. Eg: Updating User Profile.<br />
4. DELETE — As the name indicates, this request is made where we wanna delete any existing information.<br />
Note: __str__() ->in every model you should define the standard Python class method __str__() to return a human-readable string for each object.<br />
<br />

**Steps for creating a DRF Project**<br />

1. Create a Django Project<br />
2. Install Django Rest Framework<br />
3. Create a model and add __str__ as a good practice to return human-readable string<br />
4. Create API Class<br />
5. Create API View<br />
6. List API view<br />
7. Update API View<br />
8. Delete API view:<br />
9. Create Serializer class<br />
10. Map your APi class with Url in urls.py<br />
11. Code is ready. Just run your server<br />

### Assignment:

Create a Backend of Hospital Management system using DRF. App name should be patient<br />
1. Patient Data(Models) which needs to be stored
2. Patient registration number -> patient_reg_no (CharField) -> This should be Unique but should not be a primary key
3. Patient name -> patient_name (CharField) -> 
4. Patient Email -> patient_email (EmailField)
5. Patient Mobile Number -> patient_mobile (CharField)
6. admitted at -> DateTimeField (Text field)(default : current time)

#### Urls.py

1. Name in Django URL -> name is used for accessing that URL from your Django / Python code.
2. For example you have this in 'patient/urls.py
3. url(r'^main/', views.main, name='main')
4. In point 2, "main" is the name of this URL
5. URL namespaces -> URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. At Line 21 in hospital/urls.py, path('patient/', include(('patient.urls', 'patient'), namespace='patient')),
6. namespace='patient is set. Remember, Both Name and Namespace are important for the assignment
7. For this assignment's test cases we have used some predefined names and namespace
8. Those names are defined below in the problem statement describes as "Django Url name"
9. Please make sure you use those names in Django URLs or else your assignment's test will fail Summary: Namespace is "'patient" set in hospital/urls.py file and name is to be set for each URL in 'patient/urls which is stated in the problem statement

### Views

#### You have to use class based views for this assignment

**Part 1: GET and POST request for fetching Patients**

Django URL name: patient_list_create<br />

Actions:<br />

1. GET - get list of all patients
2. POST - Add a new patient 

```
1. GET
Response Format:
[{"id":id,"patient_regNo":patient_regNo,"patient_name":patient_name,"patient_email":patient_email,"patient_mobile":patient_mobile,"admitted_at":admitted_at},   {"id":id,"patient_regNo":patient_regNo,"patient_name":patient_name,"patient_email":patient_email,"patient_mobile":patient_mobile,"admitted_at":admitted_at}]
  
Request: /patient/

Response: [{"id":2,"patient_regNo":"123","patient_name":"rahul","patient_email":"rahul123@gmail.com","patient_mobile":"0000000000","admitted_at":"2021-03-24T21:30:19.667926Z"},{"id":3,"patient_regNo":"1234","patient_name":"argo","patient_email":"argo@gmail.com","patient_mobile":"999999999","admitted_at":"2021-03-24T21:30:57.277179Z"}]

Response Code : 200
```

```
2. POST
Response Format:
{"id":id,"patient_regNo":patient_regNo,"patient_name":patient_name,"patient_email":patient_email,"patient_mobile":patient_mobile,"admitted_at":admitted_at}

Request: /patient/

Response: {"id":4,"patient_regNo":"12345","patient_name":"Tarun","patient_email":"Tarun@gmail.com","patient_mobile":"777777777","admitted_at":"2021-03-24T21:39:11.495442Z"}

Response code: 201
```

**Part 2: Retrieve, Update and Delete**

Django URL name: patient_update_delete<br />


1. GET - Retrive information of each patient
2. PUT - Update any patient information
3. DELETE - Remove patient from the record

```
1.GET
Response Format:
{"id":id,"patient_regNo":patient_regNo,"patient_name":patient_name,"patient_email":patient_email,"patient_mobile":patient_mobile,"admitted_at":admitted_at}

Request: /patient/2

Response: {"id":2,"patient_regNo":"123","patient_name":"rahul","patient_email":"rahul123@gmail.com","patient_mobile":"0000000000","admitted_at":"2021-03-24T21:30:19.667926Z"}

Response code: 200
```

``` 
2. PUT
Response Format: 
{"id":id,"patient_regNo":patient_regNo,"patient_name":patient_name,"patient_email":patient_email,"patient_mobile":patient_mobile,"admitted_at":admitted_at}

Request: patient/2" -d "patient_name=rahul1&patient_regNo=123&patient_email=test@gmail.com"

Response
{"id":2,"patient_regNo":"123","patient_name":"rahul1","patient_email":"test@gmail.com","patient_mobile":"0000000000","admitted_at":"2021-03-25T15:48:40.125929Z"}
Response code: 200
```


```
3. DELETE
No Response

Request: /patient/2

Response code: 204
```
 
Note: id is the primary key which is being passed in the url<br />
 
Reference: https://www.django-rest-framework.org/api-guide/generic-views/


## Installation Steps
1. Open up your Terminal / Command Line
2. git clone the repository
3. cd into the directory of the step (the one you just git cloned)
4. make sure you have python3 installed
5. Install virtualenv by following the steps 
```
Mac
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate

Windows
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
6. Run 
```
python -m pip install -r requirements/requirements.txt
```
6. No Database setup needs to be done. Do not edit Database settings in settings.py

7. If everything runs fine till here, create the application using the command
```
python manage.py startapp patient
```
8. Now uncomment the following lines
```
Line 21 in hospital/urls.py -> path('patient/', include(('patient.urls', 'patient'), namespace='patient')),
Line 41 in hospital/settings.py -> 'patient',
```
Now Create File hospital/urls.py and add lines
```
from django.urls import path

from . import views
urlpatterns = []
```
9. Run 
```
python manage.py makemigrations
```
10. Now Run the Server using command
```
python manage.py runserver
```
11.  Great! Start Coding the assignment for above usecase
12. After Finishing the assignment, you can test them locally using command 
```
coverage run --source='.' manage.py test --no-input
```
12. Push the code into the repo using git, Check Pull Requests Tab. Open PR #1
13. Check if all the tests are Passed
14. Contact TA for the review
