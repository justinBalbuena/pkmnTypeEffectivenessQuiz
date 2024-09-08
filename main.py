import streamlit as st
import random
import functions

colors_dict = {
    "normal": '#A8A77A',
    "fire": '#EE8130',
    "water": '#6390F0',
    "electric": '#F7D02C',
    "grass": '#7AC74C',
    "ice": '#96D9D6',
    "fighting": '#C22E28',
    "poison": '#A33EA1',
    "ground": '#E2BF65',
    "flying": '#A98FF3',
    "psychic": '#F95587',
    "bug": '#A6B91A',
    "rock": '#B6A136',
    "ghost": '#735797',
    "dragon": '#6F35FC',
    "dark": '#705746',
    "steel": '#B7B7CE',
    "fairy": '#D685AD',
}

types_list = functions.get_all_types()
user_answers = []


st.set_page_config(layout="wide")
st.title("Pokemon Type Effectiveness Quiz")

st.markdown("""
                <br>
                <br>
                <br>
                <br>
            """,
            unsafe_allow_html=True)


if 'session_initialized' not in st.session_state:
    # Initialize the session state flag
    st.session_state.session_initialized = True

    # Generate and save the coinflip value
    st.session_state.coinflip = random.randint(1, 2)

    if st.session_state.coinflip == 1:
        st.session_state.dynamic_choice = functions.get_single_random_types()
    else:
        st.session_state.dynamic_choice = functions.get_double_random_types()
    st.write(f"""
                <br>
                <br>
                This is the coinflip
                {st.session_state.coinflip}
                <br>
                <br>
            """)

st.write("Dynamic Choice:", list(st.session_state.dynamic_choice))

types_to_guess = st.columns(st.session_state.coinflip)
for index, col in enumerate(types_to_guess):
    col.markdown(
        f"""
                <style>
                    .{list(st.session_state.dynamic_choice)[index]} {{
                        background-color: {colors_dict[list(st.session_state.dynamic_choice)[index]]};
                        display: flex;
                        justify-content: center;
                        align-center:center;
                    }}
                </style>
                <div class="{list(st.session_state.dynamic_choice)[index]}">
                    <h4>{list(st.session_state.dynamic_choice)[index].title()}</h4>
                </div>
            """,
        unsafe_allow_html=True
    )

st.markdown("""
                <br>
                <br>
                <br>
                <br>
            """,
            unsafe_allow_html=True)

# if 'session_initialized' not in st.session_state:
#    num = random.randint(1, 2)
#    if num == 1:
#        functions.get_dual_type_effectiveness(
#            types_list[random.randint(0, 17)], types_list[random.randint(0, 17)])
#    else:
#        functions.get_single_type_effectiveness()


num_columns = len(types_list)
columns_row1 = st.columns(9)
columns_row2 = st.columns(9)

for index, col in enumerate(columns_row1 + columns_row2):
    col.markdown(
        f"""
            <style>
                .{types_list[index]} {{
                    background-color: {colors_dict[types_list[index]]};
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
    col.text_input(label="Input:", key=f"answer{index}")

st.markdown("""
                <br>
                <br>
            """,
            unsafe_allow_html=True)

# after pressing submit, the answers will be
# collected and put into the list user_answers
if st.button("Submit"):
    try:
        for index in range(len(columns_row1) + len(columns_row2)):
            user_answers.append(float(st.session_state[f"answer{index}"]))
        st.write(user_answers)
        if st.session_state.coinflip == 1:
            for attackingType in types_list:
                functions.get_single_type_effectiveness(
                    list(st.session_state.dynamic_choice)[0],
                    attackingType
                )
            correct_answers = functions.get_answers()
            for index, col in enumerate(columns_row1 + columns_row2):
                if user_answers[index] == correct_answers[index]:
                    col.markdown(
                        f"""
                            <style>
                                .right {{
                                    background-color: green
                                }}
                            </style>
                            <h2 class="right">Correct<h2>
                            
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    col.markdown(
                        f"""
                            <style>
                                .wrong {{
                                    background-color: red
                                }}
                            </style>
                            <h2 class="wrong">Incorrect<h2>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            for attackingType in types_list:
                functions.get_dual_type_effectiveness(
                    list(st.session_state.dynamic_choice)[0],
                    list(st.session_state.dynamic_choice)[1],
                    attackingType
                )
            correct_answers = functions.get_answers()
            for index, col in enumerate(columns_row1 + columns_row2):
                if user_answers[index] == correct_answers[index]:
                    col.markdown(
                        f"""
                            <style>
                                .right {{
                                    background-color: green
                                }}
                            </style>
                            <h2 class="right">Correct<h2>

                        """,
                        unsafe_allow_html=True
                    )
                else:
                    col.markdown(
                        f"""
                            <style>
                                .wrong {{
                                    background-color: red
                                }}
                            </style>
                            <h2 class="wrong">Incorrect<h2>
                        """,
                        unsafe_allow_html=True
                    )
    except ValueError:
        st.write("Please make sure to put a valid answer into every field")
