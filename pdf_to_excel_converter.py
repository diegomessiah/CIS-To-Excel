import pandas as pd
import pdfplumber

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Extract table data ignoring non-table content
        table_data = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                table_data.append(table)
    return table_data

def save_to_excel(data, excel_path):
    # Flatten the list of tables and save to an Excel file
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)

if __name__ == "__main__":
    pdf_file = 'input.pdf'  # Change this to your PDF file path
    output_excel = 'output.xlsx'  # Desired output path
    table_data = extract_table_from_pdf(pdf_file)
    save_to_excel(table_data, output_excel)