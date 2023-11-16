## Overview

This Go program opens a CSV file ("products.csv") containing product data. It reads through each row of the CSV, extracts the image URL and product name, and then proceeds to download the associated image file. The downloaded images are saved in a local "assets" directory.

## Functionality

- **CSV Processing**: Reads the CSV file to extract image URLs and product names.
- **Image Download**: Downloads images specified by the URLs and saves them locally in the "assets" directory.
- **Logging**: Records download activity and errors in a "download_log.txt" file.

## Usage

1. **CSV File**: Ensure the CSV file ("products.csv") contains the necessary columns, including the image URL and product name.
2. **Execution**: Run the program using Go (`go run main.go`) to start the image download process.
3. **Logs**: Check the "download_log.txt" file for activity logs and any encountered errors.

## Notes

- Ensure the CSV file structure matches the program's expectations, with URLs in a specific column (index 2) and product names in another (index 1).