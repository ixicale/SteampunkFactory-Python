# Optparse & Flask restuful

This section contains a structrucure examples to init 2 apis into one out port.

The main structrucure is the next:

```
Project/
    __init__.py <- run project
    config/
    |   __init__.py
    |   flask.py <- run Optparse to flask app
    |   url_api.py <- each api consume the same url, define envoirements
    |   server.py <- select envoirement

    helper/
    |   __init__.py
    |   base_controller.py <- exported to each endpoint

    util/
    |   __init__.py
    |   world/
        |    __init__.py <- function endpoints(Api)
        |    endpoint1.py <- Class Country
        |    endpoint2.py <- Class City

    |   factory/
        |    __init__.py <- function endpoints(Api)
        |    endpoint1.py <- Class Component
        |    endpoint2.py <- Class Device
```


## Config
Into config folder we can found the most important files

Files that we can found here:
* **flask**: The main file to own project, here we set some flags to run commands to define some attributes for own Flask App (port, debug, host). This file is called to run the flask project.
* **Server**:  to consume another apis (in case we develop another and want to consume). Here we can select some envoirement where the app works. Server has the **curl function** to make request to another urls.
* **url_api**: the auxiliar for server. Contain a object to set default url by envoirement. Like server file, it **is not** so important and you can ommit.


## Helper

The helper folder. Here you can drop all your files with functions (like the name says) to help own apis to work.

Helper folder contains an unique file called **base_controller**, this file calls own server file and run with the envoirement selected. **base_controller** contains the class BaseController, it imports and uses flask_restful and server class. It works like the interpreter for each endpoint into own flask app.

BaseController start own endpoint like a request, just need to define your methods get, post or put (or another one) like:

```python
def get(self):
    response = "hello world"
    # TODO
    return response
```


## Util

Into Util folder, we define own apis and the `__init__` file, `__init__` files are required to make Python treat the directories as containing packages, so each api folder must contains also their `__init__` file.

When we create an api folder with their endpoints, into `__init__` file we must define own endpoints calling all class coded by api, for example:

We have the structrucure like this:

```
factory/
    __init__.py <- function endpoints(Api)
    endpoint1.py <- Class Component
    endpoint2.py <- Class Device
```

We contains 2 files (*endpoint1 & endpoint2*), so into `__init__` we must declare own endpoints, I declare a function to set endpoints by flask api just like this:

```python

from util.world.endpoint1 import Country
from util.world.endpoint2 import City


"-------- Set paths by class imported"
def endpoints(flask_api):
    flask_api.add_resource(Country, '/world/ep1')
    flask_api.add_resource(City, '/world/ep2')

```


## We did finish structrucure, so what now?

Okay, the last think that you must to do is: **run the Project!**

You can create a `run.py` file or use the `__init__` file and call your functions by each api and call the flask file into config. If you follow this tutorial or do something similar, your code will be like the next one:

```python
from config.flask import service, run
from util.world import endpoints as world_api
from util.factory import endpoints as factory_api

if __name__ == '__main__':
    world_api(service)
    factory_api(service)
    run()

```


# Run the project!

When we call run(), we can write the execute command like you define. My example is to execute:

> `python3 __init__.py -H 0.0.0.0 -P 9000`

or you can execute your file

> `python3 run.py -H 0.0.0.0 -P 9000`


**Remember!**

To configure your flags, go to **config/flask.py** and set all commands that you want

I hope this documentation has been useful.
## (^o^)/
