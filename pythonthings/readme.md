# to install

* cd to this directory `.\pythonthings\`
* activate a virtual environment using `py -m venv .`
* install pip requirements using `pip install -r requirements.txt`
* run using `py main.py`

# To generate requirements.txt
* cd to this directory `.\pythonthings\`
* run cmd `pipreqs --encoding=utf8 --force ./ --ignore .venv,Include,Scripts,Lib --use-local`