from django.shortcuts import render

def app(reqeust):
    return render(reqeust, 'user/app.html',)
