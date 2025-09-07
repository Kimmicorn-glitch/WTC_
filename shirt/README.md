### P-SHIRT.PY

This program takes a user’s input image and slaps a CS50 shirt.png on top of it, like a passive-aggressive reminder that you belong to the cult now.

## How it works:
- Takes two arguments: input file and output file.
- Checks: exactly two arguments, both valid image formats (.jpg, .jpeg, .png), extensions must match, input file must exist, shirt.png must exist. Fail any of these and it dies with an error message.
- Opens shirt.png and the input image.
- Resizes the input image to match shirt.png using ImageOps.fit so things don’t look warped.
- Pastes shirt.png over the resized photo, keeping transparency.
- Saves the finished image to the output file

## How I solved it
Started with argument validation (too few, too many, wrong extensions, missing files). Then Pillow handled the heavy lifting: ImageOps.fit for clean resizing, paste() for the overlay, save() for the output.


## Questions I asked myself
– Should I let people change formats on the way out? No, program says same in, same out.
– What happens if shirt.png is missing? The program crashes instantly, like CS50’s way of telling you “don’t lose the shirt.”
– How do I stop stretching faces into nightmares? Use ImageOps.fit, not naive resizing.

## Examples
$ python shirt.py input.jpg output.jpg

## Signature
// kimmy