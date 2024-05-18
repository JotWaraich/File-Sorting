# File Organizer App

Welcome to the File Organizer App! This application helps you keep your directories clean and organized by sorting files into appropriate folders based on their file types.

## Features

- **Automatic File Organization**: Automatically sorts files into folders based on their extensions.
- **Common File Types Categorization**: For common file types, files are organized into folders with simple names like `Audio`, `Video`, `Image`, etc.
- **Custom Extensions Handling**: Supports organizing files into folders named after their extensions for uncommon file types.

## Release Notes

### Latest Release

**Version 1.1.0**

- **Enhanced Folder Naming**: Previously, files were placed in folders named after their extensions. Now, for common file types, folders have simple names like `Audio`, `Video`, `Image`, etc.
- **Improved User Interface**: Minor UI improvements for better user experience.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/file-organizer-app.git
   cd file-organizer-app
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```sh
   python organize_files.py /path/to/your/directory
   ```

2. The application will scan the specified directory and organize files into appropriate folders.

### Example

Before:
