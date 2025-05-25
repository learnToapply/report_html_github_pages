from datetime import datetime

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define HTML content with dynamic date
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic HTML Page</title>
</head>
<body>
    <h1>Daily Report</h1>
    <p>This page was generated on: <strong>{current_date}</strong></p>
</body>
</html>
"""

# Write HTML content to a file
with open("output.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file with dynamic date has been generated: output.html")
