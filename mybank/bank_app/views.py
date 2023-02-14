from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Credential,Customer,Transaction,contact_us
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Signup, Transfor,Login_form,Customer_Contactus
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .generate import generate_customer_id_acc_id,generate_transaction_id
import logging
import datetime
from . password_hash import hash_password,unhash_password
logger = logging.getLogger(__name__)
logger = logging.getLogger('info_logger')
logger_warning = logging.getLogger('warning_logger')
logger_error = logging.getLogger('error_logger')


#------------------------ index page starts------------------------------
def index(request):
    try:
        logger.info('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
        return redirect('bankapp/')
    except Exception as err:
        logger_error.error(err)
        return redirect(error_404)
#------------------------ index page ends------------------------------



#------------------------ landing page starts------------------------------
def landingpage(request):
    try:
        logger.info(' landingpage was accessed at '+str(datetime.datetime.now())+' hours!')
        if request.method == 'POST':
            form = Customer_Contactus(request.POST)
            # for contact us
            if form.is_valid():
                
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                contact_details = contact_us(name=name,email=email,message=message)
                messages.success(request,f'Hi {name}, we will contact you shortly!')
                logger.info('successfully details saved for contact us'+str(datetime.datetime.now())+' hours!')
                return redirect(landingpage)

            else:
                for error in list(form.errors.values()):
                    messages.error(request, error) 
                logger_error.error('Failed to save data'+str(datetime.datetime.now())+' hours!')
                return redirect(landingpage)
        else:
            form = Customer_Contactus()
            return render(request,'landingpage.html',{'form':form})
    except Exception as err:
        logger_error.error('Failed to load landing page'+str(datetime.datetime.now())+' hours!')
        return redirect(error_404)
#------------------------ landing page ends------------------------------
    


#------------------------signup page starts------------------------------
def mysignup(request):
    try:
        logger.info('Signup was accessed at '+str(datetime.datetime.now())+' hours!')
        if request.method =='POST':
            reg = Signup(request.POST)
            if reg.is_valid():
                first_name = reg.cleaned_data['first_name']
                middle_name = reg.cleaned_data['middle_name']
                last_name = reg.cleaned_data['last_name']
                resident_addr = reg.cleaned_data['resident_addr']
                office_addr = reg.cleaned_data['office_addr']
                phone_no = reg.cleaned_data['phone_no']
                email = reg.cleaned_data['email']
                password = reg.cleaned_data['password']
                repassword = reg.cleaned_data['repassword']
                Balance = reg.cleaned_data['Balance']
                # hashing the password
                get_data = generate_customer_id_acc_id()
                cust_id = get_data[0]
                acc_no = get_data[1]
                user = User.objects.create_user(username=cust_id,password=password)
                user.save()
                password = hash_password(password)
                cust = Customer(customer_id = cust_id,account_number=acc_no,first_name=first_name,middle_name=middle_name,last_name=last_name,resident_address=resident_addr,office_address=office_addr,phone_number=phone_no,email=email,Balance=Balance)
                cust.save()
                logger.info('Customer Data successfully saved')
                cred = Credential(customer_id =cust,password = password)
                cred.save()
                logger.info('Credentials Data successfully saved')
                messages.success(request,cust_id)
                return redirect(mylogin)
            else:
                for error in list(reg.errors.values()):
                    messages.error(request, error)
                logger_error.error(error)
                return redirect(mysignup)
        else:
            reg = Signup()
            return render(request,'mysignup.html',{'reg':reg})
    except Exception as err:
        logger_error.error(err)
        return redirect(error_404)

#------------------------signup page ends------------------------------



#------------------------login page starts------------------------------

def mylogin(request):
    try:
        if request.method=='POST':
            form = Login_form(request.POST)
            if form.is_valid():
                cust_id = form.cleaned_data['cust_id']
                password = form.cleaned_data['password']
                # password = unhash_password(cust_id,password)
                user = authenticate(username = cust_id, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"you have been successfully logged in")
                    logger.info("successfully logged in")
                    return redirect("homepage",cust_id)
                else:
                    logger_error.error("Inavlid credentials")
                    messages.error(request,"Inavlid credentials")
                    return redirect(mylogin)

            else:
                for error in list(form.errors.values()):
                    messages.error(request, error) 
                logger_error.error(error)
                return redirect(mylogin)
        else:
            form = Login_form()
            for error in list(form.errors.values()):
                    messages.error(request, error)
            return render(request,'mylogin.html',{'form':form})
    except Exception as err:
        logger_error.error(err)
#------------------------login page ends------------------------------

#------------------------logout page starts------------------------------
def logoutpage(request):
    try:
        logout(request)
        messages.success(request,'you have been successfully logged out')
        logger.info('user successfully logged out')
        return redirect(mylogin)
    except Exception as err:
        logger_error.error(err)
        redirect(error_404)
    # return render(request,'landingpage.html')
#------------------------logout page ends------------------------------



#------------------------error pages starts------------------------------
def error_404(request):
    return render(request,'error_404.html')
#------------------------error page ends------------------------------




#------------------------user home page starts------------------------------

@login_required(login_url='bankapp/homepage/<cust_id>')
def homepage(request,cust_id):
    try:
        if request.method =='POST':
            customers = Customer.objects.all().values()
            trans_form = Transfor(request.POST)
            if trans_form.is_valid():
                transfer_to_account_no = trans_form.cleaned_data['transfer_to']
                amount = trans_form.cleaned_data['amount']
                flag = False
                trans_flag = False
                this_cust = None
                trans_cust = None
                for customer in customers:
                    if customer['account_number'] == transfer_to_account_no:
                        trans_flag = True
                        break

                for customer in customers:
                    if customer['customer_id'] == cust_id and int(customer['Balance'])>= int(amount):
                        this_cust = customer
                        flag = True
                        break
                if flag and trans_flag:
                    s_ac = ""
                    gen_trans_id = generate_transaction_id()
                    for customer in customers:
                        if customer['customer_id']==cust_id:
                            Customer.objects.filter(customer_id = customer['customer_id']).update(Balance = str(int(customer['Balance']) - int(amount)))
                            s_ac = customer['account_number']
                            new_amount = "-"+ amount
                            transaction = Transaction(customer_id_id = this_cust['customer_id'],transaction_id = gen_trans_id+'S',transaction_amount = new_amount,transaction_account =transfer_to_account_no)
                            transaction.save()
                            
                            break
                    for customer in customers:
                        if customer['account_number']==transfer_to_account_no:
                            trans_cust = customer
                            Customer.objects.filter(customer_id = customer['customer_id']).update(Balance = str(int(customer['Balance']) + int(amount)))
                            new_new_amt = "+" + amount
                            transaction = Transaction(customer_id_id = trans_cust['customer_id'],transaction_id = gen_trans_id+'R',transaction_amount =new_new_amt,transaction_account = s_ac)
                            transaction.save()
                            break
                    logger.info('Transaction completed')
                    messages.success(request,'Transaction completed')
                    return redirect(homepage,cust_id)
                else:
                    if not trans_flag:
                        logger.error('Invalid account details')
                        messages.error(request,'Invalid account details')
                        return redirect(homepage,cust_id)
                        
                    elif not flag:
                        logger.error('Insufficent bank Balance')
                        messages.error(request,'Insufficent bank Balance')
                        return redirect(homepage,cust_id)
                                           
        else:    
            trans_form = Transfor()
            data = Customer.objects.get(pk = cust_id)
            trans_all_data = Transaction.objects.all().values()
            trans_data = []
            for dt in trans_all_data:
                temp = []
                if dt['customer_id_id']== cust_id:
                    temp.append(dt['customer_id_id'])
                    temp.append(dt['transaction_id'])
                    temp.append(dt['transaction_account'])
                    temp.append(dt['transaction_amount'])
                    trans_data.append(temp)
                
            context = {'data':data,'trans_form': trans_form,'trans_data':trans_data}
            logger.info('transaction data logged in successfully')
            return render(request,'homepage.html',context)
    
    except Exception as err:
        logger_error.error(err)
        return redirect(error_404)
#------------------------user home page ends------------------------------

