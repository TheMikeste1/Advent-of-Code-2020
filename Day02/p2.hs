module P2 where

import qualified Data.List.Split as LSplit

data Rule = Rule {ruleMin :: Int, ruleMax :: Int, ruleChar :: Char} deriving (Show)
type Password = String
type PasswordEntry = (Rule, Password)

main = do
  passwordEntries <- parseFile "passwords.txt"
  let numValid = countValid passwordEntries
  putStrLn $ "Found " ++  show numValid ++ " valid passwords out of " ++
   show (length passwordEntries) ++ " entries."
   where countValid = length . filter (uncurry validPassword)

validPassword :: Rule -> String -> Bool
validPassword (Rule minimum maximum char) s = if minMatch then not maxMatch else maxMatch
  where minMatch = s !! (minimum - 1) == char
        maxMatch = s !! (maximum - 1) == char


parseFile :: String -> IO [PasswordEntry]
parseFile filename = do
  contents <- readFile filename
  return (map parseEntry . lines $ contents)

parseEntry :: String -> PasswordEntry
parseEntry entry = (Rule minimum maximum char, password)
   where
      parts = LSplit.splitOn " " entry
      minMax = LSplit.splitOn "-" $ head parts
      minimum = read $ head minMax
      maximum = read $ last minMax
      char = head $ parts !! 1
      password = parts !! 2



