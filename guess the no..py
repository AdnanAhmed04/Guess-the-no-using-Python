{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9fab4bda",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "import random\n",
    "\n",
    "def generate_random_number():\n",
    "    start_range = int(start_entry.get())\n",
    "    end_range = int(end_entry.get())\n",
    "    user_guess = int(guess_entry.get())\n",
    "\n",
    "    random_number = random.randint(start_range, end_range)\n",
    "\n",
    "    if user_guess == random_number:\n",
    "        result_label.config(text=\"Congratulations! You guessed the correct number.\")\n",
    "    else:\n",
    "        result_label.config(text=\"Sorry, the correct number was {}.\".format(random_number))\n",
    "\n",
    "# Create the main window\n",
    "root = tk.Tk()\n",
    "root.title(\"Random Number Guessing Game\")\n",
    "\n",
    "# Create and place widgets\n",
    "start_label = ttk.Label(root, text=\"Enter start number:\")\n",
    "start_label.grid(row=0, column=0, padx=10, pady=10)\n",
    "\n",
    "start_entry = ttk.Entry(root)\n",
    "start_entry.grid(row=0, column=1, padx=10, pady=10)\n",
    "\n",
    "end_label = ttk.Label(root, text=\"Enter end number:\")\n",
    "end_label.grid(row=1, column=0, padx=10, pady=10)\n",
    "\n",
    "end_entry = ttk.Entry(root)\n",
    "end_entry.grid(row=1, column=1, padx=10, pady=10)\n",
    "\n",
    "guess_label = ttk.Label(root, text=\"Enter your guess:\")\n",
    "guess_label.grid(row=2, column=0, padx=10, pady=10)\n",
    "\n",
    "guess_entry = ttk.Entry(root)\n",
    "guess_entry.grid(row=2, column=1, padx=10, pady=10)\n",
    "\n",
    "generate_button = ttk.Button(root, text=\"Check Guess\", command=generate_random_number)\n",
    "generate_button.grid(row=3, column=0, columnspan=2, pady=10)\n",
    "\n",
    "result_label = ttk.Label(root, text=\"\")\n",
    "result_label.grid(row=4, column=0, columnspan=2, pady=10)\n",
    "\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2958f102",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
