module P2 where

newtype Vector2 = Vector2 {getCoords :: (Int, Int)}

main :: IO()
main = do 
    slopeMap <- parseFile "map.txt"
    let numTrees =  [ 
            runSim slopeMap (Vector2 (1, 1))
            , runSim slopeMap (Vector2 (3, 1))
            , runSim slopeMap (Vector2 (5, 1))
            , runSim slopeMap (Vector2 (7, 1))
            , runSim slopeMap (Vector2 (1, 2))
            ]
    print $ product numTrees

zeroVector2 :: Vector2
zeroVector2 = Vector2 (0, 0)

parseFile :: FilePath -> IO [String]
parseFile filename = do 
    contents <- readFile filename
    return (lines contents)

runSim :: (Num a) => [String] -> Vector2 -> a
runSim slopeMap = countTrees 0 slopeMap zeroVector2

countTrees :: (Num a) => a -> [String] -> Vector2 -> Vector2 -> a
countTrees trees map pos deltaV = 
    let newPos = step pos deltaV 
        (x, y) = getCoords newPos
    in
        if y >= maxY then trees
        else countTrees (checkTree newPos + trees) map newPos deltaV
    where 
        maxY = length map
        maxX = length . head $ map
        step (Vector2 (x, y)) (Vector2 (dx, dy)) = Vector2 ((x + dx) `mod` maxX, y + dy)
        checkTree (Vector2 (x, y)) = if map !! y !! x == '#' then 1 else 0
        



