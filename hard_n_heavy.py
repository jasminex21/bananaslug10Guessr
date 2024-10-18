import streamlit as st

from lyriguessr_personal.components import *

# theme_css = {
#     "The Worst In Me": {
#         "background_color": "#6E5A4E", 
#         "button_color": "#513E32",
#         "inputs": "#7F534B",
#         "text_color": "white"},
#     "Dethrone": {
#         "background_color": "#909BA2",
#         "button_color": "#686E75",
#         "inputs": "#dcdee0",
#         "text_color": "black"
#     },
#     "THE DEATH OF PEACE OF MIND": {
#         "background_color": "#AC4735",
#         "button_color": "#82332A",
#         "inputs": "#B58B6F",
#         "text_color": "black"
#     }}

# TODO: NOT YET ACCOUNTING FOR IDENTICAL SONG NAMES IN SONG COUNTER - NOT A PROBLEM YET

acceptable_answers = {"F E R A L": ["FERAL", "F.E.R.A.L"],
                      "Reprise (The Sound Of The End)": ["Reprise"],
                      "V.A.N": ["VAN"], 
                      "Y.S.K.W.": ["YSKW"]}

set_global_vars(lyrics_path="./HARD_AND_HEAVY_LYRICS.csv", 
                leaderboard_path="leaderboard.db",
                # theme_css=theme_css,
                acceptable_answers=acceptable_answers)

config_game(game_title="hardnHeavyGuessr")
init_session_states()

ui(game_title="hardnHeavyGuessr",
   instructions=[],
   guess_placeholder="e.g. Like a Villain or Medicate Me")