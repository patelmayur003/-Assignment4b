'''
File Name: Assignment4b.py
Author: Mayur Patel
Description: An interactive list application with a GUI for searching, adding, removing, and sorting elements.
'''
# Import for the visualization of the interface (GUI)
class CustomObject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"CustomObject: {self.name}"

# Create instances of the custom class
object1 = CustomObject("Warning 4 packets remaining")
object2 = CustomObject("Full Stock")

# Create a list with a mixture of data types, including objects
my_list = ["apple ship 4", 2.5, "apple container 5", 3, 4.2,
           "banana container 6", object1, 7, 8.3, "date", object2]

# Create a Tkinter window
root = tk.Tk()
root.title("Interactive List App")

def search_element():
    search_term = search_entry.get()
    found = False
    for element in my_list:
        if isinstance(element, CustomObject):
            if search_term == element.name:
                result_label.config(text=f"{search_term} found in the list.", foreground="green")
                found = True
                break
        elif search_term == str(element):
            result_label.config(text=f"{search_term} found in the list.", foreground="green")
            found = True
            break
    if not found:
        result_label.config(text=f"{search_term} not found in the list.", foreground="red")

def add_element():
    new_element = add_entry.get()
    my_list.append(new_element)
    listbox.insert("end", new_element)
    add_entry.delete(0, "end")
    result_label.config(text=f"{new_element} added to the list.", foreground="green")

def remove_element():
    element_to_remove = remove_entry.get()
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        listbox.delete(listbox.get(0, "end").index(element_to_remove))
        remove_entry.delete(0, "end")
        result_label.config(text=f"{element_to_remove} removed from the list.", foreground="green")
    else:
        result_label.config(text=f"{element_to_remove} not found in the list.", foreground="red")

def sort_list():
    order = order_var.get()
    sorted_list = sorted(my_list, key=lambda x: (str(x) if isinstance(x, (int, float, str)) else x.name), reverse=(order == "Descending"))
    listbox.delete(0, "end")
    for element in sorted_list:
        listbox.insert("end", element)

def calculate_sum():
    total_sum = sum([x for x in my_list if isinstance(x, (int, float))])
    result_label.config(text=f"Sum of numeric elements in the list: {total_sum}", foreground="black")

def count_elements():
    total_count = len(my_list)
    result_label.config(text=f"Total number of elements in the list: {total_count}", foreground="black")

def refresh_list():
    listbox.delete(0, "end")
    search_entry.delete(0, "end")
    add_entry.delete(0, "end")
    remove_entry.delete(0, "end")
    result_label.config(text="", foreground="black")

def stop_program():
    root.destroy()  # Close the Tkinter window
    sys.exit()  # Exit the program

# Create and style the GUI elements
style = ttk.Style()
style.configure("TButton", padding=5, font=('Helvetica', 12))
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))

# Create and align labels and input fields
search_label = ttk.Label(root, text="Search for an element:")
search_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

search_entry = ttk.Entry(root)
search_entry.grid(row=0, column=1, padx=10, pady=10)

add_label = ttk.Label(root, text="Add a new element:")
add_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

add_entry = ttk.Entry(root)
add_entry.grid(row=1, column=1, padx=10, pady=10)

remove_label = ttk.Label(root, text="Remove an element:")
remove_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

remove_entry = ttk.Entry(root)
remove_entry.grid(row=2, column=1, padx=10, pady=10)

order_label = ttk.Label(root, text="Sort the list:")
order_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

order_var = tk.StringVar(value='Descending')
asc_button = ttk.Radiobutton(root, text="Ascending", variable=order_var, value='Ascending')
desc_button = ttk.Radiobutton(root, text="Descending", variable=order_var, value='Descending')

asc_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")
desc_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

# Create and align buttons
search_button = ttk.Button(root, text="Search", command=search_element)
search_button.grid(row=0, column=2, padx=10, pady=10)

add_button = ttk.Button(root, text="Add", command=add_element)
add_button.grid(row=1, column=2, padx=10, pady=10)

remove_button = ttk.Button(root, text="Remove", command=remove_element)
remove_button.grid(row=2, column=2, padx=10, pady=10)

sort_button = ttk.Button(root, text="Sort and Print", command=sort_list)
sort_button.grid(row=3, column=3, padx=10, pady=10)

listbox_label = ttk.Label(root, text="List of Elements:")
listbox_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

listbox = tk.Listbox(root, height=10, selectbackground="lightblue")
listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

result_label = ttk.Label(root, text="", font=('Helvetica', 12))
result_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

# Create additional function buttons
calculate_sum_button = ttk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_sum_button.grid(row=7, column=0, padx=10, pady=10)

count_elements_button = ttk.Button(root, text="Count Elements", command=count_elements)
count_elements_button.grid(row=7, column=1, padx=10, pady=10)

# Create the Refresh button
refresh_button = ttk.Button(root, text="Refresh", command=refresh_list)
refresh_button.grid(row=7, column=3, padx=10, pady=10)

# Create the Stop button
stop_button = ttk.Button(root, text="Stop", command=stop_program)
stop_button.grid(row=8, column=0, padx=10, pady=10)

# Start the GUI application
root.mainloop()
