# 🧠 Flash Card App — Spanish ↔ Portuguese

> A language learning flashcard application built with **Python** and **Tkinter**.  
> The program displays Spanish words and automatically flips the card after a few seconds to reveal the Portuguese translation.  
> It also keeps track of which words you’ve already learned.

## 🧩 Technologies and Tools Used

- **Python 3.10+**
- **Tkinter** — for the graphical user interface (GUI)
- **Pandas** — for data handling and CSV manipulation
- **Random** — to select words randomly

## ⚙️ Main Features

- **Interactive Flashcards:**  
  Displays Spanish words that automatically flip to show their Portuguese meaning after 3 seconds.  

- **Progress Tracking:**  
  Keeps track of the words you’ve learned and stores the remaining ones in a separate file (`words_to_learn.csv`).  

- **Data Persistence:**  
  Automatically creates or updates `words_to_learn.csv` based on your progress.  

- **Dynamic Interface:**  
  Includes images for card front, card back, and buttons (✔️ / ❌) for a more visual learning experience.  

- **Simple and Efficient:**  
  The entire project runs locally and requires only Python and Pandas to operate.

## 🖥️ Demonstration

```bash
🃏 Step 1: The app shows a Spanish word.
⏳ Step 2: After 3 seconds, the card flips and shows its Portuguese translation.
✅ Step 3: Click the ✔️ button if you know the word.
❌ Step 4: Click the ❌ button to skip and move to the next card.
📂 Step 5: Your progress is automatically saved in "data/words_to_learn.csv".
