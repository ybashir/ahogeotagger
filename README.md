# ahogeotagger

If you have thousands of passages of text and you want to search them for hundreds or thousands of search strings, the process can become very cumbersome very soon. This is where ahocorasick search becomes very relevant and blazingly fast. You can read more about the algorithm [here](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm). 

This code combines the [very efficient implementation of ahocorasick](https://github.com/WojciechMula/pyahocorasick/) in python with a pre-bundled list of cities, states and countries to tag locations in text.

## Requirements

- Python 3.6 or higher
- pyahocorasick 1.4.0 or higher

## Installation

Using PIP via PyPi

```
pip install ahogeotagger
```

## Usage

Right now the usage is pretty simple. You import and (optionally) init the tagger with the number of cities you want to search your text for, otherwise it searches the top 5000 cities by default. The cities are in order of population (Tokyo, New york, Mexico City etc.). 

The data for these cities has been prepopulated from the free version of simplemaps database which you can find [here](https://simplemaps.com/data/world-cities).

To search whether text contains locations, supply any plain text to the search function like this:

```
from ahogeotagger import tagger
results = tagger.search('New york and London are are competing for tech talent')
print(results)
```

This produces the following list of tuples as a result
```
[(0, 7, 'New York', 'New York', 'United States', 'US', 'USA', 19354922, 40.6943, -73.9249), 
 (13, 18, 'London', 'London, City of', 'United Kingdom', 'GB', 'GBR', 8567000, 51.5, -0.1167)]
```
Each tuple always contains values in this order ```start_index``` (for the match in the source string), ```end_index```, ```city```, ```state```, ```country```, ```iso2```, ```iso3```, ```population```, ```latitude```, ```longitude```

Optionally, you can provide the number of top cities you want to search your text for:

```
tagger.init(num_cities = 10000)
```

Also, optionally, if you dont want to use the built-in database of cities, you can provide your own list of cities. The list needs to be a list of tuples with each tuple's values in the following order: 

_(id,city,state,country,iso2,iso3,population,lat,lng)_

The types for ```id``` and ```population``` is ```int```, for ```lat``` and ```lng``` its ```float``` and for all the other values its ```String```.

```
tagger.init(num_cities = 500, cities = [a,b,c])
```

where a,b,c are tuples described above.


