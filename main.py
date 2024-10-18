import tkinter as tk
from tkinter import ttk

import afl_request
import nrl_request

score_info = []


def clear():
    for label in score_info:
        label.destroy()
    score_info.clear()


def most_recent_score(sport):
    clear()

    team1 = ttk.Label(window,
                      text=afl_request.common.find_home_away(sport.data)[0],
                      )
    team1.pack()
    score_info.append(team1)
    team1_score = ttk.Label(window,
                            text=sport.home_score,
                            )
    team1_score.pack()
    score_info.append(team1_score)
    team2 = ttk.Label(window,
                      text=afl_request.common.find_home_away(sport.data)[1],
                      )
    team2.pack()
    score_info.append(team2)
    team2_score = ttk.Label(window,
                            text=sport.away_score,
                            )
    team2_score.pack()
    score_info.append(team2_score)


# window
window = tk.Tk()
window.title("Sports Scores")
window.geometry("600x400")

# widgets
title = ttk.Label(window,
                  text="Sports",
                  font=("Helvetica", 20),
                  )
title.pack(anchor=tk.W, padx=10, pady=10)

NHL = ttk.Button(window,
                 text="NHL",
                 command=lambda: print("NHL button pressed")
                 )
NHL.pack(anchor=tk.W, padx=10, pady=10)

AFL = ttk.Button(window,
                 text="NFL",
                 command=lambda: print("NFL button pressed")
                 )
AFL.pack(anchor=tk.W, padx=10, pady=10)

AFL = ttk.Button(window,
                 text="AFL",
                 command=lambda: most_recent_score(afl_request),
                 )
AFL.pack(anchor=tk.W, padx=10, pady=10)

NRL = ttk.Button(window,
                 text="NRL",
                 command=lambda: most_recent_score(nrl_request),
                 )
NRL.pack(anchor=tk.W, padx=10, pady=10)


# run
window.mainloop()
