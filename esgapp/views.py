from django.shortcuts import render, HttpResponse, redirect
from esgapp.models import Finalapproverprofile, Finaluserprofile, Finaluserregister, Esgreporting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from esgsoftware.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

# Create your views here.

##############TUTION MANAGEMENT SYSTEM#############


def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')



def handleSignup(request): 
    
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['username']
        userid=request.POST['userid']
        emailsignup=request.POST['emailsignup']
        orgname=request.POST['orgname']
        passsignup=request.POST['passsignup']
        

        myuser = User.objects.create_user(username, emailsignup, passsignup)
        myuser.user_id=userid
        #myuser.Last_name=Slastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        #finalprofiletutorder = Finaltutorprofile.objects.filter(userid=lk)
        #print(finalprofiletutorder)
        

        tosign = request.POST.get('emailsignup', "default user")
        print(tosign)
        send_mail(
            'You have signed in successfully.',
            'Go Back to the website to Login.',
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        return redirect('/')
        #return render(request, '/', {"finalprofiletutorder":finalprofiletutorder})

def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        usernamelogin=request.POST['usernamelogin'] 
        passlogin=request.POST['passlogin']

        user=authenticate(username=usernamelogin, password=passlogin) #signup
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')


def approvercreateprofile(request):
    finalprofileapproverorder = Finalapproverprofile.objects.all()
    #finalprofiletutorder = Finaltutorprofile.objects.get(pk=1)
    if request.method=="POST":
        idtutor=request.POST['idtutor']
        inputfirstnamet=request.POST['inputfirstnamet']
        inputlastnamet=request.POST['inputlastnamet']
        inputemailt=request.POST['inputemailt']
        inputphonet=request.POST['inputphonet']
        inputtypet=request.POST['inputtypet']
        
        finalapproverprofiledata = Finalapproverprofile(idtutor=idtutor, inputfirstnamet=inputfirstnamet, inputlastnamet=inputlastnamet, inputemailt=inputemailt, inputphonet=inputphonet, inputtypet=inputtypet)  

        finalapproverprofiledata.save()
        messages.success(request, "Tutor Profile succesfully created and saved")
        #finalprofileapproverorder = Finalapproverprofile.objects.filter(pk=idtutor)
        #print(finalprofileapproverorder)
        #return redirect('approverprofileview', pk=finalapproverprofiledata.idtutor)
    return render(request,"approvercreateprofile.html",{"Fapproverprofileorders":finalprofileapproverorder})
        
    #return redirect('tutorprofileview', pk=finalprofiletutorder.idtutor, {"Ftutprofileorders":finalprofiletutorder})
    #return redirect('tutorprofileview', pk=finalprofiletutorder.idtutor)

def approverprofileview(request, pk):
    finalprofileapproverorder = Finalapproverprofile.objects.filter(idtutor=pk)
    print(finalprofileapproverorder)
    
    return render(request, 'approverprofileview.html', {"finalprofileapproverorder":finalprofileapproverorder})
    #return redirect('tutorprofile', pk=finalprofiletutorder.idtutor)


def approverlist(request):
    #num1=Finalstudentprofile.objects.count()
    finalprofileapproverorder = Finalapproverprofile.objects.all()
    print(finalprofileapproverorder)
    return render(request, 'approverlist.html', {"finalprofileapproverorder":finalprofileapproverorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    

def approverprofile(request, pk):
    finalprofileapproverorder = Finalapproverprofile.objects.filter(idtutor=pk)
    print(finalprofileapproverorder)
    return render(request, 'approverprofile.html', {"finalprofileapproverorder":finalprofileapproverorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')


def usercreateprofile(request):
    finalprofileuserorder = Finaluserprofile.objects.all()
    if request.method=="POST":
        idstudent=request.POST['idstudent']
        inputfirstnamestu=request.POST['inputfirstnamestu']
        inputlastnamestu=request.POST['inputlastnamestu']
        inputemailstu=request.POST['inputemailstu']
        inputphonestu=request.POST['inputphonestu']
        
        finaluserprofiledata = Finaluserprofile(idstudent=idstudent, inputfirstnamestu=inputfirstnamestu, inputlastnamestu=inputlastnamestu, inputemailstu=inputemailstu, inputphonestu=inputphonestu)  

        finaluserprofiledata.save()
        messages.success(request, "User Profile succesfully created and saved")
        #finalprofilestudorder = Finalstudentprofile.objects.filter(ik=idstudent)
        #print(finalprofilestudorder)
        #return redirect('studentprofileview', ik=finalstudprofiledata.idstudent)
              
    #return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})
    return render(request,"usercreateprofile.html",{"Fuserprofileorders":finalprofileuserorder})

def userprofileview(request, ik):
    finalprofileuserorder = Finaluserprofile.objects.filter(idstudent=ik)
    print(finalprofileuserorder)
    
    return render(request, 'userprofileview.html', {"finalprofileuserorder":finalprofileuserorder})
    #return redirect('tutorprofile', pk=finalprofiletutorder.idtutor)


def userlist(request):
    #num1=Finalstudentprofile.objects.count()
    finalprofileuserorder = Finaluserprofile.objects.all()
    print(finalprofileuserorder)
    return render(request, 'userlist.html', {"finalprofileuserorder":finalprofileuserorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    
    
def userprofile(request, ik):
    #num1=Finalstudentprofile.objects.count()
    finalprofileuserorder = Finaluserprofile.objects.filter(idstudent=ik)
    print(finalprofileuserorder)
               
    return render(request, 'userprofile.html', {"finalprofileuserorder":finalprofileuserorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    


def searchpage(request):
    finalprofileapproverorder = Finalapproverprofile.objects.all()
    print(finalprofileapproverorder)
    return render(request, 'searchpage.html', {"finalprofileapproverorder":finalprofileapproverorder})


def esgreportingform(request):
    finalreportorder = Esgreporting.objects.all()
    if request.method=="POST":
        n1=request.POST['n1']
        n2=request.POST['n2']
        n3=request.POST['n3']
        n4=request.POST['n4']
        n5=request.POST['n5']
        n6=request.POST['n6']
        n7=request.POST['n7']
        n8=request.POST['n8']
        n9=request.POST['n9']
        n10=request.POST['n10']
        n11=request.POST['n11']
        n12=request.POST['n12']
        n13=request.POST['n13']
        n14=request.POST['n14']
        n15=request.POST['n15']
        n16=request.POST['n16']
        n17=request.POST['n17']
        n18=request.POST['n18']
        n19=request.POST['n19']
        n20=request.POST['n20']
        n21=request.POST['n21']
        n22=request.POST['n22']
        n23=request.POST['n23']
        n24=request.POST['n24']
        n25=request.POST['n25']
        n26=request.POST['n26']
        n27=request.POST['n27']
        n28=request.POST['n28']
        n29=request.POST['n29']
        n30=request.POST['n30']
        n31=request.POST['n31']
        n32=request.POST['n32']
        n33=request.POST['n33']
        n34=request.POST['n34']
        n35=request.POST['n35']
        n36=request.POST['n36']
        n37=request.POST['n37']
        n38=request.POST['n38']
        n39=request.POST['n39']
        n40=request.POST['n40']
        n41=request.POST['n41']
        n42=request.POST['n42']
        n43=request.POST['n43']
        n44=request.POST['n44']
        n45=request.POST['n45']
        n46=request.POST['n46']
        n47=request.POST['n47']
        n48=request.POST['n48']
        n49=request.POST['n49']
        n50=request.POST['n50']
        n51=request.POST['n51']
        n52=request.POST['n52']
        n53=request.POST['n53']
        n54=request.POST['n54']
        n55=request.POST['n55']
        n56=request.POST['n56']
        n57=request.POST['n57']
        n58=request.POST['n58']
        n59=request.POST['n59']
        n60=request.POST['n60']
        n61=request.POST['n61']
        n62=request.POST['n62']
        n63=request.POST['n63']
        n64=request.POST['n64']
        n65=request.POST['n65']
        n66=request.POST['n66']
        n67=request.POST['n67']
        n68=request.POST['n68']
        n69=request.POST['n69']
        n70=request.POST['n70']
        n71=request.POST['n71']
        n72=request.POST['n72']
        n73=request.POST['n73']
        n74=request.POST['n74']
        n75=request.POST['n75']
        n76=request.POST['n76']
        n77=request.POST['n77']
        n78=request.POST['n78']
        n79=request.POST['n79']
        n80=request.POST['n80']
        n81=request.POST['n81']
        n82=request.POST['n82']
        n83=request.POST['n83']
        n84=request.POST['n84']
        n85=request.POST['n85']
        n86=request.POST['n86']
        n87=request.POST['n87']
        n88=request.POST['n88']
        n89=request.POST['n89']
        n90=request.POST['n90']
        
        finaluserreportdata = Esgreporting(n1=n1, n2=n2,n3=n3, n4=n4, n5=n5   ,     n6=n6     ,  n7=n7,      n8=n8 ,       n9=n9    ,    n10=n10,
        n11=n11,
        n12=n12,
        n13=n13,
        n14=n14,
        n15=n15,
        n16=n16,
        n17=n17,
        n18=n18,
        n19=n19,
        n20=n20,
        n21=n21,
        n22=n22,
        n23=n23,
        n24=n24,
        n25=n25,
        n26=n26,
        n27=n27,
        n28=n28,
        n29=n29,
        n30=n30,
        n31=n31,
        n32=n32,
        n33=n33,
        n34=n34,
        n35=n35,
        n36=n36,
        n37=n37,
        n38=n38,
        n39=n39,
        n40=n40,
        n41=n41,
        n42=n42,
        n43=n43,
        n44=n44,
        n45=n45,
        n46=n46,
        n47=n47,
        n48=n48,
        n49=n49,
        n50=n50,
        n51=n51,
        n52=n52,
        n53=n53,
        n54=n54,
        n55=n55,
        n56=n56,
        n57=n57,
        n58=n58,
        n59=n59,
        n60=n60,
        n61=n61,
        n62=n62,
        n63=n63,
        n64=n64,
        n65=n65,
        n66=n66,
        n67=n67,
        n68=n68,
        n69=n69,
        n70=n70,
        n71=n71,
        n72=n72,
        n73=n73,
        n74=n74,
        n75=n75,
        n76=n76,
        n77=n77,
        n78=n78,
        n79=n79,
        n80=n80,
        n81=n81,
        n82=n82,
        n83=n83,
        n84=n84,
        n85=n85,
        n86=n86,
        n87=n87,
        n88=n88,
        n89=n89,
        n90=n90)  

        finaluserreportdata.save()
        messages.success(request, "Student Profile succesfully created and saved")
        #finalprofilestudorder = Finalstudentprofile.objects.filter(ik=idstudent)
        #print(finalprofilestudorder)
        #return redirect('studentprofileview', ik=finalstudprofiledata.idstudent)
              
    #return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})
    return render(request,"esgreportingform.html",{"Fuserreportorders":finalreportorder})

    


def reportpdf(request, ik, hk):
    finalprofileuserorder = Finaluserprofile.objects.filter(idstudent=ik)
    finalreportorder = Esgreporting.objects.filter(n8=hk)
    print(finalreportorder, finalprofileuserorder)
    return render(request, 'reportpdf.html', {"finalreportorder":finalreportorder, "finalprofileuserorder":finalprofileuserorder})




def userdashboardpage(request, ik): #take from registeration
    #return HttpResponse("This is my home page")
    #return render(request, 'studentdashboardpage.html')
    #finalprofiletutorder = Finaltutorprofile.objects.all()
    #finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    finalprofileuserorder = Finaluserprofile.objects.filter(idstudent=ik)
    finalreportorder = Esgreporting.objects.filter(n1=ik)
    print(finalprofileuserorder, finalreportorder)
    return render(request, 'userdashboardpage.html', {"finalprofileuserorder":finalprofileuserorder, "finalreportorder":finalreportorder})


def approverdashboard(request, pk):
    #return HttpResponse("This is my home page")
    #return render(request, 'tutordashboard.html')
    finalprofileuserorder = Finaluserprofile.objects.filter()
    finalprofileapproverorder = Finalapproverprofile.objects.filter(idtutor=pk)
    finalreportorder = Esgreporting.objects.filter()
    print(finalprofileapproverorder, finalreportorder, finalprofileuserorder)
    return render(request, 'approverdashboard.html', {"finalprofileapproverorder":finalprofileapproverorder, "finalreportorder":finalreportorder, "finalprofileuserorder":finalprofileuserorder})



def checkpage(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'registernewcourse.html')
    finalregisteruserorder = Finaluserregister.objects.all()
    if request.method=="POST":
        registernewid=request.POST['registernewid']
        registernewcontact=request.POST['registernewcontact']
        registernewemail=request.POST['registernewemail']
        studentnotetotutor=request.POST['studentnotetotutor']
        tutoridnew=request.POST['tutoridnew']
        tutornewemail=request.POST['tutornewemail']
        coursesregistered=request.POST['coursesregistered']
        
        finaluserregisterdata = Finaluserregister(registernewid=registernewid, registernewcontact=registernewcontact, registernewemail=registernewemail, studentnotetotutor=studentnotetotutor, tutoridnew=tutoridnew, tutornewemail=tutornewemail, coursesregistered=coursesregistered)  

        finaluserregisterdata.save()
        messages.success(request, "Course Registered Successfully") 
        
        tosign = request.POST.get('tutornewemail')
        conver = request.POST.get('registernewid')
        conver1 = request.POST.get('registernewcontact')
        conver2 = request.POST.get('registernewemail')
        conver3 = request.POST.get('studentnotetotutor')
        conver4 = request.POST.get('coursesregistered')
        print(tosign)
        send_mail(
            'A New Registration Recieved.',
            'Student ID '+ conver +' has Registered. Courses: ' + conver4+ ' Phone Number: '+ conver1 + ' Email ID: ' + conver2 + ' Note: ' + conver3,
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        
                     
    return render(request,"checkpage.html",{"Fuserregisterorders":finalregisteruserorder})
