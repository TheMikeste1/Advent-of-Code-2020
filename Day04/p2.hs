module P2 where

import Data.List.Split
import Data.Char
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
        parsedFields = map parseField fields
    in Map.fromList parsedFields

parseField :: String -> (String, String)
parseField = makeTuple . splitOn ":"
    where makeTuple [x, y] = (x, y)

validPassport :: Map.Map String String -> Bool
validPassport passport = 
    all (`Map.member` passport) ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    && validField `all` Map.toList passport

validField :: (String, String) -> Bool
validField ("byr", val) = let year = read val in 1920 <= year && year <= 2002
validField ("iyr", val) = let year = read val in 2010 <= year && year <= 2020
validField ("eyr", val) = let year = read val in 2020 <= year && year <= 2030
validField ("hgt", val)
    | unit == "cm" = 150 <= height && height <= 193
    | unit == "in" = 59 <= height && height <= 76
    where height = read . take numberLength $ val
          unit = drop numberLength val
          numberLength = length val - 2
validField ("hcl", tag:digits) = tag == '#' && all isHexDigit digits && length digits == 6
validField ("ecl", val) = val `elem` ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
validField ("pid", val) = length val == 9
validField ("cid", _) = True
validField _ = False
