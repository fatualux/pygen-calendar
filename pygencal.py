import calendar
from flask import Flask, render_template, request

app = Flask(__name__)


def linkify(year, month, day, style):
    return f'[{day}](#{year}{str(month).zfill(2)}{str(day).zfill(2)})'


def add_notes(month_calendar):
    while True:
        message = "Enter the day you want to add note (or 'exit' to finish): "
        date = input(message)
        if date.lower() == 'exit':
            break
        try:
            date = int(date)
            if 1 <= date <= 31:
                note = input("Enter note for this date (use '\\n' for new line): ")
                color = input("Enter color for this note: ")
                month_calendar[date].append((note, color))
                print(f"Note added for {date}.")
            else:
                message = "Invalid date. Please enter \
                           a valid day between 1 and 31."
                print(message)
        except ValueError:
            print("Invalid input. Please enter a valid day as a number.")
    return month_calendar


def generate_css(font_name):
    css_content = f'''
    @font-face {{
        font-family: '{font_name}';
        font-weight: normal;
        font-style: normal;
        font-display: swap;
    }}
    body {{
        background-color: #f2f2f2;
        font-family: '{font_name}', Arial, sans-serif;
    }}
    table {{
        width: 33%;
        border-collapse: collapse;
        border-left: none;
        border-right: none;
    }}
    th, td {{
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #000000;
        text-align: center;
        border-left: none;
        border-right: none;
        border-collapse: collapse;
    }}
    tr:hover {{
        background-color: #f5f5f5;
    }}
    '''
    with open("static/calendar_style.css", "w") as css_file:
        css_file.write(css_content)


@app.route('/')
def index():
    return render_template('pygencal_index.html')


@app.route('/generate_calendar', methods=['POST'])
def generate_calendar():
    font_name = request.form['font_name']
    year = int(request.form['year'])
    month = int(request.form['month'])

    month_calendar = {day: [] for day in range(1, calendar.monthrange(year, month)[1] + 1)}
    month_calendar = add_notes(month_calendar)

    output = f'<!DOCTYPE html>\n<html>\n<head>\n<title>{calendar.month_name[month]} {year}</title>\n'
    output += f'<link rel="stylesheet" type="text/css" href="{{ url_for(\'static\', filename=\'calendar_style.css\') }}">\n</head>\n<body>\n'

    output += f'<table border="1">\n<tr><th colspan="7"><h1>{calendar.month_name[month]} {year}</h1></th></tr>\n'

    raw_calendar = calendar.monthcalendar(year, month)

    for week in raw_calendar:
        output += '<tr>'
        for day in week:
            if day != 0:
                weekday = calendar.day_abbr[calendar.weekday(year, month, day)]
                notes = '<br>'.join(['<span style="color: {}; font-weight: bold;">{}</span>'.format(color, note.replace("\\n", "<br>")) for note, color in month_calendar[day]])
                if month_calendar[day]:
                    output += f'<td style="border-left: 3px solid {month_calendar[day][0][1]}; border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]};">{weekday}</td><td style="border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]};">{day}</td><td style="border-top: 3px solid {month_calendar[day][0][1]}; border-bottom: 3px solid {month_calendar[day][0][1]}; border-right: 3px solid {month_calendar[day][0][1]};">{notes}</td>'
                else:
                    output += f'<td>{weekday}</td><td>{day}</td><td>{notes}</td>'
            else:
                output += '<td></td><td></td><td></td>'
        output += '</tr>\n'

    output += '</table>\n</body>\n</html>'

    with open(f"templates/pygencal_result.html", 'w') as f:
        f.write(output)

    generate_css(font_name)

    return render_template('pygencal_result.html')


if __name__ == '__main__':
    app.run(debug=True)
