# PYGEN-CALENDAR (HTML Calendar Generator)

![](./demo/demo.gif)

This script generates an HTML calendar for a given month and year. </br>
This is the webapp version, made with Flask.
The names of months and days are in Italian. <br/>
Users can add notes to specific dates and customize thr appearance (font, color); a CSS file will be generated for styling the calendar.

## Usage

```
git clone https://gitlab.com/fatualux/pygen-calendar && cd pygen-calendar
```
1. **Run the Script**:
```
python pygen-calendar.py
```

2. Open your browser and go to the address:port specified in the shell.

3. Insert year, month and font family name in the specified fields, and click/tap "Generate Calendar".
4. In the shell, you will be prompted to insert the day, the note and the color.
5. When you are done with inserting data, type "exit" and hit enter, and you will be redirected to the generated calendar.

## Dependencies

This script requires Python 3.x, Flask and the `calendar` module.

## Notes

Font files must be placed in the ***static*** directory.

## LICENSE

[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

This project is licensed under the GPLv3 license.
See LICENSE file for more details.
