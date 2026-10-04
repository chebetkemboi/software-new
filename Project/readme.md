# UNRAVEL
# Chebet Kemboi

## Description

Unravel is a text adventure game that takes place in a medieval town 
where the water supply has suddenly become contaminated and scarce.

The player's objective is to investigate the problem, explore
different areas, solve puzzles, collect items and earn enough
points to restore the town's water supply.

## Story

Something has happened to the town's water supply.

The player must investigate the Forest, Hill and River to
discover clues about the problem.

The player can choose different areas to investigate first.
By solving puzzles and collecting useful items, the player
can eventually discover enough information to fix the water
supply.

## Routes

The game has several possible routes.

For example, the player can investigate:

- Forest -> River -> Cave
- Hill -> River -> Cave
- River -> Forest -> Cave

The player can choose which area to investigate first.

## Game Objective

The player must:

- Explore the town
- Collect at least three items
- Solve three puzzles
- Earn at least three points
- Restore the town's water supply

## Features

- Player name and age input
- Age restriction for players under 12
- Main menu
- Movement between rooms
- Inventory
- Item collection
- Puzzles
- Points system
- Multiple routes
- Game progress
- Save game
- Continue saved game
- Game ending

## Project Structure

### game.py

Contains the main game loop, menus, game functions,
puzzles and save/load functionality.

### player.py

Contains the Player class.

The Player stores:

- name
- inventory
- location
- points
- solved puzzles

The Player class also contains methods for moving and
collecting items.

### room.py

Contains the Room class.

A room has:

- name
- item

### item.py

Contains the Item class.

An item has:

- name
- weight

### intro.txt

Contains the introduction displayed when the game starts.

### instructions.txt

Contains the instructions for the player.

## Sustainable Development Goal

The game is connected to Sustainable Development Goal 6:
Clean Water and Sanitation.

The objective of the game is to investigate and restore
a town's contaminated and scarce water supply.

The game therefore raises awareness of the importance of
clean and accessible water.

## How to Play

Start the program and enter your name and age.

Players under 12 cannot continue.

Choose New Game or Continue Game.

Use the main menu to move between locations, collect items,
solve puzzles, check inventory and view progress.

The player can save their progress and continue the game later.

The game is completed when the player has solved the three
puzzles and collected at least three items.