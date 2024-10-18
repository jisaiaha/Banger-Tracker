from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

# File to store counts
COUNTS_FILE = 'song_counts.txt'

# Initialize counts if the file doesn't exist
def initialize_counts():
    if not os.path.exists(COUNTS_FILE):
        with open(COUNTS_FILE, 'w') as f:
            f.write("0\n0\n0")  # Dougie, No Hands, FE!N

# Read the current counts from the file
def get_counts():
    with open(COUNTS_FILE, 'r') as f:
        counts = f.read().splitlines()
    return list(map(int, counts))

# Update the counts in the file
def update_counts(dougie_count, no_hands_count, fein_count):
    with open(COUNTS_FILE, 'w') as f:
        f.write(f"{dougie_count}\n{no_hands_count}\n{fein_count}")

@app.route('/')
def index():
    initialize_counts()
    counts = get_counts()
    return render_template('index.html', dougie=counts[0], no_hands=counts[1], fein=counts[2])

@app.route('/dougie')
def play_dougie():
    counts = get_counts()
    counts[0] += 1
    update_counts(counts[0], counts[1], counts[2])
    return redirect(url_for('index'))

@app.route('/no_hands')
def play_no_hands():
    counts = get_counts()
    counts[1] += 1
    update_counts(counts[0], counts[1], counts[2])
    return redirect(url_for('index'))

@app.route('/fein')
def play_fein():
    counts = get_counts()
    counts[2] += 1
    update_counts(counts[0], counts[1], counts[2])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
