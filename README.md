# 💘 Love Calculator


The **Love Calculator** is a fun and interactive desktop application built with Python and the Tkinter library. It lets users input two names and calculates a "love score" based on the occurrences of specific letters. Depending on the score, a unique message is displayed to show the compatibility between the two names.

![Love Calculator Demo](https://github.com/user-attachments/assets/db333129-5e88-4ebf-a6f6-626edfb16fc4)

## Installation and Requirements

### Requirements:
- **Python 3.x** must be installed on your system.
- **Pillow** library for handling images.

### Installation:
1. **Clone** or **download** the repository to your local machine.
2. Install the `Pillow` library by running:
   ```bash
   pip install pillow

   ## How It Works

### Input:
- Enter two names in the provided input fields.

### Calculation:
The application calculates the score by:
- Counting the occurrences of the letters in "TRUE" and "LOVE" within the combined names.
- Creating a total score from these counts.

### Result Display:
Based on the score, the following messages are shown:
- **Above 80**: "💘 You are a match made in heaven!"
- **50 - 80**: "💞 You have a strong connection!"
- **30 - 49**: "💫 There's some potential here!"
- **Below 30**: "😅 Maybe better as friends!"

## Customization
- **Background Image**: Replace `lovecalculator.png` with your own image for a personalized background.
- **Fonts and Colors**: Modify the `font`, `fg`, and `bg` parameters in the `Label` and `Entry` widgets for custom styles.


## Acknowledgments
- **Tkinter**: Used for building the user interface.
- **Pillow**: Utilized for image handling and background display.

## Enjoy using the Love Calculator and share the fun with your friends and loved ones!
