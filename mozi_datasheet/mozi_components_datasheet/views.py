from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item, TransactionList, TransactionList1
import datetime
from django.utils.dateparse import parse_datetime

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Stocks(request):

    user_name = str(request.POST['user_name'])
    password1 = str(request.POST['password1'])

    user_name1= "MOZI"
    password2= "2020"

    curr_dt= str(datetime.datetime.now())
    curr_dt= parse_datetime(curr_dt)

    items= Item.objects.all()
    ex_num= 0
    in_num= 0

    if user_name== user_name1:
        if password1== password2:
            return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items, 'ex_num': ex_num, 'in_num': in_num})
        else:
            messages.info(request, "PASSWORD MISMATCH!")
            return redirect('index')

    else:
        messages.info(request, "USERNAME INCORRECT!")
        return redirect('index')



def DetailsTransaction(request):

    i_name = str(request.GET['i_name'])
    i_name= i_name.title()
    items= Item.objects.all()
    transactions= TransactionList.objects.all().order_by('-wid_time')
    transactions1= TransactionList1.objects.all().order_by('-wid_time')
    for item in items:
        if i_name==item.id:
            
            i_stock= item.stock
            i_tested= item.tested
            i_not_tested= item.not_tested

        else:
            messages.info(request, "ITEM NOT FOUND")
            return redirect('stocks')


    return render(request, 'details_transaction.html', {'items': items, 'i_tested':i_tested, 'i_not_tested':i_not_tested, 'transactions':transactions, 'transactions1':transactions1, 'i_name': i_name, 'i_stock': i_stock})

def export1(request):

    i_name = str(request.POST['i_name'])
    i_name= i_name.title()
    items= Item.objects.all()
    
    for item in items:
        if i_name==item.id:
            
            i_stock= item.stock
            i_tested= item.tested
            
    

    return render(request, 'export.html', {'i_name': i_name, 'i_stock': i_stock, 'i_tested': i_tested})

def import1(request):

    i_name = str(request.POST['i_name'])
    i_name= i_name.title()
    items= Item.objects.all()
    for item in items:
        if i_name==item.id:
            
            i_stock= item.stock
            

    return render(request, 'import.html', {'i_name': i_name, 'i_stock': i_stock})

def exporting(request):

    pw1= '2020'

    ex_num= int(request.POST['ex_num'])
    i_name= str(request.POST['i_name'])
    your_name=str(request.POST['your_name'])
    your_purp=str(request.POST['your_purp'])
    curr_dt= str(datetime.datetime.now())
    curr_dt= parse_datetime(curr_dt)
    pw2= str(request.POST['password'])


    if pw1==pw2:

        

        transaction_list= TransactionList(name=i_name, wid_name=your_name, wid_time=curr_dt, wid_quant=ex_num, wid_purp=your_purp)
        transaction_list.save()


        



        items= Item.objects.all()
        for item in items:
            if i_name==item.id:

                if ex_num<item.stock:
                
                    item.stock = item.stock-ex_num
                    item.tested = item.tested-ex_num

                    item.save()

                else:
                    
                    item.stock = 0

                    item.save()

        

        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items})

    else:
        ex_num=0
        in_num=0

    

        messages.info(request, "PASSWORD MISMATCH!")
        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items, 'ex_num': ex_num, 'in_num': in_num})

def importing(request):

    pw1= '2020'

    in_num= int(request.POST['in_num'])
    i_name= str(request.POST['i_name'])
    your_name=str(request.POST['your_name'])
    your_purp=str(request.POST['your_purp'])
    curr_dt= str(datetime.datetime.now())
    curr_dt= parse_datetime(curr_dt)
    pw2= str(request.POST['password'])

    if pw1==pw2:

        transaction1_list= TransactionList1(name=i_name, wid_name=your_name, wid_time=curr_dt, wid_quant=in_num, wid_purp=your_purp)
        transaction1_list.save()


        items= Item.objects.all()
        for item in items:
            if i_name==item.id:
                
                item.stock = item.stock+in_num
                item.not_tested = item.not_tested+in_num
                
                item.save()


        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items})

    else:

        messages.info(request, "PASSWORD MISMATCH!")

        items= Item.objects.all()

        ex_num=0
        in_num=0
        
        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items, 'ex_num': ex_num, 'in_num': in_num})

def Test(request):
    
    i_name = str(request.POST['i_name'])
    i_name= i_name.title()
    items= Item.objects.all()
    for item in items:
        if i_name==item.id:
            
            i_tested= item.tested
            i_not_tested= item.not_tested

    return render(request, 'test.html', {'i_name':i_name, 'i_tested': i_tested, 'i_not_tested': i_not_tested})

def Testing(request):

    pw1= '2020'

    ex_num=0
    in_num=0

    t_num= int(request.POST['t_num'])
    i_name= str(request.POST['i_name'])
    your_name=str(request.POST['your_name'])
    pw2= str(request.POST['password'])
    items= Item.objects.all()
    if pw1==pw2:
        for item in items:
            if i_name== item.id:
                item.tested= item.tested+t_num
                item.not_tested= item.not_tested-t_num
                item.save()
        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items})
    else:

        messages.info(request, "PASSWORD MISMATCH!")

        return render(request, 'stocks.html', {'curr_dt':curr_dt, 'items': items, 'ex_num': ex_num, 'in_num': in_num})