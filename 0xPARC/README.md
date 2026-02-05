## Puzzle statement

Suppose I have a secret list of positive integers: $(v_1, v_2, ..., v_n)$.

You can't see my list, but you can ask me dot product questions. Give me any list of numbers $(x_1, x_2, ..., x_n)$
of the same length, and I'll tell you:

$$x_1 \cdot v_1 + x_2 \cdot v_2 + ... + x_n \cdot v_n$$

Figure out my secret list using as few questions as possible.

## Solution

This is the first solution I came up with for the 0xPARC puzzle posted in the 3b1b site. It is not very efficient and will crumble with big enough numbers, but it works. No AI used, effort ~1hr 15m. Maybe I'll give it another couple of hours to think it through again.

I coded my first approach in [puzzle.py](puzzle.py) and then tried to make it more "homework/game like" in the [runner](runner.py) + [player](player.py) combo, so that a "contestant" could modify only the [player](player.py) file with the `guess_list()` method and attempt to solve the puzzle.
