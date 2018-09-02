from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        #user has info and wants account (if would be GET its just that user wants something from the site
        #e.g. entering url to browser and pressing enter
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['username'] , request.POST['password1'])
                login(request, user)
                print (user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Sasswords need to match!'})
    else:
        #user wants to enter info (e.g. updating browser page)
        return render(request, 'signup.html')

def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        print (user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    return render(request, 'signup.html')

#HOW TRY & EXCEPT WORKS
'''If an error is encountered, a try block code execution is stopped and transferred
down to the except block. 

In addition to using an except block after the try block, you can also use the
finally block. 

The code in the finally block will be executed regardless of whether an exception
occurs.


except ValueError:
    print('Non-numeric data found in the file.')

except:
    print('An error occured.')    
    '''

