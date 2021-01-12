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
findSolution [] = Nothing
findSolution (x:xs) =
   if 2020 - x `elem` xs
   then Just (x, 2020 - x)
   else findSolution xs




