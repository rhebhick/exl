from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def index(request):
    logout(request)
    request.session.flush()
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def courses(request):
    data=Classhave.objects.all()
    data2=Batch.objects.all()
    return render(request,'courses.html',{'data':data,'data2':data2})
def contact(request) :
    return render(request,'contact.html')
def signup(request):
    
    message=''
    if request.POST:
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        age=request.POST.get('age')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        name_father=request.POST.get('fathername')
        name_mother=request.POST.get('mothername')
        foccupation=request.POST.get('foccupation')
        moccupation=request.POST.get('moccupation')
        password=request.POST.get('password')
        checkpassword=request.POST.get('checkpassword')
        batch=request.POST.get('batch')
        to_class=request.POST.get('to_class')
        a=Batch.objects.get(id=batch)
        b=Classhave.objects.get(id=to_class)
        
        if password==checkpassword :
            if User.objects.filter(username=email).exists():
                messages.info(request, "user exist") 
                return redirect('/login')
            else:

                ta=User.objects.create_user(username=email,email=email,first_name=first_name,password=password)
                ta.save()
                te=Students.objects.create(first_name=first_name,last_name=last_name,email=email,dob=dob,father=name_father,mother=name_mother,father_occupation=foccupation,mother_occupation=moccupation,password=password,to_user=ta,to_class=b,batch=a)
                te.save()
                messages.info(request, "signup successfull") 
                return redirect('/')
                
        else:
            messages.info(request, "recheck your password") 
    data2=Batch.objects.all()
    data=Classhave.objects.all()
    return render(request,'signup.html',{'message':message,'data':data,'data2':data2})
@login_required(login_url=('/'))
def signupta(request):
    if request.POST:
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        age=request.POST.get('age')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        name_father=request.POST.get('fathername')
        name_mother=request.POST.get('mothername')
        foccupation=request.POST.get('foccupation')
        moccupation=request.POST.get('moccupation')
        password=request.POST.get('password')
        checkpassword=request.POST.get('checkpassword')
        batch=request.POST.get('batch')
        to_class=request.POST.get('to_class')
        a=Batch.objects.get(id=batch)
        b=Classhave.objects.get(id=to_class)
        if password==checkpassword :
            if User.objects.filter(username=email).exists():
                messages.info(request, "Already added")   
                return redirect("/adminhome")
            else:
                ta=User.objects.create_user(username=email,email=email,first_name=first_name,password=password)
                ta.save()
                te=Students.objects.create(first_name=first_name,last_name=last_name,email=email,dob=dob,father=name_father,mother=name_mother,father_occupation=foccupation,mother_occupation=moccupation,password=password,to_user=ta,to_class=b,batch=a)
                te.save()
                messages.info(request, "successfully added")   
                return redirect("/adminhome")
                
        else:
            messages.info(request, "recheck password")   
            return redirect("/adminhome")
    data2=Batch.objects.all()
    data=Classhave.objects.all()
    return render(request,'signup.html',{'data':data,'data2':data2})
def login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        check = authenticate(username=username,password=password)
        if check:
            auth_login(request,check)
            if check.is_superuser:
                request.session['type']='admin'
                return redirect("/adminhome")
            elif check.is_staff:
                data = Teacher.objects.get(to_user=check)
                cid = data.id
                request.session['uid'] = cid
                request.session['type']='employe'
                message='login successful'
                return redirect("/employehome")
            
            else:
                print(check)
                data = Students.objects.get(to_user=check)
                cid = data.id
                request.session['uid'] = cid
                request.session['type']='student'
                return redirect("/studenthome")
        else:
            messages.info(request, "Try again")   
            return redirect("/login")
    return render(request,'login.html')

@login_required(login_url='/')              
def adminhome(request):
    typ=request.session['type']
    if typ=='admin': 
        return render(request,'adminhome.html')
    else :
        return redirect('/login')
@login_required(login_url='/')
def add_department(request):
    typ=request.session['type']
    if typ=='admin':
        message=''
        if request.POST:
            d_name=request.POST.get("department")
            headid=request.POST.get('head')
            if d_name=='':
                 message='no input given'            
            else:
                if Department.objects.filter(name=d_name).exists():
                    message='this department already exist'
                else:
                    ta=Department.objects.create(name=d_name)
                    ta.save
                    te=Departandhead.objects.create(department=ta)
                    te.save()
                    message='added successfully'
        print(message)
        return render(request,"add_department.html",{'message':message})
@login_required(login_url='/')
def add_teacher(request):
    typ=request.session['type']
    if typ=='admin':
        data=Department.objects.all()
        if request.POST:
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('lastname')
            email=request.POST.get('email')
            dob=request.POST.get('dob')
            hse_board=request.POST.get('plustwo')
            hse_mark=request.POST.get('mark_plustwo')
            degree=request.POST.get('degree')
            score=request.POST.get('score')
            password=request.POST.get('password')
            checkpassword=request.POST.get('checkpassword')
            depart=request.POST.get('department')
            if password==checkpassword:
                if User.objects.filter(username=email).exists():
                    messages.info(request, "already added")
                    return redirect("/adminhome")
                else:
                    department=Department.objects.get(id=depart)
                    ta=User.objects.create_user(username=email,email=email,first_name=first_name,password=password,is_staff=1)
                    ta.save()
                    te=Teacher.objects.create(first_name=first_name,last_name=last_name,email=email,dob=dob,hse_board=hse_board,hse_percent=hse_mark,degree=degree,score=score,password=password,to_user=ta,department=department)
                    te.save()   
                    messages.info(request, "successfully added")   
                    return redirect("/adminhome")
        return render(request,"addteachers.html",{'data':data})
@login_required(login_url=('/'))
def incharge(request):
    typ=request.session['type']
    if typ=='admin': 
        option=''   
        data=Departandhead.objects.all()
        return render(request,"incharge.html",{'data':data})
@login_required(login_url=('/'))
def logoutFun(request):
    logout(request)
    request.session.flush()
    return redirect('/')
@login_required(login_url=('/'))
def incharge_edit(request):
    typ=request.session['type']
    if typ=='admin':
        data=Teacher.objects.all()
        id=request.GET['id']
        data2=Department.objects.get(id=id)
        if request.POST:
            name=request.POST.get('department')
            headid=request.POST.get('departhead')
            headname=Teacher.objects.get(id=headid)
            data2.name=name
            
            data2.save()
            messages.info(request, "successfully edited")   
            return redirect("/adminhome")
        return render(request,'incharge_edit.html',{'data':data,'data2':data2})
def incharge_add(request):
    typ=request.session['type']
    if typ=='admin':
        
        id=request.GET['id']
        data2=Departandhead.objects.get(id=id)
        data=Teacher.objects.filter(department=data2.department)
        if request.POST:
            headid=request.POST.get('departhead')
            headname=Teacher.objects.get(id=headid)
            data2.headname=headname
            data2.save()
            messages.info(request, "successfully added")   
            return redirect("/adminhome")
        return render(request,'incharge_add.html',{'data':data,'data2':data2})
@login_required(login_url=('/'))
def batches(request):
    typ=request.session['type']
    if typ=='admin':
        data=Batch.objects.all()
        for d in data:
            print(d.batch_starting_time)
        return render(request,'batches.html',{'data':data})
@login_required(login_url=('/'))
def add_batches(request):
    typ=request.session['type']
    if typ=='admin':
        if request.POST:
            batch_title=request.POST.get('batch_head')
            batch_starting_time=request.POST.get('stime')
            batch_ending_time=request.POST.get('etime')
            ta=Batch.objects.create(batch_title=batch_title,batch_starting_time=batch_starting_time,batch_ending_time=batch_ending_time)
            ta.save()
            messages.info(request, "successfully added")   
            return redirect('/adminhome')
        return render(request,'add_batches.html')
@login_required(login_url=('/'))
def classes(request):
    typ=request.session['type']
    if typ=='admin':
        data=Classhave.objects.all()
        return render(request,'classes.html',{'data':data})
@login_required(login_url=('/'))
def add_class(request):
    typ=request.session['type']
    if typ=='admin':
        if request.POST:
            clas=request.POST.get('classes')
            desc=request.POST.get('desc')
            if Classhave.objects.filter(classes=clas).exists():
                messages.info(request, "already exist") 
                return redirect('/adminhome')  
            else:
                ta=Classhave.objects.create(classes=clas,desc=desc)
                ta.save()
                messages.info(request, "successfully added")  
                return redirect('/adminhome') 
        return render(request,"add_class.html")
@login_required(login_url=('/'))
def class_edit(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        data=Classhave.objects.get(id=id)
        if request.POST:
            classes=request.POST.get('classes')
            desc=request.POST.get('desc')
            data.classes=classes
            data.desc=desc
            data.save()
            messages.info(request, "changes applied") 
            return redirect('/adminhome')
        return render(request,'class_edit.html',{'data':data})
@login_required(login_url=('/'))
def batch_edit(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        data=Batch.objects.get(id=id)
        if request.POST:
            batch_title=request.POST.get('title')
            batch_starting_time=request.POST.get('starting_time')
            batch_ending_time=request.POST.get('ending_time')
            data.batch_title=batch_title
            data.batch_starting_time=batch_starting_time
            data.batch_ending_time=batch_ending_time
            data.save()
            messages.info(request, "changes applied") 
            return redirect('/adminhome')
        return render(request,'batch_edit.html',{'data':data})
@login_required(login_url=('/'))
def delete_class(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        data=Classhave.objects.get(id=id)    
        data.delete()
        return redirect('/classes')
@login_required(login_url=('/'))
def delete_batch(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        data=Batch.objects.get(id=id)    
        data.delete()
        return redirect('/batches')
@login_required(login_url=('/'))
def viewfpage(request):
    typ=request.session['type']
    if typ=='admin':
        return render(request,'viewfpage.html')
@login_required(login_url=('/'))
def viewstudent(request):
    typ=request.session['type']
    a=''
    if typ=='admin':
        a='cmnadmin.html'
        data=Students.objects.all().order_by("to_class")
        batch=Batch.objects.all()
        clas=Classhave.objects.all()
        if request.POST:
            search = request.POST['search']
            data=Students.objects.filter(Q(first_name__contains=search)).order_by("to_class")
    elif typ=='employe':
        a='cmnemployee.html'
        data=Students.objects.all().order_by("to_class")
        batch=Batch.objects.all()
        clas=Classhave.objects.all()
        if request.POST:
            search = request.POST['search']
            data=Students.objects.filter(Q(first_name__contains=search)).order_by("to_class")
    else:
        return redirect('/')  
    return render (request,'viewstudent.html',{'data':data,'batch':batch,'clas':clas,'alink':a})
@login_required(login_url=('/'))
def editstudent(request):
    typ=request.session['type']
    if typ!='student':
        id=request.GET['id']
        data=Students.objects.get(id=id)
        udata=User.objects.get(id=data.to_user.id)
        batchdata=Batch.objects.all()
        classdata=Classhave.objects.all()
        
        if request.POST:
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('lastname')
            email=request.POST.get('email')
            name_father=request.POST.get('fathername')
            name_mother=request.POST.get('mothername')
            foccupation=request.POST.get('foccupation')
            moccupation=request.POST.get('moccupation')
            batch=request.POST.get('batch')
            to_class=request.POST.get('to_class')
            a=Batch.objects.get(id=batch)
            b=Classhave.objects.get(id=to_class)
            data.first_name=first_name
            data.last_name=last_name
            data.email=email
            data.father=name_father
            data.mother=name_mother
            data.father_occupation=foccupation
            data.mother_occupation=moccupation
            data.batch=a
            data.to_class=b          
            udata.first_name=first_name
            udata.last_name=last_name
            udata.email=email
            udata.username=email
            data.save()
            udata.save()
            messages.info(request,'editing success')
            return redirect('/viewstudent')
        return render(request,'edit_student.html',{'data':data,'batchdata':batchdata,'classdata':classdata})
@login_required(login_url=('/'))
def viewteacher(request):
    typ=request.session['type']
    if typ=='admin':
        data=Teacher.objects.all()
        return render (request,'viewteacher.html',{'data':data})
def editteacher(request):
    typ=request.session['type']
    if typ=='admin':
         id=request.GET['id']
         data=Teacher.objects.get(id=id)
         udata=User.objects.get(id=data.to_user.id)
         departdata=Department.objects.all()
        
         if request.POST:
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('lastname')
            email=request.POST.get('email')
            hse_board=request.POST.get('plustwo')
            hse_mark=request.POST.get('mark_plustwo')
            degree=request.POST.get('degree')
            score=request.POST.get('score')
            depart=request.POST.get('department')
            a=Department.objects.get(id=depart)
            data.first_name=first_name
            data.last_name=last_name
            data.email=email
            data.hse_board=hse_board
            data.hse_percent=hse_mark
            data.degree=degree
            data.score=a
            data.score=score
            data.department=a         
            udata.first_name=first_name
            udata.last_name=last_name
            udata.email=email
            udata.username=email
            data.save()
            udata.save()
            messages.info(request,'editing success')
            return redirect('/viewteacher')
         return render(request,'editteacher.html',{'data':data,'departdata':departdata})
@login_required(login_url=('/'))
def deletestudent(request):
    typ=request.session['type']
    if typ=='admin':
         id=request.GET['id']
         data=Students.objects.get(id=id)
         udata=User.objects.get(id=data.to_user.id)
         data.delete()
         udata.delete()
         return redirect('/viewstudent')
@login_required(login_url=('/'))
def deleteteacher(request):
    typ=request.session['type']
    if typ=='admin':
         id=request.GET['id']
         data=Teacher.objects.get(id=id)
         udata=User.objects.get(id=data.to_user.id)
         data.delete()
         udata.delete()
         return redirect('/viewteacher')
@login_required(login_url=("/"))
def msg_to_student(request):
    typ=request.session['type']
    alink=''
    print(typ,"*****************************************************************")
    
    if typ=='admin':
        data=To_msg.objects.filter(to_student=True)
        alink='cmnadmin.html'
        if request.POST:
            msg=request.POST.get('msg_s')
            ta=To_msg.objects.create(content=msg,to_student=True,to_teacher=False,to_admin=False,user_type='admin',sent_by='admin')
            ta.save()
        return render(request,'msg_to_student.html',{"data":data,'alink':alink})
    elif typ=='employe':
        data=To_msg.objects.filter(Q(to_student=True)&Q(user_type='teacher'))
        alink='cmnemployee.html'
        if request.POST:
            msg=request.POST.get('msg_s')
            id=request.session['uid']
            dt=Teacher.objects.get(id=id)
            name=dt.first_name +' '+ dt.last_name
            ta=To_msg.objects.create(content=msg,to_student=True,to_teacher=False,to_admin=False,user_type='teacher',sent_by=name)
            ta.save()
        return render(request,'msg_to_student.html',{"data":data,'alink':alink})
    return render(request,'msg_to_student.html')
@login_required(login_url=("/"))
def msg_to_admin(request):
    typ=request.session['type']
    alink=''    
    if typ=='employe':
        data=To_msg.objects.filter(to_admin=True)
        alink='cmnemployee.html'
        if request.POST:
            msg=request.POST.get('msg_s')
            id=request.session['uid']
            dt=Teacher.objects.get(id=id)
            name=dt.first_name +' '+ dt.last_name
            ta=To_msg.objects.create(content=msg,to_student=False,to_teacher=False,to_admin=True,user_type='teacher',sent_by=name)
            ta.save()
        return render(request,'msg_to_admin.html',{"data":data,'alink':alink})
    elif typ=='student':
        data=To_msg.objects.filter(Q(to_teacher=True)&Q(user_type='student'))
        alink='cmnstudent.html'
        if request.POST:
            msg=request.POST.get('msg_s')
            id=request.session['uid']
            dt=Students.objects.get(id=id)
            name=dt.first_name +' '+ dt.last_name
            ta=To_msg.objects.create(content=msg,to_student=True,to_teacher=False,to_admin=False,user_type='student',sent_by=name)
            ta.save()
        return render(request,'msg_to_admin.html',{"data":data,'alink':alink})
    return render(request,'msg_to_admin.html')
@login_required(login_url=("/"))
def msg_to_teacher(request):
    typ=request.session['type']
    if typ=='admin':
        data=To_msg.objects.filter(to_teacher=True)
        if request.POST:
            msg=request.POST.get('msg_s')
            ta=To_msg.objects.create(content=msg,to_teacher=True,to_student=False,to_admin=False,sent_by='admin')
            ta.save()
        return render(request,'msg_to_teacher.html',{'data':data})
@login_required(login_url=("/"))
def dltmsg(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        url=request.GET['url']
        data=To_msg.objects.get(id=id)
        data.delete()
        return redirect(f"/{url}")
    elif typ=='employe':
        id=request.GET['id']
        url=request.GET['url']
        data=To_msg.objects.get(id=id)
        data.delete()
        return redirect(f"/{url}")
@login_required(login_url=("/"))
def received_msg(request):
    typ=request.session['type']
    if typ=='admin':
        data=To_msg.objects.filter(to_admin=True)
        return render(request,'received_msg.html',{'data':data})
@login_required(login_url=('/'))
def employehome(request):
    typ=request.session['type']
    if typ=='employe':
        id=request.session['uid']
        data=Teacher.objects.get(id=id)
        msg_by_admin=To_msg.objects.filter(to_teacher=True)
        classes=Timetable.objects.filter(department__headname=id)
        return render(request,'employehome.html',{'msg_by_admin':msg_by_admin,'classes':classes})
@login_required(login_url=('/'))
def profile_tr(request):
    typ=request.session['type']
    if typ=='employe':
        id=request.session['uid']
        data=Teacher.objects.get(id=id)
        return render(request,'profile_tr.html',{'data':data})
@login_required(login_url=('/'))
def time_table(request):
    typ=request.session['type']
    if typ=='admin':
        data=Timetable.objects.all().order_by('classes')
        if request.POST:
            search = request.POST['search']
            data=Timetable.objects.filter(Q(classes__classes__contains=search) |  Q(department__department__name__contains=search)|Q(day__contains=search)).order_by("batch")
        return render(request,'time_table.html',{'data':data}) 
@login_required(login_url=('/'))
def add_table(request):
    typ=request.session['type']
    if typ=='admin':
        cla_ss=Classhave.objects.all()
        batch=Batch.objects.all()
        department=Departandhead.objects.all()
        if request.POST:
            cla_sss=request.POST.get('cla_ss')
            batchh=request.POST.get('batch')
            departmen=request.POST.get('department')
            day=request.POST.get('day')
            classes=Classhave.objects.get(id=cla_sss)
            batc=Batch.objects.get(id=batchh)
            depart=Departandhead.objects.get(id=departmen)
            print(depart,'***********************************************************')
            if Timetable.objects.filter(Q(classes=classes)&Q(batch=batc)&Q(day=day)).exists():
                 messages.info(request,'already have class on this time')
                 return redirect('/time_table')
            else:
                ta=Timetable.objects.create(classes=classes,batch=batc,department=depart,day=day)
                ta.save()
                messages.info(request,'successfully added')
                return redirect('/time_table')
        return render(request,'add_table.html',{'cla_ss':cla_ss,'batch':batch,'department':department})
@login_required(login_url=('/'))
def edit_table(request):
    typ=request.session['type']
    if typ=='admin':
        cla_ss=Classhave.objects.all()
        batch=Batch.objects.all()
        department=Departandhead.objects.all()
        id=request.GET['id']
        table=Timetable.objects.get(id=id)
        if request.POST:
            cla_sss=request.POST.get('cla_ss')
            batchh=request.POST.get('batch')
            departmen=request.POST.get('department')
            day=request.POST.get('day')
            classes=Classhave.objects.get(id=cla_sss)
            batc=Batch.objects.get(id=batchh)
            depart=Departandhead.objects.get(id=departmen)
            print(depart,'***********************************************************')
            table.classes=classes
            table.batch=batc
            table.department=depart
            table.day=day
            table.save()
            messages.info(request,'successfully edited')
            return redirect('/time_table')
        return render(request,'edit_table.html',{'table':table,'cla_ss':cla_ss,'batch':batch,'department':department})
@login_required(login_url=('/'))
def delete_table(request):
    typ=request.session['type']
    if typ=='admin':
        id=request.GET['id']
        data=Timetable.objects.get(id=id)
        data.delete()
        return redirect('/time_table')
@login_required(login_url=('/'))
def set_class(request):
    typ=request.session['type']
    if typ=='employe':
        id=request.session['uid']
        data=Timetable.objects.filter(department__headname=id)
        return render(request,'set_class.html',{'data':data})
@login_required(login_url=('/'))
def in_set_class(request):
    typ=request.session['type']
    if typ=='employe':
        id=request.GET['id']
        data=Timetable.objects.get(id=id)
        if request.POST:
            link=request.POST.get('link')
            data.classlink=link
            data.save()
            messages.info(request,'successfully added')
            return redirect('/set_class')
        return render(request,'in_set_class.html',{'data':data})

@login_required(login_url=('/'))
def delete_set_class(request):
    typ=request.session['type']
    if typ=='employe':
        id=request.GET['id']
        data=Timetable.objects.get(id=id)
        data.classlink=''
        data.save()
        return redirect('/set_class')
@login_required(login_url=('/'))
def studenthome(request):
    typ=request.session['type']
    if typ=='student':
        id=request.session['uid']
        data=Students.objects.get(id=id)
        classes=Timetable.objects.filter(classes=data.to_class)
        msg=To_msg.objects.filter(to_student=True)
        return render(request,'studenthome.html',{'data':data,'classes':classes,'msg':msg})
@login_required(login_url=('/'))
def s_timetable(request):
    typ=request.session['type']
    if typ=='student':
        id=request.session['uid']
        d=Students.objects.get(id=id)
        data=Timetable.objects.filter(classes=d.to_class)
        return render(request,'s_timetable.html',{'data':data})
@login_required(login_url=('/'))
def join_class(request):
    typ=request.session['type']
    if typ=='student':
        id=request.session['uid']
        d=Students.objects.get(id=id)
        data=Timetable.objects.filter(classes=d.to_class)
        return render(request,'join_class.html',{'data':data})
@login_required(login_url=('/'))
def privacypolicy(request):
    typ=request.session['type']
    alink=''
    if typ :
        if typ=='student':
            alink='cmnstudent.html'
        elif typ=='admin':
            alink='cmnadmin.html'
        elif typ=='employe':
            alink='cmnemployee.html'
    return render(request,'privacypolicy.html',{'alink':alink})
def cprivacypolicy(request):
    alink='cmnpage.html'
    return render(request,'privacypolicy.html',{'alink':alink})

