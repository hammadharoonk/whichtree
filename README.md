# whichtree
Tree suggestion system from CAD blocks, using Lunchbox Neural Network components and Grasshopper. The image files contain a presentation of how the algorithm works, while the .gh files contain the actual algorithm.

Also included is a Python Wikipedia scraping script that looks up Wikipedia pages for a large list of trees, and returns select properties (height, trunk diameter, location) into a CSV that is then used to train a Grasshopper Neural Network with Lunchbox.

There are 3 visual categories: Tree, Shrub, Palm

From GlobalTreeSearch, I collected a list of trees in each country in Europe. This was juxtaposed with EU-forest, another database that contains occurrences of tree species in Europe.

Finally, trees by country were juxtaposed by proportion of large diameters to small diameters. Items of large diameters larger than a ratio of 0.6 were classified as trees, smaller than ratio of 0.3 were classified as shrubs, and 

These were placed in visual categories according to this Wikipedia page:
https://en.wikipedia.org/wiki/List_of_trees_and_shrubs_by_taxonomic_family
