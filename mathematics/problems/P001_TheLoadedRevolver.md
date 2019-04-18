# Description: The Loaded Revolver

### Problem
Let’s play a game of Russian roulette. You are tied to your chair. Here’s a gun, a revolver.
Here’s the barrel of the gun, six chambers, all empty. Now watch me as I put two bullets into
the barrel, into two adjacent chambers. I close the barrel and spin it. I put a gun to your head
and pull the trigger. Click. Lucky you! Now I’m going to pull the trigger one more time. Which
would you prefer: that I spin the barrel first or that I just pull the trigger?”

### Solution
Assume that the barrel rotates clockwise after the hammer hits and is pulled back. You
are given the choice between an unconditional and a conditional probability of death. Select a
chamber C at random from the 6 choices.

In the case the barrel is spun again, the probability of death is the (unconditional) probability
that C contains a bullet, which is 2/6 = 1/3.

If the trigger is pulled without the extra spin, the probability is P(A|B), where A is the
event that C contains a bullet and B is the event that the slot next to C in the counterclockwise
direction is empty (as this is the slot that was clicked on the previous time). Now P(B) = 4/6
and P(A ∩ B) = 1/6 (only one chamber contains a bullet and has an empty chamber next to it
in the counterclockwise direction), so P(A|B) = 1/4.

The above is written with absolute mathematical precision. More informally, you may argue,
in the second case, that only one of the four empty slots will lead to your death if the trigger is
pulled again. Note also that if the two bullets are not next to each other, two empty slots will
result in your death if the trigger is pulled again, so the second probability now equals 1/2 and
you should ask for the barrel to be spun again.

### Notes
* None