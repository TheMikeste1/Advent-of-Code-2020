module P1 where

main :: IO ()
main = do
    tickets <- parseFile "seats.txt"
    putStrLn $ "Max ID: " ++ (show . maximum . parseTickets $ tickets)

parseFile :: FilePath -> IO [String]
parseFile filename = do 
    contents <- readFile filename
    return (lines contents)


parseTickets :: (Ord a, Num a) => [String] -> [a]
parseTickets = map parseTicket


parseTicket :: (Ord a, Num a) => String -> a
parseTicket string = fromIntegral $ parseRow 0 127 (take rowLen string) * 8 + parseCol 0 7 (drop rowLen string)
    where 
        parseRow _ x [] = x
        parseRow min max (x:xs) = 
            if x == 'F' then parseRow min ((max + min) `div` 2) xs
            else parseRow ((max + min) `div` 2) max xs
        parseCol _ x [] = x
        parseCol min max (x:xs) = 
            if x == 'L' then parseCol min ((max + min) `div` 2) xs
            else parseCol ((max + min) `div` 2) max xs
        rowLen = length string - 3


