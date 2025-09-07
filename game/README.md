# game/README.md

# Game — Simple Terminal Game

## What it does
Miniature terminal game. Included example implementation: replayable guess-my-number game with saving of high scores. Add your own favorite game logic if you created something different.

## How it works 


1. The game first asks for a positive integer to set the range.

2. Level = max number possible. Secret number is randomly chosen between 1 and level.

3. Start guessing

4. You guess numbers until you get the right one.

5. Too small? You get told. Too big? You get told. Exactly right? Game over, you win!

- No funny inputs

- If you type letters or negative numbers, the game just ignores your mischief and politely asks again.

## My Struggles & How I Overcame Them
Struggle: Originally, my validation logic was letting invalid guesses through.
Solution: I put every input in a try/except block and made sure the guess had to be a positive integer before continuing.

Struggle: I kept mixing up where to put my random number generation.
Solution: Moved it into the main game() function so that it resets properly when the game starts.

Struggle: I almost made it overly complicated with multiple nested loops.
Solution: Two neat loops. One for the level, one for guessing ,keeps the game tidy.

## Example Run

Level: 10
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 7
Just right!


## Lessons Learned
- Input validation is the secret boss level of programming.

- Loops are like coffee: strong enough to keep things going, but not too many or you’ll get jittery.

- Writing code that ignores bad input without crashing makes your program feel polite.


## How to run
```bash
python game.py
```

## Sources 
CS50P Week 4 Problem Set: “Game”

Python Docs: random.randint()

My own stubbornness and one too many "Too small!" moments.