from pathlib import Path

MAX_FILE_SIZE_MB = 10

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".txt"
}


def validate_file(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise ValueError("File does not exist.")

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    size_mb = path.stat().st_size / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(
            f"File exceeds {MAX_FILE_SIZE_MB} MB."
        )

    return True


BLOCKED_PHRASES = [
    "ignore previous instructions",
    "reveal system prompt",
    "show api key",
    "print environment variables",
    "bypass security",
]


def validate_prompt(prompt: str):
    prompt_lower = prompt.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in prompt_lower:
            raise ValueError(
                "Unsafe prompt detected."
            )

    return True