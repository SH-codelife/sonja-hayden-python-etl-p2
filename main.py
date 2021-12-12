from pgsql import query
import sql
import requests
import json
import functions
from datetime import datetime


def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


if __name__ == '__main__':

    # get some movie data from the API
    #print(get_movie_data('WarGames'))
    # access sql.py to create the schema
    #query(sql.create_schema, [])
    query(sql.drop_table, [])
    # access sql.py to create the table
    query(sql.create_table, [])

    #print("success")
    #query(open_json_file, []):

    f = open("datasets/json/movies.json", "r")  # open json file to read, assigned to "f"
    reader = json.load(f)  # read "f" into "reader", load() works (loads() doesn't, file is a string??
    f.close() #  close file when done using
    
    #movies = []
    titles = []  # initialize empty list
    for i in reader:
        if i["year"] >= 2018:  # condition requirement, index value="year"
            #movies.append(['year'])
            titles.append(i["title"])  # fill list by index value="title'
            #print(i["title"])  #test
    titles_set = set(titles) # convert list to a set to eliminate duplicate titles
    #print(titles_set)

    titles_list = list(titles_set) #convert set to list to compare values in api call
    data = {} #initialize an empty set to hold movies set
    for title in titles_list:  #loop through list and get titles
        data[title] = get_movie_data(title)  # function called, titles compared
        #(data)  # testing
    file_write = open("datasets/json/filtered_movies.json", "w")  #initialize and assign value to write in filtered data
    json.dump(data, file_write, indent=4) # dump for py objects have to be stored in a file, data=to be dumped: file_write=stored data output
    file_write.close()

    f2 = open("datasets/json/filtered_movies.json", "r") #open filtereed_movie.json to  check for language
    reader_2 = json.load(f2) #variable holds output from f2
    f2.close()
    #print(reader_2)

    movie_list = []
    for movie in reader_2: # go through to get "key" from outer dictionary, for easier data handling
        movie_list.append(reader_2[movie]) # dict_of_dict list is now list of dictionary, outer "key" removed to simplify
    #print(movie_list)

    english_movies = [] # list to hold filtered language="English" , also empty titles
    for movie_dict in movie_list:
        if (movie_dict["Response"] != "False") and "English" in movie_dict["Language"]:
            english_movies.append(movie_dict)
        #print(len(english_movies))

    required_column_values = [] #list to hold column requirements, ONLY keep these fields
    columns = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Awards", "Poster"]
    for i in english_movies:  # iterate through
        x = {key: i[key] for key in columns}   # []=index {}placeholder, loop through and filter
        required_column_values.append(x) # append list with rows and only required fields

    movie_list_na_check = [] #list to hold new list with complete data (no N/A field values)
    for x in required_column_values:
        if "N/A" not in x.values():
            movie_list_na_check.append(x)
    #print(len(movie_list_na_check))

    api_check_date = [] # filtered list to check against API to eliminate odds date data
    for i in movie_list_na_check:
        if datetime.strptime(i["Released"], "%d %b %Y").year >= 2018:
            api_check_date.append(i)
   #print(len(api_check_date))

    for movie in api_check_date:
        final_list = []
        movie["Genre"] = movie["Genre"].split(',')
        movie["Writer"] = movie["Writer"].split(',')
        movie["Actors"] = movie["Actors"].split(',')
        movie["Runtime"] = int(movie["Runtime"][:3])
        final_list.append(movie["Title"])
        final_list.append(movie["Rated"])
        final_list.append(movie["Released"])
        final_list.append(movie["Runtime"])
        final_list.append(movie["Genre"])
        final_list.append(movie["Director"])
        final_list.append(movie["Writer"])
        final_list.append(movie["Actors"])
        final_list.append(movie["Plot"])
        final_list.append(movie["Awards"])
        final_list.append(movie["Poster"])
        print(final_list)

        query(sql.insert_data, final_list)

        #next((item for item in api_check_date))


    '''
    value = "English"
    english_only = [] # initialize list to hold final dictionaries
    for key_1, value_1 in reader_2.items(): # 1st for loop for outer nested dictionary, Key=title Value=everything else
        for key_2, value_2 in value_1.items(): #2nd for loop to go through value_1 items
            if key_2 == "Language":  # condition for Value of value_2
                english_only.append(value_1)  # add dictionaries that are filtered
    #print(english_only)
    print(len(english_only))

    
    
    value = "N/A"  # look for all values N/A and remove rows
    english_only_no_NA = []
    for i in range(len(english_only)):
        if english_only[i]["Poster"] =="N/A":
            del english_only[i]
            break
    print(len(english_only))
    #remove extra columns, then look for n/a values in the 11 required columns
    #LIST of dictionaries = Index values OF Key/value pairs

    i = 0
    column_1= "Title" #"Released", "Runtime", "Genre", "Director", "Writers", "Actors", "Awards", "Poster")
    title_column = [] #empty list to hold new list of movies with correct fields
    #key_values = [x[a] for x in english_only]
    #print(key_values)
    for i in len(english_only):
        for k in english_only.items():
            title_column.append(k)
        i+=1
    print(title_column)
    '''