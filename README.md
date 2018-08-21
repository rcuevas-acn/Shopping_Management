# Shopping_Management
Python Back-end Services for Shopping Management System

## System Requirements
- Python 3.6.0 or Higher
- MySQL 8.0.12
- MySQL Workbench

## Configuration
Make sure URL of SQL is correct under the constants.py and database is created\

Database creation script:\
On MySQL Workbench, execute:
```buildoutcfg
CREATE DATABASE Shopping_Management;
```
URL Format:
```buildoutcfg
mysql+pymysql://<user>:<password>@localhost:3306/shopping_management
```
## Install required libraries
On command line, execute:
```buildoutcfg
pip install -r requirements.txt --ignore-installed
```
## To run locally
On command line, execute:
```buildoutcfg
python run.py
```
## To run tests
On command line, execute:
```buildoutcfg
pytest
```
## API List
> **http://localhost:8080/api/shopping_list**
- **Get method**
    - Listing of Shopping List with Items
```buildoutcfg
    http://localhost:8080/api/shopping_list?id=1
    http://localhost:8080/api/shopping_list?title=List
    http://localhost:8080/api/shopping_list?item_id=1
    http://localhost:8080/api/shopping_list?name=Item
```
- **Post method**
    - Insert Shopping List
```buildoutcfg
    {
        "store_name": "Toy Store",
        "title": "Birthday Gift"
    }
```  
- **Put method**
    - Update Shopping List parameterized by id
```buildoutcfg
    http://localhost:8080/api/shopping_list?id=3
    
    {
        "title": "Birthday Gift2019"
    }
```  
- **Delete method**
    - Delete Shopping List parameterized by id
```buildoutcfg
    http://localhost:8080/api/shopping_list?id=5
```  
> **http://localhost:8080/api/items**
- **Post method**
    - Insert Shopping List parameterized by shopping_list_id
```buildoutcfg
    http://localhost:8080/api/shopping_list?id=4
    
    {
	    "items": [
		    {
    		    "item_id": 4,
    		    "name": "Toy",
    		    "quantity": 1
		    }
	    ]
    }   
```
### Reference Link
https://docs.python.org/3/library/subprocess.html\
http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#quickstart\
http://flask-sqlalchemy.pocoo.org/2.3/queries/\
http://flask-sqlalchemy.pocoo.org/2.3/models/\
https://stackoverflow.com/questions/3325467/elixir-sqlalchemy-equivalent-to-sql-like-statement\
https://developer.lsst.io/python/numpydoc.html#py-docstring-other-parameters\
https://docs.pytest.org/en/latest/getting-started.html#getstarted\

