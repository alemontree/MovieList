from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
import json
import os


# def get_data():
#     # print "test"
#     # print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#     json_data = open('starter/data/movies.json')
#     json_parse = json.load(json_data)
#     # print json_parse 
#     # for k, v in json_parse.iteritems():
#     #     print k, v
#     #     print
#     for k in json_parse['movies']:
#         print k
#         print 





# class Movie(models.Model):
#     title = models.CharField(max_length = 120)
#     year = models.IntegerField()
#     runtime = models.IntegerField()
#     synopsis = models.TextField()
#     # abridged_cast = 


#     def __unicode__(self): # for python 2.7
#         return self.title

#     def __str__(self):  # for python 3
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"id": self.id})
#         # return "/posts/%s/" %(self.id)

# get_data()
