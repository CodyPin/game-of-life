# Game of Life

## Welcome
This is my recreation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), this is my first
attempt in creating a cellular automation program

## Getting started
Make sure you have Python 3 installed, and then do `pip install pygame`. After that, just run the main.py!

## The basics
We have a grid, each cell contain either 1, representing alive, and 0, representing not alive.\
There are 4 rules:
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

With these 4 rules, each frame checks each cell for those conditions and react accordingly.
Eventually, given the limited screen size, all cells will reach its static state.

## Additional function(s)
- allows users to click and drag the mouse to 'create chaos' by moving a live cell!

## A glimpse of how it looks like
![python_WL2v3pMbfb.png](..%2F..%2FScreenshot%2FScreenshots%2F2024-02%2Fpython_WL2v3pMbfb.png)