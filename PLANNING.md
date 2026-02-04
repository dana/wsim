# Overview

Going to restart this from scratch with Antigravity.

Further, we're going approach this not having any idea of how to do it.

I think we're going to maybe talk to Gemini about the high level goals, as
well as some middle level goals, and iterate with it about how to achieve
those goals.

So, what am I going to send into Gemini?

# Gemini Prompts

## Background Context

The name of this project is World Simulator.

Globally, a 'tick' is a constant, never changing unit of simulation time,
measured in seconds.  Game time is time passing in the simulation, which is
not the same as real time passing.

I want to be able to rapidly iterate over a large grid that represents the
outside world, each square cell being the same size and having associated
with it some set of attributes that represent some abstract subset of
physical characteristics of a square piece, for now, of land (not open
water).

For a first iteration, I want to simulate the interaction between grass
which grows on the land, rabbits which eat the grass, and foxes which
eat the rabbits.

Fundamentally, I think this is about tracking energy over time.  Energy
comes from the sun, which is gathered by the grass, which causes
the grass to grow and reproduce, storing a portion of the gathered energy.
Rabbits come and consume the grass, which causes them to grow and
reproduce, storing a portion of the gathered energy.  Foxes come and consume
rabbits, which causes them to grow and reproduce, storing a portion of the
gathered energy.

These three things: grass, rabbits and foxes, are entities.

Each entity must be in exactly one cell.  A cell can contain zero or
more entities, eventually the upper limit will be physical space in the
cell compared to the physical space taken up by the entities.

Entities are either mobile or immobile.  For example, grass is an immobile
entity, and rabbits and foxes are mobile entities.  A given cell may have
either zero or one immobile entity of a given type.  For example, a cell
may have a grass entity or not, but it may not have more than one grass
entity.  It can different kinds of immobile entities.

Energy is always measured in kilocalorie, or kcal (kcals plural) for short.

## Possible Cell Attributes

### MaxSolarEnergy

The largest amount of solar energy that immobile entities in a cell can
collect in a tick.  This attribute would match the amount of solar
energy available on the longest, cloudless day.

## Possible Entity Attributes

### Energy

This is a broad abstraction.  For entities, it is the number of kcals
recovered when fully consumed.  So an animal of weight 100 grams will have
about twice the energy as an animal of weight 200 grams.  Energy is
also a measure of the amount of useful sunlight landing on plants that are
able to convert sunlight into chemical energy.

For example, when an entity dies, it starts to rot, which causes its energy
to slowly transfer into the ground until nothing is left of the rabbit.

When an entity eats another entity entirely, the eaten entity is
deleted/deallocated and the eating entity gains an amount of energy about
equal to the total amount of energy in the eaten entity.

### ShedEnergy

How much energy an entity releases per tick.  This is basically the
amount of energy an entity needs to consume in order to not start starving.
Initially this will be a constant.

### EnergyConsumptionRate

This is the amount of energy an entity is able to consume in a given tick
when it is eating/consuming energy.

Concrete example: a rabbit can consume EnergyConsumptionRate units of
energy from grass each tick.  We're going to assume that each cell
gets MaxSolarEnergy of solar energy every tick.  We're going to assume
that half of the cells have a grass entity, and that that grass entity will
receive MaxSolarEnergy and add that to its energy, up to the max.


### EnergyDecompositionRate

This is the amount of energy an entity automatically releases over a tick
when it is dead.

### MaximumEnergy

For mobile entities, this is the largest and fattest the thing can get.
For immobile entities, this is the maximum amount of this thing (grass
for example) that can exist in a given cell.

### MinimumEnergy

For all entities, this is the minimum amount of energy an entitie requires
to be alive.  If energy moves below this number, the entity dies.

### DefaultEnergy

When a mobile entity has Energy below DefaultEnergy, but above MinimumEnergy,
it is hungry and will be increasingly likely to seek out food/Energy.

### CloneInterval

An entity has a 50% chance of producing an exact copy of itself each tick
after CloneInterval ticks have passed.  When the entity clones, that counter
is reset.

## Bringing it together

### Initial Conditions

* There is a 2d array of cells, each cell represents a square,
  physical portion of the outside world.

* Half of all of the cells have a grass entity.

* Half of all of the cells have a rabbit entity.

* Half of all of the cells have a fox entity.

### Example

We're going to assume that MaxSolarEnergy will fall on each cell every tick,
and that the grass entities will all have MaxSolarEnergy added to their energy
totals, up to MaximumEnergy.

Every tick, each rabbit will consider all of the following

* Am I hungry?  An entity is hungry when its Energy attribute is below
  DefaultEnergy.

* Am I safe?  An entity will see if there is danger in its current cell.

Every tick, each rabbit will take zero or more actions, including:

* Eat grass if hungry.

* Move to another cell if not safe.

* Clone if a clone probability check, informed by CloneInterval, is true.

Every tick, each fox will consider all of the following

* Am I hungry?  An entity is hungry when its Energy attribute is below
  DefaultEnergy.

* Am I safe?  For now, foxes are apex predators and so never feel unsafe.

Every tick, each fox will take zero or more actions, including:

* I AM hungry
  * There IS a rabbit in my cell
    * Kill the rabbit
    * Eat some of the rabbit, at a rate defined by EnergyConsumptionRate,
      increasing my no higher than MaximumEnergy
  * There IS NOT a rabbit in my cell
    * Move into an adjacent cell with a rabbit, if available
* I AM NOT hungry
  * Clone if a clone probability check, informed by CloneInterval, is true.
  * Low probability of randomly moving to an adjacent cell.

## What I need help with

I need a way to:

* Efficiently visualize in a web page a 100x100 cell zone
* Efficiently visualize the attributes and entities, along with some of
  their attributes, in each cell.
* "Efficiently visualize" means, among other things, seeing all 10,000
  of the 100x100 cell zone on the same web page, ideally at the same time,
  or at least with easy scrolling to see everythi9ng.
* I want to be able to real-time, in the web app, define which cell
  attributes, which types of entities in each cell and select which entity
  attributes to show.
* This can be very information dense so I think it should heavily leverage
  non-text information, such as colours, lines, shapes.
* I fundamentally want a web page that shows me a 100x100 array of square
  cells, densely displayed by separated and readable.
* This page should have some controls on it allow the user to define which
  attributes in the cell entities should be displayed (in the aforementioned
  information dense format, help me figure that out) and also which entities
  in each cell should be displayed, and finally which attributes in the
  entities.
* On cell click, full, detailed and textual display of all of the attributes
  of the cell, as well as all of the entities, as well as all of the entity
  attributes found in the selected cell.
* This web app displays information that's (frequently) pulled from the
  a backend web server that presents all of the necessary information
  describe above as well defined and well formed JSON files.
* It is expected that some process will frequently change these JSON
  files.
* The web app can just be hard refreshed from the browser in order to get
  updated data from the backend files.

