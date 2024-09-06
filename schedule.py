import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



schedule = [
    {"task": "Sleep", "time": "8:30 am - 1:30 pm", "duration": 300},
    {"task": "Meal", "time": "1:30 pm - 2:00 pm", "duration": 30},
    {"task": "Work (US)", "time": "2:00 pm - 7:00 pm", "duration": 300},
    {"task": "Meal", "time": "7:30 pm - 8:00 pm", "duration": 30},
    {"task": "Work (Europe)", "time": "8:00 pm - 1:30 am", "duration": 330},
    {"task": "Break", "time": "1:30 am - 2:00 am", "duration": 30},
    {"task": "Side Prog", "time": "2:00 am - 6:00 am", "duration": 240},
    {"task": "Exercise Meal", "time": "6:00 am - 7:30 am", "duration": 90},
    {"task": "Read/Music", "time": "7:30 am - 8:00 am", "duration": 30}
]

tasks = [item["task"] for item in schedule]
durations = [item["duration"] for item in schedule]

fig, ax = plt.subplots()

wedges, texts, autotexts = ax.pie(
    durations,
    labels=None,
    autopct="",
    colors = ['white', 'white', 'gray', 'white', 'gray', 'white', 'white', 'white', 'white'],
    wedgeprops=dict(edgecolor="black", linewidth=1, alpha=0.5),
    textprops=dict(color="black"),
    pctdistance=0.85
)
outer_circle = plt.Circle((0, 0), 1.02, color="black", fill=False, linewidth=1)
ax.add_artist(outer_circle)

for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = 0.7 * np.cos(np.deg2rad(angle))
    y = 0.7 * np.sin(np.deg2rad(angle))
    
    ax.text(x, y, tasks[i], ha="center", va="center", fontsize=12, color="black")


for hour in range(24, 0, -1):
    angle = (24 - hour) * 15 + 90
    hand_angle = np.deg2rad(angle)
    x = 1.2 * np.cos(hand_angle)
    y = 1.2 * np.sin(hand_angle)
    ax.text(x, y, f'{hour:02d}', ha="center", va="center", fontsize=12, color="black")

    # Draw vertical lines
    line_x = 1.05 * np.cos(hand_angle)
    line_y = 1.05 * np.sin(hand_angle)
    line_x2 = 1.01 * np.cos(hand_angle)
    line_y2 = 1.01 * np.sin(hand_angle)
    ax.plot([line_x, line_x2], [line_y, line_y2], color="black", linewidth=1)

now = datetime.now()
current_hour = now.hour
current_minute = now.minute

# Calculate hour hand position using 24-hour format
hour_angle = (current_hour % 24) * 15 + (current_minute / 60) * 15 - 90
hour_hand_length = 0.5
hour_hand_angle = np.deg2rad(hour_angle)
hour_hand_x = hour_hand_length * np.cos(hour_hand_angle)
hour_hand_y = hour_hand_length * np.sin(hour_hand_angle)
ax.plot([0, hour_hand_x], [0, hour_hand_y], color="black", linewidth=2)

# Calculate minute hand position
minute_angle = (current_minute * 6) - 90
minute_hand_length = 0.7
minute_hand_angle_rad = np.deg2rad(minute_angle)
minute_hand_x = minute_hand_length * np.cos(minute_hand_angle_rad)
minute_hand_y = minute_hand_length * np.sin(minute_hand_angle_rad)
ax.plot([0, minute_hand_x], [0, minute_hand_y], color="black", linewidth=2.5)

#play button
play_button_radius = 0.1
circle = plt.Circle((0, 0), play_button_radius, color="blue", fill=True)
ax.add_artist(circle)

#text position
ax.text(0, 0, "Play", color="white", ha="center", va="center", fontsize=10, fontweight='bold')

ax.axis("equal")

fig.patch.set_alpha(0)

plt.show()
