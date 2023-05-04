from django.http import *
from django.shortcuts import *


def homepage(request):
    if request.method=='POST':
        num=request.POST.get('hect')

        hecAnswer={
            'answer' : [
                            f"{(eval(num) * 6.25)} Bigha.",
                            f"{(eval(num) * 17424 * 6.25)} SqrFeet.",
                            f"{(eval(num) * 1600 * 6.25)} SqrMtr.",
                            f"{(eval(num) * 20 * 6.25)} Biswa.",
                            f"{(eval(num) * 16 * 6.25)} Aer."
                           ],
            'num':eval(num)
            }

        return render(request, "index.html",hecAnswer)
    else:
        return render(request, "index.html")




def bighaPage(request):
    if request.method=='POST':
        num=request.POST.get('bigha')

        bigAnswer={
            'answer' : [
                            f"{(eval(num) * 0.16)} Hect.",
                            f"{(eval(num) * 17424)} SqrFeet.",
                            f"{(eval(num) * 1600)} SqrMtr.",
                            f"{(eval(num) * 20)} Biswa.",
                            f"{(eval(num) * 16)} Aer."
                            ],
            'num': eval(num)
            }

        return render(request, "bigha.html",bigAnswer)
    else:
        return render(request, "bigha.html")

def feetPage(request):
    if request.method=='POST':
        num=request.POST.get('foot')

        feetAnswer={
            'answer' : [
                            f"{(eval(num) / 108900)} Hect.",
                            f"{(eval(num) / 17424)} Bigha.",
                            f"{(eval(num) / 10.89)} SqrMtr.",
                            f"{(eval(num) / (17424/20))} Biswa.",
                            f"{(eval(num) / 1089)} Aer."
                            ],
            'num': eval(num)
            }

        return render(request, "feet.html",feetAnswer)
    else:
        return render(request, "feet.html")


def mtrPage(request):
    if request.method=='POST':
        num=request.POST.get('mtr')

        mtrAnswer={
            'answer' : [
                            f"{(eval(num) / 10000)} Hect.",
                            f"{(eval(num) / 1600)} Bigha.",
                            f"{(eval(num) * 10.89)} SqrFeet.",
                            f"{(eval(num) / 80)} Biswa.",
                            f"{(eval(num) / 100)} Aer."
                            ],
            'num': eval(num)
            }

        return render(request, "meter.html",mtrAnswer)
    else:
        return render(request, "meter.html")

def aboutus(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contact.html")
