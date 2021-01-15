module P1 where

import qualified Data.Map as Map  
import Data.List
import Data.List.Split

data Rule a = Rule {bagColor :: String, ruleChildren :: Map.Map String a} deriving (Show)


myBag = "shiny gold"

main :: IO ()
main = do
    rules <- parseFile "bag_rules.txt"
    let numBags = countContainingBags myBag rules
    putStrLn $ "Found " ++ show numBags ++ " bags able to hold " ++ myBag ++ " bags."

parseFile :: (Read a, Num a) => FilePath -> IO [Rule a]
parseFile filename = do 
    contents <- readFile filename
    let ls = lines contents
    return (map parseLine ls)

parseLine :: (Read a) => String -> Rule a
parseLine s = Rule color (Map.fromList rules)
    where [color, rawRules] = splitOn " bags contain " s
          stringRules = splitOn ", " $ filter (/='.') rawRules
          rules = if rawRules == "no other bags." 
              then [] 
              else map parseRule stringRules

parseRule :: (Read a) => String -> (String, a)
parseRule s = (string, num)
    where parts = words s
          num = read $ head parts
          string = unwords . init . tail $ parts

countContainingBags :: (Num a) => String -> [Rule a] -> a
countContainingBags bagName rules = fromIntegral $ length (findParents [bagName]) - 1  -- Subtract 1 since the original bag cannot contain itself
    where findParents bags = 
            let validRules = filter (\(Rule _ children) -> any (`Map.member` children) bags) rules
                validBags = nub $ map bagColor validRules ++ bags
            in if length bags == length validBags 
            then bags  
            else findParents validBags