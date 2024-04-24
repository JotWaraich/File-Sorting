import os
import shutil
import customtkinter

# used custontkinter for the GUI

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

audio_formats = [
    ".mp3",  # MPEG Layer 3 Audio
    ".wav",  # Waveform Audio File Format
    ".aac",  # Advanced Audio Coding
    ".ogg",  # Ogg Vorbis
    ".flac", # Free Lossless Audio Codec
    ".alac", # Apple Lossless Audio Codec
    ".wma",  # Windows Media Audio
    ".ape",  # Monkey's Audio
    ".m4a",  # MPEG-4 Audio
    ".mp2",  # MPEG Layer 2 Audio
    ".amr",  # Adaptive Multi-Rate Audio Codec
    ".mid",  # MIDI
    ".midi", # MIDI
    ".dts",  # Digital Theater Systems
    ".ac3",  # Audio Codec 3
    ".opus", # Opus
    ".aiff", # Audio Interchange File Format
    ".aif"   # Audio Interchange File Format
]

video_formats = [
    ".mp4",  # MPEG-4 Part 14
    ".avi",  # Audio Video Interleave
    ".mov",  # Apple QuickTime Movie
    ".wmv",  # Windows Media Video
    ".flv",  # Flash Video
    ".mkv",  # Matroska Video
    ".webm", # WebM
    ".m4v",  # MPEG-4 Video
    ".mpg",  # MPEG-1 or MPEG-2
    ".mpeg", # MPEG
    ".3gp",  # 3GPP
    ".vob",  # DVD Video Object
    ".ts",   # MPEG Transport Stream
    ".m2ts", # MPEG Transport Stream
    ".rmvb", # RealMedia Variable Bitrate
    ".ogv",  # Ogg Video
    ".asf",  # Advanced Systems Format
    ".divx"  # DivX
]

image_formats = [
    ".jpg",  # JPEG
    ".jpeg", # JPEG
    ".png",  # Portable Network Graphics
    ".gif",  # Graphics Interchange Format
    ".bmp",  # Bitmap
    ".tiff", # Tagged Image File Format
    ".tif",  # Tagged Image File Format
    ".webp", # WebP
    ".raw",  # RAW Image Formats
    ".heif", # High Efficiency Image File Format
    ".heic", # High Efficiency Image Codec
    ".ico",  # Icon Format
    ".svg",  # Scalable Vector Graphics
    ".psd",  # Adobe Photoshop Document
    ".ai",   # Adobe Illustrator Document
    ".eps",  # Encapsulated PostScript
    ".pdf"   # Portable Document Format
]

document_formats = [
    ".doc",   # Microsoft Word Document
    ".docx",  # Microsoft Word Open XML Document
    ".pdf",   # Portable Document Format
    ".txt",   # Plain Text File
    ".rtf",   # Rich Text Format
    ".odt",   # OpenDocument Text Document
    ".html",  # HyperText Markup Language
    ".htm",   # HyperText Markup Language
    ".xls",   # Microsoft Excel Spreadsheet
    ".xlsx",  # Microsoft Excel Open XML Spreadsheet
    ".ppt",   # Microsoft PowerPoint Presentation
    ".pptx",  # Microsoft PowerPoint Open XML Presentation
    ".csv",   # Comma-Separated Values
    ".epub",  # Electronic Publication
    ".md",    # Markdown Documentation
    ".tex",   # LaTeX Source Document
    ".log",   # Log File
    ".xml",   # Extensible Markup Language
    ".json"   # JavaScript Object Notation
]

installer_formats = [
    ".exe",  # Executable File for Windows
    ".msi",  # Microsoft Installer Package for Windows
    ".bat",  # Batch File for Windows
    ".cmd",  # Command Script for Windows
    ".app",  # Application for macOS
    ".pkg",  # Package Installer for macOS
    ".dmg",  # Apple Disk Image for macOS
    ".sh",   # Shell Script for Unix/Linux
    ".deb",  # Debian Software Package for Debian-based Linux distributions
    ".rpm",  # Red Hat Package Manager for Fedora/RHEL-based Linux distributions
    ".run",  # Generic installer script for Unix/Linux
    ".tar.gz", # Tarball compressed with gzip for Unix/Linux
    ".bin",  # Binary installer for Unix/Linux
    ".apk",  # Android Package for Android
    ".ipa"   # iOS App Store Package for iOS
]

compression_formats = [
    ".zip",  # ZIP Archive
    ".rar",  # RAR Archive
    ".7z",   # 7-Zip Archive
    ".tar",  # Tar Archive (uncompressed)
    ".gz",   # GZIP Compressed File
    ".bz2",  # BZIP2 Compressed File
    ".xz",   # XZ Compressed File
    ".tar.gz", # Tar Archive compressed with GZIP
    ".tar.bz2", # Tar Archive compressed with BZIP2
    ".tar.xz",  # Tar Archive compressed with XZ
    ".iso",  # ISO Disk Image
    ".lz",   # LZIP Compressed File
    ".lzma", # LZMA Compressed File
    ".z",    # Compress (UNIX compress)
    ".cab"   # Cabinet File
]

database_formats = [
    ".db",   # Generic database file
    ".dbf",  # dBASE database
    ".mdb",  # Microsoft Access database (older format)
    ".accdb", # Microsoft Access database (newer format)
    ".sql",  # SQL dump file containing SQL commands
    ".sqlite", # SQLite database file
    ".sqlite3", # SQLite3 database file
    ".fdb",  # Firebird database
    ".gdb",  # Interbase/Firebird database
    ".mde",  # Compiled Microsoft Access database
    ".accde", # Compiled Microsoft Access database (newer format)
    ".ora",  # Oracle database file
    ".myd",  # MySQL MyISAM table data
    ".myi",  # MySQL MyISAM table index
    ".ibd",  # InnoDB database file
    ".frm",  # MySQL table definition file
    ".ndf",  # SQL Server secondary data file
    ".ldf",  # SQL Server transaction log file
    ".mdf"   # SQL Server primary data file
]

root = customtkinter.CTk()
root.title("File Organiser")
root.geometry("500x350")

def close_window(window):
    window.destroy()


def open_new_window(lable_text):
    new_window = customtkinter.CTk()
    new_window.title("Alert")
    new_window.geometry("300x150")
    new_frane = customtkinter.CTkFrame(master=new_window)
    new_frane.pack(pady=20, padx=60, fill="both", expand=True)
    lable = customtkinter.CTkLabel(master=new_frane, text=lable_text)
    lable.pack(pady=20, padx=10)
    button = customtkinter.CTkButton(master=new_frane, text="Okay", command=lambda: new_window.destroy())
    button.pack(pady=12, padx=10)
    new_window.mainloop()

def FileManage(path):
    try:
        files = os.listdir(path)
        for file in files:
            filename, file_extention = os.path.splitext(file)
            file_extention  = file_extention[1:]
            file_extention = "." + file_extention
            if file_extention in audio_formats:
                file_extention = "Audio"
            elif file_extention in video_formats:
                file_extention = "Video"
            elif file_extention in image_formats:
                file_extention = "Image"
            elif file_extention in document_formats:
                file_extention = "Document"
            elif file_extention in installer_formats:
                file_extention = "Installer"
            elif file_extention in compression_formats:
                file_extention = "Compressed"
            elif file_extention in database_formats:
                file_extention = "Database"

            if os.path.exists(path+"/"+file_extention):
                shutil.move(path+"/"+file, path+"/"+file_extention+"/"+file)
            else:
                os.makedirs(path+"/"+file_extention)
                shutil.move(path+"/"+file, path+"/"+file_extention+"/"+file)
        open_new_window("Files have been sorted successfully")
    except Exception as e:
        open_new_window("Please provide a valid path")

frane = customtkinter.CTkFrame(master=root)
frane.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frane, text="Enter the path of the directory to be sorted: ")
lable.pack(pady=20, padx=10)
lable.configure(font=("Arial", 18))

path_entry = customtkinter.CTkEntry(master=frane, placeholder_text="Enter the path of the directory to be sorted")
path_entry.pack(pady=20, padx=10)
path_entry.configure(width=300, height=30, font=("Arial", 14))

button = customtkinter.CTkButton(master=frane, text="Sort", command=lambda: FileManage(path_entry.get()))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frane, text="Close", command=lambda: close_window(root))
button.pack(pady=12, padx=10)

root.mainloop()