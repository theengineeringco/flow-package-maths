Using component settings this component can be run in two modes:
- Computes the natural logarithm (base of Euler's constant $e$) of the given `Value`. This expression is typically written as $log_{e}(x)$ or $ln(x)$.
- Computes the logarithm of the given `Value` and its `Base` which can be fed in on the optional `Base` port. If no base is given then the common logarithm (base 10) is used.

The logarithm is the inverse function to exponentiation as shown in the two expressions below:

$$
log_{b}(x) = y
$$
$$
b^{y} = x
$$

For example:

$$
log_{10}(1000) = 3
$$

There are three widely used logarithms:
- Common logarithm, $log_{10}(x)$
- Natural logarithm, $log_{e}(x)$
- Binary logarithm, $log_{2}(x)$

And logarithms have the following interesting properties:
- The logarithm to any base of that base number is always $1$. E.g. $ln(e) = 1$ since $e^{1} = e$.
- The logarithm to any base of $1$ is always $0$. E.g. $log(1) = 0$ since any value to the power of 0 is always one, $10^{0} = 1$.
