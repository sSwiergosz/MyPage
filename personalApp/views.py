from Bio import Entrez, Medline
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'personalApp/index.html')

def contact(request):
	return render(request, 'personalApp/contact.html')

def news(request):
	d = {}
	
	Entrez.email='szymon.swiergosz@gmail.com' #always tell who you are!
	handle = Entrez.esearch(db='pubmed', term='bioinformatics', report='medline', format='text', retmax=5)
	results = Entrez.read(handle)
	idlist = results['IdList']
	handle = Entrez.efetch(db='pubmed', id=idlist, rettype='medline', retmode='text')
	
	records = list(Medline.parse(handle))

	for record in records:
		d[record.get("PMID")] = [record.get("TI"), ', '.join(record.get("AU"))]

	return render(request, 'personalApp/news.html', {'articles': d})
