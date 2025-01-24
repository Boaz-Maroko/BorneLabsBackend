# Django Backend

This backend uses django as the primary backend framework and that uses
django rest framework (DRF) to expose a RESTful API to the frontend.

## How to setup
### Step One: **Download and install Python**
### Windows
Go the official python website and download python v3.10.xx and above. Click
[here](https://www.python.org/) for a quick link. _Remember to add it to path_.
### Linux
You can follow a similar method as the one above to setup python in any linux
distros, _or_
run
```bash
sudo apt install python3
```
### Step Two: **Setup the Project Directory**
Make a directory for your project in a comfortable location.

### Step Three: **Clone the repo**
run this command from you terminal

```bash
git clone https://github.com/Boaz-Maroko/BorneLabsBackend.git
```

### Step Four: **Install the dependencies**
Change into the project directory and run the commands below
```bash
# For windows
py -m venv venv
venv\scripts\activate.ps1
# For linux
python3 -m venv venv # You can call the python virtual environment whatever
source venv/bin/activate

pip install -r requirements.txt
```
### Step Five: **Run the development server**
#### Change into the project directory
```bash
cd backend  
```

```bash
# windows
py manage.py makemigrations

py manage.py migrate

py manage.py runserver

# Linux
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver