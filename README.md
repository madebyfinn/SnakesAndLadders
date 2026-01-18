Snakes and Ladders (link to Codewars kata: https://www.codewars.com/kata/587136ba2eefcb92a9000027)

This project is a Python implementation of the classic Snakes and Ladders board game, built as a programming kata to practice state management, rule sequencing, and class design.

The game is implemented as a single SnakesLadders class exposing a play(die1, die2) method. Each call to play represents one dice roll and updates the game state accordingly, allowing the test suite to invoke the method independently of turn order or prior context.

Features
	•	Two-player turn-based gameplay starting from square 0
	•	Fully implemented snakes and ladders using a fixed board mapping
	•	Bounce-back logic when a roll overshoots square 100
	•	Support for extra turns when rolling doubles
	•	Exact-win condition required to finish the game
	•	Clear, test-friendly return messages describing game state

Design Approach

The solution separates board data (snakes and ladders) from game logic, with helper methods handling movement rules such as bouncing and teleports. This keeps the main play() method readable and closely aligned with the actual game rules.

This kata was completed as a learning exercise, with emphasis on clarity, correctness, and maintainable structure rather than UI or randomness.
