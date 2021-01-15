module P1 where

import Data.List
import Data.List.Split

type Group = [String]

main :: IO ()
main = do
    groups <- parseFile "customs_answers.txt"
    let totalAnswers = countAnswers groups
    putStrLn $ "Total answers: " ++ show totalAnswers

parseFile :: FilePath -> IO [Group]
parseFile filename = do 
    contents <- readFile filename
    return (map lines $ splitOn doubleNewline contents)
    where doubleNewline = "\n\n"

countAnswers :: (Num a) => [Group] -> a
countAnswers = sum . map countGroupAnswers

countGroupAnswers :: (Num a) => Group -> a
countGroupAnswers group = fromIntegral . length . nub $ allAnswers
    where allAnswers = concat group

