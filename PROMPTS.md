# Log of all gemini prompts used

Each second level header below is a github branch/PR.
Each third level header is a specific prompt effort,
and everything in text blocks is what was actually sent to gemini as a
prompt.

## create-backend

### Initial data files

Run in ~wsim

```text
As described in NOTES.md, there is a top level directory called "gdata/"

In this directory, ensure a locations.json file exists which represents a
grid of outside locations.

Please write a stand alone python program that will create a JSON file in
gdata/ called locations.json that contains a single very large JSON document.

The key of this document is the name of the location, which will run
between l1 to l100000.  Under each of these locations, there will be several
attributes, these three will be the same in all 10,000 locations.
    {   "l1": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
        }
    }

In addition to "in-zone", "type" and "entities", there will be another
attribute called "exits", which is an dictionary, where each key is an
exit name, even though it is an integer.  Here is how the exit names
associate with compass directions:

    * 0 - north
    * 45 - northeast
    * 90 - east
    * 135 - southeast
    * 180 - south
    * 225 - southwest
    * 270 - west
    * 315 - northwest

So, as an example, these the exits in location "l1" connect "90"(east) to
location "l2":

    {   "l1": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
            "exits": {
                "90": {
                    "to": "l2"
                }
            }
        }
    }

The JSON file the program constructs must have 10,000 different locations
in it, each location fully connected, as much as possible, to adjacent
locations.

These locations should form a 100 x 100 square.  The full
entry for "l1" is as follows:

    {   "l1": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
            "exits": {
                "90": {
                    "to": "l2"
                },
                "135": {
                    "to": "l102"
                },
                "180": {
                    "to": "l101"
                }
            }
        }
    }

The full entry for "l102" is as follows:

    {   "l102": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
            "exits": {
                "0": {
                    "to": "l2"
                },
                "45": {
                    "to": "l3"
                },
                "90": {
                    "to": "l103"
                },
                "135": {
                    "to": "l203"
                },
                "180": {
                    "to": "l202"
                },
                "225": {
                    "to": "l201"
                },
                "270": {
                    "to": "l101"
                },
                "315": {
                    "to": "l1"
                }
            }
        }
    }

Please have the program create the necessary JSON file with the
above described 10,000 location attributes containing the above
defined values.
```
### Initial project

Run in ~wsim

```text
Please create this project as described in NOTES.md and elsewhere,
including all of the necessary directory structure, configuration and
support files.

This should be fully testable by the 'tox' python framework.

Each API call should be testable and tested by command-line curl calls.

This is being built on and deployed to Ubuntu 24.  Make sure what you produce
passes all tests after a command-line 'tox' invocation.  Produce detailed
instructions in the README.md detailing how to configure and activiate a
typical Python venv virtual environment.

This project will be hosted on github: ensure all all standard support
and documentation files appropriate for a new github, modern python project
are included.

Use no mock objects or mocking of any kind for testing.

The test suite should run a flask server on a random, dynamic port, and then
tests should initiate HTTP methods on various routes in the flask server.  The
test suite should be fairly comprehensive.

This project should be run in a standard venv Python environment for a REST Flask
server.  Please add detailed instructions in the README.md about how to set this up on
a standard Ubuntu 24 system, how to activate the environment, and how to run the REST
Flask server in a development test as well as a production capacity.

```

Now fix the problem:
```
(venv) $ flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.
(venv) $ 

Please resolve this error, and/or tell me how to correctly run the app in development mode.

```
