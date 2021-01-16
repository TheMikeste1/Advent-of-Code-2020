module P2 where

import qualified Data.Map as Map
import P1 (Rule (..), myBag, parseFile)

main :: IO ()
main = do
    rules <- parseFile "bag_rules.txt"
    let myRule = getRule myBag rules
    let numBags = countTotalInnerBags myRule rules
    putStrLn $ show numBags ++ " bags are required to use the " ++ myBag ++ " bag."


countTotalInnerBags :: (Num a) => Rule a -> [Rule a] -> a
countTotalInnerBags (Rule _ children) rules = foldl (\acc x -> acc + countSubBags x) 0 (Map.toList children)
    where countSubBags (bag, amount) = amount * (countTotalInnerBags (getRule bag rules) rules + 1)  -- Add one to include this bag

getRule :: String -> [Rule a] -> Rule a
getRule color = head . filter (\(Rule bag _) -> bag == color) 
