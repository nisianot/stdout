# Loading Module

This Python module provides functions for simulating loading and printing animations in the console.

## Functions

### `print_string_anim(string, seconds)`

Prints each character of the input string with an animation, creating a typing effect.

- **Parameters:**
  - `string` (str): The input string to be printed.
  - `seconds` (float): The time (in seconds) for each character animation.

- **Example:**
  ```python
  from loading_module import print_string_anim

  print_string_anim("Hello, World!", 0.1)
  ```

### `simulate_loading(seconds)`

Simulates a loading animation in the console.

- **Parameters:**
  - `seconds` (float): The total time (in seconds) for the loading animation.

- **Example:**

  ```python
  from loading_module import simulate_loading
  
  simulate_loading(3)
  ```
