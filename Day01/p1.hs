main :: IO()
main = do
  numbers <- parseFile "numbers.txt"
  case findSolution numbers of
    Nothing -> putStrLn "No suitable numbers found"
    Just (x, y) -> do
      putStrLn $ "Found: (" ++ show x ++ ", " ++ show y ++ ")"
      putStrLn $ "Answer: " ++ show (x * y)

parseFile :: (Read a, Num a) => String -> IO [a]
parseFile filename = do
   contents <- readFile filename
   return $ map read (lines contents)

findSolution :: (Eq a, Num a) => [a] -> Maybe (a, a)
findSolution numbers = checkNumber 0 numbers
  where checkNumber 0 (x:xs) = checkNumber x xs
        checkNumber _ [] = Nothing
        checkNumber n allXs@(x:xs) =
          if 2020 - n `elem` allXs
          then Just (n, 2020 - n)
          else checkNumber x xs


