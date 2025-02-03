# 🎯 Quiz Game

Welcome to the **Python Quiz Game**! 🧠💡 This interactive, CLI-based quiz application tests your knowledge with multiple-choice questions. You can even extend it by adding your own questions using [Open Trivia Database](https://opentdb.com/api_config.php)! 🚀

---

## 🚀 Features

✅ **Interactive** question-answer format  
✅ **Score Tracking** to monitor progress  
✅ **Auto-fetch Questions** dynamically  
✅ **Beautifully Formatted CLI Experience** 🎨  
✅ **Easily Extendable** with [Open Trivia Database](https://opentdb.com/api_config.php)  

---

## 🛠️ Installation & Setup

### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/quiz-game.git
cd quiz-game
```

### 🐍 Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the Quiz
```bash
python main.py
```

---

## 📁 Project Structure

```
📂 quiz-game
├── 📄 main.py            # Entry point of the quiz
├── 📄 quiz_brain.py      # Handles the quiz logic
├── 📄 question_model.py  # Question structure
├── 📄 data.py            # Stores the quiz questions
└── 📄 README.md          # Documentation
```

---

## 🎨 How to Add More Questions?

You can easily add more questions by using [Open Trivia Database](https://opentdb.com/api_config.php) or manually updating the `data.py` file.

### 📝 Example:
```python
question_data = [
    {"question": "What is the capital of France?", "correct_answer": "Paris"},
    {"question": "Who developed Python?", "correct_answer": "Guido van Rossum"}
]
```

Or fetch live questions using an API:
```python
import requests
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()["results"]
```

---

## 🤝 Contributing

💡 Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Let's Connect!

🔗 [LinkedIn](https://www.linkedin.com/in/harshad-agrawal-486964322/)  
🐙 [GitHub](https://github.com/Harshad2321)  

🚀 **Happy Coding!** 🎉

