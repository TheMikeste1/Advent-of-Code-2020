module P2 where

import qualified Data.Set as Set  
import P1 (Instruction (..), parseFile)



main :: IO ()
main = do
    ops <- parseFile "code.txt"
    let acc = followInstructions ops 0 0 Set.empty 
    putStrLn $ "Accumulator finished at " ++ show acc


followInstructions :: (Ord a, Integral a) => [Instruction a] -> a -> a -> Set.Set a -> a
followInstructions instructions currentIns acc visited
    | currentIns >= fromIntegral (length instructions) = acc
    | currentIns `Set.member` visited = -1
    | otherwise = case ins of 
        Acc x -> followInstructions instructions (currentIns + 1) (acc + x) updatedVisited
        Nop x -> 
            case followInstructions instructions (currentIns + x) acc updatedVisited of
                -1 -> followInstructions instructions (currentIns + 1) acc updatedVisited
                x -> x
        Jmp x -> 
            case followInstructions instructions (currentIns + 1) acc updatedVisited of
                -1 -> followInstructions instructions (currentIns + x) acc updatedVisited
                x -> x
    where ins = instructions !! fromIntegral currentIns
          updatedVisited = currentIns `Set.insert` visited

