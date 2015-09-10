# Set Up

This homework will be turned in via a bitbucket repository. Start by making a new repository named `homework-2` in bitbucket. You must make this a _public_ repository. **Make sure it is public!**

Navigate to your home directory and clone the repository.

    cd
	    git clone git@bitbucket.org:mgidden/homework-2

Now, instead of using _my_ remote, we will change it to use _your_ remote. Replace all instances of `<your username>` with your bitbucket user name.

    cd homework-2
	    git remote rm origin
		    git remote add origin git@bitbucket.org:<your username>/homework-2
			    git push origin master

## Working on the Assignment

You should do all of your work **in the homework-2 directory**. Navigate to the directory and start IPython notebook there.

    cd ~/homework-2
	    ipython notebook

You will be creating new files in the assignment. You will also be changing and updating files. Make sure to update your repository frequently by

- `git add`ing updated files
- `git commit`ing with an appropriate message and
- `git push`ing them to your bitbucket repository.

## Turning in the Assignment

The tutors will send out an email to turn in the assignment. Respond to that email with the git command to clone your finished assignment. The command should clone your repository into a new folder named `<your username>`. For example, my turn-in email would have the following line

    git clone git@bitbucket.org:mgidden/homework-2 mgidden

because my bitbucket username is `mgidden`.
