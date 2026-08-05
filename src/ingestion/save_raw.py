# Raw JSON ingestion functionality will be implemented in Phase 2.3.

import json  # Used to convert Python dictionaries into JSON files

from pathlib import Path  # Used for platform-independent file paths

from datetime import datetime  # Used to generate timestamps


def save_raw_json(data, entity, file_name):  # Save raw API response as a JSON file

    directory = Path("data") / "raw" / "json" / entity  # Build the destination folder path

    directory.mkdir(parents=True, exist_ok=True)  # Create folders if they don't exist

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Generate timestamp

    file_path = directory / f"{file_name}_{timestamp}.json"  # Build the file name

    with open(file_path, "w", encoding="utf-8") as file:  # Open the file for writing

        json.dump(  # Write Python dictionary as formatted JSON
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved Successfully → {file_path}")  # Display saved location

    return file_path  # Return the saved file path