# Import Sorting functions
from Sorting.bubbleSort import bubbleSort
from Sorting.selectionSort import selectionSort
from Sorting.insertionSort import insertionSort

def print_menu(options:dict):
    print("\nInteractive Terminal")
    
    for key,value in options.items():
        print(f"{key}: {value['description']}")
        

def interactive_terminal(options:dict):
    while True:
        print_menu(options=options)
        choice = input("Enter the number of your choice: ")
        action = options.get(choice)
        
        if action["action"]:
            arr = action["action"]()
            print(action["description"],'\n',
                  "original:",arr['original'],'\n',
                  "arr:",arr['arr'])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":    
    options = {}
    
    # Get array with functions which has `sort` string in them  
    globals_copy = [(name, obj) for name, obj in globals().items() if callable(obj) and name.endswith("Sort")]
    
    # Populate options dictionary from the copy
    for i, (name, func) in enumerate(globals_copy, start=1):
        options[str(i)] = {
            "description": name.replace("Sort", " Sort").capitalize(),
            "action": func
        }

    # Add the exit option
    options[str(len(options) + 1)] = {
        "description": "Exit",
        "action": exit
    }
        
    interactive_terminal(options=options)