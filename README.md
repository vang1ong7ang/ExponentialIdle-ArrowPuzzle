# ExponentialIdle-ArrowPuzzle

the optimal solution for arrow puzzle of game exponential idle

## The Problem

> The goal of this minigame is to have all the arrows pointed upwards. There are four levels of difficulty:
> 
> - Easy : 3 by 3 square, 4 possible orientations
> - Medium : 4 by 4 square, 4 possible orientations
> - Hard : hexagonal pattern of side length 4, 2 possible orientations
> - Expert : hexagonal pattern of side length 4, 6 possible orientations
>
> On a square grid, whenever an arrow is touched, it will rotate 90° clockwise along with all its neighbours. The neighbours are all arrows in a 3 by 3 square centered around the touched arrow, there are less neighbours when you touch an arrow on an edge or a corner (ie the board is not a torus).
> 
> On the hexagonal grid, the neighbours are all adjacent arrows (up to 6). On the Hard difficulty, the arrows flip between up and bottom orientation when touched, on Extreme, they rotate by 60° clockwise.

external resources:

- [wiki](https://exponential-idle.fandom.com/wiki/Minigames#Arrow)
- [video](https://www.youtube.com/watch?v=aoPkibU9BBE)

## The Metric

**steps**: the less, the better

## The Solution

let `n` denote the number of arrows and `m` denote number of possible orientations of arrows (`4` for easy and medium; `2` for hard; `6` for expert)

1. define a column vector `X` (size: `n×1`)

    each element `X_i` represents the number of taps needed for `i`-th arrow

2. define a square matrix `A` (size: `n×n`)

    element `A_ij` is `1` if `i = j` or `i`-th arrow is a neighbour of `j`-th arrow, otherwise, `A_ij` is `0`

3. define a column vector `B` (size: `n×1`)

   element `B_i` represents the initial orientation of `i`-th arrow

   - for easy and medium: `0` is `up`; `1` is `right`; `2` is `down`; `3` is left;
   - for hard: `0` is `up`; `1` is `down`;
   - for expert: `0` is `up`; `1` is `60°`(right, slightly upwards); `2` is `120°`(right, slightly downwards); `3` is `down`; `4` is `240°`(left, slightly downwards); `5` is `300°`(left, slightly upwards);

4. then the following equation should be satisfied:

    ```text
    A X + B = 0 (mod m)
    ```

5. solve for `X`

    ```text
    X = (A^-1)(-B) (mod m)
    ```

### Patch for Hard and Expert

follow the steps above, you will find that `A` is not invertible.

actually the rank of matrix `A` is `33` and `n` is `37`, which means that `A` is not a full rank matrix.

solution: just remove `4` arrows of any edge of the hexagon from `A`, `X` and `B`, then `A` will be invertible and we never need to touch the `4` ignored arrows.

verify: use the unignored matrix `A` and `B` and `X` to verify the equation. actually the puzzle has a solution if and only if our solution is verified.

## The Analysis

the optimal steps is solved because all possible solutions should satisfy the equation above and we provide the minimum value of each `X_i`.

## The Experiments

see python code in this repo

## The Conclusion

good work
