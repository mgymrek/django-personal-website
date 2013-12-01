from django.db import models

class Journal(models.Model):
    """
    A journal
    """
    journal = models.CharField(max_length=500)
    def __unicode__(self):
        return self.journal

class Author(models.Model):
    """
    A single author
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Publication(models.Model):
    """
    A single publication, mapped to a pubmed ID.
    """
    pmid = models.IntegerField()
    pubdate = models.DateTimeField('date published')
    title = models.CharField(max_length=500)
    journal = models.ForeignKey(Journal)
    pages = models.CharField(max_length=20)
    volume = models.IntegerField()
    ip = models.IntegerField()
    author = models.ManyToManyField(Author, through="Authorship")
    def __unicode__(self):
        return self.title

class Authorship(models.Model):
    """
    Relationship between author and publication. Allows us to 
    keep track of authorship order
    """
    author = models.ForeignKey(Author)
    publication = models.ForeignKey(Publication)
    order = models.IntegerField()
    def __unicode__(self):
        return "author: " + self.author + " #" + str(self.order) + ", publication: " + self.publication

class Resource(models.Model):
    """
    Contains a resource related to a publication
    """
    publication = models.ForeignKey(Publication, blank=True, null=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    datalink = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    def __unicode__(self):
        return "Resource: " + self.name + ": " + self.description

class PressRelease(models.Model):
    """
    Contains a press release related to a publication
    """
    publication = models.ForeignKey(Publication)
    prdate = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    journal = models.ForeignKey(Journal)
    link = models.CharField(max_length=200)
    def __unicode__(self):
        return "PR: " + self.title
