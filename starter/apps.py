import json
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.apps import AppConfig


class Utils(object):

    # read and parse data from JSON file
    @classmethod
    def get_data(self):
        print "getting data...."

        json_data = open('starter/data/more_movies.json')
        json_parse = json.load(json_data)
        duplicated_data= json_parse['movies']
        Utils.MyData = []
        #code below is to remove duplicates
        tally = {}
        for movie in duplicated_data:
            if movie['id'] in tally:
                tally[movie['id']] += 1
            else:
                tally[movie['id']] = 1
                Utils.MyData.append(movie)


        

    # filter data based on title query
    @classmethod
    def search_data(self, query):
        print "searching data for ", query

        search_result = []
        id_number_tracker = [] #keeps track of duplicates

        for movie in Utils.MyData:
            if (fuzz.token_sort_ratio(query, movie['title']) >= 80) or (fuzz.token_set_ratio(query, movie['title']) >= 80):
                if movie['id'] not in id_number_tracker:
                    id_number_tracker.append(movie['id'])
                    search_result.append(movie)

        return search_result


    def get_absolute_url():
        return "/{}/".format(self.id)



        
class MyAppConfig(AppConfig):
    name = 'starter'

    def ready(self):   
        print "starting....." 
        # load data from JSON on startup
        Utils.get_data() 









