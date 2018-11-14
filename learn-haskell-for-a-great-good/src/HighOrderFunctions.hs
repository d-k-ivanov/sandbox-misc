module HighOrderFunctions where

mulThree :: Int -> (Int -> (Int -> Int))
mulThree x y z = x * y * z

mulTwoWithNine = mulThree 9

compareWithHundred :: Int -> Ordering
compareWithHundred  x = compare 100 x

compareWithHundred' :: Int -> Ordering
compareWithHundred'  = compare 100

divideByTen :: (Floating a) => a -> a
divideByTen = (/10)

isUpperAlpha :: Char -> Bool
isUpperAlpha = (`elem` ['A' .. 'Z'])

applyTwice :: (a -> a) -> a -> a
-- applyTwice :: (a -> a) -> a -> a
applyTwice  f x = f (f x)

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: ( a -> b -> c) -> b -> a -> c
flip' f y x = f x y
-- Non-Carried version
flip'' :: ( a -> b -> c) -> (b -> a -> c)
flip'' f = g
 where g x y = f y x

flip''' :: (a -> b -> c) -> b -> a -> c
flip''' f = \x y -> f y x

map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

map'' :: (a -> b) -> [a] -> [b]
map'' f xs = foldr (\x acc -> f x : acc) [] xs

map''' :: (a -> b) -> [a] -> [b]
map''' f xs = foldl (\acc x ->  acc ++ [f x]) [] xs

{-
map' (++ "-xx") ["aa","bb","cc","dd"]
["aa-xx","bb-xx","cc-xx","dd-xx"]
[x ++ "-xx" | x <- ["aa","bb","cc","dd"]]
["aa-xx","bb-xx","cc-xx","dd-xx"]
-}

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
  | p x       = x : filter' p xs
  | otherwise =     filter' p xs

filter'' :: (a-> Bool) -> [a] -> [a]
filter'' p = foldr (\x acc -> if p x then x : acc else acc) []

{-
filter' (<15) (filter' even [1..20])
[2,4,6,8,10,12,14]
[ x | x <- [1..20], x < 15, even x ]
[2,4,6,8,10,12,14]
-}

quicksort' :: (Ord a) => [a] -> [a]
quicksort' [] = []
quicksort' (x:xs) =
  let smaller = quicksort' (filter' (<= x)  xs)
      bigger  = quicksort' (filter' (> x)   xs)
  in  smaller ++ [x] ++ bigger

largerInvisible :: Integer
largerInvisible = head (filter' p [100000,99999..])
  where p x = x `mod` 3829 == 0

-- sum (takeWhile (<10000) (filter' odd (map' (^2) [1..])))
-- sum (takeWhile (<10000) [ m | m <- [n^2 | n <- [1..]], odd m])

chain :: Integer -> [Integer]
chain 1 = [1]
chain n
  | even n = n:chain (n `div` 2)
  | odd n = n:chain (n*3 +1)

numLongChains :: Int
numLongChains = length (filter' isLong (map' chain [1..100]))
  where isLong xs = length xs > 15

numLongChains' :: Int
numLongChains' = length (filter' (\xs -> length xs > 15) (map' chain [1..100]))

-- zipWidth (\a b -> (a * 30 + 3) / b) [5,4,3,2,1] [1,2,3,4,5]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

addThree' :: Int -> Int -> Int -> Int
addThree' = \x -> \y -> \z -> x + y + z

sumL :: (Num a) => [a] -> a
sumL xs = foldl (\acc x -> acc + x) 0 xs

sumL':: (Num a) => [a] -> a
sumL' = foldl (+) 0

sumR :: (Num a) => [a] -> a
sumR xs = foldr (\acc x -> acc + x) 0 xs

elem' :: (Eq a) => a -> [a] -> Bool
elem' y ys = foldl (\acc x -> if x == y then True else acc) False ys

maximum' :: (Ord a) => [a] -> a
maximum' = foldl1 max

reverse' :: [a] -> [a]
reverse' = foldl (\acc x -> x : acc) []

reverse'' :: [a] -> [a]
reverse'' = foldl (flip (:)) []

product' :: (Num a) => [a] -> a
product' = foldl (*) 1

last' :: [a] -> a
last' = foldl1 (\_ x -> x)
















































