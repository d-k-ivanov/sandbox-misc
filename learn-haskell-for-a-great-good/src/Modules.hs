module Modules where

-- import qualified Data.List
import Data.List

wordNums :: String -> [(String, Int)]
wordNums = map (\ws -> (head ws, length ws)) . group . sort . words

isIn :: (Eq a) => [a] -> [a] -> Bool
needle `isIn` haystack = any (needle `isPrefixOf`) (tails haystack)
-- "unch" `isIn` "crunch"


import Data.Char
-- Cesar's Code
-- ord 'a'; chr 97; map ord "abcdef"
