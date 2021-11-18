# Ex1_OOP
#### Contributors: Bar Goldenberg, Sappir Bohbot

### Literature research:
    1. https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
    2. https://www.youtube.com/watch?v=xOayymoIl8U&ab_channel=SpanningTree
    3. https://www.youtube.com/watch?v=siqiJAJWUVg&ab_channel=ThinkSoftware

### The difference between an offline algorithm and an online algorithm:
The main difference applies to the knowledge of future input and how the algorithm makes choices in consequence to those inputs which effect run time efficiency, in an offline algorithm we know the inputs ahead of time, so we can strategize a game plan to minimize the time it takes to finish the task, in an online algorithm, we receive the input in real-time, therefore the algorithm can only make decisions with the knowledge it has in this point in time.
In consequence, offline algorithms are usually more efficient than online algorithms.

### Problems facing an offline elevator algorithm:
To much data!!!
we have a lot of information about future input so there are a lot more variables to consider when thinking of an efficient algorithm.
for example, we need to consider call times, call directions, elevator speed, number of elevators ect...


### Offline Elevator Algorithm
First we will define *max_trip* as the time it takes the slowest elevator to go from the lowest floor in the building to the highest.
we will look in to the call file in segments of *max_trip*.
for each segment we will divide the sequential up calls and the sequential down calls, if there are more up calls we will send it to the fastest emptiest and closest elevator and vice versa.
then we will look into the next segment and do the same untill the call file is full.

### Class Diagram:
![Ex1Diagram](https://user-images.githubusercontent.com/89586016/142404984-3d6a0e03-e00e-47b4-b9f3-ffa8f17092a9.png)

### Results:


|Calls/Building|B1     |B2        |B3      |B4      |B5      |
|--------------|--------|----------|--------|--------|--------|
| Calls a      |112.92  | 50.64    | 24.71  |20.9    |15.66   |
| Calls b      |        |          | 454.34 |184.43  |68.88   |
| Calls c      |        |          | 451.22 |182.21  |61.18   |
| Calls d      |        |          | 432.83 |177.45  |64.04   |