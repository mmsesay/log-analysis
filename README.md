
                FULLSTACK-NANODEGREE: PROJECT 1 -> LOG ANALYSIS 
            =======================================================
Note: To execute the program please run the logfile.py file. 
There are three functions defined in that file which are:
    1. mp_articles() represents the most popular articles of all time.
    2. mp_article_authors() represents the most popular article authors of all time.
    3. error_report() represent the days the result to more than 1% of request errors.

    If you are running the logfile.py file, these three functions can be executed by just uncommenting the function you want in the main.
        if __name__ == '__main__':
            mp_articles()
            # mp_article_authors()
            # error_report()
    By default the mp_articles() is uncommented and can be execute when the file is ran.


HERE ARE THE COMANDS THAT CAN BE EXECUTED ON PGSQL TO PERFORM THE SAME OPERATIONS

<!-- The commands below return the top 3 most popular articles from the 'database'. -->
SELECT title, COUNT(*) AS total_no_views 
FROM articles JOIN log 
ON articles.slug=substring(log.path, 10) 
GROUP BY title 
ORDER BY 2 DESC 
LIMIT 3;

 <!-- This command return the most popular article authors of all time -->
SELECT authors.name, COUNT(*) AS views
FROM articles JOIN authors
ON articles.author = authors.id
GROUP BY authors.name
ORDER BY 2 DESC;

<!-- This command return all the days that leads to more than 1% of requests errors -->
SELECT Date(time) AS days,
(COUNT(*)::float/100) AS request_errors
FROM log WHERE status = '404 NOT FOUND'
GROUP BY Days;
