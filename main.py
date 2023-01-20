class Cat:
    def __init__(self, name, coat, activity, grooming, friendliness, independence, health, hypoallergenic, image,
                 intro):
        self.name = name
        self.coat = coat
        self.activity = activity
        self.grooming = grooming
        self.friendliness = friendliness
        self.independence = independence
        self.health = health
        self.hypoallergenic = hypoallergenic
        self.image = "images/" + image
        self.intro = intro


cat_list = []  # cat_list stores all the cat breeds
cat_list.append(Cat("Abyssinian", "shorthair", "high", "low", "moderate", "moderate", "low", "yes", "abyssinian.jpg",
                    "Very active, and friendly to people and animals. They are affectionate and social cats."))
cat_list.append(Cat("American Bobtail", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no",
                    "american_bobtail.jpg",
                    "Unique for their natural bobbed tail, American Bobtail is athletic and playful. They are affectionate and need lots of attention."))
cat_list.append(Cat("American Curl", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no",
                    "american_curl.jpg",
                    "They have uniquely curled-back ears. Muscled and slender in build. They're generally very healthy breed."))
cat_list.append(Cat("American Wirehair", "shorthair", "moderate", "low", "moderate", "moderate", "moderate", "no",
                    "american_wirehair.jpg",
                    "American Wirehairs have dense, coarse coat. They enjoy attention and are affectionate, loyal, and agile cats."))
cat_list.append(
    Cat("American Shorthair", "shorthair", "low", "low", "high", "high", "high", "no", "american_shorthair.jpg",
        "Well-balanced, strongly built cat. They are calm and make a good family companion."))
cat_list.append(Cat("Balinese", "longhair", "high", "low", "moderate", "low", "low", "yes", "balinese.jpg",
                    "Known for their svelte build, the Balinese is curious and outgoing cats. They are vocal and need lots of attention"))
cat_list.append(Cat("Bengal", "shorthair", "high", "low", "low", "low", "moderate", "yes", "bengal.jpg",
                    "Bengals have a wildcat-like look, but they are people-oriented and loyal. They are athletic and agile, and learn very quickly."))
cat_list.append(Cat("Birman", "longhair", "low", "high", "high", "low", "moderate", "no", "birman.jpg",
                    "Birman is a colorpointed cat with four pure white feet. They are affectionate, gentle, and intelligent"))
cat_list.append(Cat("Bombay", "shorthair", "moderate", "low", "high", "low", "moderate", "no", "bombay.jpg",
                    "Bombays are playful, agreeable, and demand a lot of attention. They are attached to their owners and like to follow them."))
cat_list.append(
    Cat("British Shorthair", "shorthair", "low", "low", "high", "high", "moderate", "no", "british_shorthair.jpg",
        "They are affectionate but not clingy, playful but not overactive. They are generally quiet and undemanding."))
cat_list.append(Cat("Burmese", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "burmese.jpg",
                    "They are very playful and intelligent cats. They have a unique rasp to their voices, so they may sound husky compared to other cats."))
cat_list.append(
    Cat("Burmilla", "shorthair and longhair", "moderate", "low", "high", "high", "moderate", "no", "burmilla.jpg",
        "They are very people-oriented cats. They are intelligent, affectionate, and not too vocal."))
cat_list.append(Cat("Chartreux", "shorthair", "moderate", "low", "high", "moderate", "high", "no", "chartreux.jpg",
                    "Loving, amiable, and adapatable. They are generally quiet and very intelligent."))
cat_list.append(
    Cat("Colorpoint Shorthair", "shorthair", "high", "low", "high", "low", "low", "yes", "colorpoint_shorthair.jpg",
        "They are very outgoing, affectionate, playful, and people-friendly cats. However, they are also sensitive and very vocal. They demand a lot of attention."))
cat_list.append(Cat("Cornish Rex", "shorthair", "high", "low", "low", "low", "low", "yes", "cornish_rex.jpg",
                    "They are extremely playful, so they are good for people who are into very active cats. They are social and agile cats"))
cat_list.append(Cat("Devon Rex", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "devon_rex.jpg",
                    "They shed less than many other breeds, and they are affectionate, playful, and curious cats."))
cat_list.append(
    Cat("Egyptian Mau", "shorthair", "high", "low", "moderate", "moderate", "moderate", "no", "egyptian_mau.jpg",
        "They are quiet and loyal cats. They like to hunt and provide small gifts to their human companions, and they want a lot of praise and pettings."))
cat_list.append(Cat("Exotic", "shorthair and longhair", "low", "low", "high", "low", "low", "no", "exotic.jpg",
                    "Laid-back, affectionate, and loyal. They're also playful and enjoy cuddles."))
cat_list.append(
    Cat("Havana Brown", "shorthair", "moderate", "low", "moderate", "low", "moderate", "no", "havana_brown.jpg",
        "One of the rare cat breeds, Havana Brown is very adaptable and agreeable cats. They love to fetch and demand a lot of attention."))
cat_list.append(Cat("Japanese Bobtail", "shorthair and longhair", "high", "low", "high", "low", "moderate", "no",
                    "japanese_bobtail.jpg",
                    "Japanese Bobtails are bold, intelligent, and energetic. They are also adaptable and highly intelligent."))
cat_list.append(Cat("Khao Manee", "shorthair", "high", "low", "high", "low", "moderate", "no", "khao_manee.png",
                    "They are devoted to their owners and they are curious and intelligent cats. They may have odd-eyes (one of them blue, the other gold)."))
cat_list.append(Cat("Korat", "shorthair", "high", "low", "moderate", "low", "low", "no", "korat.png",
                    "Korats like to fetch and they are playful and affectionate. They need a lot of affection from their owners."))
cat_list.append(Cat("LaPerm", "shorthair and longhair", "high", "low", "high", "moderate", "high", "no", "laperm.jpg",
                    "Known for their curly coats, LaPerms are gentle and people-oriented cats. They are active, agile, and quiet."))
cat_list.append(Cat("Lykoi", "shorthair", "high", "low", "high", "high", "moderate", "no", "lykoi.jpg",
                    "Lykoi cats are easygoing, affectionate, and playful. They are unique for their half-hairless appearance."))
cat_list.append(Cat("Maine Coon", "longhair", "moderate", "high", "high", "high", "high", "no", "maine_coon.jpg",
                    "Maine Coons are very large cats, weighing up to 8 kg. They are intelligent, loyal, and playful."))
cat_list.append(
    Cat("Manx", "shorthair and longhair", "moderate", "moderate", "high", "moderate", "low", "no", "manx.jpg",
        "They have round build, with short front legs and short back. They are loyal, gentle, and are great jumpers."))
cat_list.append(Cat("Norwegian Forest Cat", "longhair", "high", "moderate", "high", "moderate", "high", "no",
                    "norwegian_forest_cat.jpg",
                    "They are slowly maturing breed, and large in size. They are athletic, playful, friendly, and family-oriented."))
cat_list.append(Cat("Ocicat", "shorthair", "high", "low", "high", "low", "moderate", "yes", "ocicat.jpg",
                    "Noted for their wild appearance, they are adaptable, playful, vocal, and social cats. They need a lot of space and toys because they are very active."))
cat_list.append(
    Cat("Oriental", "shorthair and longhair", "high", "low", "moderate", "low", "low", "yes", "oriental.jpg",
        "They are very curious and active, so they require a lot of attention. They are social and loyal cats."))
cat_list.append(Cat("Persian", "longhair", "low", "high", "high", "low", "low", "no", "persian.jpeg",
                    "Well known for sweet expressions and round appearance, Persians are calm, not as active. They require daily grooming."))
cat_list.append(Cat("RagaMuffin", "longhair", "low", "high", "high", "low", "moderate", "no", "ragamuffin.jpg",
                    "RagaMuffins are people-oriented, affectionate, and not very vocal cats. They are also generally very healthy and adaptable."))
cat_list.append(Cat("Ragdoll", "longhair", "low", "high", "high", "low", "moderate", "no", "ragdoll.jpg",
                    "Docile and mild-mannered, Ragdolls are excellent indoor companions. They are laid-back, affectionate, and gentle."))
cat_list.append(
    Cat("Russian blue", "shorthair", "moderate", "low", "moderate", "high", "high", "yes", "russian_blue.jpg",
        "Quiet, gentle, and low-maintenance cats. Russian blues are generally well-behaved and good at entertaining themselves."))
cat_list.append(Cat("Scottish Fold", "shorthair and longhair", "low", "moderate", "moderate", "high", "low", "no",
                    "scottish_fold.jpg",
                    "Scottish Folds have folded ears and very round build, due to mutation. They are soft-spoken and adaptable. Some, however, develop ear infections and deafness."))
cat_list.append(
    Cat("Selkirk Rex", "shorthair and longhair", "low", "high", "high", "moderate", "high", "no", "selkirk_rex.jpg",
        "Selkirks are very friendly, playful, and loyal. They are known for their curly hair."))
cat_list.append(Cat("Siamese", "shorthair", "high", "low", "low", "low", "low", "yes", "siamese.jpg",
                    "With svelte build, Siamese are intelligent and playful, but very vocal. They crave social interaction and need a lot of daily activities."))
cat_list.append(Cat("Siberian", "longhair", "moderate", "low", "high", "moderate", "high", "yes", "siberian.png",
                    "Unlike most cats, Siberians like to play in water. They are affectionate, playful, extremely agile, and generally very healthy."))
cat_list.append(Cat("Singapura", "shorthair", "high", "low", "moderate", "moderate", "low", "no", "singapura.jpg",
                    "One of the smaller cat breeds, Singapuras are active, curious, quiet, and highly intelligent. They like to be the center of attention."))
cat_list.append(Cat("Somali", "longhair", "high", "moderate", "low", "moderate", "low", "no", "somali.jpg",
                    "Somalis are very active and intelligent, but also quite michievous. They are friendly with people but are not lap cats."))
cat_list.append(Cat("Sphynx", "shorthair", "high", "high", "high", "low", "moderate", "yes", "sphynx.jpg",
                    "Noted for their hairlessness, Sphynxes are very loyal and demand lots of attention. They need frequent bathing and are high maintenance."))
cat_list.append(Cat("Tonkinese", "shorthair", "high", "low", "high", "low", "moderate", "no", "tonkinese.jpg",
                    "Tonkinese demand a lot of attention, but they are affectionate and adaptable. They do well with pets that have similar activity level as them."))
cat_list.append(
    Cat("Toybob", "shorthair and longhair", "moderate", "low", "high", "moderate", "high", "no", "toybob.jpg",
        "One of the smallest cat breeds, Toybobs are social, active, and playful. They are agile climbers and good lap cats."))
cat_list.append(
    Cat("Turkish Angora", "longhair", "high", "moderate", "moderate", "low", "moderate", "no", "turkish_angora.jpg",
        "Turkish Angoras are good-natured, determined, and playful. They are good at swimming and they like to be in control of their surroundings."))
cat_list.append(Cat("Turkish Van", "longhair", "high", "moderate", "high", "moderate", "high", "no", "turkish_van.jpg",
                    "Turkish Vans are talkative and demand a lot of attention. They're energetic, agile, and very healthy."))

# dictionaries of the user's answer to each question. The user's answer matches with the cat's characteristics so that the user can receive the correct result.
hairtypes = {"yes": ["shorthair", "shorthair and longhair"], "no": ["longhair", "shorthair and longhair"],
             "dm": ["shorthair", "longhair", "shorthair and longhair"]}
activitytypes = {"yes": ["high", "moderate"], "no": ["low", "moderate"], "dm": ["high", "moderate", "low"]}
groomingtypes = {"yes": ["low", "moderate"], "no": ["low", "moderate", "high"]}
friendlytypes = {"yes": ["high", "moderate"], "no": ["low", "moderate"], "dm": ["high", "moderate", "low"]}
independencetypes = {"yes": ["high", "moderate"], "no": ["low", "moderate"], "dm": ["high", "moderate", "low"]}
healthtypes = {"yes": ["high", "moderate"], "dm": ["high", "moderate", "low"]}
allergytypes = {"yes": ["yes"], "no": ["yes", "no"]}

import streamlit as st

st.title("Welcome to CatFinder!")
st.markdown("Answer only 7 questions, and find out all kinds of lovely cats that will be perfect for you!")
st.markdown("When you are done, click 'Submit' button below.")

st.write("1) Would you like your cat to be shorthair? Enter 'yes', 'no', or 'dm' (doesn't matter).")
e1 = st.text_input(key='e1', label="")
st.write("2) Do you want the cat to be active (high-energy, playful)? Enter 'yes', 'no', or 'dm' (doesn't matter).")
e2 = st.text_input(key='e2', label="")
st.write("3) Would you mind if the cat requires a lot of grooming? Enter 'yes' if you don't want the cat to require lots of grooming, enter 'no' otherwise.")
e3 = st.text_input(key='e3', label="")
st.write("4) Do you want your cat to be friendly to strangers, including children? Enter 'yes', 'no' or 'dm' (doesn't matter).")
e4 = st.text_input(key='e4', label="")
st.write("5) Would you like your cat to be independent (likes to be alone)? Enter 'yes', 'no', or 'dm' (doesn't matter).")
e5 = st.text_input(key='e5', label="")
st.write("6) Should the cat be very healthy (little to no genetic health problems) in general? Enter 'yes' or 'no'.")
e6 = st.text_input(key='e6', label="")
st.write("7) Are you allergic to cats? Enter 'yes' or 'no'.")
e7 = st.text_input(key='e7', label="")


result = []  # stores all cat breeds that fit with what the user wants for their cat's qualities

@st.cache
def cat_select():
    return st.selectbox("Please select a cat breed to view more information", result)

def show_cat_info(cat_breed):
    for cat in cat_list:
        if cat.name == cat_breed:
            # display more information about the selected cat breed
            st.write("Introducing: ", cat.name)
            st.write(cat.intro)
            st.beta_container()
            st.image(cat.image)
            if 'yes' in cat.health:
                st.write("This cat breed is generally very healthy.")
            else:
                st.write("This cat breed may have some genetic health issues.")
if st.button('Submit'):
    e1_value = e1.strip().lower()
    e2_value = e2.strip().lower()
    e3_value = e3.strip().lower()
    e4_value = e4.strip().lower()
    e5_value = e5.strip().lower()
    e6_value = e6.strip().lower()
    e7_value = e7.strip().lower()

    # check user input and match with cat breeds
    for cat in cat_list:
        coat = cat.coat in hairtypes[e1_value]
        activity = cat.activity in activitytypes[e2_value]
        grooming = cat.grooming in groomingtypes[e3_value]
        friendliness = cat.friendliness in friendlytypes[e4_value]
        independence = cat.independence in independencetypes[e5_value]
        health = cat.health in healthtypes[e6_value]
        hypoallergenic = cat.hypoallergenic in allergytypes[e7_value]
        satisfy = coat and activity and grooming and friendliness and independence and health and hypoallergenic
        if satisfy:
            result.append(cat)
    if len(result) == 0:
        st.write("Sorry, we couldn't find any cat breeds that match your preferences.")
    else:
        for cat in result:
            st.write("-" * len(cat.name))
            st.write(cat.name)
            st.write(cat.intro)
            st.image(cat.image)
            name = cat.name
            wiki_name = name.replace(" ", "_")
            if cat.name == "American Wirehair" or cat.name == "Burmilla" or cat.name == "Khao Manee" or cat.name == "LaPerm" or cat.name == "Lykoi" or cat.name == "Norwegian Forest Cat" or cat.name == "Ocicat" or cat.name == "Russian Blue" or cat.name == "Toybob" or cat.name == "Turkish Van":
                pass
            else:
                wiki_name = wiki_name + "_cat"
            if cat.name == "RagaMuffin":
                wiki_name = wiki_name.lower()
            st.markdown(f'<a href="https://en.wikipedia.org/wiki/{wiki_name}" target="_blank" rel="noopener noreferrer"><img src="https://logos-world.net/wp-content/uploads/2020/09/Wikipedia-Emblem.png" alt="Foo" width="120"></a>', unsafe_allow_html=True)
