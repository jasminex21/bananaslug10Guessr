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
                      "Y.S.K.W.": ["YSKW"], 
                      "TERMS & CONDITIONS": ["TERMS AND CONDITIONS"], 
                      "</c0de>": ["code", "c0de"], 
                      "Glitter Times (1997 demo)": ["Glitter Times"], 
                      "CALL ME BEEP ME - DEMO": ["CALL ME BEEP ME"], 
                      "ALL CAPS (feat. John the Ghost)": ["ALL CAPS"], 
                      "Like We Did (Windows Down)": ["Like We Did"], 
                      "oops!": ["oops"], 
                      "Isis (feat. Logic)": ["Isis"], 
                      "Finally (feat. Chris Brown)": ["Finally"], 
                      "Dusk Till Dawn (feat. Sia) - Radio Edit": ["Dusk Till Dawn"], 
                      "Bags - Recorded At Electric Lady Studios": ["Bags"], 
                      "C’est La Vie": ["Cest La Vie"]}

set_global_vars(lyrics_path="./CURRENT_FAVORITES_LYRICS.csv", 
                leaderboard_path="current_favorites_leaderboard.db",
                # theme_css=theme_css,
                acceptable_answers=acceptable_answers)

config_game(game_title="favoritesGuessr")
init_session_states()

ui(game_title="favoritesGuessr",
   instructions=[],
   guess_placeholder="e.g. Like a Villain or Medicate Me")