# Airbnb Clone
## Description
This is a simple clone of the Airbnb website. It is a project for the Holberton School. It is a simple console that allows you to create, update, destroy, and show objects. It also allows you to store and retrieve objects from a JSON file.

## Installation
Clone this repository in your terminal:
```bash
$ git clone https://github.com/jackiejoe45/AirBnB_clone.git
```
## Usage
To start the console, run the following command:
```bash
$ ./console.py
```

To quit the console, use the following syntax:
```bash
(hbnb) quit
```
To help, use the following syntax:
```bash
(hbnb) help
```
To create an object, use the following syntax:
```bash
(hbnb) create <class name>
```
To show an object, use the following syntax:
```bash
(hbnb) show <class name> <object id>
```
To destroy an object, use the following syntax:
```bash
(hbnb) destroy <class name> <object id>
```
To update an object, use the following syntax:
```bash
(hbnb) update <class name> <object id> <attribute name> "<attribute value>"
```
To show all objects, use the following syntax:
```bash
(hbnb) all
```
To show all objects of a class, use the following syntax:
```bash
(hbnb) all <class name>
```

## Examples
```bash
(hbnb) create BaseModel
>>> 1234-1234-1234

(hbnb) show BaseModel 1234-1234-1234
>>> [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'updated_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000)}

(hbnb) destroy BaseModel 1234-1234-1234
>>> [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'updated_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000)}

(hbnb) update BaseModel 1234-1234-1234 name "Betty"
>>> [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'updated_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'name': 'Betty'}

(hbnb) all
>>> [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'updated_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'name': 'Betty'}

(hbnb) all BaseModel
>>> [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'updated_at': datetime.datetime(2020, 2, 19, 23, 55, 38, 544000), 'name': 'Betty'}

(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
>>> $

```
