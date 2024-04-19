from tkinter import *
import tkinter as tk
from backend import *
from tkinter import messagebox
from data_generator_main import *

#----------------------------------------------------------------------------------

def window_main(dept_id):
    root=tk.Tk()
    root.geometry("1000x600")
    root.resizable(False,False)
    root.title('DBMS_PROJECT') 
    
#----------------------------------------------------------------------------------

    def table1_page():#shows itemlist  
        table1_frame = tk.Frame(main_frame)

        def details():
            
            item_id = item_id_entry.get()
            quantity = quantity_entry.get()
            
            if (dept_id == "admin"):
                which_dept = which_dept_entry.get()
                temp = which_dept    
            else:
                temp = dept_id

            item_result = integer_checker(item_id)
            quantity_result = integer_checker(quantity)
            
            if ((item_id!="")and(quantity!="")and(item_result=="valid")and(quantity_result=="valid")):
                
                item_id = string_to_int(item_id)
                quantity = string_to_int(quantity)

                result3 = dept_and_item_id_checker(temp,item_id)
                result4 = quantity_checker(item_id,quantity)
                
                if (result3 == "ok"):
                    if(result4[0] == "ok"):
                        sold_quantity = quantity
                        quantity = result4[1]
                        get_sell_result_and_update_trans(item_id,sold_quantity,quantity)
                        update_quantity(item_id,quantity)     
                        messagebox.showinfo("Successful","ITEM HAS BEEN SOLD")
                        if (dept_id == "admin"):
                            which_dept_entry.delete(0, END)
                            item_id_entry.delete(0, END)
                            quantity_entry.delete(0, END)
                        else:
                            item_id_entry.delete(0, END)
                            quantity_entry.delete(0, END)
                    else:
                        messagebox.showerror("Failed","INVALID QUANTITY")
                else:
                    messagebox.showerror("Failed","INVALID DEPT")
            else:
                messagebox.showerror("Failed","INVALID ENTRY")
                
        if (dept_id == "admin"):           
            # Create label and entry
            which_dept_label = tk.Label(table1_frame, text=" WHICH_DEPT:(int) ",font=("Bold",20))
            which_dept_label.pack()
            which_dept_entry = tk.Entry(table1_frame,font=("Bold",20))
            which_dept_entry.pack()
                
        # Create label and entry
        item_id_label = tk.Label(table1_frame, text=" ITEM_ID:(int) ",font=("Bold",20))
        item_id_label.pack()
        item_id_entry = tk.Entry(table1_frame,font=("Bold",20))
        item_id_entry.pack()
        
        # Create label and entry
        quantity_label = tk.Label(table1_frame, text=" QUANTITY:(int) ",font=("Bold",20))
        quantity_label.pack()
        quantity_entry = tk.Entry(table1_frame,font=("Bold",20))
        quantity_entry.pack()
       
        add_button = tk.Button(table1_frame, text=" SELL ", command=details,font=("Bold",20))
        add_button.pack()
            
        table1_frame.pack(pady=20)    

#----------------------------------------------------------------------------------

    def table2_page():#to add_item
        table2_frame = tk.Frame(main_frame)
        
        def details():
            name = name_entry.get()
            price = price_entry.get()
            quantity = quantity_entry.get()
            
            if (dept_id == "admin"):
                which_dept = which_dept_entry.get()
                if ((which_dept!="")and((which_dept=="31#01")or(which_dept=="31#02")or(which_dept=="31#03"))):
                    temp = which_dept  
                    validity = "ok"
                else:
                    validity = "wronge"
            else:
                temp = dept_id 
                if((dept_id=="31#01")or(dept_id=="31#02")or(dept_id=="31#03")):
                    validity = "ok"
                else:
                    validity = "wronge"

            result_price = integer_checker(price)
            result_quantity = integer_checker(quantity)

            if ((price != "")and(name != "")and(quantity != "")and(validity == "ok")):
                if ((result_price == "valid")and(result_quantity == "valid")): 
                    add_data(temp,name,price,quantity)
                    messagebox.showinfo("Successful","ITEM HAS BEEN ADDED")
                    if (dept_id == "admin"):
                        which_dept_entry.delete(0, END)
                        price_entry.delete(0, END)
                        name_entry.delete(0, END)
                        quantity_entry.delete(0, END)
                    else:
                        price_entry.delete(0, END)
                        name_entry.delete(0, END)
                        quantity_entry.delete(0, END)
                else:
                    messagebox.showerror("Failed","INVALID ENTRIES")
            else:
                if(validity=="wronge"):
                    messagebox.showerror("Failed","INVALID DEPT_ID")
                else:
                    messagebox.showerror("Failed","FILL ALL FIELDS")
            
        if (dept_id == "admin"):           
            # Create label and entry
            which_dept_label = tk.Label(table2_frame, text=" WHICH_DEPT:(int) ",font=("Bold",20))
            which_dept_label.pack()
            which_dept_entry = tk.Entry(table2_frame,font=("Bold",20))
            which_dept_entry.pack()            
            
        # Create label and entry
        price_label = tk.Label(table2_frame, text=" PRICE:(int) ",font=("Bold",20))
        price_label.pack()
        price_entry = tk.Entry(table2_frame,font=("Bold",20))
        price_entry.pack()
        
        # Create label and entry
        name_label = tk.Label(table2_frame, text=" NAME:(varchar) ",font=("Bold",20))
        name_label.pack()
        name_entry = tk.Entry(table2_frame,font=("Bold",20))
        name_entry.pack()
        
        # Create label and entry
        quantity_label = tk.Label(table2_frame, text=" QUANTITY:(int) ",font=("Bold",20))
        quantity_label.pack()
        quantity_entry = tk.Entry(table2_frame,font=("Bold",20))
        quantity_entry.pack()  
        
        add_button = tk.Button(table2_frame, text=" ADD ", command=details,font=("Bold",20))
        add_button.pack()

        table2_frame.pack(pady=20) 
    
#----------------------------------------------------------------------------------
    
    def table3_page():#to delete_items
        table3_frame = tk.Frame(main_frame)
        
        def details():            
            item_id = item_id_entry.get()
            result_item_id = integer_checker(item_id)
            
            if (dept_id == "admin"):
                which_dept = which_dept_entry.get()
                temp = which_dept    
            else:
                temp = dept_id
            
            if ((item_id != "")and(result_item_id == "valid")):
                item_id = string_to_int(item_id)
                if (dept_and_item_id_checker(temp,item_id) == "ok"):
                    delete_item(item_id)
                    messagebox.showinfo("Successful","ITEM HAS BEEN DELETED")
                    if (dept_id == "admin"):
                        which_dept_entry.delete(0, END)
                        item_id_entry.delete(0, END)
                    else:
                        item_id_entry.delete(0, END)
                else:
                    messagebox.showerror("Failed","INVALID, ITEM NOT FOUND")
            else:
                messagebox.showerror("Failed","INVALID ENTRYS")
        
        if (dept_id == "admin"):           
            # Create label and entry
            which_dept_label = tk.Label(table3_frame, text=" WHICH_DEPT:(int) ",font=("Bold",20))
            which_dept_label.pack()
            which_dept_entry = tk.Entry(table3_frame,font=("Bold",20))
            which_dept_entry.pack()  
                
        # Create label and entry
        item_id_label = tk.Label(table3_frame, text=" ITEM_ID:(int) ",font=("Bold",20))
        item_id_label.pack()
        item_id_entry = tk.Entry(table3_frame,font=("Bold",20))
        item_id_entry.pack()  
        
        add_button = tk.Button(table3_frame, text=" DELETE ", command=details,font=("Bold",20))
        add_button.pack()
        
        table3_frame.pack(pady=20) 
        
#----------------------------------------------------------------------------------

    def table4_page():#to update_item
        table4_frame = tk.Frame(main_frame)
        
        def details():
            dept = dept_entry.get()
            name = name_entry.get()
            price = price_entry.get()
            quantity = quantity_entry.get()
            item_id = item_id_entry.get()
            
            if (dept_id == "admin"):
                which_dept = which_dept_entry.get()
                temp = which_dept    
            else:
                temp = dept_id
            
            if ((price != "")and(name != "")and(quantity != "")and(item_id != "")): 
                if ((dept=="31#01")or(dept=="31#02")or(dept=="31#03")):
                    result_price = integer_checker(price)
                    result_quantity = integer_checker(quantity)
                    result_item_id = integer_checker(item_id)
                    if ((result_price == "valid")and(result_quantity == "valid")and(result_item_id == "valid")):
                        result1 = string_to_int( item_id )
                        result2 = dept_and_item_id_checker(temp,result1)
                        if (result2 == "ok"):
                            item_id = int( item_id_entry.get() )
                            if item_present_or_not(item_id) == "present":
                                update_data(dept,name,price,quantity,item_id)
                                messagebox.showinfo("Successful","ITEM HAS BEEN UPDATED")
                                if (dept_id == "admin"):
                                    which_dept_entry.delete(0, END)
                                    dept_entry.delete(0, END)
                                    price_entry.delete(0, END)
                                    name_entry.delete(0, END)
                                    quantity_entry.delete(0, END)
                                    item_id_entry.delete(0, END)
                                else:
                                    dept_entry.delete(0, END)
                                    price_entry.delete(0, END)
                                    name_entry.delete(0, END)
                                    quantity_entry.delete(0, END)
                                    item_id_entry.delete(0, END)    
                            else:
                                messagebox.showerror("Failed","ITEM TO UPDATE NOT FOUND")  
                        else:
                            messagebox.showerror("Failed","NOT IN THIS DEPT")
                    else:
                        messagebox.showerror("Failed","INVALID ENTRYS")
                else:
                    messagebox.showerror("Failed","INVALID DEPT")
            else:
                messagebox.showerror("Failed","INVALID ENTRYS")
                
        if (dept_id == "admin"):           
            # Create label and entry
            which_dept_label = tk.Label(table4_frame, text=" FROM:DEPT_ID:(int) ",font=("Bold",20))
            which_dept_label.pack()
            which_dept_entry = tk.Entry(table4_frame,font=("Bold",20))
            which_dept_entry.pack()          
        
        # Create label and entry
        dept_label = tk.Label(table4_frame, text=" TO:DEPT_ID:(varchar) ",font=("Bold",20))
        dept_label.pack()
        dept_entry = tk.Entry(table4_frame,font=("Bold",20))
        dept_entry.pack()                

        
        # Create label and entry
        name_label = tk.Label(table4_frame, text=" NAME:(varchar) ",font=("Bold",20))
        name_label.pack()
        name_entry = tk.Entry(table4_frame,font=("Bold",20))
        name_entry.pack()
        
        # Create label and entry
        price_label = tk.Label(table4_frame, text=" PRICE:(int) ",font=("Bold",20))
        price_label.pack()
        price_entry = tk.Entry(table4_frame,font=("Bold",20))
        price_entry.pack()        

        # Create label and entry
        quantity_label = tk.Label(table4_frame, text=" QUANTITY:(int) ",font=("Bold",20))
        quantity_label.pack()
        quantity_entry = tk.Entry(table4_frame,font=("Bold",20))
        quantity_entry.pack()
        
        # Create label and entry
        item_id_label = tk.Label(table4_frame, text=" ITEM_ID:(int) ",font=("Bold",20))
        item_id_label.pack()
        item_id_entry = tk.Entry(table4_frame,font=("Bold",20))
        item_id_entry.pack()    
        
        add_button = tk.Button(table4_frame, text=" UPDATE ", command=details,font=("Bold",20))
        add_button.pack()

        table4_frame.pack(pady=20)

#----------------------------------------------------------------------------------

    def table5_page():#show items present in in_stock
        table5_frame = tk.Frame(main_frame)
        
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        # Create a canvas with a scroll bar
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        # Add widgets to the canvas
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        data = top_table()+in_stock(dept_id)
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(inner_frame, width=20, fg='black', font=('Arial',12,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
                
        # Update scroll region when the canvas size changes
        inner_frame.bind("<Configure>", on_canvas_configure)
        
        table5_frame.pack(pady=20) 

#----------------------------------------------------------------------------------

    def table6_page():#show items present in in_stock
        table6_frame = tk.Frame(main_frame)
        
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        # Create a canvas with a scroll bar
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        # Add widgets to the canvas
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        data = top_table()+out_stock(dept_id)
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(inner_frame, width=20, fg='black', font=('Arial',12,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
                
        # Update scroll region when the canvas size changes
        inner_frame.bind("<Configure>", on_canvas_configure)
        
        table6_frame.pack(pady=20) 

#----------------------------------------------------------------------------------

    def table7_page():#show items present in in_stock
        table7_frame = tk.Frame(main_frame)
        
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        # Create a canvas with a scroll bar
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        # Add widgets to the canvas
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        data = top_table()+all_item(dept_id)
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(inner_frame, width=20, fg='black', font=('Arial',12,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])
                
        # Update scroll region when the canvas size changes
        inner_frame.bind("<Configure>", on_canvas_configure)
        
        table7_frame.pack(pady=20) 

#----------------------------------------------------------------------------------

    def table8_page():#show items present in in_stock
        table8_frame = tk.Frame(main_frame)
        
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        # Create a canvas with a scroll bar
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        # Add widgets to the canvas
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        data = top_table_trans()+transactions(dept_id)+billing_table(dept_id)    
        total_rows = len(data)
        total_columns = len(data[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(inner_frame, width=13, fg='black', font=('Arial',12,'bold'))
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])

        # Update scroll region when the canvas size changes
        inner_frame.bind("<Configure>", on_canvas_configure)
        
        table8_frame.pack(pady=20) 

#----------------------------------------------------------------------------------

    def hide_indicators():
        table1_indicate.config(bg="darkslateblue")
        table2_indicate.config(bg="darkslateblue")
        table3_indicate.config(bg="darkslateblue")
        table4_indicate.config(bg="darkslateblue")
        table5_indicate.config(bg="darkslateblue")
        table6_indicate.config(bg="darkslateblue")
        table7_indicate.config(bg="darkslateblue")
        table8_indicate.config(bg="darkslateblue")
        
#----------------------------------------------------------------------------------

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()
            
#----------------------------------------------------------------------------------

    def indicate(lb, page):
        hide_indicators()   #hiding indicator before new touch
        lb.config(bg='pink')
        delete_pages()
        page()   
        
#----------------------------------------------------------------------------------

    options_frame = tk.Frame(root,bg="darkslateblue") #option frame 
    
    table1_btn = tk.Button(options_frame,text=" SELL_ITEM ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table1_indicate , table1_page) )
    table1_btn.place(x=10,y=50)
    table1_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table1_indicate.place(x=3 , y=50 , width=5 , height=40)    
    
    table2_btn = tk.Button(options_frame,text=" ADD ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table2_indicate , table2_page) )
    table2_btn.place(x=10,y=100)
    table2_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table2_indicate.place(x=3 , y=100 , width=5 , height=40)   

    table3_btn = tk.Button(options_frame,text=" DELETE ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table3_indicate , table3_page) )
    table3_btn.place(x=10,y=150)
    table3_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table3_indicate.place(x=3 , y=150 , width=5 , height=40)  
    
    table4_btn = tk.Button(options_frame,text=" UPDATE ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table4_indicate , table4_page) )
    table4_btn.place(x=10,y=200)
    table4_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table4_indicate.place(x=3 , y=200 , width=5 , height=40) 

    table5_btn = tk.Button(options_frame,text=" IN_STOCK ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table5_indicate , table5_page) )
    table5_btn.place(x=10,y=350)
    table5_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table5_indicate.place(x=3 , y=350 , width=5 , height=40) 
    
    table6_btn = tk.Button(options_frame,text=" OUT_STOCK ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table6_indicate , table6_page) )
    table6_btn.place(x=10,y=400)
    table6_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table6_indicate.place(x=3 , y=400 , width=5 , height=40)
    
    table7_btn = tk.Button(options_frame,text=" ALL_ITEM ",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table7_indicate , table7_page) )
    table7_btn.place(x=10,y=450)
    table7_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table7_indicate.place(x=3 , y=450 , width=5 , height=40)
    
    table8_btn = tk.Button(options_frame,text="Transaction",font=('Bold',15),fg='pink',bd=0
                        ,bg='darkslateblue',command=lambda: indicate(table8_indicate , table8_page) )
    table8_btn.place(x=10,y=500)
    table8_indicate = tk.Label(options_frame, text = '' , bg='darkslateblue')
    table8_indicate.place(x=3 , y=500 , width=5 , height=40)
    
    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=150,height=600) 

#----------------------------------------------------------------------------------

    main_frame = tk.Frame(root,highlightbackground="black",highlightthickness=2,bg="grey")

    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=850,height=600)

    root.mainloop()

#----------------------------------------------------------------------------------

def window_login():
    
    def login():
        username = username_entry.get()
        password = password_entry.get()
        result = name_acquire(username,password)

        # Check if username and password are correct
        if result[0] == "found":
            messagebox.showinfo("Login Successful","Welcome,Admin" )
            root.destroy()
            window_main(result[1])
            
        else:
            messagebox.showerror("Login Failed","Incorrect details")
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            # root.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Login Page")
    root.eval('tk::PlaceWindow . center')
    root.geometry("300x200")

    # Create username label and entry
    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Create password label and entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Create login button
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack()

    # Run the main event loop
    root.mainloop()
    
#----------------------------------------------------------------------------------

#main program call start here

result_start = starter(None)
if result_start == "yes":
    window_login()
else :
    print(" there was some error ")

# window_login()

# window_main("31#01")

#----------------------------------------------------------------------------------