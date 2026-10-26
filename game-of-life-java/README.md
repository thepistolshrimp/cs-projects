# Game of Life — Java

A simple object-oriented implementation of Conway's Game of Life.

The program represents each cell as an object, stores cells in a two-dimensional grid, connects neighbouring cells, counts living neighbours, and updates the world generation by generation.

## Structure

- `Celle.java` — represents a cell and its state.
- `Rutenett.java` — creates and manages the grid and neighbouring cells.
- `Verden.java` — represents the world and updates generations.
- `GameOfLife.java` — program entry point.

## Run

```bash
cd src
javac *.java
java GameOfLife
```
