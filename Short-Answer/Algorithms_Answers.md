#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) 


b) O(log n)


c)O(n)

## Exercise II

I would want to use a O(log n) function for this because we will be cutting the floors in half to minimize our egg usage. 

Let's say we have 100 floors of the building. We will start with by cutting the number of floors in half so we still go up to floor 50 and drop our first egg. 

If the egg breaks on floor 50, then we will cut the floors in half and go down to floor 25. If the egg does not break, then we will go up to floor 75.

If the egg breaks while being dropped on floor 25, then we will cut the remaining floors in half and go down to floor 13. If the egg does not break on floor 75, then we will cut the remaining floors in half and go to floor 87.

We will repeat this process of cutting the remaining rooms in half until we can find the highest room that allows the eggs to land without breaking.
