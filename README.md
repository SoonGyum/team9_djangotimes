**DRF 팀 프로젝트** <br>
**프로젝트 명** : Django_Times <br>
   **소 개**   : Geek News를 오마주한 뉴스 프로젝트 <br>
**Team 이름**  : 구조조정 <br>
개발환경:<br>
개발기간:<br>
각 팀원의 역할:<br>
폴더구조:<br>
wireframe, ERD, API명세서 <br>




## Project name
Django Times - A News Portal with Articles, Comments, and User Profiles (Inspired by Geek News)

## Introduction
The Django Times project is a news portal that allows users to explore, post, and engage with articles. Users can comment on articles, like both articles and comments, and manage their profiles. Built using Django, this project includes key features such as user authentication, article management, comment interaction, and social engagement through likes.

## Development Period
- Start Date: 2024.09.11
- End Date: 2024.09.20

## Team Roles and Responsibilities
|Team Member|Responsibilities|
|:--|:--|
|정순겸|- Accounts Feature(signup, login, logout, profile)<br>- Articles Feature(create, read, update, delete, detail-page)<br>- Comments Feature(create, read, update, delete)
|이규호|- Accounts Feature(signup, login, logout, profile)<br>- Article Like Feature<br>- Comment Like Feature|
|박윤성|- Accounts Feature(signup, login, logout, profile)|


## Full Technology Stack Overview
- Programming Language: python 3.10
- Web Framework: Django 4.2
- Database: SQLite
- IDE: PyCharm, Vs code
- Version Control: Git, Github
- Communication: Zep, Notion, Slack
- Technical stack
  - Backend: Python, Django
  - Database: Django ORM, SQLite

<br>

## Key Features
- User Profiles:
  - Users can create profiles with usernames and join dates.
  - Users can upload profile pictures (or use default ones).
  - View written articles, liked articles, and profile details.

- Article System:
  - Users can post articles with titles, content, and optional files.
  - A CRUD (Create, Read, Update, Delete) system for articles.
  - Articles can receive likes and comments.

- Social Interactions:
  - Users can comment on articles.
  - Users can like both articles and comments.

## Folder Structure
```bash
DJANGO_TIMES
│
├── accounts/           # App handling user authentication and profile management
│   ├── migrations/     # Database migration files for accounts app
│   ├── models.py       # User model and related authentication logic
│   ├── serializers.py  # Serializers for user authentication and profile handling
│   ├── views.py        # Views for signup, signin, signout, and profile management
│   └── urls.py         # URL configurations for accounts app
│
├── articles/           # App managing articles, categories, and comments
│   ├── migrations/     # Database migration files for articles app
│   ├── models.py       # Article, Category, and Comment models
│   ├── serializers.py  # Serializers for articles, categories, comments, and likes
│   ├── views.py        # Views for article and comment CRUD, and like management
│   └── urls.py         # URL configurations for articles app
│
├── media/              # Folder for storing uploaded media files (e.g., user profile images)
│
├── django_times/       # Project configuration files (settings.py, urls.py, etc.)
│   ├── settings.py     # Project settings file, including authentication and JWT settings
│   ├── urls.py         # Root URL configuration, includes paths for accounts and articles
│   └── wsgi.py         # WSGI entry point for the project
│
├── db.sqlite3          # SQLite database file for local development
│
├── manage.py           # Django management command file
│
├── requirements.txt    # List of dependencies for the project (Django, DRF, etc.)
│
├── .gitignore          # Files and directories to be ignored by Git (e.g., __pycache__, *.pyc)
```