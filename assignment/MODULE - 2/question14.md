14. What are negative indexes and why are they used? 

->  you have a list of shopping list:
    shopping_list = ["milk", "meggie", "chocolate", "icecream"]
    You can access items in this list using their index, which is like their position number. The first item ("milk") has an index of 0, the second ("meggie") has an index of 1, and so on.

    Negative indexes are a special way to access items from the end of the list. Instead of counting from the beginning, they count backward from the end.

    shopping_list[-1] refers to the last item ("icecream").
    shopping_list[-2] refers to the second-to-last item ("chocolare").
    shopping_list[-3] refers to the third-to-last item ("meggie").
- Why use negative indexes?

- Convenience: Sometimes it's easier to work with items from the end of a list without having to count how many items are in it.
- Code Readability: Negative indexes make your code more understandable when you want to work with the end of a list.

- Example:
shopping_list.pop(-1)  # This removes the last item ("icecream")
Using a negative index here is cleaner and easier to understand than figuring out the index of the last item each time.