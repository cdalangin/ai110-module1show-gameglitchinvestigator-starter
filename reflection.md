# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - When I try to start a new game, it would reset the secret but not clear the message and allow you to submit anything, which I suspect happens in the if statement line 134 in app.py. When you submit a new guess, you have to hit submit twice or it won't register it or add it to the history, and I think that happens under the if statement in app.py line 147. The hints were wrong as well because for an input that was over the secret, it would say "Too Low" and if it was under the secret it would say "Too High", that happens in the check_guess function in app.py line 32


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   9   | Show "Go Higher"  | Show "Go Lower" | N/A                    |
|  99   | Show "Go Lower"   | Show "Go Higher"| N/A                    |
|  21.5 | Show "Go lower"   | Show "Correct"  | N/A                    |

(For the secret code 21)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Bug 1: Hints backwards ("Too High" says "Go HIGHER", "Too Low" says "Go LOWER")

    File: logic_utils.py:15-33 (check_guess)
    Change: swap the message strings so guess > secret (too high) pairs with "📉 Go LOWER!" and guess < secret (too low) pairs with "📈 Go HIGHER!". Applies to both the normal branch and the TypeError string-comparison fallback branch.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - While asking for a fix for the submit bug, Claude mentioned this bug that I didn't catch:
    - Bug 3: New Game resets the secret but leaves the old message/input submittable
      File: app.py:118-124 (if new_game: block)
      Change: the raw_guess text input keeps its old text after a new game starts because its widget key only depends on difficulty, not on the game/session. I'd add a session-tracked counter (e.g. st.session_state.game_id, incremented on new game) into the text_input's key so the widget resets to empty on a new game. I'd also reset st.session_state.score = 0 here since a fresh game should start from zero score (currently score carries over silently).

  - I didn't accept it because it was kind of confusing, so I asked it to explain it again while fixing all the other more obvious bug fixes (backwards hints and submit attempt logic turning secret into string)

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I ran the app again and tried the same inputs I used to see if the issue was resolved. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - With the new game bug, I tried to finish a game and hit the new game button, and it now behaved properly. I can play the game again and the variables updated as expected, like the history was empty and I could submit new guesses again.
- Did AI help you design or understand any tests? How?
  - I asked the AI to write a test to check the new game button functionality. It simulated a completed game by updating the states of the relevant variables, ran the function, then tested if the variables updated. This proved the code now works properly

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
