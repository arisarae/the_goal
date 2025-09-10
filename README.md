# The GOAL

[https://arisa-raezzura-thegoal.pbp.cs.ui.ac.id/](https://arisa-raezzura-thegoal.pbp.cs.ui.ac.id/)

## How to Create the Project

1. Open the command prompt and run `mkdir the_goal` to create a new directory. Then, run `cd the_goal` to enter it.

2. Create and activate an isolated virtual environment by entering

    ```
    python -m venv env
    env\Scripts\activate
    ```

3. In the current directory, create a `requirements.txt` file containing these dependencies:

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    python-dotenv
    ```

4. Install the dependency with this command

    ```
    pip install -r requirements.txt
    ```

5. Initialize a Django project by entering

    ```
    django-admin startproject the_goal .
    ```

6. In the same directory, create a `.env` file for local deployment. Add the given configuration.

    ```
    PRODUCTION=False
    ```

7. I\Still in the same directory, create a `.env.prod` file for production deployment configuration.

    ```
    DB_NAME=<database name>
    DB_HOST=<database host>
    DB_PORT=<database port>
    DB_USER=<database username>
    DB_PASSWORD=<database password>
    SCHEMA=tugas_individu
    PRODUCTION=True
    ```

8. Open `the_goal/settings.py` and insert the code below `import Path`.

    ```
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()
    ```

9. Inside the same setting file, locate `ALLOWED_HOSTS` and add these strings inside the square brackets

    ```
    "localhost", "127.0.0.1"
    ```

10. Add this code right above the `DEBUG` section

    ```
    PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
    ```

11. Modify the database configuration in `settings.py` as follows:

    ```
    # Database configuration
    if PRODUCTION:
        # Production: use PostgreSQL with credentials from environment variables
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                }
            }
        }
    else:
        # Development: use SQLite
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```

12. In the root directory of your project (the outer the_goal directory), migrate the database first using this command

    ```
    python manage.py migrate
    ```

13. Check if the Django server has already worked successfully by running the server using

    ```
    python manage.py runserver
    ```

14. Initialize a Git repository by entering `git init` inside the command prompt. Make sure to do it in the root directory (the outer `the_goal` directory)

15. Inside the outer directory of `the_goal`, create a `.gitignore` file and fill it with the following

    ```
    # Django
    *.log
    *.pot
    *.pyc
    **pycache**
    db.sqlite3
    media
    # Backup files
    *.bak
    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf
    # AWS User-specific
    .idea/**/aws.xml
    # Generated files
    .idea/**/contentModel.xml
    .DS_Store
    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml
    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries
    # File-based project format
    *.iws
    # IntelliJ
    out/
    # JIRA plugin
    atlassian-ide-plugin.xml
    # Python
    *.py[cod]
    *$py.class
    # Distribution / packaging
    .Python build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    *.manifest
    *.spec
    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt
    # Unit test / coverage reports
    htmlcov/
    .tox/
    .coverage
    .coverage.*
    .cache
    .pytest_cache/
    nosetests.xml
    coverage.xml
    *.cover
    .hypothesis/
    # Jupyter Notebook
    .ipynb_checkpoints
    # pyenv
    .python-version
    # celery
    celerybeat-schedule.*
    # SageMath parsed files
    *.sage.py
    # Environments
    .env*
    !.env.example*
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/
    # mkdocs documentation
    /site
    # mypy
    .mypy_cache/
    # Sublime Text
    *.tmlanguage.cache
    *.tmPreferences.cache
    *.stTheme.cache
    *.sublime-workspace
    *.sublime-project
    # sftp configuration file
    sftp-config.json
    # Package control specific files Package
    Control.last-run
    Control.ca-list
    Control.ca-bundle
    Control.system-ca-bundle
    GitHub.sublime-settings
    # Visual Studio Code
    .vscode/*
    !.vscode/settings.json
    !.vscode/tasks.json
    !.vscode/launch.json
    !.vscode/extensions.json
    .history
    ```

16. Connect the local repository to the GitHub repo by using

    ```
    git remote add origin https://github.com/arisarae/the_goal.git
    ```

17. Create a main branch named `master`

    ```
    git branch -M master
    ```

18. Perform git add, commit, push at the terminal/command prompt of the local directory

    ```
    git add .
    git commit -m "initial commit: set up django"
    git push origin master
    ```

19. Deploy the project to PWS by opening [https://pbp.cs.ui.ac.id/web/](https://pbp.cs.ui.ac.id/web/), logging in, and clicking `Create New Project`

20. Filled the project name with `thegoal` and then clicked the `Create New Project` button

21. Save `username` and `password` credentials

22. On the sidebar, click the newly created project and open the `Environment` tab

23. Click the `Raw Editor` and paste the content of `.env.prod` of our project, then click `Update All Variables`

24. Go back to the `setting.py` inside the inner directory of `the_goal` and add this new string to the `ALLOWED_HOSTS`

    ```
    "arisa-raezzura-thegoal.pbp.cs.ui.ac.id"
    ```

25. Run the project command found before or check in the `Build` tab

26. Enter the credentials by using the `username` and `password` saved before

27. We can git add, commit, push again here using the commit message `chore: adding pws deployment url as allowed hosts`

28. After making sure the virtual environment inside the root directory is still active, create a new application named `main` using the command prompt

    ```
    python manage.py startapp main
    ```

29. Register the application to the project by adding `'main'` to the list of `INSTALLED_APPS` inside the `settings.py` in the `the_goal` project directory

30. Inside the `main` directory, create another directory named `templates` and add a new `main.html` file. Filled the file with the following code

    ```
    <h1>{{ app }}</h1>

    <h4>Name: </h4>
    <p>{{ name }}</p>
    <h4>Class: </h4>
    <p>{{ class }}</p>
    ```

31. Open the `models.py` file in the `main` directory and fill it with this code

    ```
    import uuid
    from django.db import models

    class Product(models.Model):
        CATEGORY_CHOICES = [
            ('shoes', 'Shoes'),
            ('clothing', 'Clothing'),
            ('equipment', 'Equipment'),
        ]

        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField(default=0)
        description = models.TextField()
        thumbnail = models.URLField(blank=True, null=True)
        category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='equipment')
        stock = models.PositiveIntegerField(default=0)
        is_featured = models.BooleanField(default=False)

        def __str__(self):
            return self.name
    ```

32. Run these in the root directory terminal/command prompt to create and apply the model migration

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

33. Open the `views.py` located in the `main` application directory and modify its code to this

    ```
    from django.shortcuts import render

    # Create your views here
    def show_main(request):
        context = {
            'app' : 'The GOAL',
            'name': 'Arisa Raezzura Zahra',
            'class': 'PBD KKI'
        }

        return render(request, "main.html", context)
    ```

34. Create a `urls.py` file in the `main` directory and paste this code

    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

35. Open the `urls.py` file in `the_goal` inner project directory and modify it to this

    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

36. Save the changes and run these lines in the root directory command prompt

    ```
    git add .
    git commit -m "feat: create main app"
    git push origin master
    git push pws master
    ```

37. Create a `README.md` file in the root directory, fill it with the information needed, and do another git add, commit, push with the commit message `"docs: create README.md"`

## Client Request-Response

Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.

![Client Request-Response Diagram](ClientRequestResponseDiagram.png)

## Role of `settings.py`

`setting.py` is like the project's control center. It defines how the project behaves, holding all the key configurations necessary to manage the app’s behavior across development, testing, and production environments.

## How does Database Migration work?

Database migration refers to the process of transferring data from a source database to a target database. When this process is complete, the dataset from the source database will be entirely transferred to the target database.

## Why Django?

Since the main language used in Django is Python, which we are all already familiar with, we can focus on building and developing the application rather than doing it on top of learning a completely new language. Additionally, the Django framework offers both a frontend and a backend within a single application.

## Feedback for TA

I currently have no feedback for the TAs since they already helped us a lot during the Tutorial. For future tutorials, I hope they continue to do what they're doing now and help us when we encounter problems.
