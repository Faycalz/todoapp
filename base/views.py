from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
data = [{"id":1,"first_name":"Archy","last_name":"Eckley","email":"aeckley0@altervista.org","gender":"Male","ip_address":"225.97.193.86"},
{"id":2,"first_name":"Carlie","last_name":"Kohneke","email":"ckohneke1@networkadvertising.org","gender":"Male","ip_address":"138.74.10.17"},
{"id":3,"first_name":"Silvia","last_name":"Shafto","email":"sshafto2@washingtonpost.com","gender":"Female","ip_address":"12.128.96.218"},
{"id":4,"first_name":"Earvin","last_name":"Baitey","email":"ebaitey3@huffingtonpost.com","gender":"Male","ip_address":"103.85.178.158"},
{"id":5,"first_name":"Park","last_name":"Gut","email":"pgut4@whitehouse.gov","gender":"Male","ip_address":"143.229.193.140"},
{"id":6,"first_name":"Agnes","last_name":"Pitney","email":"apitney5@amazonaws.com","gender":"Female","ip_address":"95.47.75.41"},
{"id":7,"first_name":"Sher","last_name":"Dessaur","email":"sdessaur6@paypal.com","gender":"Genderqueer","ip_address":"130.107.20.60"},
{"id":8,"first_name":"Loydie","last_name":"Dowthwaite","email":"ldowthwaite7@discovery.com","gender":"Male","ip_address":"247.13.122.66"},
{"id":9,"first_name":"Sashenka","last_name":"Stormes","email":"sstormes8@buzzfeed.com","gender":"Female","ip_address":"113.202.54.169"},
{"id":10,"first_name":"Isahella","last_name":"Cranch","email":"icranch9@about.com","gender":"Female","ip_address":"55.129.233.109"}]
    
def home(request):
    username = ['faycal','nabil','amar']
    age = 24
    context = {'username':username , 'age':age , 'data':data}
    return render(request , 'base/home.html' , context)

def room(request):
    return render(request , 'base/room.html')

def employee(request , id):
     
    for employee in data : 
        if employee['id'] == id: 
            employee_data = employee
    context = {'employee':employee_data}
       
    return render(request , 'base/employee.html' , context)