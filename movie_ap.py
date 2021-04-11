import imdb
import csv

moviesDB = imdb.IMDb()
put_movie = input('Enter a title: ')
movies = moviesDB.search_movie(put_movie)


# for movie in movies:
#     title = movie['title']
#     year = movie['year']
#     print(f'{title} {year}')

id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
box_office = movie['box office']
print('Movie info: ')
print(f'{title} - {year}')
print(f'IMBD Rating: {rating}')
print(f'Box office:{box_office} ')

fields = ['Title', 'Year', 'Rating', 'Box office ']
rows = [[title, year, rating, box_office]]

best_rated = moviesDB.get_top250_movies()


"""Save input data to csv file"""

with open('File', 'a') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

"""Show all movies saved in csv file"""

print('\nList of chosen films')

with open('File') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


"""Print average of all rating in saved movies"""

with open('File') as f:
    reader = csv.reader(f)
    Sum = 0
    row_count = 0
    rating = movie['rating']
    maxr = 0
    # gross = box_office['Budget']
    for row in reader:
        row_count += 1
        p = int(rating)
        Sum += p
        # a = float(gross)
        # maxr = max(maxr, a)
    average = Sum/row_count

print(f'\nAverage rating of my films is: {average}')


"""Show the best movie in IMDB"""

print('\nBest rated movie in IMDB: ')
for movie in best_rated[0:1]:
    print(movie)


# list_of_gross_amount = []
#
# for movie in best_rated:
#     try:
#         a = box_office['Cumulative Worldwide Gross']
#         gross = float(a)
#         list_of_gross_amount.append(gross)
#     except:
#         pass


