[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16716414)
# First Letter Shift

Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

## Examples:
```
shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"
```

## Notes:
* The last word shifts its first letter to the first word in the sentence.
* All sentences will be given in lowercase.
* Note how single words remain untouched (example #4).