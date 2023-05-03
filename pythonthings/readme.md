# to install

If you're on a mac, you may need to replace `py` with `python3` in the commands below. You may also need to replace `pip` with `pip3`

* cd to this directory `.\pythonthings\`
* activate a virtual environment using `py -m venv .`
* make sure `pip` is installed `py -m ensurepip`
* check which version of `pip` you've got: \
   * try `pip -V`, it should return a version number, if not:
   * try `pip3 -V` 
* install pip requirements using `pip install -r requirements.txt`
* run using `py main.py`

# To generate requirements.txt
* cd to this directory `.\pythonthings\`
* run `pip install pipreqs`
* run cmd `pipreqs --encoding=utf8 --force ./ --ignore .venv,Include,Scripts,Lib --use-local`'