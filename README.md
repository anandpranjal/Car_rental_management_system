# Campus Car Rental System

A beginner-friendly Python terminal application built to manage car rentals, calculate rental bills, track customer bookings, and monitor fleet stock.

---

## About the Project
This project was developed as a university programming assignment to practice **modular programming** and basic Python data structures. 

Instead of writing all the logic into one huge file, the program is broken into **6 focused Python files**. This makes the code organized, easy to debug, and simple to explain during viva presentations. It does not use any complex libraries or shortcuts—just standard loops, lists, dictionaries, and functions.

---

## File Structure & Module Breakdown

```text
car_rental_system/
├── cars.py         # Module 1: Fleet inventory & stock updater
├── pricing.py      # Module 2: Daily rates & bill calculation
├── customers.py    # Module 3: Active booking records list
├── rules.py        # Module 4: 1-car limit validation rule
├── reports.py      # Module 5: Alert limits and message constants
└── main.py         # Module 6: Interactive terminal menu
