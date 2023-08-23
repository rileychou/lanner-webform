# lanner-webform

## Setup instructions
First, make sure Python is installed on your computer. Open command prompt / terminal and type
```
python
```

If it shows a version number, you are good to go. If Python is not installed, download it here: https://www.python.org/downloads/

Next, install Django:
```
pip install django
```

Open up command prompt / terminal, and navigate to the folder you want to put this project in by typing
```
cd <path-to-folder>
```
For example, if I want it in my desktop folder on my windows machine I would type this. Replace the filepath with your own.
```
cd \Users\Riley\Desktop
```

Now we can pull the code onto your computer.

Before we do that, sure git is installed on your computer: https://git-scm.com/downloads

Next, clone the repository. This downloads the code onto your computer.
```
git clone https://github.com/rileychou/lanner-webform.git
```

Switch into the project folder:
```
cd lanner-webform
```

Start up the server (run this line every time you want to start the server):
```
python manage.py runserver
```

Next, go to your browser and go to http://localhost:8000/ to view the webform!
