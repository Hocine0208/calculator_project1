# Project 1: Calculator (Python + CustomTkinter)
## Full to-do: 6 days, about 60-90 min each

Rules: write the code yourself first. Ask me for hints before solutions. A task is only done when you show it works or explain it.

## Final result (definition of done)
- [ ] Window with display + buttons 0-9, `.`, `+ - x /`, `=`, `C`
- [ ] Correct results for one operation at a time (e.g. 12 + 5)
- [ ] No crash on division by zero or bad input
- [ ] Logic separated from UI, with pytest tests passing
- [ ] Code on GitHub with a README

---
## Day 1: Requirements, design, environment
**Goal:** know what you build; working environment.  **Outcome:** empty window titled "Calculator".
**Concepts:** requirements, 3 layers (UI / logic / state), venv, event loop.
- [ ] Check `python --version` and `pip --version`
- [ ] Create and activate `.venv`, run `pip install -r requirements.txt`
- [ ] Complete `main.py` (window, title, size, mainloop)
- [ ] Predict: what if `.mainloop()` is missing? Then test it
**Tests:** window opens/closes cleanly; geometry "500x200" changes the shape.
**Checkpoint:** why separate logic from buttons?

## Day 2: Layout (display + buttons) + Git
**Goal:** build the full interface (no behavior yet).  **Outcome:** a calculator that looks right.
**Concepts:** widgets (CTkEntry or CTkLabel, CTkButton), `grid` layout (row, column, columnspan, padx/pady), building widgets in a loop, intro to Git.
- [ ] Add a display at the top spanning all columns
- [ ] Plan the button grid on paper first (4 columns; where do `C`, `=`, `0` go?)
- [ ] Create buttons from a list of labels with a loop, not 17 copy-pasted lines
- [ ] Make columns resize evenly (hint: `grid_columnconfigure` with `weight`)
- [ ] `git init`, add a `.gitignore` containing `.venv/`, make your first commit
**Tests:** every button appears once; window resize keeps the layout tidy; `git log` shows 1 commit.
**Checkpoint:** why use a loop? What does `columnspan` do?

## Day 3: Logic layer + pytest
**Goal:** a calculation function that works without any GUI.  **Outcome:** passing tests.
**Concepts:** functions, modules (`logic.py`), exceptions, `try/except`, pytest basics.
- [ ] Create `logic.py` with `calculate(a, op, b)` returning a number
- [ ] Support `+ - * /`; raise `ZeroDivisionError` (or your own error) for division by zero
- [ ] Reject an unknown operator with a clear error
- [ ] Create `test_logic.py` and install pytest (`pip install pytest`)
- [ ] Write the tests BEFORE the code for at least two operations
**Tests (minimum):** 2+3=5; 5-8=-3; 4*2.5=10; 9/3=3; 5/0 raises an error; 5 ^ 2 raises an error.
**Checkpoint:** why return a number instead of printing? What does a failing test tell you?

## Day 4: State and events
**Goal:** make the buttons work.  **Outcome:** type digits and see them on the display.
**Concepts:** application state, event handlers, `command=`, `lambda` / `functools.partial`, global vs class state.
- [ ] Decide what state you need (current text? first number? operator?) and write it down
- [ ] One handler for digit buttons that appends to the display
- [ ] Handler for operator buttons: store the first number and the operator, then clear for the next number
- [ ] Handler for `=`: call `calculate()` from `logic.py` and show the result
- [ ] Handler for `C`: reset all state
**Tests:** 7 + 8 = 15; C after a result gives a clean state; pressing `=` with nothing typed does not crash.
**Checkpoint:** explain what happens, step by step, when you click `7`, `+`, `8`, `=`.

## Day 5: Edge cases, errors, polish
**Goal:** make it robust.  **Outcome:** no crash on weird input.
**Concepts:** input validation, user-friendly error messages, small refactor, OOP when useful.
- [ ] Block two decimal points in one number (`1.2.3`)
- [ ] Show "Error" (not a crash) on division by zero, then recover on the next input
- [ ] Handle an operator pressed twice (`5 + * 3`) and a leading operator
- [ ] Format results (show `5` not `5.0`)
- [ ] Refactor: wrap the UI in a `class Calculator(ctk.CTk)` if the code feels messy
- [ ] Optional: backspace button, light/dark mode (`ctk.set_appearance_mode`)
**Tests:** 5 / 0; 1..2; 0.1 + 0.2 (look at the result and explain why); very long numbers.
**Checkpoint:** which bug was hardest, and how did you find it?

## Day 6: Review, README, GitHub
**Goal:** finish like a professional.  **Outcome:** published project.
**Concepts:** architecture review, documentation, GitHub, improvement planning.
- [ ] Review architecture: can you draw UI / logic / state and name the files for each?
- [ ] Run all pytest tests; fix failures
- [ ] Write `README.md`: what it does, how to install and run, screenshot, project structure
- [ ] Add `requirements.txt` (check it is correct)
- [ ] Create a GitHub repo, `git push`
- [ ] Write 3 improvements for later (e.g. parentheses, history, keyboard input)
**Checkpoint:** explain your whole project in 2 minutes as if to a teammate.

---
## Progress tracker
| Day | Status | Problems | To review |
|-----|--------|----------|-----------|
| 1 | in progress | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

## Paste into a new conversation to resume
"Project 1 Calculator (Python + CustomTkinter), following the 6-day to-do. Current day: __. Done: __. Problems: __. Please continue as my mentor: hints first, no full solutions."
