module P2 where

import Data.List (sort)
import P1 (parseFile, parseTickets)

main :: IO ()
main = do
    t <- parseFile "seats.txt"
    let tickets = sort $ parseTickets t
    let myTicket = findMissingSeat tickets
    putStrLn $ "Missing ticket: " ++ show myTicket

findMissingSeat :: (Enum a, Eq a) => [a] -> a
findMissingSeat (x:y:xs) = if nextX /= y then nextX else findMissingSeat (y:xs)
    where nextX = succ x
findMissingSeat _ = error "All seats accounted for."


