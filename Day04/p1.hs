module P1 where

import Data.List.Split
import qualified Data.Map as Map  


main :: IO ()
main = do
    passports <- parseFile "passports.txt"
    let numValid = length . filter validPassport $ passports
    putStrLn $ "Found " ++ show numValid ++ " valid passports out of " ++ show (length passports)

parseFile :: FilePath -> IO [Map.Map String String]
parseFile filename = do 
    contents <- readFile filename
    let passports = splitOn "\n\n" contents
    return (map parsePassport passports)

parsePassport :: String -> Map.Map String String
parsePassport entry = 
    let fields = words entry
        listFields = map (splitOn ":") fields
        tupleFields = map (\[x, y] -> (x, y)) listFields
    in Map.fromList tupleFields

validPassport :: Map.Map String String -> Bool
validPassport passport = all (`Map.member` passport) ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
