import os
import random
import mysql.connector
f = open("credentials.txt")
mydb = mysql.connector.connect(host=f.readline(),user=f.readline(),password=f.readline())
print(mydb)
f.close()

mycursor = mydb.cursor()

#----------------------------------------------------------------------------------------------

def data_eraser():
    mycursor.execute("use zACM_enterprises")
    mycursor.execute( "TRUNCATE TABLE INVENTORY_OF_ALL_ITEMS" )
    mycursor.execute("use zACM_enterprises")
    mycursor.execute( "TRUNCATE TABLE TRANSACTION_ITEM_DATA" )
    mydb.commit()
                
#----------------------------------------------------------------------------------------------

def random_generator(count):
    for i in range(0,count): 
        dept_id = ["31#01","31#02","31#03"]
        dept = random.choice(dept_id)
        name1 = [
                "Microwave",
                "Blender",
                "Toaster",
                "Coffee Maker",
                "Food Processor",
                "Stand Mixer",
                "Electric Kettle",
                "Slow Cooker",
                "Instant Pot",
                "Air Fryer",
                "Juicer",
                "Rice Cooker",
                "Waffle Maker",
                "Panini Press",
                "Bread Maker",
                "Electric Grill",
                "Hand Mixer",
                "Immersion Blender",
                "Pressure Cooker",
                "Sous Vide Cooker",
                "Toaster Oven",
                "Espresso Machine",
                "Ice Cream Maker",
                "Fryer",
                "Soda Maker",
                "Dehydrator",
                "Popcorn Maker",
                "Food Steamer",
                "Electric Can Opener",
                "Food Scale",
                "Vacuum Sealer",
                "Induction Cooktop",
                "Electric Griddle",
                "Hot Plate",
                "Food Slicer",
                "Electric Knife",
                "Milk Frother",
                "Electric Skillet",
                "Grain Mill",
                "Seltzer Maker",
                "Food Warmer",
                "Margarita Machine",
                "Electric Pressure Cooker",
                "Yogurt Maker",
                "Tea Maker",
                "Kitchen Timer",
                "Digital Thermometer",
                "Meat Thermometer",
                "Oven Thermometer",
                "Kitchen Scale",
                "Kitchen Timer",
                "Kitchen Thermometer",
                "Air Purifier",
                "Water Purifier",
                "Robot Vacuum",
                "Smart Refrigerator",
                "Smart Oven",
                "Smart Coffee Maker",
                "Smart Slow Cooker",
                "Smart Blender",
                "Smart Sous Vide Cooker",
                "Smart Rice Cooker",
                "Smart Kettle",
                "Smart Toaster",
                "Smart Microwave",
                "Smart Dishwasher",
                "Smart Air Fryer",
                "Smart Grill",
                "Smart Scale",
                "Smart Food Processor",
                "Smart Food Steamer",
                "Smart Induction Cooktop",
                "Smart Electric Skillet",
                "Smart Food Dehydrator",
                "Smart Panini Press",
                "Smart Waffle Maker",
                "Smart Bread Maker",
                "Smart Ice Cream Maker",
                "Smart Popcorn Maker",
                "Smart Hand Mixer",
                "Smart Immersion Blender",
                "Smart Stand Mixer",
                "Smart Electric Can Opener",
                "Smart Vacuum Sealer",
                "Smart Food Warmer",
                "Smart Milk Frother",
                "Smart Food Slicer",
                "Smart Electric Knife",
                "Smart Grain Mill",
                "Smart Food Scale"
                ]

        name2 =  [
                "Pizza",
                "Burger",
                "Sushi",
                "Pasta",
                "Steak",
                "Salad",
                "Tacos",
                "Sandwich",
                "Fried Chicken",
                "Soup",
                "Rice",
                "Curry",
                "Nachos",
                "Burrito",
                "Lasagna",
                "Hot Dog",
                "Fish and Chips",
                "Wings",
                "Muffins",
                "Donuts",
                "Bagel",
                "Croissant",
                "French Toast",
                "Pancakes",
                "Waffles",
                "Omelette",
                "Quiche",
                "Crepes",
                "Frittata",
                "Eggs Benedict",
                "Toast",
                "Cereal",
                "Granola",
                "Yogurt",
                "Fruit Salad",
                "Smoothie",
                "Milkshake",
                "Ice Cream",
                "Gelato",
                "Sorbet",
                "Cake",
                "Cookies",
                "Brownies",
                "Cupcakes",
                "Cheesecake",
                "Pie",
                "Tiramisu",
                "Creme Brulee",
                "Macarons",
                "Truffles",
                "Pudding",
                "Cobbler",
                "Baklava",
                "Cannoli",
                "Mousse",
                "Biscotti",
                "Fudge",
                "Churros",
                "Doughnuts",
                "Eclairs",
                "Gingerbread",
                "Shortbread",
                "Biscuits",
                "Cinnamon Rolls",
                "Croissants",
                "Danish",
                "Pretzels",
                "Meringue",
                "Pavlova",
                "Banana Bread",
                "Zucchini Bread",
                "Cornbread",
                "Garlic Bread",
                "Focaccia",
                "Breadsticks",
                "Pita Bread",
                "Naan",
                "Tortillas",
                "English Muffins",
                "Rye Bread",
                "Baguette",
                "Ciabatta",
                "Panini",
                "Sourdough Bread",
                "Pumpernickel Bread",
                "Multigrain Bread",
                "Scones",
                "Brioche",
                "Hummus",
                "Guacamole",
                "Salsa",
                "Pesto",
                "Tzatziki",
                "Baba Ganoush",
                "Tapenade",
                "Bruschetta",
                "Caprese Salad",
                "Antipasto",
                "Stuffed Mushrooms",
                "Deviled Eggs",
                "Spring Rolls",
                "Empanadas",
                "Calamari",
                "Crab Cakes",
                "Shrimp Cocktail",
                "Escargot",
                "Caviar"
                ]

        name3 = [
                "T-shirt",
                "Jeans",
                "Dress",
                "Shirt",
                "Skirt",
                "Blouse",
                "Shorts",
                "Sweater",
                "Jacket",
                "Coat",
                "Hoodie",
                "Cardigan",
                "Blazer",
                "Suit",
                "Trousers",
                "Leggings",
                "Jumpsuit",
                "Romper",
                "Pajamas",
                "Robe",
                "Sweatshirt",
                "Tank Top",
                "Polo Shirt",
                "Halter Top",
                "Crop Top",
                "Button-up Shirt",
                "Sweatpants",
                "Capris",
                "Cargo Pants",
                "Chinos",
                "Corduroys",
                "Khakis",
                "Dungarees",
                "Overalls",
                "Maxi Dress",
                "Midi Dress",
                "Mini Dress",
                "Wrap Dress",
                "Shift Dress",
                "Bodycon Dress",
                "A-line Skirt",
                "Pencil Skirt",
                "Mini Skirt",
                "Maxi Skirt",
                "Denim Skirt",
                "Pleated Skirt",
                "Leather Jacket",
                "Bomber Jacket",
                "Windbreaker",
                "Parka",
                "Trench Coat",
                "Peacoat",
                "Raincoat",
                "Fleece Jacket",
                "Down Jacket",
                "Vest",
                "Puffer Vest",
                "Sweat Vest",
                "Biker Jacket",
                "Fur Coat",
                "Fur Vest",
                "Varsity Jacket",
                "Tailored Suit",
                "Tuxedo",
                "Wedding Dress",
                "Evening Gown",
                "Cocktail Dress",
                "Ball Gown",
                "Formal Wear",
                "Swimsuit",
                "Bikini",
                "One-piece Swimsuit",
                "Swim Trunks",
                "Board Shorts",
                "Rash Guard",
                "Cover-up",
                "Sarong",
                "Sun Hat",
                "Beanie",
                "Fedora",
                "Baseball Cap",
                "Bucket Hat",
                "Beret",
                "Newsboy Cap",
                "Snapback",
                "Trapper Hat",
                "Visor",
                "Scarf",
                "Gloves",
                "Mittens",
                "Handkerchief",
                "Necktie",
                "Bowtie",
                "Ascot Tie",
                "Belt",
                "Suspenders",
                "Headband",
                "Bandana",
                "Hair Clip",
                "Hair Band",
                "Hair Tie",
                "Barrette"
                ]
        
        if (dept == "31#01"):#electrical
            name = random.choice(name1)

        if (dept == "31#02"):#food
            name = random.choice(name2)
    
        if (dept == "31#03"):#clothes
            name = random.choice(name3)
    
        price = random.randint(500,1000)
        quantity = random.randint(0,1)
        
        if quantity == 1:
            quantity = random.randint(50,100)
            status = "IN"
        
        if quantity == 0 :
            status = "OUT"
  
        # print (dept,name,price,quantity,status)
        mycursor.execute("use zACM_enterprises")
        sql = "INSERT INTO INVENTORY_OF_ALL_ITEMS (DEPT_ID,ITEM_NAME,ITEM_PRICE,QUANTITY,STATUS) VALUES (%s, %s, %s, %s, %s)"
        values = (dept,name,price,quantity,status)
        mycursor.execute( sql , values )
        mydb.commit()

#----------------------------------------------------------------------------------------------

def starter(choice):
    os.system('cls')
    print("\n")
    choice = str ( input ("would you like to generate random entries in your database type 'yes' or 'no'  or 'nochange' = "))   
    if (choice == "yes"):
        os.system('cls')
        print("\n")
        count = int (input ("enter no. of row's (data) you want in your database = "))
        data_eraser()
        random_generator(count)
    elif (choice == "no"):
        os.system('cls')
        print("\n")
        data_eraser()
        print ("empty database will be provided to you ")
    elif (choice == "nochange"):
        os.system('cls')
    else :
        os.system('cls')
        print("\n")
        starter(None)
        
    os.system('cls')
    print("\n")
    print("done")
    return("yes")

#----------------------------------------------------------------------------------------------