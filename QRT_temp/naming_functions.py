# week6_naming_functions.py
# My naming convention: Qual_Research_Template

from datetime import date
from slugify import slugify  # external package

# 1️ Function to create folder names
def create_folder_names(section):
    """
    Return folder names consistent with my Qual_Research_Template system.
    """
    subfolders = {
        "data": ["0_raw", "01_processed", "02_reference"],
        "analysis": ["01_coding", "02_memos", "03_scripts"],
        "literature": [],
        "writing": ["01_drafts", "02_figures", "03_presentations"],
        "outputs": [],
        "admin": ["budgets", "correspondence", "IRB", "proposals"]
    }
    return subfolders.get(section.lower(), [])

# 2️ Function to create file names
def create_file_name(section, name, version=1, ext=".txt"):
    """
    Return a standardized file name for the given section and file type.
    """
    sections = {
        "data": "01_data",
        "analysis": "02_analysis",
        "literature": "03_literature",
        "writing": "04_writing",
        "outputs": "05_outputs",
        "admin": "0_admin"
    }
    today = date.today().strftime("%Y%m%d")
    section_name = sections.get(section.lower(), "misc")
    file_name = f"{section_name}_{today}_{slugify(name)}_v{version:02d}{ext}"
    return file_name

# --- Demo for screen capture ---
if __name__ == "__main__":
    print("Folder names for 'analysis':", create_folder_names("analysis"))
    print("Example file name:", create_file_name("analysis", "thematic codebook", 1, ".py"))

