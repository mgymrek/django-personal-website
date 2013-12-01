from publications.models import *

from Bio import Entrez
from Bio import Medline
Entrez.email = "your_email@whatever.com"
import datetime

def GetMyPubmedIDs():
    handle = Entrez.esearch(db="pubmed", term="your name", retmax=463)
    record = Entrez.read(handle)
    idlist = record["IdList"]
    return idlist

def UpdatePublicationDatabase():
    idlist = GetMyPubmedIDs()
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    for rec in records:
        authors = rec["FAU"]
        journal = rec["TA"]
        pubdate = rec["DA"]
        pubdate = datetime.datetime(int(pubdate[0:4]), int(pubdate[4:6]), int(pubdate[6:]))
        try:
            pages = rec["PG"]
        except: pages = ""
        volume = rec["VI"]
        title = rec["TI"]
        pmid = rec["PMID"]
        ip = rec.get("IP",0)
        # check if authors in database, if not then make an entry
        authors_list=[]
        for author in authors:
            lastname = author.split(",")[0]
            firstname = author.split(",")[1].split()[0].strip()
            try:
                middle = author.split(",")[1].split()[1]
            except: middle = ""
            search_authors = Author.objects.filter(first_name=firstname, last_name=lastname)
            if len(search_authors) == 0:
                a = Author(first_name=firstname, last_name=lastname, middle_name=middle)
                a.save()
                authors_list.append(a)
            else: authors_list.append(search_authors[0])
        
        # add journal if not there
        search_journals = Journal.objects.filter(journal=journal)
        if len(search_journals) == 0:
            j = Journal(journal=journal)
            j.save()
            journal_obj = j
        else: journal_obj = search_journals[0]
        
        pub_search = Publication.objects.filter(title=title)
        if len(pub_search) == 0:
            pub = Publication(pmid=pmid, pubdate=pubdate, title=title, journal=journal_obj, pages=pages, volume=volume, ip=ip)
            pub.save()
            # add authors
            order = 0
            for a in authors_list:
                auth = Authorship(author=a, publication=pub, order=order)
                auth.save()
                order = order + 1
