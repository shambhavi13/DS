---
Question 1
You are given a train data set having 1000 columns and 1 million rows. The data set is based on a classification problem. Your manager has asked you to reduce 
the dimension of this data so that model computation time can be reduced. Your machine has memory constraints. What would you do? (You are free to make practical assumptions.)
---
# Answer 1

1. Random sample dataset: 
We can create a smaller dataset by random sampling (to avoid bias) for example we can sample 1000 columns and 400,000 rows to do computations
2. PCA (Principal component analysis): 
Use PCA technique to extract important variables. PCA basically extracts low dimensional set of features from  high dimensional dataset.
3. Online learning algorithm: 
In batch learning algorithm take batches of training data to train model (multi pass). Whereas online learning algorithm use one pass over the data, it basically takes an initial guess model
and then picks up one-one observation from training population and recalibrates the weights on each input parameter. The one pass over the data makes it computationally much faster.
Vowpal Wabbit is most widely used ML library for online learning
4. Building linear model with SGD
We use gradient descent for linear model. Basically partially derivative over weights. An iterative training procedure defined by simple weight update formula. This maths works fine until the amount of data
isn't very huge. There is an issue with this approach (batch gradient descent)  gradient evaluation requires the summation of some values for every object from training set. 
In other words, the algorithm requires a lot of iterations, at every iteration we have to recompute weights with formula which have a sum  ∑ℓ𝑖=1  over the whole training set. To tackle this issue we can use
stochastic gradient descent, where we update the weights only over single training sample.

---
Question 2
You are given a data set on cancer detection. You’ve built a classification model and achieved an accuracy of 96%. Why shouldn’t you be happy with your model performance? What can you do about it?
---

# Answer 2

For cancer detection classification model the model will predict either the patient have cancer or do not have cancer. With accuracy of 96% it can be possible that model is predicting majority class correctly but our class of 
interest is minority class which can be people who actually got diagnosed cancer. This can be a case of imbalanced data. In an imbalanced data set accuracy should not be used to measure the performance. We can use sensitivity (True positive rate), 
F1 measure to determine class wise performance of the classifier. We can also perform steps like:
1. undersampling and oversampling or SMOTE to make the data balanced
2. Assign weights to classes such that minority class gets larger weight
3. Generate synthetic data

---
Question 3
You realize that your model is suffering from low bias and high variance. Which algorithm should you use to tackle it? Why?
---

# Answer 3
Low bias and high variance occur when model predicted value is near actual values i.e model pays lot of attention to training data and it becomes flexible to mimic training data but this kind model has no generalisation capabilities. That means when model is 
tested on unseen data it has high error rates on test data. To tackle this 
1. we can use Bagging algorithm (like random forest) Bagging algorithms divides a data set into subsets made with repeated randomized sampling. Then these samples are used to generate a set of models using a single learning algorithm. 
Later the model predictions are combined using voting (classification) or averaging (regression) [ensemble ML algorithm]
2. Regularization technique where higher model coeffiencts gets penalized lowering model complexity
3. Use top features with all variable in dataset model is over complex.