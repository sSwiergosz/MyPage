from Bio import Entrez, Medline
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'personalApp/index.html')

def contact(request):
	return render(request, 'personalApp/contact.html')

def news(request):
	d = {}
	term = 'bioinformatics'

	if 'term' in request.GET:
		term = request.GET['term']

	if term == '':
		term = 'bioinformatics'
	
	Entrez.email='guest@email.com' #always tell who you are!
	handle = Entrez.esearch(db='pubmed', term=term, report='medline', format='text', retmax=5)
	results = Entrez.read(handle)

	if results['RetMax'] != '0': #if articles exist, then RetMax has some values
		idlist = results['IdList']
		handle = Entrez.efetch(db='pubmed', id=idlist, rettype='medline', retmode='text')
		records = list(Medline.parse(handle))
		print(records)
		for record in records:
			if "AU" in record:
				d[record.get("TI")] = [', '.join(record.get("AU")), record.get("JT"), record.get("PMID"),]
			else: #without authors and journals
				if record.get("TI") is not None: #sometimes even title is missing...
					d[record.get("TI")] = record.get("PMID")
	else: #if articles don't exist, then we send empty dictionary
		d = {}

	return render(request, 'personalApp/news.html', {'articles': d, 'search_value': term,})

