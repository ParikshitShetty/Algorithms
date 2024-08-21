from Sorting.bubbleSort import bubbleSort
from Sorting.selectionSort import selectionSort

def print_menu(options:list):
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
    options = {
        "1": {
            "description": "Bubble Sort",
            "action":bubbleSort
        },
        "2": {
            "description": "Selection Sort",
            "action": selectionSort
        },
        "3": {
            "description": "Exit",
            "action": exit
        }
    }
    interactive_terminal(options=options)