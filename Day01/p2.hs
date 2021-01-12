main :: IO()
main = do
  numbers <- parseFile "numbers.txt"
  case findSolution numbers of
    Nothing -> putStrLn "No suitable numbers found"
    Just (x, y, z) -> do
      putStrLn $ "Found: (" ++ show x ++ ", " ++ show y ++ ", " ++ show z ++ ")"
      putStrLn $ "Answer: " ++ show (x * y * z)

parseFile :: (Read a, Num a) => String -> IO [a]
parseFile filename = do
   contents <- readFile filename
   return $ map read (lines contents)

{-
Since Haskell is lazy, we can just take the head of the list and it won't generate the whole list.*

*This is proved by doing something in GHCi like:
   > let xs = [(x, y) | x <- [1..], y <- [1..10000], x + y == 2020]
   > :sp(rint) xs
   xs = _
   > head xs
   (1, 2019)
   >:sp xs
   xs = (1, 2019) : _
This shows that the list is built dynamically, and so the list won't be built all at once.
This also works with case statements:
   > test xs =
   >   case xs of
   >     [] -> "False"
   >     (x:_) -> show x
   > test xs
   > :sp xs

-}
findSolution :: (Eq a, Num a) => [a] -> Maybe (a, a, a)
findSolution xs =
   case [(a, b, c) | a <- xs, b <- xs, c <- xs, a + b + c == 2020] of
     [] -> Nothing
     (x:_) -> Just x
