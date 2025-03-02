from django.shortcuts import render
from .forms import EMIForm
import math
# Create your views here.
def emi(request):
    emi = None
    if request.method == "POST":
        form = EMIForm(request.POST)
        if form.is_valid():
            Principal= form.cleaned_data["Principal"]
            Rate = form.cleaned_data["Rate"]
            Tenure= form.cleaned_data["Tenure"]


            monthly_interest= (Rate/100)/12
            emi=Principal*monthly_interest* math.pow(1 + monthly_interest,Tenure) / (math.pow(1 + monthly_interest,Tenure)-1)

    else:
        form = EMIForm()

    return render(request, "emi.html", {"form": form,'emi':emi})
