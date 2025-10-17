# wsim - World Simulator

(Not grandiose at all)

# Broad Steps - backend

- create code that creates all of the above files in JSON.

# somewhat raw thoughts

Don't try to build the game first, build the simulation first.

outside locations are 10m^2
indoor locations are 1m^2

Each location has eight standard exits, in degrees from north: 0, 45, 90,
135, 180, 225, 270, 315

Each has an elevation which provides for slope/difficult terrain across exits.

Grass in a room is an immobile entity ... Weeds would be another immobile
entity. On a cycle immobile entities might consume each other as mobile life
forms do.

We can look at adjacent rooms for information about what an entity will do
for a given tick.

Rabbits eat grass.

Mobile entities have a hunger number that when it stays high adds to their
energy, and when low reduces energy.

Energy is always measured in kilocalorie, or kcal for short.

Each zone is 1km^2 and locations within are given temperature and moisture
based on this zone.

Visibility in a location acts kind of like fog, in that it just lowers what
things can detetect as it geta higher.  For example, high grass lowers
visibility.

We don't have hitpoints.  A mouse can never kill a human, it can inflict
scratches.  Which could get infected.

A human will cause massive internal crushing to a mouse which will cause it
to bleed to death almost instantly.

Grass takes energy from the sun in calories the same way that rabbits take
energy from the grass the same way that foxes take energy from rabbits.

The transfer mechanism differs, as does the quanta.  A rabbit continuously
releases small chunks of energy in small quanta as heat.  When a rabbit dies,
all of its remaining energy is made available, and will slowly transfer into
the ground.  Grass gives energy to rabbits as a room total.  So a rabbit
eating grass reduces the amount of grass in a location, in small quanta.

The sun gives energy to grass in small quanta, variable based on the weather.

A rabbit currently has X energy and must have Y energy available to live, up
to a max of Z energy. 

Z energy is the biggest, plumpest rabbit.

When X energy reaches Y, the rabbit dies of starvation.

A Z energy rabbit will be obese and slow, the fox gets the most energy from
this.

As a body is eaten its energy goes down.  When energy, in kcalories, reaches
0, the body is gone, but perhaps not deallocated.  It might turn into some
hair and bones and blood that fade over time.



Make a web page that shows a 2x2 grid of adjacent independently colored circles in a horizontally and vertically acrollable view where each circle has color ranges based on a selected view, for instance grass energy.  This would start with 100x100 circles/locations.

Perhaps let each circle, by half, show a different selected view, for example grass and weeds.

The underlying data would be more useful for analysis if historical versions were available.

Need to think about how location wide life forms spread between locations.

For plant competition, each type, say thistles, would have a maximum energy absorption.  That is, as light falls on the location, it's energy is given by percentage chunk to all of the plants there.

Thistles that have taken over a local meeting that gave qq max energy collection percentage of 70%, always leaving room for grass to creep in.  Grass can collect energy in wider temp/environment condition than thistles.  When it is warm and wet thistles will get big and slow grass energy growth.  Be cool thistles will die and grass grows more.

Energy of all of the plants in a location does not have a firm max.  There can be heavy grass and heavy thistles, or both can be light.  This amount of energy for a plant informs the text generates for players....how dense and green a location is 

Root energy and stem energy are separate.

Thistles can have big root and but stem energy...but when it cools the stem energy goes down fast until there is no stem.  But it's roots retain potentially high energy, but they can gather no more until after it warms up and they send some root energy to stems, which will then start collecting sun energy.  Stems collecting sun energy keep a percentage for the stem and send the rest to the roots.

Grass has mostly stem energy but it doesn't lose very much when it is cool or cold.  But it gathers some but little sun energy when cold.

When plants and animals die and rots the ground gets most or all of their energy.  This causes the ground to be more rich and depending on the plant help them grow better.

# Project Layout

Top level directories

## gdata

The following files (by example) are in the gdata directory.

### zones.json
zones =
```json
    {   "z1": {
            "comments": "
                this requires some additional thought.
                what initially comes to mind is a bunch of parameters
                that kind of simulates weather patterns.
                Instead of that, perhaps find a historical data source
                for temp/rain/snow in a given real location and
                reference that data source here, so we can, hour by hour,
                plug that real-life data in.
            "
        }
    }
```

### locations.json
locations =
```json
    {   "l1": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [
                "e1", "e2", "e3", "e4"
            ],
            "exits": {
                "0": {
                    "to": "l2",
                }, "45": {
                    "to": "l102",
                }, "90": {
                    "to": "l101",
                }
            }
        },
        "l2": {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
            "exits": {
                "0": {
                    "to": "l3",
                }, "45": {
                    "to": "l103",
                }, "90": {
                    "to": "l102",
                }, "135": {
                    "to": "l101",
                }, "180": {
                    "to": "l1",
                }
            }
        }
    }
```

### entities.json
entities = 
```json
    {   "e1": {
            "name": "Eastern Cottontail",
            "type": "animal",
            "energy": 4000,
        },
        "e2": {
            "name": "Bluebunch wheatgrass",
            "type": "plant",
            "stem-energy": 312500,
            "root-energy": 156250,
            "comments": "
                above energy is based on 3125 kcal/kg of wheatgrass,
                one kilo per m^2,
                100 m^2 in an outside location.

                Also we're going for root energy as half of the stem energy.
            ",
        },
        "e3": {
            "name": "Canada thistle",
            "type": "plant"
            "stem-energy": 312500,
            "root-energy": 156250,
            "comments": "
                Most of their energy is in their roots.
            "
        },
        "e4": {
            "name": "loam",
            "type": "ground",
            "energy": 10240,
            "comments": "
                energy for ground represents a kind of fertility.
                when things rot in this location, some/all of their
                energy goes into the ground.
                plants get most of their energy from the sun, but they do
                extract a bit from the ground.
            "
        }
    }
```

### entityInfo.json
entityInfo =
```json
    {   "Eastern Cottontail": {
            "default-energy": 4000,
            "minimum-energy": 2000,
            "maximum-energy": 8000
        },
        "Bluebunch wheatgrass": {
            "default-stem-energy": 1000,
            "default-root-energy": 2000,
            "maximum-stem-energy": 625000,
            "maximum-root-energy": 312500,
            "minimum-temp": -10,
            "maximum-temp": 40,
            "growth-rate": 1.002,
            "comments": "
                for plants, the default root energy starts low,
                and default stem energy starts very low.

                Maximum energy for a location?  Let's go with
                2kg per m^2 for stem, half that for root energy

                minimum-temp: at -10C or lower this plant starts to die
                maximum-temp: at 40C or higher this plant starts to die
                That is, this wheatgrass has a very broad temperature range.

                growth-rate: under ideal conditions, this plants energy
                    is multiplied by 1.002 per hour of sunlight.
            "
        }
    }
```

## backend

This directory holds a modern Python, standards and PEP compliant Flask
based REST API server, called backend-server.
backend-server will also handle the actual background computations that make
up the logic of wsim.

On startup, backend-server will read the JSON files in the gdata/ directory,
each file's contents into a global dictionary variable called "gdata".  gdata
will have a top level key for each of the files in the gdata/ directory.
Below is an incomplete example, based on the example data defined above:

```python
gdata["locations"] = {
    "l1": {
        "in-zone": "z1",
        "type": "outside",
        "entities": [
            "e1", "e2", "e3", "e4"
        ]
    }
}
gdata["entities"] = {
    "e1": {
        "name": "Eastern Cottontail",
        "type": "animal",
        "energy": 4000
    }
}
```

Every 10 seconds, backend-server will write the current in memory contents
of gdata back to the files as described previously.

The REST route base path is /wsim/v1/

There will be a REST GET route for each of the top level gdata attributes.

For example:

```bash
$ curl http://localhost:5000/wsim/v1/entities
{  
   "status" : "success",
    "entities": {
         "e1": {
            "name": "Eastern Cottontail",
            "type": "animal",
            "energy": 4000,
        },
        "e2": {
            "name": "Bluebunch wheatgrass",
            "type": "plant",
            "stem-energy": 312500,
            "root-energy": 156250,
            "comments": "
                above energy is based on 3125 kcal/kg of wheatgrass,
                one kilo per m^2,
                100 m^2 in an outside location.

                Also we're going for root energy as half of the stem energy.
            ",
        },
    }
}
```

# Broad Approach

- start with JSON for data storage
- switch to something more performant later
