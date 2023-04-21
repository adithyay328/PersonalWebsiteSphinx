# Optimization
Optimization is a fundamental competency for
SLAM systems and Machine Learning, among
other things. This group of pages
goes over common procedures and concepts within
optimization, many of which underpin other topics
covered on this site.

Below are some topics we will cover.

## Topics

### Linear Least Squares

#### Formulation

Linear Least Squares(LLS) is a common case of optimization, and, using matrix notation,
concerns itself with solving problems of the form $Ax=b$, where $A$ is an MxN matrix,
$b$ is some Nx1 output vector we are given, and $x$ is an Nx1 vector
we want to optimize.

Specifically, we want to optimize $x$ such that the product
$Ax$ is as close to $b$ as possible; this can
be rewritten mathematically as minimizing the L2/Euclidean norm of the difference between
$Ax$ and $b$, which is equivalent to

$$
\DeclareMathOperator*{\argmin}{arg\,min}
\argmin_x ||Ax - b||_2
$$



#### Special Cases

While all Linear Least Squares problems have the above formulation,
there are a couple special variations of this problem that introduce
their own special nuances and approaches. We will cover each of
these special cases by themselves:

- Dealing with a sparse $A$ matrix. Enables a lot of efficient operations
due to sparsity, exploited extensively in SLAM and Factor Graph Optimization
- Dealing with the $A$ matrix being singular. Sometimes occurs, and we need to deal with
this specially
- Dealing with the case where $b$ is the zero vector. Known as homogenous linear least squares,
shows up a lot in computer vision when dealing with homogenous transforms
- Converting problems involving similarity relations into homogenous LLS problems(direct linear transform).
This is one of the main reasons homogenous linear least squares is so useful, atleast with respect
to computer vision and other topics this site is concerned with

#### Approaches

To fully cover Linear Least Squares and deal with all of these special cases,
we will mainly focus on 3 approaches to solving LLS, and ways to adapt
these methods to special cases:
1. Normal Equations
2. QR Decomposition
3. SVD Decomposition

#### Pages
Here is a list of pages on this topic that I've already written; more
will be added in the future.

- [Non-Trivial Homogenous LLS with the SVD](homogenous_linear_least_squares.md)