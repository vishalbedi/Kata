--1. Select the first element of the list.
first' [] = -1
first' (a:as) = a
--2. Remove the first element of the list.
rest' [] = []
rest' (a:as) = as
--3. Select nth element of the list.
nThElement _ [] = -1
nThElement n (a:as)
  | n == 1 = a
  | otherwise = nThElement (n-1) as
--4. Select the first n elements of a list.
nElements _ [] = []
nElements 0 _ = []
nElements n (a:as) = a: nElements (n-1) as
--5. Calculate the length of the list.
length' [] = 0
length' (a:as) = 1 + length' as
--6. Calculate the sum/product of a list.
calc' f a [] = a
calc' f a (x:xs) = f x $ calc' f a xs
sum' = calc' (+) 0
mul' = calc' (*) 1
--7. Reverse the list.
reverse' [] = []
reverse' (a:as) = reverse' as ++ [a]
--8. Consider a function safetail that behaves in the same way as tail, except that safetail maps the empty list to the empty list, whereas tail gives an error in this case.  Define safetail using:
--  (a)	a conditional expression;
safetail1 as = if (null as) then [] else tail as
--  (b)	guarded equations;
safetail2 as
 | null as  = []
 | otherwise = tail as

--  (c)	pattern matching.
safetail [] = []
safetail (a:as) = as

--9. Give three possible definitions for the logical or operator (||) using pattern matching.

isOr False x = x
isOr True _ = True

--10. A triple (x,y,z) of positive integers is called pythagorean if
--x^2 + y^2 = z^2.
--Using a list comprehension, define a function that maps an integer n to all such triples with components in [1..n].
--For example:
-- pyths 5
--[(3,4,5),(4,3,5)]
pythagoreanTriplet n
  = [(x,y,z)|x<-[1..n],y<-[1..n],z<-[1..n], (x*x) + (y*y) == (z*z)]

--11. A positive integer is perfect if it equals the sum of all of its factors, excluding the number itself.  Using a list comprehension, define a function that returns the list of all perfect numbers up to a given limit.
--For example:
-- perfects 500
--[6,28,496]
factors 0 = [0]
factors n = [x|x<-[1..n-1],(mod n x) == 0]
perfectInt 0 = []
perfectInt n = [x|x<-[1..n],sum' (factors x) == x]

--12. The scalar product of two lists of integers xs and ys of length n is give by the sum of the products of the corresponding integers.
--Using a list comprehension, define a function that returns the scalar product of two lists.

--13. Implement Quicksort in Haskell. (Hint: Use recursion !!)

--14. Define a recursive function
--	merge :: [Int] -> [Int] -> [Int]
--that merges two sorted lists of integers to give a single sorted list.  For example:
-- merge [2,5,6] [1,3,4]
--[1,2,3,4,5,6]

--15. Express the comprehension [f x | x <- xs, p x] using the functions map and filter.

--16. Redefine map f and filter p using recursion.
--17. Redefine map f and filter p using foldr.
