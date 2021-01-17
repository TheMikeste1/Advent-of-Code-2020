module P1 where

import qualified Data.Set as Set  

data Instruction a = Nop a | Acc a | Jmp a deriving (Show)

main :: IO ()
main = do
    ops <- parseFile "code.txt"
    let acc = followInstructions ops 0 0 Set.empty 
    putStrLn $ "Accumulator finished at " ++ show acc


parseFile :: (Read a, Num a) => FilePath -> IO [Instruction a]
parseFile filename = do
    contents <- readFile filename
    return (map (parseInstruction . words) (lines . filter (/='+') $ contents))


parseInstruction :: (Read a, Num a) => [String] -> Instruction a
parseInstruction [op, sval]
    | op == "nop" = Nop val 
    | op == "acc" = Acc val
    | op == "jmp" = Jmp val 
    where val = read sval

followInstructions :: (Ord a, Integral a) => [Instruction a] -> a -> a -> Set.Set a -> a
followInstructions instructions currentIns acc visited
    | currentIns >= fromIntegral (length instructions) = acc
    | currentIns `Set.member` visited = acc
    | otherwise = case ins of 
        Nop x -> followInstructions instructions (currentIns + 1) acc updatedVisited
        Acc x -> followInstructions instructions (currentIns + 1) (acc + x) updatedVisited
        Jmp x -> followInstructions instructions (currentIns + x) acc updatedVisited
    where ins = instructions !! fromIntegral currentIns
          updatedVisited = currentIns `Set.insert` visited

