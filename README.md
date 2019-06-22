
# LOG ANALYSIS - Udacity Project 1
## FULLSTACK-NANODEGREE
------
## About

This is a project that is analyzing some news data by display the: 
1. most popular articles of all time
2. most popular articles of all time and
3. the day that most requests leads to more than 1% of errors.

## Prerequisites
Below are the tools you need to have in order to execute this program:
1. Python:
Installation for windows
* Download the Python 3 Installer
* Open a browser window and navigate to https://www.python.org/downloads/windows/ or at https://www.python.org/.
* Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
* Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. (See below.)
* run the installer

Installation for Linux
* There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.

* To find out what version(s) you have, open a terminal window and try the following commands:
    * python --version
    * python2 --version
    * python3 --version

If no python version dispalys then run the following commands:
* open your terminal CTRL + ALT + T
* sudo add-apt-repository ppa:jonathonf/python-3.7
* sudo apt-get update
* sudo apt-get install python3.7

Installation for macOS / Mac OS X
* Well the current versions of macOS include a version of Python 2 but still follow the process to install the python 3.
* Open a browser and navigate to http://brew.sh/. After the page has finished loading, select the Homebrew bootstrap code under “Install Homebrew”. Then hit Cmd+C to copy it to the clipboard. Make sure you’ve captured the text of the complete command because otherwise the installation will fail.
* Now you need to open a Terminal.app window, paste the Homebrew bootstrap code, and then hit Enter. This will begin the Homebrew installation.
* If you’re doing this on a fresh install of macOS, you may get a pop up alert asking you to install Apple’s “command line developer tools”. You’ll need those to continue with the installation, so please confirm the dialog box by clicking on “Install”.
* Confirm the “The software was installed” dialog from the developer tools installer.
* Back in the terminal, hit Enter to continue with the Homebrew installation.
* Homebrew asks you to enter your password so it can finalize the installation. Enter your user account password and hit Enter to continue.
* Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you’ll end up back at the command prompt in your terminal window.
* Once Homebrew has finished installing, return to your terminal and run the following command:

`$ brew install python3`

2. Virtual Machine
Installation
* Goto this https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 for your OS
* Install the progam

3. Vagrant
Installation
* Goto this link https://www.vagrantup.com/downloads.html to dowload the setup for your OS
* Run the installer and verify if complete by typing : `vagrant --version`
* Download the configuration file https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
* Unzip the file. You will see a folder called FSND-Virtual-Machine. It may be located inside your Downloads folder.
* change directory to FSND-Virtual-Machine. Inside, you will find another directory called vagrant.
* run `vargran up` to start the vm
* secondly run `vagrant ssh` to log into the vm-machine
* Inside the vm change to the vagrant directory, `cd /vagrant`
* then type `psql` to enter into postgres 

4. Data
* You may need a data to query so dhowload it from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* You will need to unzip this file after downloading it. The file inside is called newsdata.sql. * Put this file into the vagrant directory, which is shared with your virtual machine.
* To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql


## How To execute the program
Make sure to be in the log-analysis directory to run the logfile.py file in a terminal. 
```cd /log-analysis
python3 logfile.py
```
There are three functions defined in that file which are:
1. mp_articles() represents the most popular articles of all time.
2. mp_article_authors() represents the most popular article authors of all time.
3. error_report() represent the days the result to more than 1% of request errors.

If you are running the logfile.py file, these three functions can be executed by just uncommenting the function you want in the main.
```if __name__ == '__main__':
    mp_articles()
    # mp_article_authors()
    # error_report()
```
By default the `mp_articles()` is uncommented and can be execute when the file is ran.


## HERE ARE THE COMANDS THAT CAN BE EXECUTED ON PGSQL TO PERFORM THE SAME OPERATIONS

<!-- The commands below return the top 3 most popular articles from the 'database'. -->
```SELECT title, COUNT(*) AS total_no_views 
    FROM articles JOIN log 
    ON articles.slug=substring(log.path, 10) 
    GROUP BY title 
    ORDER BY 2 DESC 
    LIMIT 3;
```

 <!-- This command return the most popular article authors of all time -->
```SELECT authors.name, count(*) AS total_no_views
    FROM articles, authors, log 
    WHERE articles.slug = substring(log.path, 10) AND articles.author = authors.id
    GROUP BY authors.name 
    ORDER BY 2 DESC;
```

<!-- This command return all the days that leads to more than 1% of requests errors -->
```SELECT to_char(time,'MONTH DD,YYYY') AS Day, 
    (COUNT(*)::float/100) AS errors_in_percentage 
    FROM log WHERE status = '404 NOT FOUND' 
    GROUP BY Day 
    ORDER BY 2 DESC 
    LIMIT 1; 
```
## Author
---
* Muhammad Mustapha Sesay
