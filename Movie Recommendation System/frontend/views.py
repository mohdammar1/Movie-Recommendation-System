from django.shortcuts import render
from machinelearning.machinelearning import Recommend

def show():
        return Recommend.available()

def predict(viewed):
        return Recommend.run(viewed)
        
        
        
def home(request):
    if request.method=="POST":
        input=request.POST.get('input')
        post=predict(input)
        return render(request,"gui.html",{"post":post})
    else:
        pre=show()
        return render(request,"gui.html",{"pre":pre})
    


