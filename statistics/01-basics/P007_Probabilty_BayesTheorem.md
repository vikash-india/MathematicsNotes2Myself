# Description: Write here

## Write here
------------------------------------- Bayes Theorem (Positive)
Prior = P(C)

Sensitivity = P(Positive | C)               1 - Sensitivity
Specivity   = P(Negative | Not C)           1 - Specivity

P(C, Positive) = P(C) * P(Positive | C)                 - I
P(Not C, Positive) = P(Not C) * P(Positive | Not C)     - II
P(Positive) = I + II

P(C | Positive) = I / P(Positive)
P(Not C | Positive) = II / P(Positive)

------------------------------------- Bayes Theorem (Negative)
Prior = P(C)

Sensitivity = P(Negative | C)
Specivity   = P(Negative | Not C)

P(C, Negative) = P(C) * P(Negative | C)                 - I
P(Not C, Negative) = P(Not C) * P(Negative | Not C)     - II
P(Negative) = I + II

P(C | Negative) = I / P(Negative)
P(Not C | Negative) = II / P(Negative)
------------------------------------- Go From Below
Given: P(Home) or P(Gone) or both
Given: P(Rain|Home)
Given: P(Rain|Gone)

P(Home, Rain) = P(Home) * P(Rain | Home) = .4*.01= .004
P(Gone, Rain) = P(Gone) * P(Rain | Not Home) = .6*.3 = .18
P(Rain) = .184

P(Home|Rain) = P(Home, Rain) / P(Rain) = .004/.184


### Usage


#### Note
- None

##### TODO
- None