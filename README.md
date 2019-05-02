# Content-Based-Image-Retrieval

When building an image search engine we will first have to index our dataset. Indexing a dataset is the process of quantifying our dataset by utilizing an image descriptor to extract features from each image.
An image descriptor defines the algorithm that we are utilizing to describe our image.

The important takeaway here is that the image descriptor governs how the image is quantified.
Features, on the other hand, are the output of an image descriptor. When you put an image into an image descriptor, you will get features out the other end.
In the most basic terms, features (or feature vectors) are just a list of numbers used to abstractly represent and quantify images.

Feature vectors can then be compared for similarity by using a distance metric or similarity function. Distance metrics and similarity functions take two feature vectors as inputs and then output a number that represents how “similar” the two feature vectors are.
Given two feature vectors, a distance function is used to determine how similar the two feature vectors are. The output of the distance function is a single floating point value used to represent the similarity between the two images.

The 4 Steps of Any CBIR System

1. Defining your image descriptor: At this phase you need to decide what aspect of the image you want to describe. Are you        interested in the color of the image? The shape of an object in the image? Or do you want to characterize texture? 

2. Indexing your dataset: Now that you have your image descriptor defined, your job is to apply this image descriptor to each image in your dataset, extract features from these images, and write the features to storage (ex. CSV file, RDBMS, Redis, etc.) so that they can be later compared for similarity. 

3. Defining your similarity metric: Cool, now you have a bunch of feature vectors. But how are you going to compare them? Popular choices include the Euclidean distance, Cosine distance, and chi-squared distance, but the actual choice is highly dependent on (1) your dataset and (2) the types of features you extracted. 

4. Searching: The final step is to perform an actual search. A user will submit a query image to the system and your job will be to (1) extract features from this query image and then (2) apply your similarity function to compare the query features to the features already indexed. From there, you simply return the most relevant results according to your similarity function. 

These are the most basic 4 steps of any CBIR system. As they become more complex and utilize different feature representations, the number of steps grow and a substantial number of sub-steps are added to each step mentioned above. For the time being, let’s keep things simple and utilize just these 4 steps.

![alt text](https://www.researchgate.net/profile/Ahmed_Amin43/publication/310465433/figure/fig1/AS:429744039698434@1479470371504/Block-diagram-of-Content-Based-Image-Retrieval-5.png)
