# PYGEN-CALENDAR (HTML Calendar Generator)

![](./demo/demo.gif)

This script generates an HTML calendar for a given month and year.
The name of months and days are in Italian.
Users can add notes to specific dates and customize thr appearance (font, color); an CSS file will be generated for styling the calendar.

## Usage

```
git clone https://gitlab.com/fatualux/pygen-calendar && cd pygen-calendar
```
1. **Run the Script**: Execute the script `html-calendar-generator.py`.
```
python pygen-calendar.py
```
2. **Enter Font Name**: Enter the name of the font family when prompted. This font will be used for the ientire calendar.
3. **Input Year and Month**: Provide the year and month for which you want to generate the calendar.
4. **Add Notes**: Optionally, add notes to specific dates by following the prompts; newlines are supported (with the escape character '\n').
5. **Output**: The script will generate an HTML file with the calendar and a corresponding CSS file for styling. (Note that the font file/s must be in the same directory as the script.)

## Dependencies

This script requires Python 3.x and the `calendar` module.

## LICENSE

[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

This project is licensed under the GPLv3 license.
See LICENSE file for more details.
