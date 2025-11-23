from openpyxl import Workbook

# Step 1: Create workbook and add data
wb = Workbook()
ws = wb.active
ws.append(["Item", "Price"])
ws.append(["Apple", 1.00])
ws.append(["Banana", 0.50])

# Step 2: Update prices
for row in ws.iter_rows(min_row=2, max_col=2):
    row[1].value *= 1.1  # Increase prices by 10%

# Save workbook
wb.save("prices.xlsx")