import xlsxwriter
def wexcel(path, data):
    #new_list = [['first', 'second'], ['third', 'four'], [1, [2,3], 3, 4, 5, 6]]


    with xlsxwriter.Workbook(path) as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                if isinstance(col_data, list):
                    newcol_data=(",".join(str(elem) for elem in col_data))

                    worksheet.write(row_num, col_num, newcol_data)

                else:
                    worksheet.write(row_num, col_num, col_data)

