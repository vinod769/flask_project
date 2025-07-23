from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Home redirects to registration
@app.route('/')
def home():
    return redirect(url_for('register'))

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('main'))
    return render_template('login.html')

# Main Dashboard
@app.route('/main')
def main():
    return render_template('mainfirst.html')

# Example subpages
@app.route('/subpage1')
def subpage1():
    return render_template('subpage1.html')

@app.route('/subpage2')
def subpage2():
    return render_template('subpage2.html')


@app.route('/subpage11')
def subpage11():
    return render_template('subpage11.html')

@app.route('/subpage12')
def subpage12():
    return render_template('subpage12.html')

@app.route('/subpage13')
def subpage13():
    return render_template('subpage13.html')

@app.route('/subpage14')
def subpage14():
    return render_template('subpage14.html')

@app.route('/subpage15')
def subpage15():
    return render_template('subpage15.html')


# ---------- STORAGE PAGE 21 ----------
@app.route('/storagepage21', methods=['GET', 'POST'])
def storagepage21():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        value = request.form.get('value')

        file_exists = os.path.isfile('data.csv')
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Date', 'Value'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Name': name, 'Phone': phone, 'Date': date, 'Value': value})

        return redirect(url_for('storagepage21'))

    return render_template('storagepage21.html')

@app.route('/displaydata21')
def displaydata21():
    names = set()
    if os.path.exists('data.csv'):
        with open('data.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Name'].strip())
    return render_template('namelist21.html', names=sorted(names))

@app.route('/displaydata21/<name>')
def user_details(name):
    entries = []
    if os.path.exists('data.csv'):
        with open('data.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == name.strip().lower():
                    entries.append(row)
    return render_template('user_details21.html', name=name, entries=entries)


# ---------- STORAGE PAGE 22 ----------
@app.route('/storagepage22', methods=['GET', 'POST'])
def storagepage22():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        value = request.form.get('value')

        file_exists = os.path.isfile('data22.csv')
        with open('data22.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Date', 'Value'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Name': name, 'Phone': phone, 'Date': date, 'Value': value})

        return redirect(url_for('storagepage22'))

    return render_template('storagepage22.html')

@app.route('/displaydata22')
def displaydata22():
    names = set()
    if os.path.exists('data22.csv'):
        with open('data22.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Name'].strip())
    return render_template('namelist22.html', names=sorted(names))

@app.route('/displaydata22/<name>')
def user_details22(name):
    entries = []
    if os.path.exists('data22.csv'):
        with open('data22.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == name.strip().lower():
                    entries.append(row)
    return render_template('user_details22.html', name=name, entries=entries)


# ---------- STORAGE PAGE 23 ----------
@app.route('/storagepage23', methods=['GET', 'POST'])
def storagepage23():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        value = request.form.get('value')

        file_exists = os.path.isfile('data23.csv')
        with open('data23.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Date', 'Value'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Name': name, 'Phone': phone, 'Date': date, 'Value': value})

        return redirect(url_for('storagepage23'))

    return render_template('storagepage23.html')

@app.route('/displaydata23')
def displaydata23():
    names = set()
    if os.path.exists('data23.csv'):
        with open('data23.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Name'].strip())
    return render_template('namelist23.html', names=sorted(names))

@app.route('/displaydata23/<name>')
def user_details23(name):
    entries = []
    if os.path.exists('data23.csv'):
        with open('data23.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == name.strip().lower():
                    entries.append(row)
    return render_template('user_details23.html', name=name, entries=entries)


# ---------- STORAGE PAGE 24 ----------
@app.route('/storagepage24', methods=['GET', 'POST'])
def storagepage24():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        value = request.form.get('value')

        file_exists = os.path.isfile('data24.csv')
        with open('data24.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Date', 'Value'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Name': name, 'Phone': phone, 'Date': date, 'Value': value})

        return redirect(url_for('storagepage24'))

    return render_template('storagepage24.html')

@app.route('/displaydata24')
def displaydata24():
    names = set()
    if os.path.exists('data24.csv'):
        with open('data24.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Name'].strip())
    return render_template('namelist24.html', names=sorted(names))

@app.route('/user_details24/<name>')
def user_details24(name):
    entries = []
    if os.path.exists('data24.csv'):
        with open('data24.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip() == name:
                    entries.append(row)
    return render_template('user_details24.html', name=name, entries=entries)

# ---------- STORAGE PAGE 25 ----------

@app.route('/seedmain1')
def seedmain1():
    return render_template('seedmain1.html')

@app.route('/storagepage25', methods=['GET', 'POST'])
def storagepage25():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        value = request.form.get('value')

        file_exists = os.path.isfile('data25.csv')
        with open('data25.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Date', 'Value'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Name': name, 'Phone': phone, 'Date': date, 'Value': value})

        return redirect(url_for('storagepage25'))

    return render_template('storagepage25.html')

@app.route('/displaydata25')
def displaydata25():
    names = set()
    if os.path.exists('data25.csv'):
        with open('data25.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Name'].strip())
    return render_template('namelist25.html', names=sorted(names))

@app.route('/displaydata25/<name>')
def user_details25(name):
    entries = []
    if os.path.exists('data25.csv'):
        with open('data25.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == name.strip().lower():
                    entries.append(row)
    return render_template('user_details25.html', name=name, entries=entries)


# ---------- SEED STORAGE SYSTEM ----------
CSV_FILE = 'seed_data.csv'

@app.route('/seedstorage1', methods=['GET', 'POST'])
def seedstorage1():
    if request.method == 'POST':
        data = {
            'Name': request.form['name'],
            'Seed Name': request.form['seed_name'],
            'Date': request.form['date'],
            'Shop': request.form['shop'],
            'Quantity': request.form['quantity'],
            'Cost': request.form['cost'],
            'Phone': request.form['phone']
        }
        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
        return redirect(url_for('seeddisplay1'))
    return render_template('seedstorage1.html')

@app.route('/seeddisplay1')
def seeddisplay1():
    search_name = request.args.get('seed_name', '').strip().lower()
    entries = []
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not search_name or search_name in row['Seed Name'].lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('seeddisplay1.html', entries=entries, search_name=search_name)

@app.route('/seednamelist1')
def seednamelist1():
    names = set()
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Seed Name'])
    except FileNotFoundError:
        pass
    return render_template('seednamelist1.html', names=sorted(names))

@app.route('/seeduser_details1/<seed_name>')
def seeduser_details1(seed_name):
    entries = []
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Seed Name'].lower() == seed_name.lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('seeduser_details1.html', seed_name=seed_name, entries=entries)

FERTILIZER_CSV_FILE = 'fertilizers.csv'

# Fertilizers main page
@app.route('/fertilizersmain1')
def fertilizers_main():
    return render_template('fertilizersmain1.html')

# Fertilizers storage page
@app.route('/fertilizersstorage1', methods=['GET', 'POST'])
def fertilizers_storage():
    if request.method == 'POST':
        data = {
            'Name': request.form['name'],
            'Fertilizer Name': request.form['fertilizer_name'],
            'Date': request.form['date'],
            'Shop': request.form['shop'],
            'Quantity': request.form['quantity'],
            'Cost': request.form['cost'],
            'Phone': request.form['phone']
        }

        file_exists = os.path.isfile(FERTILIZER_CSV_FILE)
        with open(FERTILIZER_CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists or file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        return redirect(url_for('fertilizers_display'))
    return render_template('fertilizersstorage1.html')

# Fertilizers display page
@app.route('/fertilizersdisplay1')
def fertilizers_display():
    search_name = request.args.get('fertilizer_name', '').strip().lower()
    entries = []
    try:
        with open(FERTILIZER_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not search_name or search_name in row['Fertilizer Name'].lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('fertilizersdisplay1.html', entries=entries, search_name=search_name)

# Fertilizers name list page
@app.route('/fertilizersnamelist1')
def fertilizers_name_list():
    names = set()
    try:
        with open(FERTILIZER_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Fertilizer Name'].strip())
    except FileNotFoundError:
        pass
    return render_template('fertilizersnamelist1.html', names=sorted(names))

# Fertilizers user details page
@app.route('/fertilizersuserdetails1/<fertilizer_name>')
def fertilizers_user_details(fertilizer_name):
    entries = []
    try:
        with open(FERTILIZER_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Fertilizer Name'].strip().lower() == fertilizer_name.strip().lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('fertilizersuserdetails1.html', fertilizer_name=fertilizer_name, entries=entries)

PESTICIDE_CSV_FILE = 'pesticides.csv'

# Pesticides main page
@app.route('/pesticidesmain1')
def pesticides_main():
    return render_template('pesticidesmain1.html')


# Pesticides storage page
@app.route('/pesticidesstorage1', methods=['GET', 'POST'])
def pesticides_storage():
    if request.method == 'POST':
        data = {
            'Name': request.form['name'],
            'Pesticide Name': request.form['pesticide_name'],
            'Date': request.form['date'],
            'Shop': request.form['shop'],
            'Quantity': request.form['quantity'],
            'Cost': request.form['cost'],
            'Phone': request.form['phone']
        }

        file_exists = os.path.isfile(PESTICIDE_CSV_FILE)
        with open(PESTICIDE_CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists or file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        return redirect(url_for('pesticides_display'))
    return render_template('pesticidesstorage1.html')


# Pesticides display page
@app.route('/pesticidesdisplay1')
def pesticides_display():
    search_name = request.args.get('pesticide_name', '').strip().lower()
    entries = []
    try:
        with open(PESTICIDE_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not search_name or search_name in row['Pesticide Name'].lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('pesticidesdisplay1.html', entries=entries, search_name=search_name)


# Pesticides name list page
@app.route('/pesticidesnamelist1')
def pesticides_name_list():
    names = set()
    try:
        with open(PESTICIDE_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Pesticide Name'].strip())
    except FileNotFoundError:
        pass
    return render_template('pesticidesnamelist1.html', names=sorted(names))


# Pesticides user details page
@app.route('/pesticidesuserdetails1/<pesticide_name>')
def pesticides_user_details(pesticide_name):
    entries = []
    try:
        with open(PESTICIDE_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Pesticide Name'].strip().lower() == pesticide_name.strip().lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('pesticidesuserdetails1.html', pesticide_name=pesticide_name, entries=entries)
GODAN_CSV_FILE = 'godan.csv'

# Main menu page
@app.route('/godanmain1')
def godan_main():
    return render_template('godanmain1.html')

# Storage page
@app.route('/godanstorage1', methods=['GET', 'POST'])
def godan_storage():
    if request.method == 'POST':
        data = {
            'Name': request.form['name'],
            'Panta Peru': request.form['panta_peru'],
            'Date': request.form['date'],
            'Shop': request.form['shop'],
            'Quantity': request.form['quantity'],
            'Cost': request.form['cost'],
            'Phone': request.form['phone']
        }

        file_exists = os.path.isfile(GODAN_CSV_FILE)
        with open(GODAN_CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists or file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        return redirect(url_for('godan_display'))

    return render_template('godanstorage1.html')

# Display all records
@app.route('/godandisplay1')
def godan_display():
    search_name = request.args.get('panta_peru', '').strip().lower()
    entries = []
    try:
        with open(GODAN_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not search_name or search_name in row['Panta Peru'].lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('godandisplay1.html', entries=entries, search_name=search_name)

# Unique list of panta_peru
@app.route('/godannamelist1')
def godan_name_list():
    names = set()
    try:
        with open(GODAN_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.add(row['Panta Peru'].strip())
    except FileNotFoundError:
        pass
    return render_template('godannamelist1.html', names=sorted(names))

# User details for a specific crop
@app.route('/godanuserdetails1/<panta_peru>')
def godan_user_details(panta_peru):
    entries = []
    try:
        with open(GODAN_CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Panta Peru'].strip().lower() == panta_peru.strip().lower():
                    entries.append(row)
    except FileNotFoundError:
        pass
    return render_template('godanuserdetails1.html', panta_peru=panta_peru, entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
