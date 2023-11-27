import smtplib

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login (request):
    return render(request,'login_index.html')

def login_Post(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    log=Login.objects.filter(username=uname,password=password)
    if log.exists():
        obj=Login.objects.get(username=uname,password=password)
        request.session['lid']=obj.id
        if obj.type == 'Admin':
            return HttpResponse('''<script> alert('Login Successfull');window.location="/myapp/Admin_home/"</script>''')
        elif obj.type == 'Photographer':
            return HttpResponse('''<script> alert('Login Successfull');window.location="/myapp/Photographer_Home/"</script>''')

        elif obj.type == 'user':
            return HttpResponse('''<script> alert('Login Successfull');window.location="/myapp/User_Home/"</script>''')

        else:
            return HttpResponse('''<script> alert('Invalid username or Password');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script> alert('Invalid username or Password');window.location="/myapp/login/"</script>''')

def logout(request):
    request.session['lid']=""
    return redirect('/myapp/login/')



def forgotpassword(request):
    return render(request, 'forgotpassword.html')


def forgotpassword_post(request):
    email = request.POST['textfield']
    res = Login.objects.filter(username=email)
    if not res.exists():
        return HttpResponse('''<script>alert('Invalid...');window.location='/myapp/login/'</script>''')
    else:
        import random
        new_pass = random.randint(0000, 9999)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("lensupcommunity@gmail.com", "kryqnndauqwnkpwt")  # App Password

        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)

        # Disconnect from the server
        server.quit()

        res= Login.objects.filter(username=email).update(password=new_pass)
        return HttpResponse(
            '''<script>alert('New password added.Please check your email..');window.location='/myapp/login/'</script>''')
    # else:



def Admin_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Admin/change password.html')

def Admin_change_password_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        current_password=request.POST['textfield']
        new_password=request.POST['textfield2']
        confirm_password=request.POST['textfield3']
        lid=request.session['lid']
        log=Login.objects.get(id=lid)
        if log.password==current_password:
            if new_password==confirm_password:
                log.password=confirm_password
                log.save()
                return HttpResponse('''<script> alert('Password changed successfully');window.location="/myapp/login/"</script>''')
            else:
                return HttpResponse('''<script> alert('Password does not match');window.location="/myapp/Admin_change_password/"</script>''')
        else:
            return HttpResponse('''<script> alert('Password does not match');window.location="/myapp/Admin_change_password/"</script>''')

def admin_add_category(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Admin/add category.html')

def admin_add_category_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        name = request.POST['textfield']
        cobj = Category()
        cobj.name = name
        cobj.save()
        return HttpResponse('''<script>alert("Added Successfully...");window.location='/myapp/admin_add_category/'</script>''')

def admin_view_category(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Category.objects.all()
        return render(request,'Admin/view category.html',{'data':res})

def admin_view_category_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        search=request.POST['textfield']
        res=Category.objects.filter(name__icontains=search)
        return render(request,'Admin/view category.html',{'data':res})

def delete_category(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Category.objects.filter(pk=id).delete()
        return redirect('/myapp/admin_view_category/')

def view_approved_photographers(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        var=Photographer.objects.filter(status='approved')
        return render(request, 'Admin/view approved photographer.html',{'data':var})


def Search_Approved_pg_post(request):
    pname=request.POST['textfield']
    var=Photographer.objects.filter(name__icontains=pname,status='approved')

    return render(request, 'Admin/view approved photographer.html',{'data':var})


def view_pending_photographers(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        var=Photographer.objects.filter(status='pending')
        return render(request, 'Admin/view pending photographers.html',{'data':var})

def pending_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        Search=request.POST['textfield']
        var=Photographer.objects.filter(name__icontains=Search,status='pending')
        return render(request, 'Admin/view pending photographers.html',{'data':var})



def approve_photographer(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        var=Photographer.objects.filter(LOGIN=id).update(status='approved')
        varr=Login.objects.filter(pk=id).update(type='Photographer')
        return HttpResponse( '''<script> alert('Approved..');window.location="/myapp/view_pending_photographer/"</script>''')



def reject_photographer(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        var=Photographer.objects.filter(LOGIN=id).update(status='rejected')
        varr=Login.objects.filter(pk=id).update(type='Rejected')
        return HttpResponse( '''<script>alert('Rejected..');window.location="/myapp/view_pending_photographer/"</script>''')

def view_rejected_photographers(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        var=Photographer.objects.filter(status='rejected')
        return render(request, 'Admin/view rejected photographer.html',{'data':var})

def Search_rejected_pg_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        s=request.POST['textfield']
        var=Photographer.objects.filter(name__icontains=s,status='rejected')
        return render(request, 'Admin/view rejected photographer.html',{'data':var})



def view_content(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.all()
        # res=Contents.objects.exclude(PHOTOGRAPHER__LOGIN_id=request.session['lid'])
        return render(request, 'Admin/view contents.html',{'data':res})


def view_contents_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        title=request.POST['textfield']
        # To=request.POST['textfield2']
        res = Contents.objects.filter(title__icontains=title)
        return render(request, 'Admin/view contents.html', {'data': res})

def admin_remove_content(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.filter(pk=id).delete()
        return redirect('/myapp/view_content/')

def view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Feedback.objects.all()
        l=[]
        for i in res:
            name = ""
            if i.type == 'Photographer':
                name=Photographer.objects.get(LOGIN_id=i.LOGIN_id).name
            if i.type == 'User':
                name=Users.objects.get(LOGIN_id=i.LOGIN_id).name
            l.append({'id':i.id,'name':name,'date':i.date,'feedback':i.Feed_back})


        return render(request,'Admin/view feedback.html',{'data':l})

def view_feedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        From1=request.POST['textfield']
        To1=request.POST['textfield2']

        res = Feedback.objects.filter(date__range=[From1,To1])
        l=[]
        for i in res:
            name = ""
            if i.type == 'Photographer':
                name = Photographer.objects.get(LOGIN_id=i.LOGIN_id).name
            if i.type == 'User':
                name = Users.objects.get(LOGIN_id=i.LOGIN_id).name
            l.append({'id': i.id, 'name': name, 'date': i.date, 'feedback': i.Feed_back})

        return render(request, 'Admin/view feedback.html', {'data': l})



def view_users(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Users.objects.all()
        return render(request,'Admin/view users.html',{'data':res})

def view_users_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        view=request.POST['textfield']
        res = Users.objects.filter(name__icontains=view)
        return render(request, 'Admin/view users.html', {'data': res})

def adm_view_blog(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.all()
        return render(request,'Admin/view blog.html',{'data':res})

def adm_view_blog_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        res = Blogs.objects.filter(date__range=[fdate,tdate])
        return render(request,'Admin/view blog.html',{'data':res})

def adm_remove_blog(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.filter(pk=id).delete()
        return redirect('/myapp/adm_view_blog/')



def Admin_home(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Admin/home_index.html')




#photographer

def photgrapher_Add_Blog(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Photographer/Add blog.html')

def Add_Blog_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        title=request.POST['textfield1']
        blog=request.POST['textfield']
        images=request.FILES['image']
        from datetime import datetime
        date = 'image/' + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fn = fs.save(date, images)
        path = fs.url(date)

        bobj=Blogs()
        bobj.title=title
        bobj.blog=blog
        bobj.image=path
        from datetime import datetime
        datee=datetime.now().strftime("%Y%m%d")
        bobj.date=datee
        bobj.PHOTOGRAPHER_id=Photographer.objects.get(LOGIN=request.session['lid']).id
        bobj.save()
        return HttpResponse('''<script> alert('Added..Sucessfully..');window.location="/myapp/photgrapher_Add_Blog/"</script>''')

def photgrapher_View_Blog(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'])
        return render(request,'Photographer/view blog.html',{'data':res})

def p_view_blog_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        From = request.POST['textfield']
        to = request.POST['textfield2']
        res = Blogs.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'],date__range=[From,to])
        return render(request, 'Photographer/view blog.html', {'data': res})

def photgrapher_Edit_Blog(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.get(pk=id)
        return render(request,'Photographer/edit blog.html',{'data':res})

def Edit_Blog_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        title=request.POST['textfield1']
        blog=request.POST['textfield']
        id=request.POST['id']

        if 'imagee' in request.FILES:
            images = request.FILES['imagee']
            if images !="":
                from datetime import datetime
                date = 'image/' + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                fs = FileSystemStorage()
                fn = fs.save(date,images)
                path = fs.url(date)
                res=Blogs.objects.filter(pk=id).update(title=title,blog=blog,image=path)
                return HttpResponse('''<script> alert('Updated...');window.location="/myapp/photgrapher_View_Blog/"</script>''')
        else:
            res = Blogs.objects.filter(pk=id).update(title=title,blog=blog)
            return HttpResponse(
                '''<script> alert('Updated...');window.location="/myapp/photgrapher_View_Blog/"</script>''')


def delete_blog(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.filter(pk=id).delete()
        return redirect('/myapp/photgrapher_View_Blog/')


def view_others_blog(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res = Blogs.objects.exclude(PHOTOGRAPHER__LOGIN_id  = request.session['lid'])
        return render(request, 'Photographer/view others blog.html',{'data':res})


def view_others_content(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.exclude(PHOTOGRAPHER__LOGIN_id=request.session['lid'])
        return render(request,'Photographer/View_others_Contents.html',{'data':res})



def photographer_Add_Contents(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Photographer/Add contents.html')

def Add_contents_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        title=request.POST['textfield']
        photo=request.FILES['fileField']
        amount=request.POST['textfield2']
        from datetime import datetime
        date = 'content/'+datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fn = fs.save(date, photo)
        path = fs.url(date)
        cobj=Contents()
        cobj.title=title
        cobj.photo=path
        cobj.amount=amount
        cobj.PHOTOGRAPHER_id=Photographer.objects.get(LOGIN=request.session['lid']).id
        cobj.save()
        return HttpResponse('''<script> alert('Added...');window.location="/myapp/photographer_Add_Contents/"</script>''')

def photgrapher_View_Contents(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'])
        return render(request,'Photographer/view contents.html',{'data':res})

def photgrapher_Edit_Contents(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.get(pk=id)
        return render(request,'Photographer/edit contents.html',{'data':res})

def Edit_Content_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        title1 = request.POST['textfield']
        amount1 = request.POST['textfield2']
        id=request.POST['id']
        if 'fileField' in request.FILES:
            photo1 = request.FILES['fileField']
            if photo1 !="":
                from datetime import datetime
                date = 'content/' + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                fs = FileSystemStorage()
                fn = fs.save(date, photo1)
                path = fs.url(date)
                res=Contents.objects.filter(pk=id).update(title=title1,photo=path,amount=amount1)
                return HttpResponse('''<script> alert('Updated...');window.location="/myapp/photgrapher_View_Contents/"</script>''')
        else:
            res = Contents.objects.filter(pk=id).update(title=title1,amount=amount1)
            return HttpResponse(
                '''<script> alert('Updated...');window.location="/myapp/photgrapher_View_Contents/"</script>''')

def delete_content(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.filter(pk=id).delete()
        return redirect('/myapp/photgrapher_View_Contents/')

def P_View_content_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        search = request.POST['textfield']
        res = Contents.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'],title__icontains=search)
        return render(request, 'Photographer/view contents.html', {'data': res})


def photgrapher_Photographer_Registration(request):
    return render(request,'Photographer/signup_index.html')

def Photographer_Registration_Post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    photo = request.FILES['fileField']

    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,photo)
    path=fs.url(date)

    dob = request.POST['textfield4']
    experience = request.POST['textfield5']
    place = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    password = request.POST['textfield9']
    confirm_password = request.POST['textfield10']

    if password==confirm_password:
        lobj=Login()
        lobj.username=email
        lobj.password=password
        lobj.type='pending'
        lobj.save()


        pobj=Photographer()
        pobj.name=name
        pobj.email=email
        pobj.phone=phone
        pobj.gender=gender
        pobj.photo=path
        pobj.dob=dob
        pobj.experiance=experience
        pobj.place=place
        pobj.pin=pin
        pobj.district=district
        pobj.LOGIN=lobj
        pobj.status='pending'
        pobj.save()



        return HttpResponse('''<script> alert('Registration completed.Please wait for the confirmation..');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script> alert('Password does not match');window.location="/myapp/login/"</script>''')

def photgrapher_View_Profile(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Photographer.objects.get(LOGIN=request.session['lid'])
        return render(request,'Photographer/view profile.html',{'i':res})

def photgrapher_Edit_Profile(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Photographer.objects.get(LOGIN=request.session['lid'])
        return render(request,'Photographer/edit profile.html',{'data':res})

def Photographer_Edit_Profile_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        name = request.POST['textfield6']
        email = request.POST['textfield7']
        phone = request.POST['textfield8']
        gender = request.POST['RadioGroup1']
        dob = request.POST['textfield']
        experience = request.POST['textfield2']
        place = request.POST['textfield3']
        pin = request.POST['textfield4']
        district = request.POST['textfield5']
        if 'fileField' in request.FILES:
            photo = request.FILES['fileField']
            if photo !="":
                from datetime import datetime
                date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                fs = FileSystemStorage()
                fn = fs.save(date, photo)
                path = fs.url(date)
                res=Photographer.objects.filter(LOGIN=request.session['lid']).update(name=name,email=email,phone=phone,gender=gender,dob=dob,experiance=experience,place=place,pin=pin,district=district,photo=path)

                return HttpResponse('''<script> alert('Updated..');window.location="/myapp/photgrapher_View_Profile/"</script>''')
        else:
            res = Photographer.objects.filter(LOGIN=request.session['lid']).update(name=name, email=email, phone=phone,
                                                                                   gender=gender, dob=dob,
                                                                                   experiance=experience, place=place,
                                                                                   pin=pin, district=district)
            return HttpResponse(
                '''<script> alert('Updated..');window.location="/myapp/photgrapher_View_Profile/"</script>''')


def photgrapher_Send_Feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Photographer/send feedback.html')

def P_Send_Feedback_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        feedback = request.POST['textfield']
        fobj=Feedback()
        from datetime import datetime
        datee = datetime.now().strftime('%Y%m%d')
        fobj.date=datee
        fobj.Feed_back=feedback
        fobj.type='Photographer'
        fobj.LOGIN_id=Login.objects.get(pk=request.session['lid']).id
        fobj.save()
        return HttpResponse('''<script> alert('Feedback Added..');window.location="/myapp/photgrapher_Send_Feedback/"</script>''')

def p_view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Feedback.objects.filter(LOGIN_id=Login.objects.get(pk=request.session['lid']))
        return render(request,'Photographer/view feedback.html',{'data':res})

def p_view_feedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        res = Feedback.objects.filter(LOGIN_id=Login.objects.get(pk=request.session['lid']),date__range=[fdate,tdate])
        return render(request, 'Photographer/view feedback.html', {'data': res})

def p_delete_feedback(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res = Feedback.objects.filter(pk=id).delete()
        return redirect('/myapp/p_view_feedback/')


def photgrapher_View_Order_More(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Photographer/view order more.html')

def photgrapher_View_Orders(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Orders_Main.objects.filter(CONTENT__PHOTOGRAPHER__LOGIN_id=request.session['lid'])
        return render(request,'Photographer/view orders.html',{'data':res})

def P_View_Order_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fromd = request.POST['textfield']
        tod = request.POST['textfield2']
        res = Orders_Main.objects.filter(CONTENT__PHOTOGRAPHER__LOGIN_id=request.session['lid'],date__range=[fromd,tod])
        return render(request, 'Photographer/view orders.html', {'data': res})

def photgrapher_View_user_Booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'],status='pending')
        return render(request,'Photographer/view user booking.html',{'data':res})


def photgrapher_View_user_Booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        Fromd = request.POST['textfield']
        tod = request.POST['textfield2']
        res = Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'], status='pending',date__range=[Fromd,tod])
        return render(request, 'Photographer/view user booking.html', {'data': res})

def p_approve_booking(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(pk=id).update(status='approved')
        return HttpResponse('''<script> alert('Approved..');window.location="/myapp/photgrapher_View_user_Booking/"</script>''')

def p_view_approved_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'],status='approved')
        return render(request,'Photographer/view user approved booking.html',{'data':res})


def p_view_approved_booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        Fromd = request.POST['textfield']
        tod = request.POST['textfield2']
        res = Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'], status='approved',
                                     date__range=[Fromd, tod])
        return render(request, 'Photographer/view user booking.html', {'data': res})


def p_view_rejected_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'],status='rejected')
        return render(request,'Photographer/view user rejected booking.html',{'data':res})

def p_view_rejected_booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        Fromd = request.POST['textfield']
        tod = request.POST['textfield2']
        res = Booking.objects.filter(PHOTOGRAPHER__LOGIN_id=request.session['lid'], status='rejected',
                                     date__range=[Fromd, tod])
        return render(request, 'Photographer/view user booking.html', {'data': res})


def p_reject_booking(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(pk=id).update(status='rejected')
        return HttpResponse('''<script> alert('Rejected..');window.location="/myapp/photgrapher_View_user_Booking/"</script>''')


def Photographer_Home(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'Photographer/home_index.html')

#=========user


def u_view_blog(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Blogs.objects.all()
        return render(request,'User/view blog.html',{'data':res})

def u_view_blog_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        res = Blogs.objects.filter(date__range=[fdate,tdate])
        return render(request, 'User/view blog.html', {'data': res})

def User_Payment(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.get(pk=id)
        return render(request, 'User/payment.html',{'data':res})

def User_Payment_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        Acno = request.POST['textfield']
        id=request.POST['id']
        amount=request.POST['amnt']
        # Cvv = request.POST['textfield2']
        # IFSC = request.POST['textfield3']
        # Owner_name = request.POST['textfield4']
        res=bank.objects.filter(AcNO=Acno)
        if res.exists():
            ress = bank.objects.get(AcNO=Acno)
            if ress.balance >= float(amount):

                obj=Orders_Main()
                from datetime import datetime
                datee = datetime.now().strftime('%Y%m%d')
                obj.date=datee
                obj.USER_id=Users.objects.get(LOGIN=request.session['lid']).id
                obj.CONTENT_id=Contents.objects.get(pk=id).id
                obj.status='paid'
                obj.save()

                bnk=bank.objects.filter(AcNO=Acno).update(balance=float(ress.balance)-float(amount))

                # bobj=bank.objects.get(AcNO=Acno)
                # bl=float(ress.balance)-float(amount)
                # ress.balance=bl
                # # bobj.ORDER_id=obj.id
                # ress.save()
                return HttpResponse('''<script> alert('Paid Successfully..');window.location="/myapp/User_Home/"</script>''')
            else:
                return HttpResponse('''<script> alert('Insufficient bank balance..');window.location="/myapp/User_Home/"</script>''')
        else:
            return HttpResponse(
                '''<script> alert('User not found..');window.location="/myapp/User_Home/"</script>''')

def user_view_order(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Orders_Main.objects.filter(USER__LOGIN_id=request.session['lid'])
        return render(request,'User/view_order.html',{'data':res})

def user_view_order_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate = request.POST['textfield']
        tdate = request.POST['textfield2']
        res = Orders_Main.objects.filter(USER__LOGIN_id=request.session['lid'],date__range=[fdate,tdate])
        return render(request, 'User/view_order.html', {'data': res})



def User_Purchase_Photos(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Contents.objects.filter(PHOTOGRAPHER=id)
        return render(request,'User/Purchase photos.html',{'data':res})

def User_Search_Photographers(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Photographer.objects.filter(status='approved')
        return render(request,'User/search photographers.html',{'data':res})

def User_Search_Photographers_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        search = request.POST['textfield']
        res = Photographer.objects.filter(status='approved',place__icontains=search)
        return render(request, 'User/search photographers.html', {'data': res})

def u_book_photographer(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Category.objects.all()
        return render(request,'User/book_photographer.html',{'data':res,'pid':id})

def u_book_photographer_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        pid=request.POST['id']
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        description=request.POST['description']
        cat=request.POST['category']

        res=Booking.objects.filter(from_d=fdate,to_d=tdate)
        if not res.exists():

            bobj=Booking()
            from datetime import datetime
            datee = datetime.now().strftime('%Y%m%d')
            bobj.date=datee
            bobj.status='pending'
            bobj.CATEGORY_id=Category.objects.get(pk=cat).id
            bobj.from_d=fdate
            bobj.to_d=tdate
            bobj.description=description
            bobj.PHOTOGRAPHER_id=Photographer.objects.get(pk=pid).id
            bobj.USER_id=Users.objects.get(LOGIN=request.session['lid']).id
            bobj.save()
            return HttpResponse('''<script> alert('Booked..');window.location="/myapp/User_Search_Photographers/"</script>''')
        else:
            return HttpResponse('''<script> alert('Booking already exists above date..');window.location="/myapp/User_Search_Photographers/"</script>''')

def u_view_approved_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(USER__LOGIN_id=request.session['lid'],status='approved')
        return render(request,'User/view approved booking.html',{'data':res})

def u_view_approved_booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate = request.POST['textfield']
        tdate = request.POST['textfield2']
        res = Booking.objects.filter(USER__LOGIN_id=request.session['lid'], status='approved',date__range=[fdate,tdate])
        return render(request, 'User/view approved booking.html', {'data': res})

def u_view_rejected_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(USER__LOGIN_id=request.session['lid'],status='rejected')
        return render(request,'User/view rejected booking .html',{'data':res})

def u_view_rejected_booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate = request.POST['textfield']
        tdate = request.POST['textfield2']
        res = Booking.objects.filter(USER__LOGIN_id=request.session['lid'], status='rejected',date__range=[fdate,tdate])
        return render(request, 'User/view rejected booking .html', {'data': res})


def u_view_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(USER__LOGIN_id=request.session['lid'])
        return render(request,'User/view booked photographer.html',{'data':res})

def u_view_booking_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        res = Booking.objects.filter(USER__LOGIN_id=request.session['lid'],status='pending',date__range=[fdate,tdate])
        return render(request, 'User/view booked photographer.html', {'data': res})

def u_delete_booking(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Booking.objects.filter(pk=id).delete()
        return redirect('/myapp/u_view_booking/')



def User_Send_Feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'User/send feedback.html')

def User_Send_Feedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        feedback = request.POST['textfield']
        fobj = Feedback()
        from datetime import datetime
        datee = datetime.now().strftime('%Y%m%d')
        fobj.date = datee
        fobj.Feed_back = feedback
        fobj.type = 'User'
        fobj.LOGIN_id = Login.objects.get(pk=request.session['lid']).id
        fobj.save()
        return HttpResponse(
            '''<script> alert('Feedback Added..');window.location="/myapp/User_Send_Feedback/"</script>''')

def u_view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Feedback.objects.filter(LOGIN_id=Login.objects.get(pk=request.session['lid']))
        return render(request,'User/view feedback.html',{'data':res})

def u_view_feedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield2']
        res = Feedback.objects.filter(LOGIN_id=Login.objects.get(pk=request.session['lid']),date__range=[fdate,tdate])
        return render(request, 'Photographer/view feedback.html', {'data': res})

def u_delete_feedback(request,id):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res = Feedback.objects.filter(pk=id).delete()
        return redirect('/myapp/u_view_feedback/')


def User_Registration(request):
    return render(request,'User/signup_index.html')

def User_Registration_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield4']
    from datetime import datetime
    date ="user/"+ datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    photo = request.FILES['fileField']
    fs =FileSystemStorage()
    fn =fs.save(date,photo)
    path = fs.url(date)

    place = request.POST['textfield5']
    district = request.POST['textfield6']
    pin = request.POST['textfield7']
    password = request.POST['textfield9']
    confirm_password = request.POST['textfield10']

    ress=Login.objects.filter(username=email)
    if not ress.exists():

        if password == confirm_password:
            lobj = Login()
            lobj.username = email
            lobj.password = password
            lobj.type = 'user'
            lobj.save()

            uobj=Users()
            uobj.name=name
            uobj.email=email
            uobj.phone=phone
            uobj.gender=gender
            uobj.photo=path
            uobj.dob=dob
            uobj.place=place
            uobj.pin=pin
            uobj.district=district
            uobj.LOGIN=lobj
            uobj.save()
            return HttpResponse('''<script> alert('Registred Successfully..');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script> alert('Password does not match');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script> alert('Email is Already Exists..');window.location="/myapp/login/"</script>''')


def User_View_Profile(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Users.objects.get(LOGIN=request.session['lid'])
        return render(request,'User/view profile.html',{'data':res})

def User_Edit_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        res=Users.objects.get(LOGIN=request.session['lid'])
        return render(request,'User/edit profile.html',{'data':res})


def User_Edit_profile_post(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        name= request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        gender= request.POST['RadioGroup1']
        dob = request.POST['textfield4']
        place = request.POST['textfield5']
        district = request.POST['textfield6']
        pin = request.POST['textfield7']
        if 'fileField' in request.FILES:
            photo = request.FILES['fileField']
            if photo !="":
                from datetime import datetime
                date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                fs = FileSystemStorage()
                fn =  fs.save(date, photo)
                path =fs.url(date)
                res=Users.objects.filter(LOGIN=request.session['lid']).update(name=name,dob=dob,gender=gender,phone=phone,email=email,place=place,district=district,pin=pin,photo=path)
                return HttpResponse('''<script> alert('Updated..');window.location="/myapp/User_View_Profile/"</script>''')
        else:
            res = Users.objects.filter(LOGIN=request.session['lid']).update(name=name, dob=dob, gender=gender, phone=phone,
                                                                            email=email, place=place, district=district,
                                                                            pin=pin)
            return HttpResponse('''<script> alert('Updated..');window.location="/myapp/User_View_Profile/"</script>''')


def User_View_Booked_Photographer(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'User/view booked photographer.html')




def User_Home(request):
    if request.session['lid'] == '':
        return HttpResponse('Login Required')
    else:
        return render(request,'User/home_index.html')



