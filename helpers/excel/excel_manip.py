import openpyxl as xl
import pandas as pd
import os


def get_headers(df: pd.DataFrame) -> list[str]:
    return df.columns.to_list()


class ExcelManip:
    def __init__(self, files_dir: str) -> None:
        self.files_dir: str = files_dir

    def pull_all_excel_files(self) -> list[str]:
        """
        Pulls all Excel files from the __init__ specified directory.
        :return: list of all Excel files
        """
        result: list = []
        for root, dirs, files in os.walk(self.files_dir):
            structure = {
                'directory': root,
                'subdirectories': [],
                'files': files
            }
            for directory in dirs:
                structure['subdirectories'].append(directory)
            result.append(structure)
        return result

    def pull_sheet_names(self, filename: str) -> list[str]:
        """
        Pulls all Sheet names from an Excel file.
        :param filename: name of file (including extension)
        :return: list of all Sheet names
        """
        wb = xl.load_workbook(f"{self.files_dir}/{filename}")
        return wb.sheetnames

    def convert_sheet_to_df(self, sheet_name: str, workbook: str) -> pd.DataFrame:
        df = pd.read_excel(
            f"{self.files_dir}/{workbook}",
            sheet_name=sheet_name,
        )
        return df

