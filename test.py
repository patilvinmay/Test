from openpyxl import load_workbook, Workbook
from copy import copy


def is_orange(cell):
    """
    Detect an orange-filled cell.

    This checks the RGB value of the cell's fill and allows
    for different shades of orange.
    """

    fill = cell.fill

    if fill.fill_type != "solid":
        return False

    color = fill.fgColor

    # Direct RGB color
    if color.type == "rgb" and color.rgb:
        rgb = color.rgb[-6:]  # remove possible alpha prefix

        try:
            r = int(rgb[0:2], 16)
            g = int(rgb[2:4], 16)
            b = int(rgb[4:6], 16)

            # Orange generally has:
            # High red, medium green, relatively low blue
            return (
                r >= 180
                and 70 <= g <= 220
                and b <= 150
                and r > g + 30
                and g > b
            )

        except ValueError:
            return False

    return False


def find_orange_row(ws):
    """
    Find the first row containing an orange cell.
    Returns None if no orange cell is found.
    """

    for row in ws.iter_rows():
        for cell in row:
            if is_orange(cell):
                return cell.row

    return None


def copy_cell(source_cell, target_cell):
    """
    Copy value and formatting from one cell to another.
    """

    target_cell.value = source_cell.value

    if source_cell.has_style:
        target_cell.font = copy(source_cell.font)
        target_cell.fill = copy(source_cell.fill)
        target_cell.border = copy(source_cell.border)
        target_cell.alignment = copy(source_cell.alignment)
        target_cell.number_format = source_cell.number_format
        target_cell.protection = copy(source_cell.protection)


def copy_row(ws_source, ws_target, source_row, target_row):
    """
    Copy an entire row including formatting.
    """

    for col in range(1, ws_source.max_column + 1):

        source_cell = ws_source.cell(
            row=source_row,
            column=col
        )

        target_cell = ws_target.cell(
            row=target_row,
            column=col
        )

        copy_cell(source_cell, target_cell)

    # Preserve row height
    if source_row in ws_source.row_dimensions:
        ws_target.row_dimensions[target_row].height = \
            ws_source.row_dimensions[source_row].height


def process_excel(input_file, output_file):

    # Open source workbook
    source_wb = load_workbook(input_file)

    # Create output workbook
    output_wb = Workbook()

    # Use only one sheet
    output_ws = output_wb.active
    output_ws.title = "Combined Data"

    output_row = 1

    for ws in source_wb.worksheets:

        print(f"Processing sheet: {ws.title}")

        # Find orange cell row
        orange_row = find_orange_row(ws)

        if orange_row is None:
            print(f"  No orange cell found - skipped")
            continue

        print(f"  Orange cell found at row: {orange_row}")

        # Copy everything ABOVE the orange row
        for source_row in range(1, orange_row):

            copy_row(
                ws,
                output_ws,
                source_row,
                output_row
            )

            output_row += 1

        print(f"  Copied rows 1 to {orange_row - 1}")

    # Copy column widths from the first source sheet
    if source_wb.worksheets:
        first_ws = source_wb.worksheets[0]

        for col_letter, dimension in first_ws.column_dimensions.items():
            output_ws.column_dimensions[col_letter].width = dimension.width

    # Save output
    output_wb.save(output_file)

    print()
    print("Done!")
    print(f"Output file: {output_file}")


# ---------------------------------------------------
# CHANGE THESE TWO PATHS
# ---------------------------------------------------

input_file = r"C:\Users\YourName\Documents\DailyTasks.xlsx"
output_file = r"C:\Users\YourName\Documents\CombinedTasks.xlsx"


process_excel(input_file, output_file)
