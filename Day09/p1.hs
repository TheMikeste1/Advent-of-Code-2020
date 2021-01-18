module P1 where


main :: IO ()
main = do
    contents <- parseFile "XMAS cipher.txt"
    let weakness = findWeakness (take 25 contents) (drop 25 contents)
    print weakness


parseFile :: (Num a, Read a) => FilePath -> IO [a]
parseFile filename = do
    contents <- readFile filename
    return (map read (lines contents))

findWeakness :: (Eq a, Num a) => [a] -> [a] -> a
findWeakness _ [] = error "No valid number found"
findWeakness pre (x:xs) = 
    if x `elem` [a + b | a <- pre, b <- pre]
    then findWeakness (tail (pre ++ [x])) xs
    else x



