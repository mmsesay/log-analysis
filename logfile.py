#!/usr/bin/env python3

import psycopg2

# databaase name
newsdb = "news"
# db = psycopg2.connect(database=newsdb)

try:
   db = psycopg2.connect(database=newsdb)
   c = db.cursor()
except psycopg2.Error as e:
   print("Unable to connect to the database")
   print(e.pgerror)
   print(e.diag.message_detail)
   sys.exit(1)

# most popular articles as mp_articles function()
def mp_articles():
   """Returns top 3 most popular articles from the 'database"""
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
   c.execute('SELECT authors.name, count(*) AS total_no_views '
            +'FROM articles, authors, log ' 
            +'WHERE articles.slug = substring(log.path, 10) AND articles.author = authors.id '
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
   c.execute('SELECT to_char(time,\'MONTH DD,YYYY\') AS Day, '
            +'(COUNT(*)::float/100) AS errors_in_percentage '
            +'FROM log WHERE status = \'404 NOT FOUND\' '
            +'GROUP BY Day '
            +'ORDER BY 2 DESC '
            +'LIMIT 1; ')
   requestErrors = c.fetchall()
   db.close()

   for days, errors in requestErrors:
      print(str(days) +' ---> '+ str(errors) + ' % errors\n')

if __name__ == '__main__':
   mp_articles()
   # mp_article_authors()
   # error_report()