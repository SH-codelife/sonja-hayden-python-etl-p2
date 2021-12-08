from pgsql import query
import sql
import requests
import json
import functions

def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


if __name__ == '__main__':

    # get some movie data from the API
    #print(get_movie_data('WarGames'))
    # access sql.py to create the schema
    #query(sql.create_schema, [])
    # access sql.py to create the table
    #query(sql.create_table, [])
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
        print(data)  # testing
    file_write = open("datasets/json/filtered_movies.json", "w")  #initialize and assign value to write in filtered data
    json.dump(data, file_write, indent=4) # dump for py objects have to be stored in a file, data=to be dumped: file_write=stored data output
    file_write.close()