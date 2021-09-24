Tutorial video: https://www.youtube.com/watch?v=qbLc5a9jdXo

Fix potential errors links: 
https://fixexception.com/flask/could-not-locate-a-flask-application-you-did-not-provide-the-flask-app-environment-variable-and-a-wsgi-py-or-app-py-module-was-not-found-in-the-current-directory/
https://code.visualstudio.com/docs/python/tutorial-flask#_refactor-the-project-to-support-further-development

# Developing environment setup
# 1. create my own API
python, postman, virtual environment
-cd my_api
-pwd
# 2. create a virtual environment to isolate dependencies for this specific application (YouTube, 28:25)
-python3 -m venv .venv
# 3. activate the virtual environment
-.venv/bin/activate
# 4. 
-pip3 install flask
-pip3 install flask-sqlalchemy
· to have all the requirements in the below txt file when adding a new dependency
-pip3 freeze > requirements.txt
# 5. (need to do this everytime you reopen a terminal)
-export FlASK_APP=my_api_application.py
-export FlASK_ENV=development
# 6. leave the virtual environment
-deactivate