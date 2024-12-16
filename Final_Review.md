## Chapter 1: What is Data Science?
- Exploration: identifying patterns, (using visualizations)
- Inference: determine whether those patterns are reliable (using randomization)
- Prediction: make informed guesses, (using machine learning)

## Chapter 2: Causality and Experiments
**Observational study**: conclusions based on data that is observed but not actively generated.

*Treatment*: the factor of interest

*Outcome*: result measured on each individual.

Key question: does treatment have an effect on the outcome?

*Assocation*: any relation between treatment & outcome.
- *Causal* association: treatment causes outcome.

How to establish causality? COMPARE treatment vs control group
- *treatment group* receives treatment
- *control group* does not
	- *Confounding variable*: underlying difference between the 2 groups other than treatment
	- groups must be as similar as possible to eliminate confounding variables
	- if outcome differs, can infer causality


## Chapter 13: Confidence intervals, bootstrap
*Percentile*: p'th percentile of a collection = smallest value in the collection that is at least as large as p% of all the values.

*n% Confidence interval*: Interval that will contain the desired quantity n% of the time.
- **NOT: n% OF THE VALUES IN THE SAMPLE LIE IN THIS INTERVAL**

*Resampling*: new samples drawn at random from the original *sample*.

*BOOTSTRAP*: generates new random samples by *resampling* with replacement.
- most helpful for estimating sample median, mean, percentiles
- **key assumption**: sample has the same distribution as underlying population.
From the textbook (https://www.inferentialthinking.com/chapters/13/3/Confidence_Intervals): The bootstrap is an elegant and powerful method. Before using it, it is important to keep some points in mind.
- *Start with a large random sample.* If you don’t, the method might not work. Its success is based on large random samples (and hence also resamples from the sample) resembling the population. The Law of Averages says that this is likely to be true provided the random sample is large.
- To approximate the probability distribution of a statistic, it is a good idea to replicate the resampling procedure as many times as possible. A few thousand will result in decent approximations to the distribution of sample median, especially if the distribution of the population has one peak and is roughly symmetric. We *recommend 1e4 replications in general.*
- The bootstrap percentile method works well for estimating the population median or mean based on a large random sample. However, it has limitations, as do all methods of estimation. For example, it is not expected to do well in the following situations.
- The goal is to estimate the minimum or maximum value in the population, or a very low or very high percentile, or *parameters that are greatly influenced by rare elements of the population.*
- The probability distribution of the statistic is not roughly bell shaped.
- The original sample is very small, say less than 15.

## Chapter 14: Why the Mean Matters
Invariants about random samples can be applied to any sample from any dataset:

*Mean/Average*: sum of all elements of a set, divided by the number of elements of the set. 

*Skewed*: histogram has a tail on one side
- *left-skewed*: mean < median (e.g. 61b midterm scores)
- *right-skewed*: mean > median (e.g. incomes)

*Normal curve*: e^{-x^2}

*Central Limit Theorem*: the distribution of the mean or sum of a bunch of random variables approaches the normal distribution.

## Chapter 15: Prediction (Linear Regression)
Calculating `r`: 
- Convert `x` and `y` to z-scores, call them `z_x` and `z_y`
- `r` = dot product of `z_x` and `z_y` / number of points

`r` describes how well `x` predicts `y`
estimate of `y` = `r*x` when everything is measured as z-scores
- slope: `r` * `y.std` / `x.std`
- intercept: `y.mean` - `slope` * `x.mean`

```
KEY OBSERVATION: 
y 	 - fitted y 	  = residuals
V(y) - V(fitted y)	= V(residuals)
1    - r^2 			    = (1-r^2)
From this, it is clear that 
V(y_hat)/V(y)   = r^2
sd(y_hat)/sd(y) = r
sd(resids)      = sqrt(1-r^2)sd(y)
```

## ｗｈａｔ　ｔｈｅ　ｆrog　ｉｓ　ＴＶＤ

**tl;dr analog of abs(diff between means) for categorical data**

Total variation distance: "distance" between 2 CATEGORICAL DISTRIBUTIONS
- for each category, compute abs(diff in proportions between 2 dists)
- TVD = sum(abs(diff)) / 2
