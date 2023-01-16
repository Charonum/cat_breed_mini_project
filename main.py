import json
from PIL import Image
import streamlit as st

# Open the JSON file and read the data
with open("cat_data.json", "r") as file:
    data = json.load(file)

# Create options for the size filter
size = st.sidebar.selectbox("Size", ["All", "Small", "Medium", "Large"])
# Create options for the coat size filter
coat_size = st.sidebar.selectbox("Coat Size", ["All", "Short", "Medium", "Long"])
# Create options for the shedding filter
shedding = st.sidebar.selectbox("Shedding", ["All", "Low", "Moderate"])
# Create options for the energy filter
energy = st.sidebar.selectbox("Energy", ["All", "Low", "Moderate", "High"])

# Create a function to filter the cat breeds by the selected filters
def filter_breeds():
    cat_names = []
    for cat in data["cat_breeds"]:
        if (size == "All" or cat["size"] == size) and (coat_size == "All" or cat["coat_size"] == coat_size) and (shedding == "All" or cat["shedding"] == shedding) and (energy == "All" or cat["energy"] == energy):
            cat_names.append(cat["name"])
    return cat_names

cat_names = filter_breeds()

if cat_names:
    # Display the cat images in a gallery
    for cat_name in cat_names:
        try:
            # Open the cat photo
            image = Image.open(cat_name + ".png")
            if cat_name == "Sokoke":
                st.image(image, caption="⭐ " + cat_name, use_column_width=True)
            else:
                st.image(image, caption=cat_name, use_column_width=True)
        except:
            st.warning(f"Could not load image for {cat_name}")
else:
    st.warning("No cats match the selected filters.")
