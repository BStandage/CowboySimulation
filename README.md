# CowboySimulation
I ran into a confusing problem in my Probability Theory class and decided to make a simulation out of it. 

## Problem Statement
There are *n* cowboys.

Each cowboy has a gun with unlimited ammunition.

The cowboys stand in a circle, and each cowboy chooses randomly and shoots another cowboy.



The surviving cowboys again form a circle, and the process continues.

**Rules**:   
--no suicides  
--shots are 100% accurate and 100% lethal.

**Examples**
With two cowboys A and B, they must shoot each other. Nobody survives.

With three cowboys A, B, C, maybe A-->B-->C-->A and they all die, or maybe 
A<-->B<--C and C survives.

## What must you solve for?
*f(n)*, the probability that there is one cowboy left alive.

It can be assumed, and easily verified, that *f(2)=0* and *f(3)>0*
