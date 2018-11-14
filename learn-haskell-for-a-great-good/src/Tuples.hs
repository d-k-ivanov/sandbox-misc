module Tuples where


{-
(1,2)
[(1,3),(2,4),(5,7)]
[(1,3),(2,4,5),(5,7)]
fst (1,3)
snd (4,5)
zip [1,2,3,4,5] [10,20,30,40,50]
zip [1..] ["one","two","three","four","five", "six", "seven", "eight"]
-}

triples = [(a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10]]
rightTriples = [(a,b,c) | c <- [2..10], b <- [1..10], a <- [1..10], a^2 + b^2 == c^2]
rightTriples' = [(a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10], a^2 + b^2 == c^2, a+b+c == 24]
rightTriples'' = [(a,b,c) | c <- [1..100], b <- [1..100], a <- [1..100], a^2 + b^2 == c^2]



