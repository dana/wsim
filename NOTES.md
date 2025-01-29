# Broad Ideas

- start with JSON for data storage
- switch to something more performant later

# Data

## Zones
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

## Locations
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

## Entities
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

## Entity Info
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
                2kg per m^2 foor stem, half that for root energy

                minimum-temp: at -10C or lower this plant starts to die
                maximum-temp: at 40C or higher this plant starts to die
                That is, this wheatgrass has a very broad temperature range.

                growth-rate: under ideal conditions, this plants energy
                    is multiplied by 1.002 per hour of sunlight.
            "
        }
    }

# Broad Steps

- create code that creates all of the above files in JSON.
- create a web page that shows all 10,000 outside locations in a zone
- this will display a 100x100 grid of coloured circles, each a location
- the web page will take as user input the selected view
- views include all of the entity names/various dynamic fields
- for example, "Bluebunch wheatgrass", "stem-energy"
- the brightness of a circle's colour represents the relative value of a field

