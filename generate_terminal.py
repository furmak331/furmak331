import os
import gifos

# Initialize the terminal (adjust width/height as needed)
t = gifos.Terminal(width=700, height=450, xpad=10, ypad=10)

# Set the framerate 
t.set_fps(15)

# 1. The Boot Sequence
t.gen_text(text="[    0.000000] Booting Homelab Kernel 6.8.0-custom...", row_num=1)
t.gen_text(text="[    0.453211] Initializing Hardware: C++ Execution Engines [OK]", row_num=2)
t.gen_text(text="[    1.109234] Mounting Data Volumes: PostgreSQL [OK]", row_num=3)
t.gen_text(text="[    1.845012] Allocating Tensors for FedLogitALA... [OK]", row_num=4)
t.gen_text(text="[    2.100000] System Ready.", row_num=5)

# --- THE FIX: Clear the boot log by deleting the rows ---
for i in range(1, 6):
    t.delete_row(row_num=i)

# 2. The User Prompt and Output (Now resetting to row_num=1)
t.gen_text(text="furqan@homelab:~$ ./fetch_profile.sh", row_num=1)

# (Keep the rest of your script exactly the same from here)
t.gen_text(text="\x1b[32m--- Furqan Makhdoomi ---\x1b[0m", row_num=2)
t.gen_text(text="Software Engineer | Systems & Data Infrastructure | ML Researcher", row_num=3)
t.gen_text(text="", row_num=4)
t.gen_text(text="\x1b[36m> Stack:\x1b[0m C++, Python, PostgreSQL, PyTorch", row_num=5)
t.gen_text(text="\x1b[36m> Focus:\x1b[0m Federated Learning, Open-Source Engines", row_num=6)
t.gen_text(text="\x1b[36m> Status:\x1b[0m Intern @ UKG | Final Year @ NIT Srinagar", row_num=7)
t.gen_text(text="", row_num=8)

# 3. Fetch and Display Live GitHub Stats
t.gen_text(text="furqan@homelab:~$ ./get_stats.sh", row_num=9)

github_token = os.environ.get("GITHUB_TOKEN")
if github_token:
    stats = gifos.utils.fetch_github_stats(user_name="furmak331", token=github_token)
    t.gen_text(text=f"Total Commits: {stats.commits}", row_num=10)
    t.gen_text(text=f"Total Stars:   {stats.stars}", row_num=11)
    t.gen_text(text=f"Repositories:  {stats.repos}", row_num=12)
else:
    t.gen_text(text="Error: GITHUB_TOKEN not found.", row_num=10)

t.gen_text(text="furqan@homelab:~$ _", row_num=13, contin=True)

# Generate the final GIF
t.gen_gif(output_name="terminal_profile.gif")
