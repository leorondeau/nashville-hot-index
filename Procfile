web: gunicorn nashvillehotindex.wsgi

Use a Procfile, a text file in the root directory of your application, 
to explicitly declare what command should be executed to start your app.

This declares a single process type, web, and the command needed to run it. 
The name web is important here. It declares that this process type will be 
attached to the HTTP routing stack of Heroku, and receive web traffic when deployed.

Procfiles can contain additional process types. For example, you might declare one 
for a background worker process that processes items off of a queue.


