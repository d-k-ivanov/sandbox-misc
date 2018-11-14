module Lists where

lostNumbers = [4,8,15,16,23,42] --ghci> let lostNumbers = [4,8,15,16,23,42]"
-- "Steve Bushemi" !! 6
-- [2,5,6,66,7,7,3,5,7] !! 1
list_a = [[1,2,3,4],[5,6,7,8],[10,10,10,10],[11,22,33,44,55,66]]
list_b = [1,2,3,4,5,6,7,8,9,10]
list_c = [1..20]
list_d = [2,4..100]
list_e = ['a'..'z']
list_f = [13,26..24*23]
list_g = [13,26..]
list_null = []

{-
b ++ [[0,0,0,0]]
[8,8,8,8]: b
drop 3 list_c
drop 1000 list_c
maximum list_b !! 3
maximum ( list_b !! 3 )
sum list_e
product list_e
elem 4 list_e
4 `elem` list_e
take 10 (repeat 5)
take 10 (cycle [12,13,14])

-- list generator
[x*2 | x <- [1..10]]
[x*2 | x <- [1..10], x*2 >= 12]
[x | x <- [50..100], x `mod` 7 == 3]
[x | x <- [10..20], x /= 13, x /= 15, x /=19]
[x+y | x <- [1..3], y <- [10,20,30]]
-}

boomBangs xs =      [
  if x < 10
  then "BOOM!"
  else "BANG!"
  | x <- xs, odd x  ]
