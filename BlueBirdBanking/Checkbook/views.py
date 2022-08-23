from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


#   Render the home page
def home(request):
    form = TransactionForm(data = request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account'] #  If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) #   Call balance function to render that account's balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


#   Render the create account page
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve the account form and store all the data in form
    #   Check if request method is POST
    if request.method == 'POST':
        if form.is_valid():     #   if the form's valid, save it.
            form.save()
            return redirect('index')    #   Send the user back to the home page
    content = {'form': form} #  Saves content to the template as a dictionary
    #   Now we need to pass it to our form
    return render(request, 'checkbook/CreateNewAccount.html', content)


#   Render the balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


#   Render the Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form' : form}
    return render(request, 'checkbook/AddTransaction.html', content)



