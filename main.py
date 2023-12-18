import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd

def get_image(gid):
    image_folder = ".\\photos\\" 
    return f"{image_folder}{gid}.png"

def get_player_info(player_id):
    df = pd.read_csv('SPL_player_data.csv')

    # key = str(player_id).lower()
    # player = df[df['name'] == key]

    player = df[df['ID'] == int(player_id)]

    if player.empty:
        return None
    else:
        player_info = {
            'name': player['Name'].values[0],
            'skills': player['skills'].values[0],
            'image_path': get_image(player['GID'].values[0]),
            'total_match': player['total_match'].values[0],
            'bat_innings': player['bat_innings'].values[0],
            'total_runs': player['total_runs'].values[0],
            'highest_run': player['highest_run'].values[0],
            'bat_average': player['bat_average'].values[0],
            'ball_innings': player['ball_innings'].values[0],
            'total_wickets': player['total_wickets'].values[0],
            'highest_wicket': player['highest_wicket'].values[0],
            'ball_economy': player['ball_economy'].values[0],
            'BU': player['BU'].values[0],
        }
        return player_info


def show_player_details(event=None):
    id_input = id_entry.get().strip()

    player_info = get_player_info(id_input)

    if player_info:
        player_image = Image.open(player_info['image_path'])
        player_image = player_image.resize((400, 400), Image.BILINEAR)
        img = ImageTk.PhotoImage(player_image)

        image_label.configure(image=img)
        image_label.image = img  # Keep reference to avoid garbage collection
        name_label.configure(text=f"{player_info['name']}")
        details_label.configure(text=f"{player_info['skills']}")
        bu_label.configure(text=f"{player_info['BU']}")

        heading_label.configure(text="Player Details")
        total_match_label.configure(text=f"Total Matches Played: {player_info['total_match']}")
        bat_innings_label.configure(text=f"Batting Innings: {player_info['bat_innings']}")
        total_runs_label.configure(text=f"Total Runs Scored: {player_info['total_runs']}")
        highest_run_label.configure(text=f"Highest Runs: {player_info['highest_run']}")
        bat_average_label.configure(text=f"Batting Average: {player_info['bat_average']}")
        ball_innings_label.configure(text=f"Bowling Innings: {player_info['ball_innings']}")
        total_wickets_label.configure(text=f"Total Wickers: {player_info['total_wickets']}")
        highest_wicket_label.configure(text=f"Highest Wickets: {player_info['highest_wicket']}")
        ball_economy_label.configure(text=f"Bowling Economy: {player_info['ball_economy']}")
    else:
        player_image = Image.open(".\\image\\player_icon.png")
        player_image = player_image.resize((400, 400), Image.BILINEAR)
        img = ImageTk.PhotoImage(player_image)

        image_label.configure(image=img)
        image_label.image = img

        heading_label.configure(text="Player Details")
        name_label.configure(text="Player ID not found!")
        details_label.configure(text='NA')
        bu_label.configure(text='NA')

        total_match_label.configure(text="NA")
        bat_innings_label.configure(text="NA")
        total_runs_label.configure(text="NA")
        highest_run_label.configure(text="NA")
        bat_average_label.configure(text="NA")
        ball_innings_label.configure(text="NA")
        total_wickets_label.configure(text="NA")
        highest_wicket_label.configure(text="NA")
        ball_economy_label.configure(text="NA")

    id_entry.delete(0, tk.END)


# Screen 1
root = tk.Tk()
root.title("Player Auction")

id_label = tk.Label(root, text="Enter Player ID:")
id_label.pack(padx=20, pady=20)

id_entry = tk.Entry(root)
id_entry.pack(padx=20, pady=20)
id_entry.bind("<Return>", show_player_details)

search_button = tk.Button(root, text="Search", command=show_player_details)
search_button.pack(padx=20, pady=20)


# screen 2
root2 = tk.Toplevel()
root2.title("Player Details")
root2.attributes('-fullscreen', True)


frame_width = root2.winfo_screenwidth() // 2
frame_height = root2.winfo_screenheight()


left_frame = tk.Frame(root2, width=frame_width, height=frame_height, borderwidth=100, relief=tk.RAISED)
left_frame.pack_propagate(False)  # Prevent frame from resizing based on content
left_frame.pack(side=tk.LEFT)


right_frame = tk.Frame(root2, width=frame_width, height=frame_height, borderwidth=100, relief=tk.RAISED)
right_frame.pack_propagate(False)
right_frame.pack(side=tk.RIGHT)


image = Image.open(".\\image\\blurr_background.png")
image = image.resize((frame_width, frame_height))
background_image = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(left_frame, image=background_image)
background_label.place(x=0, y=0,relwidth=1, relheight=1)
background_label = tk.Label(right_frame, image=background_image)
background_label.place(x=0, y=0,relwidth=1, relheight=1)

#####
image_label = tk.Label(left_frame)
image_label.pack(expand=True)
# image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Labels on the right side
name_label = tk.Label(left_frame, font=('Georgia', 25))
name_label.pack(expand=True)
# name_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

details_label = tk.Label(left_frame, font=('Georgia', 20))
details_label.pack(expand=True)
# details_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

bu_label = tk.Label(left_frame, font=('Georgia', 20))
bu_label.pack(expand=True)
# details_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

heading_label = tk.Label(right_frame, font=('Georgia', 20, "bold"))
heading_label.pack(expand=True, pady=5, anchor=tk.CENTER)

total_match_label = tk.Label(right_frame, font=('Century', 16))
total_match_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# total_match_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

bat_innings_label = tk.Label(right_frame, font=('Century', 16))
bat_innings_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# bat_innings_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

total_runs_label = tk.Label(right_frame, font=('Century', 16))
total_runs_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# total_runs_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

highest_run_label = tk.Label(right_frame, font=('Century', 16))
highest_run_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# highest_run_label.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

bat_average_label = tk.Label(right_frame, font=('Century', 16))
bat_average_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# bat_average_label.place(relx=0.5, rely=0.11, anchor=tk.CENTER)

ball_innings_label = tk.Label(right_frame, font=('Century', 16))
ball_innings_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# ball_innings_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

total_wickets_label = tk.Label(right_frame, font=('Century', 16))
total_wickets_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# total_wickets_label.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

highest_wicket_label = tk.Label(right_frame, font=('Century', 16))
highest_wicket_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# highest_wicket_label.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

ball_economy_label = tk.Label(right_frame, font=('Century', 16))
ball_economy_label.pack(expand=True, pady=5, anchor=tk.CENTER)
# ball_economy_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)


root.mainloop()
