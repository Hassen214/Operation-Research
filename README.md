https://www.overleaf.com/read/dyfxhvwjyrgr#883f49
Latex code file
This is Hassene's approach to solving the problem.

The idea is fairly straightforward.

First, we linearize the problem by transforming the rolling window constraint into a linear constraint. This allows us to leverage linear solvers, such as PULP (an excellent online solver), to find a solution.

Since all cost functions, except for resequencing between shops, rely solely on entry permutations, we can apply an earlier formulation to address these aspects.

Next, we divide the shops into two categories: tone shops and other shops.

For the other shops, the problem can potentially be solved directly using linear solvers, assuming it performs efficiently within a reasonable timeframe.

For the tone shops, one less-than-ideal approach is to exclude the resequencing constraint between shops, as it’s the only constraint involving both permutations. Using a solver, we can first obtain a solution for this simplified problem and then construct 

​
$\(\tilde{\sigma}_s\)$ from it. Once this initial solution is achieved, further improvements could be made.

I also put in the latex code file my formulation for the linear problem. Read it and tell me if you find errors.

This does not work for large instances. One needs to find a greedy approach.







