module P2 where

import Data.List
import P1 (Group, parseFile)

main :: IO ()
main = do
    groups <- parseFile "customs_answers.txt"
    let totalAnswers = countAnswers groups
    putStrLn $ "Total answers: " ++ show totalAnswers


countAnswers :: (Num a) => [Group] -> a
countAnswers = sum . map countGroupAnswers

countGroupAnswers :: (Num a) => Group -> a
countGroupAnswers groupAnswers = foldl' isUnanimous 0 allAnswers
    where allAnswers = group . sort . concat $ groupAnswers
          numActors = length groupAnswers
          isUnanimous acc g = 
              if length g == numActors then acc + 1 else acc

