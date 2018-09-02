from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #user has info and wants account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Sasswords need to match!'})
    else:
        #user wants to enter info
        return render(request, 'signup.html')

def login(request):
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

