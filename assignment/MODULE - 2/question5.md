5. What is the purpose continue statement in python? 
-> Let's break down the continue statement in Python:

Purpose:

- this is  a list of items.  The continue statement will skip this item,  move on to the next one,  It tells Python to immediately jump back to the beginning of the loop, skipping any code that comes after it in the current iteration.

Example:    fruits = ["apple", "banana", "cherry", "orange"]

            for fruit in fruits:
              if fruit == "banana":
                continue  # Skip the "banana" and move to the next fruit
              print(fruit)

              Explanation:

- Output: The output will be:
    apple
    cherry
    orange
    The "banana" is skipped!

- Key Points:

    Skips the Rest: The continue statement only skips the remaining code within the current iteration of the loop. It doesn't stop the loop altogether.
    Use Cases: It's helpful for situations where you want to handle certain conditions differently or skip specific iterations based on criteria.
    Alternatives: You could also use if statements and nested else blocks to achieve similar results, but continue often provides a cleaner and more concise way to handle conditional skipping in loops.