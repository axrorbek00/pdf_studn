from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
from helpers import get_data
from reportlab.lib.utils import ImageReader

# Example data
# data = [
#     {"fullname": "John Doe", "group": "Group A", "is_present": True},
#     {"fullname": "Jane Smith", "group": "Group B", "is_present": False},
#     Add more data here...
# ]
data = get_data(1, "2023-10-15")
print(data)


def generate_pdf(data):
    # Create a new PDF document
    doc = SimpleDocTemplate("outputtest.pdf", pagesize=letter)

    # Define the table data
    table_data = [
                     ['Full Name', 'Group', 'Is Present']
                 ] + [
                     [row['fullname'], row['group'], 'Present' if row['is_present'] else 'Absent']
                     for row in data
                 ]

    # Create the table and set its style
    table = Table(table_data, colWidths=[150, 150, 150])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Load the logo image
    logo = Image("logo.png", width=100, height=100)

    # Build the PDF document content
    content = []
    content.append(logo)
    content.append(table)

    # Add the content to the PDF document
    doc.build(content)


# Generate the PDF
generate_pdf(data)
