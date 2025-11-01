# What To Eat Today+ (Combo Version)

Author:Yihan Xiao  
Created for:UTS Code Prototype Project  
Language:Python 3  

1. Introduction  
What To Eat Today+ is a Python-based meal suggestion prototype that uses global cuisine categories to recommend a main dish + a drink combo.  
The motivation: to demonstrate code literacy by integrating data structures, randomness logic, file persistence and user interface (GUI/CLI) in one coherent prototype.

2. Technologies Used  
- Python 3.9+  
- Standard libraries: `random`, `time`, `csv`, `os`  
- GUI: `tkinter` (built-in)  
- Markdown for documentation  

3. Project Status  
Status:Prototype complete for submission.  
Further work could include:  
- More dynamic user preferences (e.g., dietary restrictions)  
- Multi-user history / cloud persistence  
- More sophisticated UI/UX design  

4. Features  
- Meal combo: the program randomly selects a **main dish** from a chosen cuisine, plus a drink associated with that cuisine (or a generic drink)  
- Global cuisine dataset: Japanese, Chinese, Korean, Thai, Vietnamese, Indian, Malaysian, Spanish, Mexican, Western/Fastfood  
- Random emoji-based reactions (1-3 emojis) to add a playful feedback feel  
- Dual interface: **GUI mode** (via Tkinter) and **CLI mode** (in the console)  
- Automatic persistence: every suggestion saved into `history.csv` (date, cuisine, main, drink)  

5. How to Run  
GUI Mode  
1. Open `what_to_eat_today_plus.py` in PyCharm (or other IDE)  
2. Run the file  
3. When prompted in console ：
Enter `1`, press Enter  
4. In the window: select a cuisine from dropdown → click **Suggest Combo** → view recommendation  
5. The recommendation is saved into `history.csv`

CLI Mode  
1. Run the same file  
2. When prompted, enter `2`  
3. At prompt, type a cuisine exactly as listed (e.g., `Japanese`, `Thai`, `Chinese`)  
4. Console returns: date, cuisine, main dish, drink, and emoji reaction  

6. File Structure  
   .what_to_eat_today_plus.py # Main program code
   .README.md # This file
   .history.csv # Auto-generated log of suggestions


7. Example Output
   <img width="600" height="392" alt="截屏2025-11-01 下午8 05 35" src="https://github.com/user-attachments/assets/88cc72e4-ec57-4124-ab5c-be396ba94e27" />

   
8. License & Acknowledgements  
This project was developed as part of an academic assignment at the University of Technology Sydney (UTS).  
For educational use only; attribution required for reuse.

9. Contact  
For questions or feedback, contact: Yihan Xiao (Yihan.Xiao-2@student.uts.edu.au)  （+61 406520726）
