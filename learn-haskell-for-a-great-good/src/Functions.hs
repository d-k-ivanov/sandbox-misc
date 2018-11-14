module Functions (lucky) where

lucky :: Int -> String
lucky 7 = "You lucky man!"
lucky x = "Sad for you :("

num2txt :: Int -> String
--num2txt :: Int -> [Char] -- This is the same
num2txt 1 = "One"
num2txt 2 = "Two"
num2txt 3 = "Three"
num2txt 4 = "Four"
num2txt 5 = "Five"
num2txt 6 = "Six"
num2txt 7 = "Seven"
num2txt 8 = "Eight"
num2txt 9 = "Nune"
num2txt 0 = "Zero"
num2txt x = "Wrong number! Only from 0 to 9"

-- (num2txt 9) ++ [' '] ++ (num2txt 1) ++ [' '] ++ (num2txt 1)
-- num2txt 9 ++ [' '] ++ num2txt 1 ++ [' '] ++ num2txt 1

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n -1)

addVectors :: (Double,Double) -> (Double,Double) -> (Double,Double)
addVectors a b = (fst a + fst b, snd a + snd b)

addVectors' :: (Double,Double) -> (Double,Double) -> (Double,Double)
addVectors' (a1,a2) (b1,b2) = (a1 + b1, a2 + b2)

fst3 :: (a,b,c) -> a
fst3 (a,_,_) = a

mid3 :: (a,b,c) -> b
mid3 (_,b,_) = b

trd3 :: (a,b,c) -> c
trd3 (_,_,c) = c

xs = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]
-- [a+b | (a,b) <- xs]

head' :: [a] -> a
head' [] = error "You could not call head on emty list"
head' (a:_) = a

tellMeElements :: (Show a) => [a] -> String
tellMeElements [] = "Empty list"
tellMeElements (a:[]) = "List of one element: " ++ show a
tellMeElements (a:b:[]) = "List of two elements: " ++ show a ++ " and " ++ show b
tellMeElements (a:b:_) = "List of many elements: " ++ show a ++ ", " ++ show b ++ ", ... , n"

firstLetter :: [Char] -> [Char]
firstLetter "" = "Oops, empty string"
firstLetter all@(x:xs) = "First letter of the string " ++ all ++ " is '" ++ [x] ++ "'"

{-bmiTell :: Double -> String
bmiTell bmi
  | bmi <= 18.5 = "Thin"
  | bmi <= 25 = "Medium"
  | bmi <= 30 = "Thick"
  | otherwise = "Too much"-}

bmiTell :: Double -> Double -> String
bmiTell w h
  | w/h^2 <= 18.5 = "Thin"
  | w/h^2 <= 25 = "Medium"
  | w/h^2 <= 30 = "Thick"
  | otherwise = "Too much"

max' :: (Ord a) => a -> a -> a
max' a b
  | a <= b = b
  | True = a

myCmp :: (Ord a) => a -> a -> Ordering
a `myCmp` b
  | a == b = EQ
  | a <= b = LT
  | otherwise = GT

bmiTell' :: Double -> Double -> String
bmiTell' w h
  | bmi <= 18.5 = "Thin"
  | bmi <= 25 = "Medium"
  | bmi <= 30 = "Thick"
  | otherwise = "Too much"
  where bmi = w/h^2

bmiTell'' :: Double -> Double -> String
bmiTell'' w h
  | bmi <= skinny = "Thin"
  | bmi <= normal = "Medium"
  | bmi <= fat = "Thick"
  | otherwise = "Too much"
  where bmi = w/h^2
        (skinny, normal, fat) = (18.5,25,30)

badGreeting :: String
badGreeting = "Fuck you, "

niceGreeting :: String
niceGreeting = "I love you, "

greet :: String -> String
greet "Juan" = niceGreeting ++ "Juan"
greet "Fernando" = niceGreeting ++ "Fernando"
greet name = badGreeting ++ name

initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
  where (f:_) = firstname
        (l:_) = lastname

cylinder :: Double -> Double -> Double
cylinder r h =
  let sideArea = 2 * pi * r * h
      topArea = pi * r^2
  in sideArea + 2 * topArea

calcBMI :: [(Double, Double)] -> [Double]
calcBMI xs = [bmi | (w,h) <- xs, let bmi = w/h^2]

head'' :: [a] -> a
head'' xs =
  case xs of
    [] -> error "Empty list"
    (x:_) -> x

describeList :: [a] -> String
describeList xs = "The list " ++
  case xs of
    [] -> "is empty"
    [x] -> "with one element"
    xs -> "is long"

