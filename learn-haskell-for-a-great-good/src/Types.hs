module Types where

factorial :: Int -> Int
factorial n = product [1..n]

factorial' :: Integer -> Integer
factorial' n = product [1..n]

circumference :: Float -> Float
circumference r = 2 * pi * r

circumference' :: Double -> Double
circumference' r = 2 * pi * r

-- Type classes
{-
:t (==)
(==) :: Eq a => a -> a -> Bool
:t (>)
(>) :: Ord a => a -> a -> Bool
Show:
  show 3
  show True
Read:
  read "True" || False
  read "4" :: Int
  read "4" :: Integer
  read "4" :: Float
  read "(4, True)" :: (Int, Bool)
  read "(4, ['T','r','u','e'])" :: (Int, Bool)
  :t read
  read :: Read a => String -> a
Enum:
  :t succ
  succ :: Enum a => a -> a
  [LT .. GT]
  ['a'..'e']
Bounded:
  minBound :: Int
  minBound :: Integer -- not valid
  minBound :: Float   -- not valid
  minBound :: Double  -- not valid
  minBound :: Char
  minBound :: (Int,Bool, Char)
  maxBound :: Int
  maxBound :: Integer -- not valid
  maxBound :: Float   -- not valid
  maxBound :: Double  -- not valid
  maxBound :: Char
  maxBound :: (Int,Bool, Char)
Num: Int, Integer, Float, Double
Floating: Float, Double
Integral: Int, Integer
  :t fromIntegral
  fromIntegral :: (Num b, Integral a) => a -> b
  :t length
  length :: Foldable t => t a -> Int
  fromIntegral (length [1,2,3]) + 2.3
-}
