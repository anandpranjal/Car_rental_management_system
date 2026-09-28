# Problem Statement: Car Rental System

## 1. Background & Problem
Managing car bookings with pen and paper or basic text files is confusing and prone to errors. At small rental desks or campus vehicle hubs:
- Staff often lose track of which cars are currently parked on the lot and which ones are out with drivers.
- There are no automatic safeguards to stop one person from booking several cars at once, leaving no options for others.
- Staff have to manually calculate daily rental fees, which often leads to billing mistakes.
- It is difficult to spot when stock for a specific vehicle category is running dangerously low.

## 2. Project Objective
The goal of this project is to build a simple, clean, and modular Python program that handles everyday car rental operations directly from the terminal:
- Keep an accurate, real-time count of available cars (Sedan, SUV, Hatchback).
- Automatically calculate rental charges based on the vehicle type and number of days.
- Ensure fair access by strictly limiting each driving license to one car at a time.
- Process vehicle returns cleanly and return them back to available stock.
- Alert staff when stock for any car type drops below 2 units.

## 3. Scope & Target Users
- **Target Users:** Desk operators, student coordinators, or small rental desk managers.
- **Application Scope:** A lightweight command-line interface (CLI) divided cleanly across 6 separate Python files, utilizing core concepts like dictionaries, lists, and standard functions without requiring external libraries.

## 4. System Modules & Responsibilities
1. **`cars.py`:** Stores the car fleet inventory and updates stock counts.
2. **`pricing.py`:** Manages daily rental rates and computes billing amounts.
3. **`customers.py`:** Maintains the list of active bookings and handles check-in/check-out records.
4. **`rules.py`:** Enforces the 1-car borrowing limit per driving license.
5. **`reports.py`:** Stores alert limits and status messages.
6. **`main.py`:** Runs the main menu loop and user prompts.