# Description: The Ants Problem

### Problem
Three ants are sitting at the three corners of an equilateral triangle. Each ant starts randomly picks a direction and 
starts to move along the edge of the triangle. What is the probability that none of the ants collide?

### Solution
Each of the ants can move in 2 direction - clockwise or anti-clockwise. Total combination will be 2 * 2 * 2 = 8.

The ants can only avoid a collision if they all decide to move in the same direction - either clockwise or 
anti-clockwise. Hence there are just 2 ways out of possible 8 ways in which they can avoid collision. 

P(No collision) = 2/8 = .25 

Alternatively, If the ants do not pick the same direction, there will definitely be a collision. Each ant has the 
option to either move clockwise or anti-clockwise. There is a one in two chance that an ant decides to pick a particular 
direction. 

P(No collision) = P(All ants go in a clockwise direction) + P( All ants go in an anti-clockwise direction) 
or, P(No collision) = 0.5 * 0.5 * 0.5 + 0.5 * 0.5 * 0.5 = 0.25

### Notes
* None