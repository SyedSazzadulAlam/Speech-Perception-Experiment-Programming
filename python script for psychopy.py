import os
from random import shuffle

PICTURE_FOLDER = "Stimuli"
EXPECTED_PICTURES = 12

picture_files = [
    os.path.join(PICTURE_FOLDER, filename)
    for filename in os.listdir(PICTURE_FOLDER)
    if filename.lower().endswith((".png", ".jpg", ".jpeg"))
]

if len(picture_files) != EXPECTED_PICTURES:
    raise ValueError(
        f"Expected {EXPECTED_PICTURES} production pictures, "
        f"but found {len(picture_files)}."
    )

shuffle(picture_files)

picture_number = 0

print(f"Production pictures loaded: {len(picture_files)}")
print("Randomized order:")
for filepath in picture_files:
    print(filepath)
