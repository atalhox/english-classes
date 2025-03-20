import os

def create_structure(base_path="docs/verb-tenses"):
    structure = {
        "present": [
            "index.md",
            "simple-present.md",
            "present-continuous.md",
            "present-perfect.md",
            "present-perfect-continuous.md",
        ],
        "past": [
            "index.md",
            "simple-past.md",
            "past-continuous.md",
            "past-perfect.md",
            "past-perfect-continuous.md",
        ],
        "future": [
            "index.md",
            "simple-future.md",
            "future-continuous.md",
            "future-perfect.md",
            "future-perfect-continuous.md",
        ],
    }
    
    # Create base directory
    os.makedirs(base_path, exist_ok=True)
    
    for tense, files in structure.items():
        tense_path = os.path.join(base_path, tense)
        os.makedirs(tense_path, exist_ok=True)
        
        for file in files:
            file_path = os.path.join(tense_path, file)
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('-', ' ').replace('.md', '').title()}\n\n")
                f.write("(Content to be added)\n")
    
    print("Verb tenses documentation structure created successfully.")

if __name__ == "__main__":
    create_structure()
