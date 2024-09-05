import streamlit as st
import functions

colors_dict = {
    "Normal": '#A8A77A',
    "Fire": '#EE8130',
    "Water": '#6390F0',
    "Electric": '#F7D02C',
    "Grass": '#7AC74C',
    "Ice": '#96D9D6',
    "Fighting": '#C22E28',
    "Poison": '#A33EA1',
    "Ground": '#E2BF65',
    "Flying": '#A98FF3',
    "Psychic": '#F95587',
    "Bug": '#A6B91A',
    "Rock": '#B6A136',
    "Ghost": '#735797',
    "Dragon": '#6F35FC',
    "Dark": '#705746',
    "Steel": '#B7B7CE',
    "Fairy": '#D685AD',
}

st.set_page_config(layout="wide")
st.title("Pokemon Type Effectiveness Quiz")
types_list = functions.get_types()

num_columns = len(types_list)
columns_row1 = st.columns(9)
columns_row2 = st.columns(9)
for index, col in enumerate(columns_row1 + columns_row2):
    col.markdown(
        f"""
            <style>
                .{types_list[index]} {{
                    background-color: {colors_dict[types_list[index].title()]};
                    display: flex;
                    justify-content: center;
                    align-center:center;
                }}
            </style>
            <div class="{types_list[index]}">
                <h4>{types_list[index].title()}</h4>
            </div>
        """,
        unsafe_allow_html=True
    )
    col.text_input(label="Input:", key=index)

# Button to submit and display the inputs
if st.button("Submit"):
    st.write("Submit button clicked!")

print(colors_dict['Normal'])