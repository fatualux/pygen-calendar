from flask import Flask, render_template, request
import calendar
import os
from utils import linkify, add_notes, generate_css, italian_weekday_abbr
import webbrowser

app = Flask(__name__)

# Function to open browser on server startup
def startup_server(address, port):
    if os.name == 'nt':
        address = '127.0.0.1'
    webbrowser.open(f"http://{address}:{port}")


startup_server('0.0.0.0', 5000)

# Define Italian month names
italian_month_names = ['', 'Gennaio', 'Febbraio', 'Marzo', 'Aprile',
                        'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre',
                       'Ottobre', 'Novembre', 'Dicembre']

# Create HTML folder if it doesn't exist
html_folder = 'HTML'
if not os.path.exists(html_folder):
    os.makedirs(html_folder)


# Route to handle form submission and display result
@app.route('/generate_calendar', methods=['POST'])
def generate_calendar():
    # Get form data
    year = int(request.form['year'])
    month = int(request.form['month'])
    font_name = request.form['font_name']

    # Generate CSS file with the user-provided font name
    generate_css(font_name)

    # Create month calendar and add notes
    month_calendar = {day: [] for day in range(1, calendar.monthrange(year, month)[1] + 1)}
    month_calendar = add_notes(month_calendar)

    # Generate HTML content
    output = f'<!DOCTYPE html>\n<html>\n<head>\n<title>{italian_month_names[month]} {year}</title>\n'
    output += f'<link rel="stylesheet" type="text/css" href="{os.path.join("calendar_style.css")}">\n</head>\n<body>\n'

    # Generate table
    output += f'<table border="1">\n<tr><th colspan="7"><h1>{italian_month_names[month]} {year}</h1></th></tr>\n'

    raw_calendar = calendar.monthcalendar(year, month)

    for week in raw_calendar:
        output += '<tr>'
        for day in week:
            if day != 0:
                # Get the Italian weekday abbreviation
                weekday = italian_weekday_abbr[calendar.weekday(year, month, day)]
                # Check if there are notes for this day
                notes = '<br>'.join(['<span style="color: {}; font-weight: bold;">{}</span>'.format(color, note.replace("\\n", "<br>")) for note, color in month_calendar[day]])
                # Add styling to create a frame around the cells with notes
                if month_calendar[day]:
                    output += f'<td style="border-left: 3px solid {month_calendar[day][0][1]}; border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]};">{weekday}</td><td style="border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]};">{day}</td><td style="border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]}; border-right: 3px solid {month_calendar[day][0][1]};">{notes}</td>'
                else:
                    output += f'<td>{weekday}</td><td>{day}</td><td>{notes}</td>'
            else:
                output += '<td></td><td></td><td></td>'
        output += '</tr>\n'

    output += '</table>\n</body>\n</html>'

    # Save HTML file
    filename = os.path.join(html_folder, f"{year}-{month}.html")
    with open(filename, 'w') as f:
        f.write(output)

    # Render template with generated calendar content
    return render_template('pygencal_result.html', calendar_html=output)


@app.route('/')
def index():
    return render_template('pygencal_index.html')


if __name__ == '__main__':
    app.run(debug=True)
