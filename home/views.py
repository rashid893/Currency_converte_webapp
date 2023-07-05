from django.shortcuts import render
from .models import CurrencyRate
from forex_python.converter import CurrencyRates, RatesNotAvailableError

def currency_converter(request):
    currencies = ['USD', 'AED', 'SAR', 'PKR']  # Add more currencies as needed
    
    if request.method == 'POST':
        source_currency = request.POST['source_currency']
        target_currency = request.POST['target_currency']
        amount = float(request.POST['amount'])
        
        c = CurrencyRates()
        
        try:
            converted_amount = c.convert(source_currency, target_currency, amount)
            context = {'converted_amount': converted_amount, 'currencies': currencies}
        except RatesNotAvailableError:
            context = {'error_message': 'Currency rates are not available at the moment'}
        
        return render(request, 'currency_converter.html', context)
    
    context = {'currencies': currencies}
    return render(request, 'currency_converter.html', context)

