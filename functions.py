import json

'''        
def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()
'''

#def open_json_file():
'''
f = open('datasets/json/movies.json', 'r')  # open json file to read, assigned to "f"
reader = json.load(f)  # read "f" into "reader", load() works (loads() doesn't, file is a string??
f.close()  # close file when done using
# movies = []
titles = []  # initialize empty list
for i in reader:
    if i['year'] >= 2018:  # condition requirement, index value="year"
        # movies.append(['year'])
        titles.append(i["title"])  # fill list by index value="title'
        # print(i["title"])  #test
titles_set = set(titles)
print(titles_set)
'''

