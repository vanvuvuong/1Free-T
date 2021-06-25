
## 1. Install the requirements.txt to run the scripts

```
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## 2. Guide to run the script

### 2.1. Copy the csv file to `files`

### 2.2 Change the mySQL configuration & database information in `config/mysql.sample.ini` and change the name to `config/mysql.ini`

### 2.3 Run script

```
python3 main.py --file files/samples.csv --deli ,
```

##### Note: Please note that some csv file have the different delimiter, you could change
##### them in line 40 in `main.py`  