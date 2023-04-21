# Non-Trivial Homogenous LLS with the SVD

## Overview
Homogenous LLS is a special
case of Linear Least Squares, and it is quite a common
problem that shows up in Computer Vision and SLAM, for example
for estimating Homography and Fundamental Matrices.

Homogenous LLS is a special case of LLS where $b$ is the zero
vector; this leads to a total optimization problem of the form

$$
\DeclareMathOperator*{\argmin}{arg\,min}
\argmin_x ||Ax - \vec{0}||_2 = \argmin_x ||Ax||_2
$$

One major effect of this property is that the main
approaches to LLS we've covered **only yield the trivial solution**,
which we are oftentimes not interested in.

To get non-trivial solutions we must **add constraints to the given objective
function**.

We'll discuss these notes shortly.

## Why most aproaches of Linear Least Squares don't yield useful results
In other posts(some of which may not be written yet; will update once I write them),
we've covered a couple methods of solving LLS, including using the normal equations.
While these do work(albeit with numerical stability issues in certain cases) on most
LLS problems, we can easily see a problem with them in this special case.

### Applying the normal equations

Let's try and apply the normal equations to this special case right now,
and see what happens.

Writting the problem out as a matrix equation, we want to apply the normal
equations to get a least squares estimate for $x$ in the following equation:

$$
A\vec{x} = \vec{0}
$$

Applying the normal equations, we can determine the least squares solution
through the following steps:

$$
\begin{gather}
A\vec{x} = \vec{0} \\
A^TA\vec{x} = A^T\vec{0} \\
\vec{x} = (A^TA)^{-1}A^T\vec{0}
\end{gather}
$$

At first, this might seem like it worked out just fine. However, looking
at the final expression for $x$, we see something interesting.

Let's start by assuming the expression $(A^TA)^{-1}A^T$ exists, in which
case it is equivalent to some matrix $M$; if $(A^TA)$ is not invertible
this expression isn't defined, and we can't apply the normal equations.
In such cases, we'll look at alternative approaches to LLS.

Assuming $M$ exists, the last equation reduces to

$$
\begin{gather}
\vec{x} = M\vec{0} \\
\therefore \vec{x} = \vec{0}
\end{gather}
$$

In other words, directly applying the normal equations to this problem
**always yields the zero vector as a solution**; the reason this
is the case is that the trivial solution is always a perfect solution
to homogenous linear systems, and thus is also a valid least squares
solution to homogenous systems in all cases.

### Looking for non-trivial solutions

In the previous section, we saw that the normal equation always yield
a zero solution, also know as a **trivial solution**.

Is this a problem? Not really; these are still valid solutions to the least
squares problem. The only thing is that oftentimes, **we are not looking
for trivial solutions**; rather, we are often interested in **non-trivial** solutions
to these problems, which are usually more meaningful to us than the always-available
trivial solution. If we really wanted the trivial solution, we wouldn't even
need to apply least-squares.

With this in place, we need to refine our objective function by adding a constraint
to the solution. The new objective function is

$$\argmin_x ||Ax||_2 \text{  subject to  } |x|_2 = 1$$

Notice that there is a new term here, which is that $x$ must have an L2 norm
of 1. We could've picked any other value for the norm as long as it isn't
zero, but outputting a vector of 