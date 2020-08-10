import praw
import subprocess
import os

# Creating the reddit object
reddit = praw.Reddit("BackgroundFromReddit")
file_extension = ['jpg', 'png']  # For now, we only want these two extensions
subreddit_name = "EarthPorn"  # The name of the subreddit we want

# We are only interested in the top url whih contains an easy to extract image
# So we only keep the first submission whose extension is correct
for submission in reddit.subreddit(subreddit_name).top(time_filter="day"):
    url = submission.url
    if url.split(".")[-1] in file_extension:
        print(url)
        break

# Configuring so that the image is centered
# then setting the background image
bg_centred = "gsettings set org.gnome.desktop.background picture-options scaled"
set_bg = f"gsettings set org.gnome.desktop.background picture-uri {url}"

subprocess.run(bg_centred.split(), stdout=subprocess.PIPE)
subprocess.run(set_bg.split(), stdout=subprocess.PIPE)

# Saving the files
home_dir = os.getenv("HOME")
subprocess.run(f"mkdir -p {home_dir}/Pictures/Backgrounds".split(),
               stdout=subprocess.PIPE)
subprocess.run(f"wget {url}".split(),
               stdout=subprocess.PIPE,
               cwd=f"{home_dir}/Pictures/Backgrounds")
