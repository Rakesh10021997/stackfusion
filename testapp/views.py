from django.shortcuts import render
from testapp.models import Register
from testapp.forms import RegisterForm
from django.contrib import messages
from rest_framework.views import APIView
from testapp.serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.

def home(request):
    form=RegisterForm
    print('hiiiiiiiiiiiiii')
    print(request.POST)
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        form = RegisterForm()
        messages.success(request, 'You have registered successfully.',extra_tags = 'alert alert-success alert-dismissible show')
    return render(request,'home.html',{'form':form})

def register(request):
    reg=Register.objects.all()
    if request.method =='POST':
        print(request.POST)
        first = request.POST.get('firstName')
        dobirth = request.POST.get('dob')
        emailid = request.POST.get('email')
        mobile = request.POST.get('mobilenumber')
        Register( first_name = first,
                  dob =dobirth,
                  email=emailid,
                  mobilenumber=mobile ).save()                
        messages.success(request, 'Register has been successfully',extra_tags = 'alert alert-success alert-dismissible show')
    return render(request,'testapp/home.html')

class RegisterAPIView(APIView):
    def get(request,self,format=None,*args,**kwargs):
        qs=Register.objects.all()
        serializer=RegisterSerializer(qs,many=True)
        return Response(serializer.data)
