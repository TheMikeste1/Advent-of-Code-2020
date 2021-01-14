module P1 where

newtype Vector2 = Vector2 {getCoords :: (Int, Int)}

deltaV = Vector2 (3, 1)

main :: IO()
main = do 
    map <- parseFile "map.txt"
    let numTrees = countTrees 0 map zeroVector2
    print numTrees

zeroVector2 :: Vector2
zeroVector2 = Vector2 (0, 0)

parseFile :: FilePath -> IO [String]
parseFile filename = do 
    contents <- readFile filename
    return (lines contents)

countTrees :: (Num a) => a -> [String] -> Vector2 -> a
countTrees trees map pos = 
    let newPos = step pos deltaV 
        (x, y) = getCoords newPos
    in
        if y >= maxY then trees
        else countTrees (checkTree newPos + trees) map newPos
    where 
        maxY = length map
        maxX = length . head $ map
        step (Vector2 (x, y)) (Vector2 (dx, dy)) = Vector2 ((x + dx) `mod` maxX, y + dy)
        checkTree (Vector2 (x, y)) = if map !! y !! x == '#' then 1 else 0
        



