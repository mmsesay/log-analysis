#!/usr/bin/env python3

import psycopg2

# databaase name
newsdb = "news"

# most popular articles as mp_articles function()
def mp_articles():
   """Returns top 3 most popular articles from the 'database"""
   db = psycopg2.connect(database=newsdb)
   c = db.cursor()
   c.execute('SELECT title, COUNT(*) AS total_no_views '
            +'FROM articles JOIN log '
            +'ON articles.slug = substring(log.path, 10) '
            +'GROUP BY title '
            +'ORDER BY 2 DESC '
            +'LIMIT 3;')
   mostPopularArticles = c.fetchall()
   db.close()

   # looping through the data
   for article, view in mostPopularArticles:
      print('"'+ article +'" ---> '+ str(view) +' views\n')


# most popular authors of all time as mp_article_authors()
def mp_article_authors():
   """Return the most popular article authors of all time"""
   db = psycopg2.connect(database=newsdb)
   c = db.cursor()
   c.execute('SELECT authors.name, COUNT(*) AS views '
            +'FROM articles JOIN authors '
            +'ON articles.author = authors.id '
            +'GROUP BY authors.name '
            +'ORDER BY 2 DESC;')
   mostPopularAuthors = c.fetchall()
   db.close()

   # looping through the data
   for author, view in mostPopularAuthors:
      print(author +' ---> '+ str(view) +' views\n')

# days that leads to more than 1% of requests errors as error_report()
def error_report():
   """Return all the days that leads to more than 1% of requests errors."""
   db = psycopg2.connect(database=newsdb)
   c = db.cursor()
   c.execute('SELECT Date(time) AS days, '
            +'(COUNT(*)::float/100) AS request_errors '
            +'FROM log WHERE status = \'404 NOT FOUND\' '
            +'GROUP BY Days;')
   requestErrors = c.fetchall()
   db.close()

   for days, errors in requestErrors:
      print(str(days) +' ---> '+ str(errors) + ' % errors\n')

if __name__ == '__main__':
   mp_articles()
   # mp_article_authors()
   # error_report()

