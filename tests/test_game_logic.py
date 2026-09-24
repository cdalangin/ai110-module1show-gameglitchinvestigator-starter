import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from streamlit.testing.v1 import AppTest

APP_PATH = os.path.join(os.path.dirname(__file__), "..", "app.py")

from logic_utils import check_guess

def test_new_game_resets_session_state():
    at = AppTest.from_file(APP_PATH)
    at.run()

    # Simulate an in-progress (and finished) game before resetting.
    at.session_state["attempts"] = 5
    at.session_state["status"] = "lost"
    at.session_state["history"] = [10, 20, 30]

    new_game_button = next(b for b in at.button if b.label == "New Game 🔁")
    new_game_button.click().run()

    assert at.session_state["attempts"] == 0
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert 1 <= at.session_state["secret"] <= 100


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"
