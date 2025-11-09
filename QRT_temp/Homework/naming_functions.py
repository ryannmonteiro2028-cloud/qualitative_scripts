# naming_functions.py
from pathlib import Path
from slugify import slugify
from datetime import date

SECTION_MAP = {
    "data": "01_data",
    "analysis": "02_analysis",
    "literature": "03_literature",
    "writing": "04_writing",
    "outputs": "05_outputs",
    "admin": "0_admin",
}

SUBFOLDERS_MAP = {
    "data": ["0_raw", "01_processed", "02_reference"],
    "analysis": ["01_coding", "02_memos", "03_scripts"],
    "writing": ["01_drafts", "02_figures", "03_presentations"],
    "admin": ["budgets", "correspondence", "IRB", "proposals"],
    "literature": [],
    "outputs": [],
}

def create_folder_names(project_root, section, include_subfolders=True):
    if section not in SECTION_MAP:
        raise ValueError(f"Unknown section '{section}'. Choose from: {list(SECTION_MAP)}")
    project_root = Path(project_root)
    section_folder = project_root / SECTION_MAP[section]
    if not include_subfolders:
        return [str(section_folder)]
    subs = SUBFOLDERS_MAP.get(section, [])
    paths = [section_folder / s for s in subs] if subs else [section_folder]
    return [str(p) for p in paths]

def create_file_name(project_root, section, subfolder=None, base_name="notes",
                     ext=".txt", add_date=True, version=1):
    if section not in SECTION_MAP:
        raise ValueError(f"Unknown section '{section}'. Choose from: {list(SECTION_MAP)}")
    project_root = Path(project_root)
    section_folder = project_root / SECTION_MAP[section]
    if subfolder:
        known = set(SUBFOLDERS_MAP.get(section, []))
        if known and subfolder not in known:
            raise ValueError(f"Unknown subfolder '{subfolder}' for section '{section}'. "
                             f"Choose from: {sorted(known)}")
        target_dir = section_folder / subfolder
    else:
        target_dir = section_folder
    parts = []
    if add_date:
        parts.append(date.today().strftime("%Y%m%d"))
    parts.append(slugify(base_name))
    if version is not None:
        parts.append(f"v{version:02d}")
    filename = "_".join(parts) + ext
    return str(target_dir / filename)

if __name__ == "__main__":
    print(create_folder_names("Qual_Research_Template", "data", True))
    print(create_file_name("Qual_Research_Template", "analysis", "03_scripts",
                           base_name="thematic codebook", ext=".py"))
if __name__ == "__main__":
    print(create_folder_names("Qual_Research_Template", "data", True))
    print(create_file_name("Qual_Research_Template", "analysis", "03_scripts",
                           base_name="thematic codebook", ext=".py"))

    # --- NEW: Actually create the folders and file on disk ---
    from pathlib import Path

    # Create folders
    for folder in create_folder_names("Qual_Research_Template", "data", True):
        Path(folder).mkdir(parents=True, exist_ok=True)

    # Create the file (empty file for demo)
    file_path = create_file_name("Qual_Research_Template", "analysis", "03_scripts",
                                 base_name="thematic codebook", ext=".py")
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    Path(file_path).touch(exist_ok=True)
    print(f"\n✅ Created folders and file:\n{file_path}")

