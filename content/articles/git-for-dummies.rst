Git For Dummies
###############

:date: 2014-03-20
:tags: git, programming, github
:description: This is my notes on using `git` and github. Will work through some basics and discuss some how tos.

I have had to do a lot of googling lately to get familiar with `git`. My understanding of git is a
work in progress. Here I summarize some of the basic commands and features that I learnt. I plan to 
keep this article updated as and when I learn something new.


Git Basics
----------
One of the basic concepts in git is the notion of *upstream* and *origin*. The term *upstream* refers to the main
repository lets say the pandas on github hosted at `https://github.com/pydata/pandas`. However you have forked the 
to work on an issue, then the *origin* would refer to the user's fork of the *upstream* repository.


- **Initialize repositor**: in an empty folder
  ``
  git init
  ``
  You should see a message akin to
  ``
  Initialized empty Git repository in /home/username/test/.git/
  ``
  
- **Add remote repository**:  To hook up to your local repository to a remote repository, such as the `pandas` repository on github.
  ``
  git remote add upstream https://github.com/pydata/pandas.git
  ``
  Note that instead of adding upstream, I could have added my fork as origin as shown below:
  ``
  git remote add origin https://github.com/gouthambs/pandas.git
  ``
  
  
- **Remove remote repository**: You have made a mistake and added a wrong remote repository. To remove a remote repo:
  ``
  git remote remove upstream
  ``
  You can do the same to remove a remote origin.
  ``
  git remote remove origin
  ``
  
- Check what the remote repositories are.
  ``
  git remote -v
  ``
  This after adding the above pandas repo would show something like:
  ``
  upstream	https://github.com/pydata/pandas.git (fetch)
  upstream	https://github.com/pydata/pandas.git (push)
  ``
- **Fetching code from remote**: Now that you have hooked up to a remote repository, how do you fetch the code from 
  there? Lets say we have added remote upstream, and we want to fetch the code, then do the following:
  ``
  git fetch upstream
  ``
  What this does is it fetches the whole repository, with all its branches and tags etc. Now to actually start using 
  a particular branch you have to checkout.
  
- **Checkout code**: To checkout the master try
  ``
  git checkout master
  ``
  


