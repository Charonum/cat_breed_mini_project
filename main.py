import json

from bokeh.models import Button, CustomJS
from petpy import Petfinder
from streamlit_bokeh_events import streamlit_bokeh_events

from scraper import find


class Cat:
    def __init__(self, name, coat, activity, grooming, friendliness, independence, health, hypoallergenic, image,
                 intro, adopt_id):
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
        self.adopt_id = adopt_id


cat_list = [Cat("Abyssinian", "shorthair", "high", "low", "moderate", "moderate", "low", "yes", "abyssinian.jpg",
                "Very active, and friendly to people and animals. They are affectionate and social cats.",
                "real%3D967"),
            Cat("American Bobtail", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no",
                "american_bobtail.jpg",
                "Unique for their natural bobbed tail, American Bobtail is athletic and playful. They are affectionate and need lots of attention.",
                "real%3D1119"),
            Cat("American Curl", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no",
                "american_curl.jpg",
                "They have uniquely curled-back ears. Muscled and slender in build. They're generally very healthy breed.",
                "real%3D1120"),
            Cat("American Wirehair", "shorthair", "moderate", "low", "moderate", "moderate", "moderate", "no",
                "american_wirehair.jpg",
                "American Wirehairs have dense, coarse coat. They enjoy attention and are affectionate, loyal, and agile cats.",
                "real%3D968"),
            Cat("American Shorthair", "shorthair", "low", "low", "high", "high", "high", "no", "american_shorthair.jpg",
                "Well-balanced, strongly built cat. They are calm and make a good family companion.", "real%3D1122"),
            Cat("Balinese", "longhair", "high", "low", "moderate", "low", "low", "yes", "balinese.jpg",
                "Known for their svelte build, the Balinese is curious and outgoing cats. They are vocal and need lots of attention",
                "real%3D969"),
            Cat("Bengal", "shorthair", "high", "low", "low", "low", "moderate", "yes", "bengal.jpg",
                "Bengals have a wildcat-like look, but they are people-oriented and loyal. They are athletic and agile, and learn very quickly.",
                "real%3D970"),
            Cat("Birman", "longhair", "low", "high", "high", "low", "moderate", "no", "birman.jpg",
                "Birman is a colorpointed cat with four pure white feet. They are affectionate, gentle, and intelligent",
                "real%3D971"),
            Cat("Bombay", "shorthair", "moderate", "low", "high", "low", "moderate", "no", "bombay.jpg",
                "Bombays are playful, agreeable, and demand a lot of attention. They are attached to their owners and like to follow them.",
                "real%3D972"),
            Cat("British Shorthair", "shorthair", "low", "low", "high", "high", "moderate", "no",
                "british_shorthair.jpg",
                "They are affectionate but not clingy, playful but not overactive. They are generally quiet and undemanding.",
                "real%3D973"),
            Cat("Burmese", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "burmese.jpg",
                "They are very playful and intelligent cats. They have a unique rasp to their voices, so they may sound husky compared to other cats.",
                "real%3D974"),
            Cat("Burmilla", "shorthair and longhair", "moderate", "low", "high", "high", "moderate", "no",
                "burmilla.jpg",
                "They are very people-oriented cats. They are intelligent, affectionate, and not too vocal.", None),
            Cat("Chartreux", "shorthair", "moderate", "low", "high", "moderate", "high", "no", "chartreux.jpg",
                "Loving, amiable, and adapatable. They are generally quiet and very intelligent.", "real%3D1123"),
            Cat("Colorpoint Shorthair", "shorthair", "high", "low", "high", "low", "low", "yes",
                "colorpoint_shorthair.jpg",
                "They are very outgoing, affectionate, playful, and people-friendly cats. However, they are also sensitive and very vocal. They demand a lot of attention.",
                "real%3D1124"),
            Cat("Cornish Rex", "shorthair", "high", "low", "low", "low", "low", "yes", "cornish_rex.jpg",
                "They are extremely playful, so they are good for people who are into very active cats. They are social and agile cats",
                "real%3D1125"),
            Cat("Devon Rex", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "devon_rex.jpg",
                "They shed less than many other breeds, and they are affectionate, playful, and curious cats.",
                "real%3D1126"),
            Cat("Egyptian Mau", "shorthair", "high", "low", "moderate", "moderate", "moderate", "no",
                "egyptian_mau.jpg",
                "They are quiet and loyal cats. They like to hunt and provide small gifts to their human companions, and they want a lot of praise and pettings.",
                "real%3D1130"),
            Cat("Exotic", "shorthair and longhair", "low", "low", "high", "low", "low", "no", "exotic.jpg",
                "Laid-back, affectionate, and loyal. They're also playful and enjoy cuddles.", "real%3D1132"),
            Cat("Havana Brown", "shorthair", "moderate", "low", "moderate", "low", "moderate", "no", "havana_brown.jpg",
                "One of the rare cat breeds, Havana Brown is very adaptable and agreeable cats. They love to fetch and demand a lot of attention.",
                "real%3D1133"),
            Cat("Japanese Bobtail", "shorthair and longhair", "high", "low", "high", "low", "moderate", "no",
                "japanese_bobtail.jpg",
                "Japanese Bobtails are bold, intelligent, and energetic. They are also adaptable and highly intelligent.",
                "real%3D1134"),
            Cat("Khao Manee", "shorthair", "high", "low", "high", "low", "moderate", "no", "khao_manee.png",
                "They are devoted to their owners and they are curious and intelligent cats. They may have odd-eyes (one of them blue, the other gold).",
                None),
            Cat("Korat", "shorthair", "high", "low", "moderate", "low", "low", "no", "korat.png",
                "Korats like to fetch and they are playful and affectionate. They need a lot of affection from their owners.",
                "real%3D1136"),
            Cat("LaPerm", "shorthair and longhair", "high", "low", "high", "moderate", "high", "no", "laperm.jpg",
                "Known for their curly coats, LaPerms are gentle and people-oriented cats. They are active, agile, and quiet.",
                "real%3D1137"),
            Cat("Lykoi", "shorthair", "high", "low", "high", "high", "moderate", "no", "lykoi.jpg",
                "Lykoi cats are easygoing, affectionate, and playful. They are unique for their half-hairless appearance.",
                None),
            Cat("Maine Coon", "longhair", "moderate", "high", "high", "high", "high", "no", "maine_coon.jpg",
                "Maine Coons are very large cats, weighing up to 8 kg. They are intelligent, loyal, and playful.",
                "real%3D977"),
            Cat("Manx", "shorthair and longhair", "moderate", "moderate", "high", "moderate", "low", "no", "manx.jpg",
                "They have round build, with short front legs and short back. They are loyal, gentle, and are great jumpers.",
                "real%3D1138"),
            Cat("Norwegian Forest Cat", "longhair", "high", "moderate", "high", "moderate", "high", "no",
                "norwegian_forest_cat.jpg",
                "They are slowly maturing breed, and large in size. They are athletic, playful, friendly, and family-oriented.",
                "real%3D979"),
            Cat("Ocicat", "shorthair", "high", "low", "high", "low", "moderate", "yes", "ocicat.jpg",
                "Noted for their wild appearance, they are adaptable, playful, vocal, and social cats. They need a lot of space and toys because they are very active.",
                "real%3D980"),
            Cat("Oriental", "shorthair and longhair", "high", "low", "moderate", "low", "low", "yes", "oriental.jpg",
                "They are very curious and active, so they require a lot of attention. They are social and loyal cats.",
                "real%3D1140"),
            Cat("Persian", "longhair", "low", "high", "high", "low", "low", "no", "persian.jpeg",
                "Well known for sweet expressions and round appearance, Persians are calm, not as active. They require daily grooming.",
                "real%3D981"),
            Cat("RagaMuffin", "longhair", "low", "high", "high", "low", "moderate", "no", "ragamuffin.jpg",
                "RagaMuffins are people-oriented, affectionate, and not very vocal cats. They are also generally very healthy and adaptable.",
                "real%3D1141"),
            Cat("Ragdoll", "longhair", "low", "high", "high", "low", "moderate", "no", "ragdoll.jpg",
                "Docile and mild-mannered, Ragdolls are excellent indoor companions. They are laid-back, affectionate, and gentle.",
                "real%3D982"),
            Cat("Russian blue", "shorthair", "moderate", "low", "moderate", "high", "high", "yes", "russian_blue.jpg",
                "Quiet, gentle, and low-maintenance cats. Russian blues are generally well-behaved and good at entertaining themselves.",
                "real%3D983"),
            Cat("Scottish Fold", "shorthair and longhair", "low", "moderate", "moderate", "high", "low", "no",
                "scottish_fold.jpg",
                "Scottish Folds have folded ears and very round build, due to mutation. They are soft-spoken and adaptable. Some, however, develop ear infections and deafness.",
                None),
            Cat("Selkirk Rex", "shorthair and longhair", "low", "high", "high", "moderate", "high", "no",
                "selkirk_rex.jpg",
                "Selkirks are very friendly, playful, and loyal. They are known for their curly hair.", "real%3D1143"),
            Cat("Siamese", "shorthair", "high", "low", "low", "low", "low", "yes", "siamese.jpg",
                "With svelte build, Siamese are intelligent and playful, but very vocal. They crave social interaction and need a lot of daily activities.",
                "real%3D984"),
            Cat("Siberian", "longhair", "moderate", "low", "high", "moderate", "high", "yes", "siberian.png",
                "Unlike most cats, Siberians like to play in water. They are affectionate, playful, extremely agile, and generally very healthy.",
                "real%3D1151"),
            Cat("Singapura", "shorthair", "high", "low", "moderate", "moderate", "low", "no", "singapura.jpg",
                "One of the smaller cat breeds, Singapuras are active, curious, quiet, and highly intelligent. They like to be the center of attention.",
                "real%3D1145"),
            Cat("Somali", "longhair", "high", "moderate", "low", "moderate", "low", "no", "somali.jpg",
                "Somalis are very active and intelligent, but also quite michievous. They are friendly with people but are not lap cats.",
                "real%3D1146"),
            Cat("Sphynx", "shorthair", "high", "high", "high", "low", "moderate", "yes", "sphynx.jpg",
                "Noted for their hairlessness, Sphynxes are very loyal and demand lots of attention. They need frequent bathing and are high maintenance.",
                "real%3D1147"),
            Cat("Tonkinese", "shorthair", "high", "low", "high", "low", "moderate", "no", "tonkinese.jpg",
                "Tonkinese demand a lot of attention, but they are affectionate and adaptable. They do well with pets that have similar activity level as them.",
                "real%3D1148"),
            Cat("Toybob", "shorthair and longhair", "moderate", "low", "high", "moderate", "high", "no", "toybob.jpg",
                "One of the smallest cat breeds, Toybobs are social, active, and playful. They are agile climbers and good lap cats.",
                None),
            Cat("Turkish Angora", "longhair", "high", "moderate", "moderate", "low", "moderate", "no",
                "turkish_angora.jpg",
                "Turkish Angoras are good-natured, determined, and playful. They are good at swimming and they like to be in control of their surroundings.",
                "real%3D1149"),
            Cat("Turkish Van", "longhair", "high", "moderate", "high", "moderate", "high", "no", "turkish_van.jpg",
                "Turkish Vans are talkative and demand a lot of attention. They're energetic, agile, and very healthy.",
                "real%3D986")]  # cat_list stores all the cat breeds

# dictionaries of the user's answer to each question. The user's answer matches with the cat's characteristics so that the user can receive the correct result.
hairtypes = {"Yes": ["shorthair", "shorthair and longhair"], "No": ["longhair", "shorthair and longhair"],
             "Doesn't Matter": ["shorthair", "longhair", "shorthair and longhair"]}
activitytypes = {"Yes": ["high", "moderate"], "No": ["low", "moderate"], "Doesn't Matter": ["high", "moderate", "low"]}
groomingtypes = {"Yes": ["low", "moderate"], "No": ["low", "moderate", "high"]}
friendlytypes = {"Yes": ["high", "moderate"], "No": ["low", "moderate"], "Doesn't Matter": ["high", "moderate", "low"]}
independencetypes = {"Yes": ["high", "moderate"], "No": ["low", "moderate"],
                     "Doesn't Matter": ["high", "moderate", "low"]}
healthtypes = {"Yes": ["high", "moderate"], "No": ["high", "moderate", "low"]}
allergytypes = {"Yes": ["yes"], "No": ["yes", "no"]}

import streamlit as st

st.title("Welcome to CatFinder!")
st.markdown("Answer only 7 questions, and find out all kinds of lovely cats that will be perfect for you!")
st.markdown("When you are done, click 'Submit' button below.")

st.write("1) Would you like your cat to be shorthair?")
e1 = st.radio("e1", ('Yes', 'No', "Doesn't Matter"), label_visibility="hidden")
st.write("2) Do you want the cat to be active (high-energy, playful)?")
e2 = st.radio("e2", ('Yes', 'No', "Doesn't Matter"), label_visibility="hidden")
st.write("3) Would you mind if the cat requires a lot of grooming?")
e3 = st.radio("e3", ('Yes', 'No', "Doesn't Matter"), label_visibility="hidden")
st.write(
    "4) Do you want your cat to be friendly to strangers, instead of being specially affectionate towards their owners?")
e4 = st.radio("e4", ('Yes', 'No', "Doesn't Matter"), label_visibility="hidden")
st.write("5) Would you like your cat to be independent (likes to be alone)?")
e5 = st.radio("e5", ('Yes', 'No', "Doesn't Matter"), label_visibility="hidden")
st.write("7) Are you allergic to cats?")
e7 = st.radio("e7", ('Yes', 'No'), label_visibility="hidden")

result = []  # stores all cat breeds that fit with what the user wants for their cat's qualities

search = st.button('Search Breeds')
if not st.session_state.get('button'):
    st.session_state['button'] = search

if st.session_state['button']:
    e1_value = e1.strip()
    e2_value = e2.strip()
    e3_value = e3.strip()
    e4_value = e4.strip()
    e5_value = e5.strip()
    e7_value = e7.strip()

    for cat in cat_list:
        coat = cat.coat in hairtypes[e1_value]
        activity = cat.activity in activitytypes[e2_value]
        grooming = cat.grooming in groomingtypes[e3_value]
        friendliness = cat.friendliness in friendlytypes[e4_value]
        independence = cat.independence in independencetypes[e5_value]
        hypoallergenic = cat.hypoallergenic in allergytypes[e7_value]
        satisfy = coat and activity and grooming and friendliness and independence and hypoallergenic
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
            cfa = cat.name.replace(" ", "-")
            cfa = "https://cfa.org/" + cfa
            st.markdown(
                f'<a href="https://en.wikipedia.org/wiki/{wiki_name}" target="_blank" rel="noopener noreferrer"><img src="https://logos-world.net/wp-content/uploads/2020/09/Wikipedia-Emblem.png" alt="Foo" width="120"></a>',
                unsafe_allow_html=True)
            st.markdown(
                f'<a href="{cfa}" target="_blank" rel="noopener noreferrer"><img src="https://cfa.org/wp-content/uploads/elementor/thumbs/CFA-Stacked-Logo-Tag_RGB-pw2rsxqcvgiq1hkawgyqkzxqld5u52met6br1ioto8.png" alt="Foo" width="120"></a>',
                unsafe_allow_html=True)
            adoptid = cat.adopt_id
            adopt = st.button(cat.name + " cats for adoption at PetSmart!")
            if adopt:
                data = find(
                    f"https://petsmartcharities.org/adopt-a-pet/find-a-pet?city_or_zip=92024&species=cat&cats_or_dogs=cat&other_pets=_none&age=young&breed_id={adoptid}&color_id=&geo_range=50&hair=&sex=&form_build_id=form-DyX1RJLS72qoLdOEMGFVOZZX4V3q9WUNjML--XZFM6c&form_id=adopt_a_pet_search_form")
                parsed_data = json.loads(data)
                n_rows = 1 + len(parsed_data) // int(4)
                rows = [st.container() for _ in range(n_rows)]
                cols_per_row = [r.columns(4) for r in rows]
                cols = [column for row in cols_per_row for column in row]
                count = []
                for cat in parsed_data:
                    if "ERROR" in cat:
                        st.subheader("Uh-Oh! There are no furry friends of your liking nearby.")
                        break
                    else:
                        number = cat["number"]
                        image_src = cat["image_src"]
                        name = cat["name"]
                        location = cat["location"]
                        url = cat["URL"]
                        if number not in count:
                            cols[number].markdown(
                                f'<a href="{url}" target="_blank" rel="noopener noreferrer"><img src="{image_src}" alt="0" style="max-width: 100%;"></a>',
                                unsafe_allow_html=True)
                            cols[number].header(f"Hi, I'm {name}")
                            cols[number].write(location)
                            count.append(number)

