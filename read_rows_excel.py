import openpyxl

def read_last_x_rows(file_path, x):
    # Load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Determine the total number of rows in the sheet
    total_rows = sheet.max_row

    # Calculate the starting row
    start_row = max(1, total_rows - x + 1)

    # Extract data from the last x rows
    data = []
    for row_num in range(start_row, total_rows + 1):
        row_data = [cell.value for cell in sheet[row_num]]
        data.append(row_data)

    return data

file_path = "sample_file.xlsx"
x = 3  # For example, to read the last 3 rows
last_x_rows = read_last_x_rows(file_path, x)

for row in last_x_rows:
    print(row)
