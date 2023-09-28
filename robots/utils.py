from openpyxl.workbook import Workbook


def create_xlsx(file_path, data):
    wb = Workbook(file_path)
    for model, stats in data.items():
        wb_sheet = wb.create_sheet(model)
        wb_sheet.append(["Модель", "Версия", "Количество за неделю"])
        for stat in stats:
            wb_sheet.append([model, stat["version"], stat["total"]])
    wb.save(file_path)

    return wb
