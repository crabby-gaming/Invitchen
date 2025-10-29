import mysql
import mysql.connector
import tkinter as tk
from tkinter import * 
from tkinter.font import Font

db = mysql.connector.connect( host ="localhost", user="root", passwd ="placeholder", database = "IAdatabase")

def destroy_previous_page():
    # Destroy all widgets and frames in the root window
    for widget in action_frame.winfo_children():
        widget.destroy()

def addrec():

    destroy_previous_page()

    def delete():
        inputrecipe.delete(1.0, END)
        inputname.delete(1.0, END)
        ingrquant.delete(1.0,END)
        ingtype.delete(1.0, END)

    def save(): 
       x = inputrecipe.get(1.0,END).strip()
       y = inputname.get(1.0,END).strip()
       z = ingrquant.get(1.0, END).strip()
       e = ingtype.get(1.0, END).strip()

       query = "INSERT INTO recipe (ingname , ingquant, type, name) VALUES (%s, %s, %s, %s)"
       data = (x,z,e,y)

       recursor = db.cursor()
       recursor.execute(query,data)
       db.commit()
       recursor.close()

    addrectlbl = tk.Label(action_frame, text= " the name of your recipe ", fg ='#FFD300' ,font= 'bold')
    addrecilabel = tk.Label(action_frame, text= "add new recipe", fg ='#FFD300' ,font= 'bold')
    addinglabel = tk.Label(action_frame, text= " add quantity", fg ='#FFD300' ,font= 'bold')
    addtypelabel =tk.Label(action_frame, text= " add type", fg ='#FFD300' ,font= 'bold')

    inputname = Text(action_frame,font=("Times", 16),height=1, width=40)

    inputrecipe = Text(action_frame, font=("Times", 16), height=1, width= 40)

    ingrquant = Text(action_frame, font=('Times', 16), height = 1, width = 40)

    ingtype = Text(action_frame, font=('Times', 16), height = 1, width = 40)
    
    addrectlbl.pack()
    inputname.pack(padx= 20, pady =20)
    addrecilabel.pack(padx=20, pady=20)
    inputrecipe.pack(padx= 20,pady=20)
    addinglabel.pack(padx=20, pady=20)
    ingrquant.pack(padx= 20, pady=20)
    addtypelabel.pack(padx=20, pady=20)
    ingtype.pack(padx=20, pady= 20)
    
    buttonframe = Frame(action_frame)
    buttonframe.pack(pady=20)

    deleteallbutton = Button(buttonframe, command= delete, text= "delete all", font= ("times", 16))
    deleteallbutton.grid(row=0, column=0,padx=20)
    savebutton = Button(buttonframe, command= save, text= "save", font= ("times", 16))
    savebutton.grid(row=0, column=1,padx=20)

def seerec(): 
    destroy_previous_page()

    def search_recipe():
        name = searchbar.get(1.0, END).strip()  # Get the value when the search button is clicked
        query = "SELECT * FROM recipe WHERE name = %s"
        seerecursor.execute(query, (name,))
        data = seerecursor.fetchall()
        # Do something with the fetched data, such as displaying it in the GUI
        info.config(text=str(data))

    heading = tk.Label(action_frame, text="What recipe would you like to make", fg='#FFD300', font='bold')
    heading.pack()

    searchbar = Text(action_frame, font=("Times", 16), height=1, width=40)
    searchbar.pack()

    search_button = Button(action_frame, text="Search", command=search_recipe)
    search_button.pack()

    # Label to display the fetched data
    info = tk.Label(action_frame, text="", fg='#FFD300', font='bold')
    info.pack()

    # Create a cursor
    seerecursor = db.cursor()

def inventory(): 
    destroy_previous_page()

    invcursor = db.cursor()
    inventorylabel = tk.Label(action_frame, text= "Your current foodstuff", fg ='#FFD300' ,font= 'bold')

    invqy = "SELECT * FROM inventory"
    invcursor.execute(invqy)

    data = invcursor.fetchall()
    invcursor.close()

    invcont = tk.Label(action_frame, text= str(data), fg ='#FFD300' ,font= 'bold')

    inventorylabel.pack(padx=20, pady=20)
    invcont.pack(padx= 20, pady= 20)

    invcursor.close()

def addgrcpage():
    destroy_previous_page()

    def delete(): 
        groceryname.delete(1.0, END)
        groceryquant.delete(1.0, END)

    def save(): 
        x = groceryname.get(1.0, END).strip()
        y = groceryquant.get(1.0, END).strip()

        # Forming SQL query and data
        query = "INSERT INTO groceries (itemname, quant) VALUES (%s, %s)"
        data = (x, y)

        # Executing the query
        grcursor = db.cursor()
        grcursor.execute(query, data)
        db.commit()
        grcursor.close()
        
        # Clear the entry fields after saving
        delete()

    groceryname = Text(action_frame, height=5, width=40)
    groceryquant = Text(action_frame, height=5, width=40)

    addnamelbl = tk.Label(action_frame, text="Name of ingredient", fg='#FFD300', font='bold')
    addquantlbl = tk.Label(action_frame, text="How many?", fg='#FFD300', font='bold')

    addnamelbl.pack()
    groceryname.pack()
    addquantlbl.pack()
    groceryquant.pack()

    grcbtnframe = tk.Frame(action_frame)
    grcbtnframe.pack(padx=20, pady=10)

    delbtn = tk.Button(grcbtnframe, text='Delete', font=('Times', 16), command=delete)
    delbtn.pack(side=tk.LEFT, padx=5)

    addbtn = tk.Button(grcbtnframe, text='Add', font=('Times', 16), command=save)
    addbtn.pack(side=tk.LEFT, padx=5)

def yourlistpg():
    destroy_previous_page()

    licursor = db.cursor()

    query = "SELECT itemname, quant FROM groceries"
    licursor.execute(query)
    data = licursor.fetchall()

    licursor.close()

    message = "Here is your grocery list:"
    glist_label = Label(action_frame, text=message, font=("times", 16))
    glist_label.pack()

    grocery_list_text = Text(action_frame, height=10, width=50)
    grocery_list_text.pack()

    grocery_list = ""
    for item in data:
        grocery_list += f"{item[0]} - {item[1]}\n"

    grocery_list_text.insert(END, grocery_list)



    licursor.close()

def addinv():
    destroy_previous_page()

    def save():
        x = inputinv.get(1.0, END).strip()
        y = inputinvq.get(1.0, END).strip()
        z = inputleftover.get(1.0, END).strip()
        e = inputleftoverq.get(1.0, END).strip()

        # Execute queries to insert data into inventory and leftovers tables
        addinvcursor = db.cursor()
        query_inv = "INSERT INTO inventory (invname, invnum) VALUES (%s, %s)"
        data_inv = (x, y)
        addinvcursor.execute(query_inv, data_inv)

        query_leftover = "INSERT INTO leftovers (leftovername, leftovernum) VALUES (%s, %s)"
        data_leftover = (z, e)
        addinvcursor.execute(query_leftover, data_leftover)

        db.commit()
        addinvcursor.close()

    inputinv = Text(action_frame, font=("Times", 16), height=1, width=40)
    inputinvq = Text(action_frame, font=("Times", 16), height=1, width=40)
    inputleftover = Text(action_frame, font=("Times", 16), height=1, width=40)
    inputleftoverq = Text(action_frame, font=("Times", 16), height=1, width=40)

    invlbl = tk.Label(action_frame, text="Name of item", fg='#FFD300', font='bold')
    invqlbl = tk.Label(action_frame, text="How many items?", fg='#FFD300', font='bold')
    leftoverlbl = tk.Label(action_frame, text="Name of dish", fg='#FFD300', font='bold')
    leftoverqlbl = tk.Label(action_frame, text="How many?", fg='#FFD300', font='bold')

    invlbl.pack()
    inputinv.pack()
    invqlbl.pack()
    inputinvq.pack()
    leftoverlbl.pack()
    inputleftover.pack()
    leftoverqlbl.pack()
    inputleftoverq.pack()

    # Add button to execute the insertion
    add_button = Button(action_frame, text="Add to Inventory and Leftovers", command=save)
    add_button.pack()







def leftoverpg(): 
    destroy_previous_page()

    leftovers = Label(action_frame, text="Your Leftovers", fg='#FFD300', font='bold')
    leftovers.pack()

    # Create a frame to contain the scrollable list
    leftover_frame = Frame(action_frame)
    leftover_frame.pack(padx=20, pady=20)

    # Create a scrollbar
    scrollbar = Scrollbar(leftover_frame, orient=VERTICAL)

    # Create a Text widget to display the leftovers
    leftover_text = Text(leftover_frame, height=10, width=50, yscrollcommand=scrollbar.set)
    scrollbar.config(command=leftover_text.yview)

    scrollbar.pack(side=RIGHT, fill=Y)
    leftover_text.pack(side=LEFT, fill=BOTH, expand=True)

    # Fetch data from the database
    leftovercursor = db.cursor() 
    query = "SELECT * FROM leftovers"
    leftovercursor.execute(query)

    info = leftovercursor.fetchall()
    leftovercursor.close()

    # Display the fetched data in the Text widget
    for item in info:
        leftover_text.insert(END, f"{item}\n")

#done
def toggle_menu():


    def collapse_menu():
        toggle_menu_frame.destroy()
        toggle_btn.config(text= '≡',command=toggle_menu)

    toggle_menu_frame = tk.Frame(root , bg= '#FFD300')
    window_height = root.winfo_height()
    toggle_menu_frame.place(x= 0, y= 50, height= window_height, width= 200 )
    toggle_btn.config(text= 'X' , command= collapse_menu)
    
    invpage_button = tk.Button(toggle_menu_frame, text= 'your inventory', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white' )
    invpage_button.place(x = 20 , y = 20)
    invpage_button.config( command=inventory)

    addrecbtn = tk.Button(toggle_menu_frame, text= 'add recipe', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white' )
    addrecbtn.place(x = 20 , y = 100)
    addrecbtn.config( command=addrec )

    recipebrowsebtn = tk.Button(toggle_menu_frame, text= 'recipes', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white' )
    recipebrowsebtn.place(x = 20 , y = 180)
    recipebrowsebtn.config(command= seerec)

    grocerybtn = tk.Button(toggle_menu_frame, text= 'add grocery', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white' )
    grocerybtn.place(x = 20 , y = 260)
    grocerybtn.config(command = addgrcpage)

    grclistbtn = tk.Button(toggle_menu_frame, text= 'your list', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white')
    grclistbtn.place(x = 20 , y = 340)
    grclistbtn.config(command= yourlistpg)

    leftoverbtn = tk.Button(toggle_menu_frame, text= 'leftovers', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white')
    leftoverbtn.place(x = 20 , y = 420)
    leftoverbtn.config(command= leftoverpg)

    addinvbtn = tk.Button(toggle_menu_frame, text= 'add leftovers', font = ('bold', 20), bd= 0 , bg='#FFD300' , fg= 'white')
    addinvbtn.place(x = 20 , y = 500)
    addinvbtn.config(command= addinv)





root = tk.Tk()
root.geometry('300x500')
root.title('divyans comp sci IA')

head_frame = tk.Frame(root , bg='#FFD300' , highlightbackground= 'white' , highlightthickness= 1)

action_frame = tk.Frame(root)


toggle_btn = tk.Button(head_frame, text='≡', bg= '#FFD300' , fg= 'white', font=('Bold', 30), bd=0 , activebackground='#FFD300', activeforeground= 'white' , command= toggle_menu)
toggle_btn.pack(side=tk.LEFT)

logo_lbl = tk.Label(head_frame,text='🍲', bg='#FFD300', fg='white', font=('bold', 30))
logo_lbl.pack(side=tk.RIGHT ,fill= tk.Y)

title_font = Font(family='Helvetica', size = 20, weight= 'bold')
title_label = tk.Label(head_frame, text='INVITCHEN', bg= '#FFD300' , fg= 'white', font=title_font)
title_label.pack(side= tk.TOP, fill= tk.Y)

head_frame.pack(side = tk.TOP , fill = tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)
action_frame.pack()

root.mainloop()
db.close()