# ahogeotagger
Uses the very efficient ahocorasick search library with a pre-bundled list of cities, states and countries to tag locations in text.

## Requirements

- Python 3.6 or higher
- pyahocorasick 1.4.0 or higher

## Installation

Using PIP via PyPi

```
pip install ahogeotagger
```

## Usage

Right now the usage is pretty simple. You import and init the tagger with the number of cities you want to search through. The cities are in order of population (Tokyo, then New york etc.).

```
from aholocationtagger import tagger
tagger.init(num_cities = 10000)
```

To search whether text contains locations, supply any plain text to the search function like this:

```
results = tagger.search('New york and London are are competing for tech talent')
print(results)
```

This produces the following list of tuples as a result
```
[(0, 7, 'New York', 'New York', 'United States', 'US', 'USA', 19354922, 40.6943, -73.9249), 
 (13, 18, 'London', 'London, City of', 'United Kingdom', 'GB', 'GBR', 8567000, 51.5, -0.1167)]
```
Each tuple always contains values in this order ```start_index``` for the match in the source string, ```end_index```, ```city```, ```state```, ```country```, ```iso2```, ```iso3```, ```population```, ```latitude```, ```longitude```
