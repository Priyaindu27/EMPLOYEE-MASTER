from django.shortcuts import render,HttpResponseRedirect,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.template import loader
from .models import *
from .forms import *

# Create your views here.
def smms(request):
    return render(request,'home.html')
def insert(request):
    return render(request,'insert.html')
def display_batch(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template("batch_master.html")
    context={
        'data':allbatch
    }
    return HttpResponse(temp.render(context,request))
def batch_insert(request):
    context={}
    context['form']=BatchMaster()
    return render(request,"batch_insert.html",context)
def home_view(request):
    context={}
    context['form']=BatchMasterForm()
    return render(request,"home_view.html",context)

def displaybatchinput(request):
    return render(request, 'batch_entry.html')
def process_batch_entry(request):
    if request.method =='POST':
        batchno_inp = request.POST.get('batchno')
        batchid_inp = request.POST.get('batchid')
        ob=BatchMaster(batchno=batchno_inp , batchid=batchid_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("Inavalid request method.")

def batch_update(request, id):
    context ={}
    obj = get_object_or_404(BatchMaster, id = id)
    form = BatchForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_batch/") 
    context["form"] = form 
    return render(request, "batch_update.html", context)
def b_delete(request,pk):
    BatchMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_batch/") 
def batch_delete(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template("batch_delete1.html")
    context={
        'data':allbatch
        }
    return HttpResponse(temp.render(context,request))
def search_view_batch(request):
    if request.method == 'GET':
        form = BatchMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = BatchMaster.objects.filter(batchno=query)  
        else:
            results = None
    else:
        form = BatchMasterForm()
        results = None
    
    return render(request, 'search_results_batch.html', {'form': form, 'results': results})
def edit_batch(request, id):
    obj=get_object_or_404(BatchMaster,pk=id)
    if request.method == 'POST':
        form = BatchForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('batch_all_details')
    else:
        form = BatchForm(instance=obj)
    return render(request,'edit_batch.html',{'form':form})
def batch_detail(request,id):
    obj=get_object_or_404(BatchMaster,pk=id)
    return render(request,'batch_detail.html',{'batch':batch})
def batch_all_details(request):
    ob=BatchMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('batch_all_details.html')
    return HttpResponse(temp.render(context,request))



def display_student(request):
    allstudent=StudentMaster.objects.all().values()
    temp=loader.get_template("student_master.html")
    context={
        'data':allstudent
    }
    return HttpResponse(temp.render(context,request))
def student_insert(request):
    context={}
    context['form']=StudentForm()
    return render(request,"student_insert.html",context)
def process_student_entry(request):
    if request.method=='POST':
        studentname_inp=request.POST.get('studentname')
        studentregno_inp=request.POST.get('studentregno')
        ob=StudentMaster(studentname=studentname_inp,studentregno=studentregno_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("INVALID REQUEST")
def displaystudentinput(request):
    return render(request,"student_entry.html")
def student_update(request, id):
    context ={}
    obj = get_object_or_404(StudentMaster, id = id)
    form = StudentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_student/") 
    context["form"] = form 
    return render(request, "student_update.html", context)
def student_delete(request, id):
    context ={}
    obj = get_object_or_404(StudentMaster, id = id) 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/app1/display_student/") 
    return render(request, "student_delete.html", context)


def display_course(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template("course_master.html")
    context={
        'data':allcourse
    }
    return HttpResponse(temp.render(context,request))
def course_insert(request):
    context={}
    context['form']=CourseForm()
    return render(request,"course_insert.html",context)
def process_course_entry(request):
    if request.method=='POST':
        course_inp=request.POST.get('course')
        courseid_inp=int(request.POST.get('courseid'))
        ob=CourseMaster(course=course_inp,courseid=courseid_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("INVALID REQUEST")
def displaycourseinput(request):
    return render(request,"course_entry.html")
def course_update(request, id):
    context ={}
    obj = get_object_or_404(CourseMaster, id = id)
    form = CourseForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_course/") 
    context["form"] = form 
    return render(request, "course_update.html", context)
def c_delete(request,pk):
    CourseMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_course/") 
def course_delete(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template("course_delete1.html")
    context={
        'data':allcourse
        }
    return HttpResponse(temp.render(context,request))
def search_view_course(request):
    if request.method == 'GET':
        form = CourseMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = CourseMaster.objects.filter(course=query)  
        else:
            results = None
    else:
        form = CourseMasterForm()
        results = None
    
    return render(request, 'search_results_course.html', {'form': form, 'results': results})
def edit_course(request, id):
    obj=get_object_or_404(CourseMaster,pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('course_all_details')
    else:
        form = CourseForm(instance=obj)
    return render(request,'edit_course.html',{'form':form})
def course_detail(request,id):
    obj=get_object_or_404(CourseMaster,pk=id)
    return render(request,'course_detail.html',{'course':course})
def course_all_details(request):
    ob=CourseMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('course_all_details.html')
    return HttpResponse(temp.render(context,request))


def display_sem(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template("sem_master.html")
    context={
        'data':allsem
    }
    return HttpResponse(temp.render(context,request))
def sem_insert(request):
    context={}
    context['form']=SemForm()
    return render(request,"sem_insert.html",context)
def process_sem_entry(request):
    if request.method=='POST':
        sem_inp=request.POST.get('sem')
        semid_inp=int(request.POST.get('semid'))        
        ob=SemMaster(sem=sem_inp,semid=semid_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("INVALID REQUEST")
def displayseminput(request):
    return render(request,"sem_entry.html")
def sem_update(request, id):
    context ={}
    obj = get_object_or_404(SemMaster, id = id)
    form = SemForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_sem/") 
    context["form"] = form 
    return render(request, "sem_update.html", context)
def s_delete(request,pk):
    SemMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_sem/") 
def sem_delete(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template("sem_delete1.html")
    context={
        'data':allsem
        }
    return HttpResponse(temp.render(context,request))
def search_view_sem(request):
    if request.method == 'GET':
        form = SemMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = SemMaster.objects.filter(sem=query)  
        else:
            results = None
    else:
        form = SemMasterForm()
        results = None
    
    return render(request, 'search_results_sem.html', {'form': form, 'results': results})
def edit_sem(request, id):
    obj=get_object_or_404(SemMaster,pk=id)
    if request.method == 'POST':
        form = SemForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('sem_all_details')
    else:
        form = SemForm(instance=obj)
    return render(request,'edit_sem.html',{'form':form})
def sem_detail(request,id):
    obj=get_object_or_404(SemMaster,pk=id)
    return render(request,'sem_detail.html',{'sem':sem})
def sem_all_details(request):
    ob=SemMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('sem_all_details.html')
    return HttpResponse(temp.render(context,request))



def display_paper(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template("paper_master.html")
    context={
        'data':allpaper
    }
    return HttpResponse(temp.render(context,request))
def paper_insert(request):
    context={}
    context['form']=PaperForm()
    return render(request,"paper_insert.html",context)
def process_paper_entry(request):
    if request.method=='POST':
        papername_inp=request.POST.get('papername')
        papercode_inp=request.POST.get('papercode')
        papertype_inp=request.POST.get('papertype')
        papersheetname_inp=request.POST.get('papersheetname')
        ob=PaperMaster(papername=papername_inp,papercode=papercode_inp,papertype=papertype_inp,papersheetname=papersheetname_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("INVALID REQUEST")
def displaypaperinput(request):
    return render(request,"paper_entry.html")
def paper_update(request, id):
    context ={}
    obj = get_object_or_404(PaperMaster, id = id)
    form = PaperForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_paper/") 
    context["form"] = form 
    return render(request, "paper_update.html", context)
def p_delete(request,pk):
    PaperMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_paper/") 
def paper_delete(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template("paper_delete1.html")
    context={
        'data':allpaper
        }
    return HttpResponse(temp.render(context,request))
def search_view_paper(request):
    if request.method == 'GET':
        form = PaperMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = PaperMaster.objects.filter(papercode=query)  
        else:
            results = None
    else:
        form = PaperMasterForm()
        results = None
    
    return render(request, 'search_results_paper.html', {'form': form, 'results': results})
def edit_paper(request, id):
    obj=get_object_or_404(PaperMaster,pk=id)
    if request.method == 'POST':
        form = PaperForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('paper_all_details')
    else:
        form = PaperForm(instance=obj)
    return render(request,'edit_paper.html',{'form':form})
def paper_detail(request,id):
    obj=get_object_or_404(PaperMaster,pk=id)
    return render(request,'paper_detail.html',{'paper':paper})
def paper_all_details(request):
    ob=PaperMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('paper_all_details.html')
    return HttpResponse(temp.render(context,request))



def display_exam(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template("exam_master.html")
    context={
        'data':allexam
    }
    return HttpResponse(temp.render(context,request))
def exam_insert(request):
    context={}
    context['form']=ExamForm()
    return render(request,"exam_insert.html",context)
def process_exam_entry(request):
    if request.method=='POST':
        examid_inp=int(request.POST.get('examid'))
        examtype_inp=request.POST.get('examtype')
        ob=ExamMaster(examid=examid_inp,examtype=examtype_inp)
        ob.save()
        return redirect('insert')
    else:
        return HttpResponse("INVALID REQUEST")
def displayexaminput(request):
    return render(request,"exam_entry.html")
def exam_update(request, id):
    context ={}
    obj = get_object_or_404(ExamMaster, id = id)
    form = ExamForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_exam/") 
    context["form"] = form 
    return render(request, "exam_update.html", context)
def e_delete(request,pk):
    ExamMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_exam/") 
def exam_delete(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template("exam_delete1.html")
    context={
        'data':allexam
        }
    return HttpResponse(temp.render(context,request))
def search_view_exam(request):
    if request.method == 'GET':
        form = ExamMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = ExamMaster.objects.filter(examtype=query)  
        else:
            results = None
    else:
        form = ExamMasterForm()
        results = None
    
    return render(request, 'search_results_exam.html', {'form': form, 'results': results})
def edit_exam(request, id):
    obj=get_object_or_404(ExamMaster,pk=id)
    if request.method == 'POST':
        form = ExamForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('exam_all_details')
    else:
        form = ExamForm(instance=obj)
    return render(request,'edit_exam.html',{'form':form})
def exam_detail(request,id):
    obj=get_object_or_404(ExamMaster,pk=id)
    return render(request,'exam_detail.html',{'exam':exam})
def exam_all_details(request):
    ob=ExamMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('exam_all_details.html')
    return HttpResponse(temp.render(context,request))



def display_transaction(request):
    alltrans=Transaction.objects.all().values()
    temp=loader.get_template("transaction_master.html")
    context={
        'data':alltrans
    }
    return HttpResponse(temp.render(context,request))
def transaction_insert(request):
    context={}
    context['form']=TransactionForm()
    return render(request,"transaction_insert.html",context)
def process_transaction_entry(request):
    if request.method=='POST':
        '''batch_inp=request.POST.get('batch')
        course_inp=request.POST.get('course')
        semester_inp=request.POST.get('semester')
        exam_type_inp=request.POST.get('exam_type')
        registernumber_inp=int(request.POST.get('registernumber'))
        name_inp=request.POST.get('name')
        papername_inp=request.POST.get('papername')
        student_reg_no_inp=request.POST.get('student_reg_no')
        student_name_inp=request.POST.get('student_name') 
        paper_code_inp=request.POST.get('paper_code') '''       
        marks_inp=int(request.POST.get('marks'))
        #ob=Transaction(batch=batch_inp,course=course_inp,semester=semester_inp,exam_type=exam_type_inp,registernumber=registernumber_inp,name=name_inp,papercode=papercode_inp,papername=papername_inp,marks=marks_inp)
        ob=Transaction( marks=marks_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displaytransactioninput(request):
    return render(request,"transaction_entry.html")
def transaction_update(request, id):
    context ={}
    obj = get_object_or_404(Transaction, id = id)
    form = TransactionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/display_transaction/") 
    context["form"] = form 
    return render(request, "transaction_update.html", context)
def transaction_delete(request, id):
    context ={}
    obj = get_object_or_404(Transaction, id = id) 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/app1/display_transaction/") 
    return render(request, "transaction_delete.html", context)


def insert_employee(request):
    context={}
    ob_form=EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return redirect('insert')
    context['form']=ob_form
    return render(request,"insert_employee.html",context)

def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("view_employee.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))


def delete_employee(request,pk):
    EmployeeModel.objects.get(id=pk).delete()
    return render(request,"delete_employee.html")

def update_employee(request, pk):
    obe=get_object_or_404(EmployeeModel,id=pk)
    if request.method == 'POST':
        obf = EmployeeForm(request.POST ,instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('update_view_employee1')
    else:
        formdata = EmployeeForm(instance=obe)
    return render(request,'update_employee.html',{'form':formdata})

def update_view_employee1(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("view_employee1.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))
def delete_view_employee2(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("view_employee2.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))

def search_employee(request):
    if request.method == 'GET':
        form = EmployeeSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results =EmployeeModel.objects.filter(first_name=query)  
        else:
            results = None
    else:
        form =EmployeeSearchForm()
        results = None
    
    return render(request, 'search_employee.html', {'form': form, 'results': results})
