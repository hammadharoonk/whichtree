# whichtree

![alt text](https://github.com/hammadharoonk/whichtree/blob/main/Output.jpg?raw=true)

## What's included?

Tree suggestion system from CAD blocks, using Lunchbox Neural Network components and Grasshopper. The image files contain a presentation of how the algorithm works, while the .gh files contain the actual algorithm.

Also included is a Python Wikipedia scraping script that looks up Wikipedia pages for a large list of trees, and returns select properties (height, trunk diameter, location) into a CSV that is then used to train a Grasshopper Neural Network with Lunchbox. 

## Description:

Landscape features such as trees are of special interest as non-standard representations. The features of these vector geometries, usually propagated in libraries over the internet and used in the form of CAD blocks, or extended geometries, can be interpreted as humans to understand the ‘green’ nature of a space, by certain visual cues. These 2d representations of trees can potentially provide information on the diameter of the tree crown, density of greenery, ‘bushiness’, or other features that communicate the atmosphere of the space to the reader of the plan. This model was built for the purpose of percieving input vector geometries, 2d representation of trees, and using user-input and implicit data to suggest a tree species to the user.

Tree species by country were obtained from GlobalTree-Search.com, for 15 countries, amounting to 480 distinct species.

## Scraping:

In order to find the type of each tree species, datasets by EU-forest, and Eurasian Research were utilized. These yielded several diverse datapoints; however their collections were aimed at cataloguing trees within forested areas of several countries, and only 120 tree species were described in detail, with max/median height, diameter, etc.
In order to fill the gaps, Wikipedia pages relating to the 480 species were scraped to find the heights of each tree, and filled in where the datasets were lacking. This completed the necessary tree height dataset.

![alt text](https://github.com/hammadharoonk/whichtree/blob/main/Scraping.jpg?raw=true)

