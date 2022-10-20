import xlrd
#Open the Excel File
loc = ("iplogs.xlsx")
xfile = xlrd.open_workbook(loc)
xfile.sheet_by_index(2)
sheet = xfile.sheet_by_index(0)

# print number of rows
print("There are %i rows" % sheet.nrows)
#Array Initilize
duplicates = []
ip_Addresses = []
#check all rows
for i in range(sheet.nrows):
    # get value of current column.
        value = sheet.cell_value(i, 0)
        #check if value already exists in
if value in ip_Addresses:
    ip_Addresses.append(sheet.cell_value(i, 0))
else:
    ip_Addresses.append(sheet.cell_value(i, 0))
    print(duplicates)
