# faces.py

## Purpose
Takes text with emoticons like :) and :( and replaces them with emojis 😄 and 😢.

## How It Works
1. Get text input from the user.
2. Replace :) with 😄 and :( with 😢.
3. Output the upgraded text — now with more emotional range.

## Struggles
- The replacement order mattered: replacing :) first worked, but if done in reverse, the face got *mutilated*.
- Initially forgot that .replace() can be chained.

## Lesson Learned
- Order of operations isn’t just for maths.
- Chaining .replace() can be neat if you keep it in the right sequence.

## Example
I am happy :) but also sad :( → I am happy 😄 but also sad 😢

