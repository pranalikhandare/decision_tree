# Define the knowledge base
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

# Function to traverse the decision tree
def traverse_tree(tree):
    if isinstance(tree, dict):
        # Get the first question in the dictionary
        question = next(iter(tree))
        print(question)
        
        # Get user input (Yes/No)
        answer = input("Enter Yes or No: ").capitalize()
        
        # Recursively call traverse_tree on the next node
        return traverse_tree(tree[question][answer])
    else:
        # Base case: we've reached a solution
        return tree

# Start traversal
print("Troubleshooting result:", traverse_tree(K_Base))
