module P2 where

import qualified P1


main :: IO ()
main = do
    contents <- P1.parseFile "XMAS cipher.txt"
    let weakness = P1.findWeakness (take 25 contents) (drop 25 contents)
    print $ exploit [] contents weakness

exploit :: (Num a, Ord a, Show a) => [a] -> [a] -> a -> a
exploit [] xs weakness = exploit (take 2 xs) (drop 2 xs) weakness
exploit [x] (y:xs) weakness = exploit [x, y] xs weakness
exploit current [] weakness =
    if sum current == weakness
    then maximum current + minimum current
    else error "No answer found"
exploit current axs@(x:xs) weakness =
    case sum current `compare` weakness of
        EQ -> maximum current + minimum current
        LT -> exploit (current ++ [x]) xs weakness
        GT -> exploit (tail current) axs weakness
