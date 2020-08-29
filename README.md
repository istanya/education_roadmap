# education_roadmap


# Setting up a development environment

We assume that you have `git` and `virtualenv` and `virtualenvwrapper` installed.

    # Clone the code repository into ~/dev/education_roadmap
    mkdir ~/dev
    cd ~/dev
    git clone https://github.com/istanya/education_roadmap

    # Create the 'education_roadmap' virtual environment
    mkvirtualenv my-virtualenv --python=python3.7

    # Install required Python packages
    cd ~/dev/education_roadmap
    workon my-virtualenv
    pip3.7 install -r requirements.txt


## Running the app

    # Start the Flask development web server
    python manage.py runserver

Point your web browser to http://localhost:5000/