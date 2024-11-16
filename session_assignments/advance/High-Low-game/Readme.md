```markdown
# High-Low Game

## Problem Overview
The **High-Low Game** is a fun way to practice working with control flow and Booleans in Python. The objective of the game is to guess whether your number is higher or lower than the computer's hidden number. 

### Gameplay
1. Two random numbers (1 to 100) are generated—one for the player and one for the computer.
2. The player can see their number but not the computer's number.
3. The player guesses if their number is higher or lower than the computer's number.
4. Points are awarded if the guess is correct. The game ends after a set number of rounds.

---

## Milestones

### **Milestone #1: Generate Random Numbers**
- Randomly generate numbers for both the player and the computer.
- Initially, display both numbers for testing purposes.

---

### **Milestone #2: Get User Input**
- Prompt the player to guess whether their number is "higher" or "lower" than the computer's number.

---

### **Milestone #3: Write Game Logic**
- Implement logic to determine if the player’s guess is correct.
- Handle edge cases, such as when both numbers are equal (the computer wins).

---

### **Milestone #4: Play Multiple Rounds**
- Extend the game to include multiple rounds using a constant (`NUM_ROUNDS`).
- Display the round number and visually separate each round with a blank line.

---

### **Milestone #5: Add a Points System**
- Track and display the player’s score after each round.

---

## Extensions

### **Extension #1: Input Validation**
- Safeguard against invalid input (e.g., anything other than "higher" or "lower").
- Reprompt the player if they enter an invalid choice.

### **Extension #2: Conditional Ending Messages**
- Add customized ending messages based on the player's performance:
  - Perfect score: "Wow! You played perfectly!"
  - At least half rounds won: "Good job, you played really well!"
  - Less than half rounds won: "Better luck next time!"

---

