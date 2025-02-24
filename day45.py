#if__name__=="__main__" in python 
# if __name__=="__main__" in python
# The if __name__ == "__main__": construct in Python is used to determine whether the current script is being run as the main program or if it’s being imported as a module into another script. This construct allows you to define code that should only be executed when the script is run directly, not when it’s imported as a module.

# Here’s a breakdown of its functionality:

# When a Python file is run directly (e.g., python myscript.py), the interpreter sets __name__ to "__main__".
# When a Python file is imported as a module (e.g., import mymodule), the interpreter sets __name__ to the name of the module (e.g., "mymodule").
# By using if __name__ == "__main__":, you can execute code only when the script is run directly, and not when it’s imported as a module. This is useful for several reasons:

# It prevents code from running accidentally when a module is imported.
# It allows you to write reusable code that can be imported and used in other scripts without executing its main logic.
# It provides a clear separation between executable code and reusable code.
import akash

akash.welcome()