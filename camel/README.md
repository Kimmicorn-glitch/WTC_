# camel.py

##  Purpose
Converts a variable name from camelCase to snake_case , because sometimes Python just likes to hiss instead of hump.

##  How It Works
1. Prompt user for a camelCase string.
2. Loop through each character:
   - If it’s uppercase, prepend an underscore _ and make it lowercase.
   - Otherwise, leave it as is.
3. Output the new snake_case string.

## Struggles
- Initially overthought the logic, almost built an entire regex engine in my head.
- Tried .replace() but realised it wouldn’t catch uppercase letters dynamically.
- Remembered that looping through each character is simpler (and less headache-inducing).

## Lesson Learned
- Iteration is often the cleaner option.
- Uppercase checks are your friend.
- Resist the urge to make things *fancier than they need to be*.



