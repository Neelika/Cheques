import datetime
from datetime import timedelta
from django.forms.fields import DateField, TimeField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect
try:
    from decimal import Decimal
except ImportError:
    from django.utils._decimal import Decimal

class NavigationTestCase(TestCase):
    
    def setUp(self):
        pass        
   
    def test_NavigationHome(self):
        """
        Checks whether all the pages are navigable or not.
        """
        c = Client()
        response = c.post('/cheques/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_IssueChequeBook(self):
	account_number='30446461991'
	newAccount = Account.objects.create(account_number= '30446461991', balance= 5000, name='sakshi', number_of_chequebooks=0)
	first_cheque_number=111111
	c = Client()

	response = c.post('/cheques/employeeMenu/e_issueChequeBook/?account_number=30446461991',{'size': 20})
	cb_size=0
	for num in ChequeBook.objects.all():
		a_num=num.account_number_id
		if account_number=='30446461991':
			cb_size=num.size

        self.assertEqual(response.status_code,200)