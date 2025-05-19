import json
import os


#I want the quiz.json not be included and the exe should read it    
def load_quiz():
    """Loads quiz questions from an external JSON file located next to the .exe."""
    json_path = os.path.join(os.getcwd(), "quiz_data.json")  # Use `os.getcwd()` instead of `__file__`
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Quiz file missing! Please place 'quiz_data.json' next to the .exe")

    with open(json_path, "r") as file:
        return json.load(file)


def play_quiz():
    quiz_data = load_quiz()
    score = 0

    for item in quiz_data:
        print("\n" + item["question"])
        for i, option in enumerate(item["options"], 1):
            print(f"{i}. {option}")

        try:
            user_answer = int(input("Your choice (1-4): "))
            if item["options"][user_answer - 1] == item["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {item['answer']}.")
        except (ValueError, IndexError):
            print("⚠️ Invalid input, skipping to next question.")

    print(f"\nGame Over! 🎉 Your Score: {score}/{len(quiz_data)}")

if __name__ == "__main__":
    play_quiz()