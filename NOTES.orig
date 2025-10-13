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



# raw thoughts

I e-mailed these to myself in the middle of the night.  They are rough,
incomplete, with errors, but here they are.

These thoughts are what directly drove the stuff commited here so far.


Don't try to build the game first, build the simulation first.

Build the minimum sim that is interesting.

Both city and country.

Research such open simulations.


Simulation at a low level as a basis for a high level simulation both of playable. 


Each location, outside, is 10m^2 and indoor is 1m^2

Each location has eight standard exits. N, nw, etc but perhaps named differently

Each has an election which provides for slope/difficult terrain across exits.

Grass Ina room is a lifeform ... Weeds would be another lifeform. On a cycle they consume each other as mobile life forms do.

We can look at adjacent rooms for information about what a life form will do for a given tick.

Rabbits eat grass.

Animals have a hunger number that when it stays high adds to the fat reserve, and when low reduces fat reserve.

Come up with a name for fat reserve that encapsulates plants.

Each zone is 1km^2 and locations within are given temperature and moisture based on this zone

Visibility in a location is kind of a fog, just lowers what things can detetect as it geta higher.

High grass for example lowers visibility.

We don't have hitpoints.  A mouse can never kill a human, it can inflict scratches.  Which could get infected.

A human will cause massive  internal crushing to a mouse which will cause it to bleed to death almost instantly.

Future ML tools will, as a way to top down refactor for example legacy code vases, ingest the view/screen/browser of all of the users of the legacy app, and then make changes/refactor the underlying code.

Grass takes energy from the sun in calories the same way that rabbits take energy from the grass the same way that foxes take energy from rabbits.

The transfer mechanism differs, as does the quanta.  A rabbit only gives energy only after it dies.  Grass gives energy to rabbits as a room total.  So a rabbit eating grass reduces the amount of grass, in small quanta.

The sun gives energy to grass in small quanta, variable based on the weather.

Energy rather than the previously mentioned fat reserves.

A rabbit has X energy and must have Y energy available to live, up to a max of Z energy. 

Z energy is the biggest, plumpest rabbit.
X energy is a rabbit that just died of starvation, which happened when Y energy fell to X.

A Z energy rabbit will be obese and slow, the fox gets the most energy from this.

As a body is eaten it's energy goes down.  When energy, in kcalories, reaches 0, the body is gone, but perhaps not deallocated.  It might turn into some hair and bones and blood that fade over time.

How to make weeds and grass compete when they are location wide life forms

Complicated. In real life there are root systems and all sorts of other mostly invisible complications.

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



