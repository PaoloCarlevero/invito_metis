import streamlit as st
import pandas as pd
import numpy as np


def get_n_rows(answers):
    return max(answers.keys())

def get_padded_word(word, colored_letter_pos, colored_col_pos, n_cols):
    l_padding = colored_col_pos-colored_letter_pos+1 
    r_padding = (n_cols-colored_col_pos)-(len(word)-colored_letter_pos)+1

    return ' '*l_padding+ word + ' '*r_padding

st.set_page_config(layout="wide")

n_cols = 28
colored_col_pos = 13

answers = {
    1: 'MUSICA',
    2: 'PYTHON',
    3: 'CAWI',
    4: 'MODELLI',
    5: 'METISRICERCHE',
    6: 'REPORT',
    7: 'SAS',
    8: 'CATI',
    9: 'ADABI',
    10: 'BONIFACIO',
    11: 'GIOLITTI',
    12: 'ANALYTICS',
    13: 'DIPENDENTI',
    14: 'DATAQUALITY',
    15: 'SURVEY',
    16: 'CURVAROC',
    17: 'SIMULAZIONE',
    18: 'ALKEMY',
    19: 'CHITARRA',
    20: 'DATAMINING',
    21: 'INTELLIGENZA',
    22: 'DATAMINING',
    23: 'RISKANALYSIS'
}

colored_letter_pos = {
    1: 3,
    2: 5,
    3: 1,
    4: 7,
    5: 13,
    6: 6,
    7: 2,
    8: 1,
    9: 1,
    10: 3,
    11: 3,
    12: 6,
    13: 9,
    14: 9,
    15: 5,
    16: 3,
    17: 2,
    18: 1,
    19: 7,
    20: 5,
    21: 7,
    22: 1,
    23: 5
}

def get_ordinal_cols_index(colored_letter_pos, colored_col_pos):
    return colored_col_pos - colored_letter_pos

def get_grid_row(answer, colored_letter_pos, colored_col_pos, n_cols, visible = False):
    padded_answer = get_padded_word(answer, colored_letter_pos, colored_col_pos, n_cols)

    if visible:
        row = [' ' if letter == ' ' else letter.lower()  for letter in padded_answer]
        row[colored_col_pos] = row[colored_col_pos].upper()
        
    else:
        row = [' ' if letter == ' ' else '_' for letter in padded_answer]
        row[colored_col_pos] = '?'

    return row


def get_empty_grid(answers, colored_letter_pos, n_cols, colored_col_pos):
    
    grid = []
    n_rows = get_n_rows(answers)

    for i in range(1, n_rows+1):

        curr_answer = f'{answers[i]}'
        curr_colored_letter_pos = colored_letter_pos[i]
        ordinal_cols_index = get_ordinal_cols_index(colored_letter_pos[i], colored_col_pos)

        new_row = get_grid_row(curr_answer, curr_colored_letter_pos, colored_col_pos, n_cols, visible = False)
        new_row[ordinal_cols_index] = str(i)

        grid.append(new_row)


    grid = pd.DataFrame(grid)
    grid.index = np.arange(1, len(grid)+1)


    return grid

def style_grid(grid):

    grid = grid.style.map(lambda x: f"background-color: {'black' if str(x).isnumeric() else 'pink' if (str(x) == '?' or str(x).isupper()) else'white'}")
    grid = grid.map(lambda x: f"color: {'white' if str(x).isnumeric() else 'black'}")

    return grid


# -------------------
# Session states
# -------------------
if 'grid' not in st.session_state:
    empty_grid = get_empty_grid(answers, colored_letter_pos, n_cols, colored_col_pos)
    st.session_state['grid'] = style_grid(empty_grid)

    for i in range(1, get_n_rows(answers)+1):
        st.session_state[f'risposta_{i}'] = None

else:

    empty_grid = get_empty_grid(answers, colored_letter_pos, n_cols, colored_col_pos)

    for i in range(1, get_n_rows(answers)+1):
        if st.session_state[f'risposta_{i}'] == answers[i]:

            empty_grid.loc[i] = get_grid_row(answers[i], colored_letter_pos[i], colored_col_pos, n_cols, visible = True)

    st.session_state['grid'] = style_grid(empty_grid)


st.table(st.session_state.grid)

st.text("Domanda 1")
st.text_input("Testo domanda 1", key='risposta_1')

st.text("Domanda 2")
risposta_2 = st.text_input("Testo domanda 2", key='risposta_2')
st.text("Domanda 3")
risposta_3 = st.text_input("Testo domanda 3", key='risposta_3')
st.text("Domanda 4")
risposta_4 = st.text_input("Testo domanda 4", key='risposta_4')
st.text("Domanda 5")
risposta_5 = st.text_input("Testo domanda 5", key='risposta_5')
st.text("Domanda 6")
risposta_6 = st.text_input("Testo domanda 6", key='risposta_6')
st.text("Domanda 7")
risposta_7 = st.text_input("Testo domanda 7", key='risposta_7')
st.text("Domanda 8")
risposta_8 = st.text_input("Testo domanda 8", key='risposta_8')
st.text("Domanda 9")
risposta_9 = st.text_input("Testo domanda 9", key='risposta_9')
st.text("Domanda 10")
risposta_10 = st.text_input("Testo domanda 10", key='risposta_10')
st.text("Domanda 11")
risposta_11= st.text_input("Testo domanda 11", key='risposta_11')
st.text("Domanda 12")
risposta_12 = st.text_input("Testo domanda 12", key='risposta_12')
st.text("Domanda 13")
risposta_13= st.text_input("Testo domanda 13", key='risposta_13')
st.text("Domanda 14")
risposta_14 = st.text_input("Testo domanda 14", key='risposta_14')
st.text("Domanda 15")
risposta_15 = st.text_input("Testo domanda 15", key='risposta_15')
st.text("Domanda 16")
risposta_16 = st.text_input("Testo domanda 16", key='risposta_16')
st.text("Domanda 17")
risposta_17 = st.text_input("Testo domanda 17", key='risposta_17')
st.text("Domanda 18")
risposta_18 = st.text_input("Testo domanda 18", key='risposta_18')
st.text("Domanda 19")
risposta_19 = st.text_input("Testo domanda 19", key='risposta_19')
st.text("Domanda 20")
risposta_20 = st.text_input("Testo domanda 20", key='risposta_20')
st.text("Domanda 21")
risposta_21 = st.text_input("Testo domanda 21", key='risposta_21')
st.text("Domanda 22")
risposta_22 = st.text_input("Testo domanda 22", key='risposta_22')
st.text("Domanda 23")
risposta_23 = st.text_input("Testo domanda 23", key='risposta_23')