module Main where

import qualified P1
import qualified P2

main :: IO ()
main = do
    putStrLn "Part 1:"
    P1.main
    putStrLn "\nPart 2:"
    P2.main
