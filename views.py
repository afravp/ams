from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from admin_master.models import Subject,Class,Division,Department,Designation,Qualification,Employee_Category
from admin_employee.models import adminemp,scd,empdesig,empdpt,salary
# Create your views here.
def employee_reg(request):
    sub=Subject.objects.filter(status=1)
    cla=Class.objects.filter(status=1)
    div=Division.objects.filter(status=1)
    qul=Qualification.objects.filter(status=1)
    desg=Designation.objects.filter(status=1)
    dep=Department.objects.filter(status=1)
    emp=Employee_Category.objects.filter(status=1)
    if request.method == 'POST':
        name = request.POST.get('emp_name')
        dob = request.POST.get('dob')
        department = request.POST.get('department')
        jdate = request.POST.get('join_date')

        # qr_data = f"Name: {name}\nDOB: {dob}\nDepartment: {department}\nJoin Date: {jdate}"

        # Generate QR code image
        # qr = qrcode.QRCode(
        #     version=1,
        #     error_correction=qrcode.constants.ERROR_CORRECT_L,
        #     box_size=10,
        #     border=4,
        # )
        # qr.add_data(qr_data)
        # qr.make(fit=True)
        # img = qr.make_image(fill_color="black", back_color="white")

        # # Save the QR code image to a BytesIO object
        # qr_image_io = BytesIO()
        # img.save(qr_image_io, format='PNG')
        # qr_image_io.seek(0)

        # # Create an InMemoryUploadedFile from BytesIO
        # qr_image = InMemoryUploadedFile(
        #     file=qr_image_io,
        #     field_name=None,
        #     name=f'qr_code_{name}.png',
        #     content_type='image/png',
        #     size=qr_image_io.tell(),
        #     charset=None,
        # )
        # Extract data from the form
        emp_name = request.POST.get('emp_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        employee_area = request.POST.get('employee_area')
        emp_id=employee_area.split("_")[0]
        empc=get_object_or_404(Employee_Category,id=emp_id)
        qualification = request.POST.get('qualification')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        salary_amount = request.POST.get('salary')
        join_date = request.POST.get('join_date')
        # photo = request.FILES.get('photo')

        # Create and save the employee instance
        new_employee = adminemp(
            empcatid=empc,
            empname=emp_name,
            dob=dob,
            gender=gender,
            mobile=mobile,
            email=email,
            address=address,
            joindate=join_date,
            qualifid_id=qualification,
            desigid_id=designation,
            dptid_id=department,
            salary=salary_amount,
            # photo=photo,
            # barcode=qr_image,
        )
        new_employee.save()

         # Handle empdesig
        empdesig.objects.create(
            empid=new_employee,
            desigid_id=request.POST.get('designation'),
            from_date=request.POST.get('join_date'),
        )

         # Handle empdpt
        empdpt.objects.create(
            empid=new_employee,
            dptid_id=request.POST.get('department'),
            from_date=request.POST.get('join_date'),
        
        )

        # Handle salary
        salary.objects.create(
            empid=new_employee,
            salary=request.POST.get('mobile'),
            from_date=request.POST.get('join_date'),
        )

        # Handle scd
        class_ids = request.POST.getlist('class_ids[]')
        division_ids = request.POST.getlist('division_ids[]')
        subject_ids = request.POST.getlist('subject_ids[]')


        for class_id, division_id, subject_id in zip(class_ids, division_ids, subject_ids):
            scd.objects.create(
                empid=new_employee,
                classid_id=class_id,
                divid_id=division_id,
                subid_id=subject_id
            )
        employee_data=adminemp.objects.filter(status=True)
        return render(request,'get_employee_details.html',{'employee_data':employee_data})
        # Handle other related models like scd, empdesig, empdpt, salary as neede
    return render(request,'employee_registration.html',{'subject':sub,'class':cla,'division':div,'department':dep,'designation':desg,'qualification':qul,'employee':emp})

def select_subject(request):
    class_id=request.GET['classid']
    clas=get_object_or_404(Class,id=class_id,status=1)
    subject=list(Subject.objects.filter(classes=clas,status=1).values('id','sub_name'))
    res={'subjects':subject}
    return JsonResponse(res)