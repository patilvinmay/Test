from openpyxl import load_workbook, Workbook
from copy import copy
from openpyxl.utils import get_column_letter


def copy_cell(source, target):
    target.value = source.value

    if source.has_style:
        target.font = copy(source.font)
        target.fill = copy(source.fill)
        target.border = copy(source.border)
        target.alignment = copy(source.alignment)
        target.number_format = source.number_format
        target.protection = copy(source.protection)


def process_excel(input_file, output_file):
    source_wb = load_workbook(input_file)
    output_wb = Workbook()

    output_ws = output_wb.active
    output_ws.title = "Combined Data"

    output_row = 1

    for ws in source_wb.worksheets:
        print(f"Processing {ws.title}")

        # Copy rows 5 to 100
        for r in range(5, 101):

            # Column A = Sheet name (Date)
            output_ws.cell(row=output_row, column=1).value = ws.title

            # Copy original columns starting from Column B
            for c in range(1, ws.max_column + 1):
                source_cell = ws.cell(row=r, column=c)
                target_cell = output_ws.cell(row=output_row, column=c + 1)
                copy_cell(source_cell, target_cell)

            # Preserve row height
            if r in ws.row_dimensions:
                output_ws.row_dimensions[output_row].height = ws.row_dimensions[r].height

            output_row += 1

    # Copy column widths from first sheet
    first_ws = source_wb.worksheets[0]
    output_ws.column_dimensions["A"].width = 15

    for c in range(1, first_ws.max_column + 1):
        src_letter = get_column_letter(c)
        dst_letter = get_column_letter(c + 1)
        output_ws.column_dimensions[dst_letter].width = first_ws.column_dimensions[src_letter].width

    output_wb.save(output_file)
    print("Done! Output saved to:", output_file)


# --------- File Paths ---------
input_file = r"C:\Users\YourName\Documents\DailyTasks.xlsx"
output_file = r"C:\Users\YourName\Documents\CombinedTasks.xlsx"

process_excel(input_file, output_file)
