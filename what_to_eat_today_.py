"""
What To Eat Today+ (Combo Version)
Author: Yihan Xiao
Description:
An upgraded food randomizer that uses country-based categories and
suggests a meal combo (main + drink). Data is persisted into a CSV file
so users can review what was suggested previously.
"""

import random
import time
import csv
import os
import tkinter as tk
from tkinter import messagebox

# --------------------------------------------------
# 1. CONFIG & DATA
# --------------------------------------------------
HISTORY_FILE = "history.csv"

# main dishes by cuisine
FOOD_DB = {
    "Japanese": [
        "Sukiyaki",
        "Sushi",
        "Yakitori",
        "Wagyu Beef Don",
        "Tempura",
        "Udon",
        "Katsu Curry",
        "UNAGI HITSUMABUSHI",
        "CHICKEN NANBAN",
        "WAGYU MIX TOJI",
        "CHICKEN KARA-AGE",
        "TERIYAKI CHICKEN",
        "MISO PORK LOIN KATSU",
        "PORK LOIN KATSU-TOJI",
        "NASU MISO and SABA SHIO-YAKI",
        "SABA SHIO-YAKI",
        "SALMON TERIYAKI",
        "TERIYAKI SABA",
        "SPICY SALMON TERIYAKI",
        "SABA NAMBAN",
        "SALMON DON",
        "WAGYU BEEF UDON",
        "CHASHU RAMEN",
    ],
    "Chinese": [
        "Hotpot",
        "BBQ",
        "Fried Rice",
        "Pan-fried Dumplings",
        "Steamed Dumplings",
        "Kung Pao Chicken",
        "Mapo Tofu",
        "Deep fried Chicken with Chili Peppers",
        "Clay Pot Braised Chicken Feet",
        "Deep Fry Spicy Clams",
        "Fried Prawns with Cucumber",
        "Kung Pao Prawns",
        "Spicy Seafood with Pork Blood",
        "Pork Feet in Pickle Chilli Sauce",
        "Pork Feet in Fresh Chilli Sauce",
        "Roasted Lamb Ribs",
        "Cumin flavored Lamb Ribs",
        "Cumin flavored Lamb Cubes",
        "Spicy Crispy Chicken Cartilage",
        "Nanjing Style Salty Duck",
        "Duck Giblet Liver Blood Jelly Soup with Noodle",
        "Pork Spare Ribs with Veggie mixed Rice",
        "Duck Giblet Liver Blood Jelly Soup with Rice",
        "Boiled Chicken with Veggie mixed Rice",
        "Spicy Tender Chicken with Veggie mixed Rice",
        "Shredded Pork With Pickled Vegetable Rice",
        "Spicy Duck Blood With Veggie Mixed Rice",
        "Sour and Spicy Beef noodle soup",
        "Braised Beef Brisket Noodle Soup",
        "Pork Tripe Chicken Mushroom Noodle soup",
        "Cubic Veges Noodles Soup",
        "Gravy Noodle Soup",
        "Spicy Crawfish Noodles",
        "Oil-Splashed Noodles",
        "Stir Fried Shredded Pancake",
        "Spicy Pork Tripe Noodles",
        "Snakehead Fish Noodles in Pickled Chili Sauce",
        "Shredded Chicken Cold Noodles",
        "BEEF FILLET IN SPICY SAUCE",
        "BLACK TRUFFLE SAUCE FRIED RICE WITH ABALONE",
        "BLACK TRUFFLE WITH TARO",
        "CRAB MEAT WITH MIX SEAFOOD SOUP",
        "CRISPY EGGPLANT WITH SWEET SOUR SAUCE AND CHILLI",
        "CRISPY MILK ROLL WITH CHICKEN SOFT BONES",
        "DICED CHICKEN MARYLAND FILLETS IN AROMATIC SAUCE WITH MUSHROOM",
        "DICED WAGYU BEEF IN SPECIAL JAPANESE SAUCE",
        "DUCK WITH FIVE SPICES SAUCE",
        "GREEN CHILLI SOUR SOUP WITH SLICED BEEF",
        "FUJIAN BRAISED PORK BELLY WITH DRY PRAWN & DRY SQUID & MUSHROOMS",
        "HANDMADE TOFU WITH FIN & SEA CUCUMBER SAUCE",
        "KUNG PO DICED CHICKEN THIGH",
        "MINI CUTTLE FISH IN XO SPICY SAUCE",
        "MUSSELS & GARLIC PRAWN WITH STIR FRIED RICE IN SQUID INK SAUCE",
        "OXTAIL IN SPECIAL SAUCE",
        "SINGAPORE STYLE BARRAMUNDI",
    ],
    "Korean": [
        "Bibimbap",
        "Tteokbokki",
        "Korean BBQ",
        "Kimchi Fried Rice",
        "Army Stew",
        "Cold Noodles",
        "Kimbap",
        "Haemul Pa Jeon",
        "Jap Chae",
        "Kimchi Jjigae",
        "Suntofu-jjigae",
        "RAW BEEF Yukhoe Bibimbap",
        "Chadol Doenjang-jjigae",
        "Bornga Naengmyeo",
    ],
    "Thai": [
        "Pad Thai",
        "Thai Curry",
        "Tom Yum Soup",
        "Pad Kra Pao",
        "Mango Sticky Rice",
        "Holy Basil with prawns and rice",
        "Spicy salty stir fried prawns with rice",
        "Chili Basil with cuttlefish and rice",
        "Chili Basil with squid roe and rice",
    ],
    "Vietnamese": [
        "Pho",
        "Vietnamese Pho",
        "Spring Rolls",
        "Banh Mi",
        "Lemongrass Chicken",
        "Grilled Pork Chop",
        "Seafood Laksa",
        "Beef Laksa",
    ],
    "Indian": [
        "Indian Curry",
        "Butter Chicken",
        "Naan with Curry",
        "Biryani",
        "Paneer Masala",
        "Lamb Keema Samosa",
        "Malai Chicken Tikka",
        "Momos (Dumplings)",
        "Chilli Chicken or Paneer",
        "Amritsari Fish Pakora",
        "Pepper Fry Chicken or Paneer",
        "Bhel Puri",
        "Tandoori Soya Chaap",
        "Onion Bhaji",
    ],
    "Malaysian": [
        "Hainanese Chicken Rice",
        "Laksa",
        "Nasi Lemak",
        "Char Kway Teow",
        "Signature Salted Egg Yolk King Prawn",
        "Singapore Chili King Prawn",
        "Cereal Butter King Prawn",
        "Cereal Butter Calamari",
        "Salt & Pepper Calamari",
        "Malaysian Sambal Calamari",
        "Curry Chicken Roti Canai",
        "Roti Telur Curry Sauce",
        "Basil Crispy Spicy Chicken",
        "Sizzling Mongolian Beef/Chicken",
        "Three Cup Chicken",
        "Sizzling Black Pepper Tofu",
        "Marmite Pork Ribs",
    ],
    "Spanish": ["Paella", "Tapas", "Spanish Omelette", "Churros"],
    "Mexican": ["Taco", "Mexican Platter", "Burrito", "Quesadilla", "Nachos"],
    "Western / Fastfood": [
        "Pasta",
        "Pizza",
        "KFC",
        "McDonald's",
        "Hungry Jack's",
        "Burger",
        "Fish and Chips",
        "Caesar Salad",
    ],
}

# fallback drinks
GENERIC_DRINKS = [
    "Heytea",
    "Molly Tea",
    "CoCo Milk Tea",
    "MachiMachi",
    "Cotti",
    "Gongcha",
    "Sharetea",
    "Boost",
    "Starbucks",
]

# drinks by cuisine (used first)
DRINK_DB = {
    "Japanese": ["Matcha Latte", "Iced Green Tea", "MachiMachi"],
    "Chinese": ["Heytea", "CoCo Milk Tea", "Oolong Milk Tea"],
    "Korean": ["Iced Americano", "Milk Tea", "Sparkling Water"],
    "Thai": ["Thai Milk Tea", "Lemongrass Tea"],
    "Vietnamese": ["Vietnamese Iced Coffee", "CoCo Milk Tea"],
    "Indian": ["Masala Chai", "Mango Lassi"],
    "Malaysian": ["Teh Tarik", "Iced Milk Tea"],
    "Spanish": ["Sparkling Water", "Latte"],
    "Mexican": ["Horchata", "Lime Soda"],
    "Western / Fastfood": ["Coke", "Lemonade", "Iced Tea"],
}

# your emojis – do NOT change ✅
REACTIONS = [
    "😋", "😄", "Wow 🩷", "🤤", "🤔", "😗", "💕", "😘", "😍", "🥲",
    "😌", "😛", "🤩", "🙂‍↔️", "😕", "😞", "🥵", "😨", "🫡", "🙄",
    "😶", "😲", "🤮", "💩", "🤡", "👍", "👎", "🥴", "😱"
]


# --------------------------------------------------
# 2. FILE HELPERS
# --------------------------------------------------
def init_history() -> None:
    """Create history.csv with header if it does not exist."""
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "cuisine", "main", "drink"])


def save_history(cuisine: str, main: str, drink: str) -> None:
    """Append a new combo record to history.csv."""
    init_history()
    today = time.strftime("%Y-%m-%d")
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([today, cuisine, main, drink])


def get_last_combo():
    """Return the last (main, drink) from history or (None, None)."""
    if not os.path.exists(HISTORY_FILE):
        return None, None
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
        if len(rows) > 1:
            last = rows[-1]
            return last[2], last[3]
    return None, None


# --------------------------------------------------
# 3. REACTION HELPER
# --------------------------------------------------
def get_random_reaction() -> str:
    """
    Return 1-3 random emojis from REACTIONS.
    This makes it look more like a 'random evaluation' of the food.
    """
    # how many emojis to show this time?
    count = random.randint(1, 3)
    # random.sample avoids duplicates when count > 1
    chosen = random.sample(REACTIONS, k=count)
    return " ".join(chosen)


# --------------------------------------------------
# 4. CORE LOGIC
# --------------------------------------------------
def suggest_combo(cuisine: str) -> str:
    """Suggest a combo (main + drink) for the given cuisine."""
    foods = FOOD_DB.get(cuisine, [])
    if not foods:
        return f"No foods found for cuisine: {cuisine}"

    last_main, _ = get_last_combo()
    main = random.choice(foods)
    if last_main in foods and len(foods) > 1:
        for _ in range(10):
            if main != last_main:
                break
            main = random.choice(foods)

    drinks = DRINK_DB.get(cuisine, GENERIC_DRINKS)
    drink = random.choice(drinks)
    save_history(cuisine, main, drink)

    today = time.strftime("%A, %B %d, %Y")
    return (
        f"🍽️ {today}\n"
        f"Cuisine: {cuisine}\n"
        f"Main: {main}\n"
        f"Drink: {drink}\n\n"
        f"{get_random_reaction()}"
    )


# --------------------------------------------------
# 5. GUI
# --------------------------------------------------
def run_gui() -> None:
    """Run the Tkinter GUI version."""
    root = tk.Tk()
    root.title("What To Eat Today+ (Combo)")
    root.geometry("480x360")
    root.config(bg="#FFF8DC")

    tk.Label(
        root,
        text="🍱 What To Eat Today+ (Combo Version)",
        font=("Helvetica", 14, "bold"),
        bg="#FFF8DC",
        fg="black"
    ).pack(pady=12)

    tk.Label(root, text="Choose a cuisine:", bg="#FFF8DC", fg="black").pack()

    cuisine_var = tk.StringVar(value=list(FOOD_DB.keys())[0])
    tk.OptionMenu(root, cuisine_var, *FOOD_DB.keys()).pack(pady=5)

    def on_suggest():
        cuisine = cuisine_var.get()
        msg = suggest_combo(cuisine)
        messagebox.showinfo("Your Meal Combo", msg)

    tk.Button(
        root,
        text="🎲 Suggest Combo",
        bg="#FFDEAD",
        font=("Helvetica", 12),
        fg="black",
        command=on_suggest,
        activebackground="#FFEFD5",
        activeforeground="black"
    ).pack(pady=15)

    tk.Label(
        root,
        text="Combos are saved to history.csv automatically.",
        bg="#FFF8DC",
        fg="black"
    ).pack(side="bottom", pady=10)

    root.mainloop()


# --------------------------------------------------
# 6. CLI
# --------------------------------------------------
def run_cli() -> None:
    """Run the CLI version in the terminal."""
    print("What To Eat Today+ (Combo Version)")
    print("Available cuisines:")
    for c in FOOD_DB.keys():
        print(" -", c)

    choice = input("Type a cuisine exactly as shown above: ").strip()
    if choice not in FOOD_DB:
        print("Cuisine not found. Please run again and choose from the list.")
        return

    print()
    print(suggest_combo(choice))


# --------------------------------------------------
# 7. ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    print("Choose mode:")
    print("1. GUI")
    print("2. CLI")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":
        run_gui()
    else:
        run_cli()
