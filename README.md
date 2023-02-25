# __PARALLAX HRMS__

1. ### ADD CREDENTIALS
    - OPEN the settings.py File.
   ```
   # CREATE A NEW DB AND UPDATE SETTINGS FILE
   DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', 5432),
        'NAME': os.getenv('DB_NAME', 'YOUR DB NAME'),
        'USER': os.getenv('DB_USER', 'YOUR USER NAME'),
        'PASSWORD': os.getenv('DB_PASS', 'PASSWORD')
    }
}
   

2. ### RUN WITH VIRTUAL ENVIRONMENT
    - Run `Venv` and `and set the interpreter`.
   ```
    python3.9 -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate

    pip install pip --upgrade pip
    pip install -r requirements.txt
    python manage.py runserver 0.0.0.0:8000
    ```
3. ### RUN WITH DOCKER
    - Install Docker in our System.
   ```
   # docker build . 
   # docker up

   ```
   > _NOTE: Browse to [http://0.0.0.0:9000/](http://0.0.0.0:9000/) or Your your http://localhost:port as BASE URL. To view the api Please follow the [Documentation](https://hackmd.io/@dkkundu/r1Da9oPCi)

