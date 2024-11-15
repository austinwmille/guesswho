from moviepy.editor import *

# Set up variables
width, height = 720, 480
duration = 5  # seconds
bg_color = (250, 230, 100)  # Background color

# Create a solid background
background_clip = ColorClip(size=(width, height), color=bg_color, duration=duration)

# Add main title text
title_text = TextClip("It's tiiiiime for...", fontsize=50, color='red', font='Amiri-Bold', size=(width, None)).set_position('center').set_duration(2)

# Add “Guess That Meme!” text with animation
meme_text = TextClip("Guess That Meme!", fontsize=70, color='blue', font='Amiri-Bold', size=(width, None)).set_position('center').set_duration(3)
meme_text = meme_text.set_start(2).crossfadein(0.5)

# Add confetti effect (optional, using transparency overlay)
confetti = ColorClip((width, height), color=(255, 255, 255)).set_duration(duration).fl_image(lambda pic: (pic * 0.5).astype("uint8"))
confetti = confetti.set_opacity(0.2)

# Combine everything
final_clip = CompositeVideoClip([background_clip, title_text, meme_text, confetti])

# Save the result
final_clip.write_videofile("guess_that_meme_intro.mp4", fps=24)
