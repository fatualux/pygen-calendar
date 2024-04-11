import calendar

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

    with open("calendar_style.css", "w") as css_file:
        css_file.write(css_content)
    print("CSS file generated: calendar_style.css")
    try:
        with open("static/calendar_style.css", "w") as css_file:
            css_file.write(css_content)
        print("CSS file generated: static/calendar_style.css")
    except Exception as e:
        print(f"Error occurred while generating CSS file: {e}")

italian_weekday_abbr = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
