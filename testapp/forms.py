from django import forms
class EMIForm(forms.Form):
    Principal=forms.FloatField(label="Principal Amount" )
    interest_rate = forms.IntegerField(label="Interest Rate (%)")
    loan_term = forms.IntegerField(label="Loan Term (Months)")