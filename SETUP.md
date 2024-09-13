<h1 align="center">Setup</h1>
<h4 align="center">Instruction on how to set up the environment for the homeworks and seminars</h4>

> [!IMPORTANT]
> First, read the whole instruction from the bottom to the end. \
> If You can barely understand some moments, don't hesitate to ask questions in the [Telegram chat](https://t.me/+zrpqje4r7U05MzUy) and pay attention to the [must have](#must-have) section.


## First steps

1) Install [PyCharm IDE](https://www.jetbrains.com/pycharm/download). It is recommended to use [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) for that. You can also use any other IDE you want
2) Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

	<details><summary>For Windows Users</summary>

	In case you have an error like that:
	```bash
	Git is not recognized as an internal or external command
	```

	You need to edit the environment variables. YouTube video [here](https://youtu.be/v3RCp26naoI?si=qQMGsX3QLf4SNfQq).
	</details>

3) [Generate SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys) and [add it in GitHub](https://github.com/settings/keys)

	If you have troubles generating an SSH key, try googling how to do it for your OS. \
	For example, a YouTube video for Windows [here](https://www.youtube.com/watch?v=a-zX_qc2S-M).

4) Clone your first repository (link in the [Telegram Chat](https://t.me/+zrpqje4r7U05MzUy)) and open it in the terminal. See ["How to contribute"](#cloning-the-repository) section for instructions

5) Install all the necessary packages

	<details><summary>Advanced topic: virtual environment</summary>

	*Note:* It's a good practice to use a virtual environment for the following steps. \
	You can find more information about virtual environments on the internet.
	</details>

	Execute the following commands in the terminal:
	```bash
	pip install -r requirements.txt
	pip install --editable tools/testlib
	```

6) Check the installation

	Execute the following commands in the terminal:
	```bash
	python --version
	pytest --version
	mypy --version
	flake8 --version
	```

	You should see the versions of the installed packages:

	```bash
	Python 3.12.6
	pytest 8.3.3
	mypy 1.11.2
	7.1.1 <...>
	```

	Congratulations! You are now ready to start coding! 🚀


## How to contribute

#### Cloning the repository
* Open PyCharm and create a new project, call it whatever you want
* Go to your repository (the link to it will be in the [Telegram chat](https://t.me/+zrpqje4r7U05MzUy)) and click <img src="http://gg.gg/click_code"> ➔ SSH ➔ copy the link
* Go to PyCharm and open the terminal in the bottom dock (or use your system terminal):
	```bash
	git clone <the link you've just copied>
	```
* Write code!

#### Testing the code
* Open the terminal (e.g. in PyCharm) and navigate to your project root folder
* `pytest tasks/{task_name}` (running tests)
* `flake8 tasks/{task_name}` (checking code style)
* `mypy tasks/{task_name}` (checking types)

You can also run `pytest tasks` or `flake8 tasks` or `mypy tasks` to run tests for all tasks altogether

You should see all the tests, code style checks, and typing checks green and passing

#### Pushing changes to the repository
* Open the terminal (e.g. in PyCharm) and navigate to your project root folder
* `git add .` (adding all the modified files in the current directory to the staging area)
* `git commit -m "Homework solution"` (committing changes in your local copy of the repository)
* `git push` (pushing changes to the GitHub repository)

After pushing your changes, you can review your solution on the "Pull Requests" tab of your repository

## Must have

### Terminal commands

You need to understand what the terminal is, how to navigate through directories, and how to execute commands. \
Here are some useful commands:
* `cd` – change directory
* `ls` – list files and directories
* `pwd` – print working directory
* `mkdir` – create directory
* `rm` – remove file or directory
* `cp` – copy file or directory
* `mv` – move file or directory

You can find plenty of tutorials on YouTube or other platforms. \
For example, this [one](https://youtu.be/uwAqEzhyjtw?si=um_ysNdEo1f5oi8z).

<details><summary>Windows users note</summary>

You can use Git Bash terminal which should be installed with Git. \
Another option is to use Windows Powershell or Windows Command Prompt.
* Command prompt [tutorial](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDV6SnbINlVUd0o2xT4JbMu) (1-5, 9 videos)

I strongly recommend you use the Git Bash terminal. You can set up Git Bash in PyCharm: [Instruction](https://ubuntuask.com/blog/how-to-invoke-pycharm-from-git-bash)

</details>

### Git

You need to understand the basics of Git. \
Here are some useful commands:
* `git clone` - clone a repository
* `git add` - add file or directory to the staging area
* `git commit` - commit changes
* `git push` - push changes to the remote repository
* `git pull` - pull changes from the remote repository
* `git status` - show the status of the working directory
<br>

* [Basic Git and GitHub tutorial](https://www.youtube.com/watch?v=RGOj5yH7evk)
* [Git cheat sheet](https://www.freecodecamp.org/news/git-cheat-sheet-and-best-practices-c6ce5321f52/)
* [Git book](https://git-scm.com/book/en/v2) (you can read the few first chapters; it's very useful)
* [Git exercises](https://gitexercises.fracz.com/)

### Flake8, MyPy, Pytest

You need to understand how to use these tools. \
For this google some tutorials or read the documentation.

### Useful to know

* PyCharmd IDE [tutorial](https://www.youtube.com/watch?v=2EB8siO-_OM&list=PLCTHcU1KoD98IeuVcqJ2rt1FNytfR_C90) (maybe too simple)
* Jupyter Notebook tutorial
* Touch typing
