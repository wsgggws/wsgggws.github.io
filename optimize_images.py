import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

# Configuration
CONTENT_DIR = "content/blogs"
# Ensure output dir exists
OUTPUT_DIR = "static/images/covers"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

FONT_PATH = "/System/Library/Fonts/PingFang.ttc"  # macOS Standard Chinese Font
IMAGE_WIDTH = 900
IMAGE_HEIGHT = 500


def get_color_from_string(s):
    """Generate a consistent pastel color from a string."""
    hash_object = hashlib.md5(s.encode())
    hash_hex = hash_object.hexdigest()

    # Use parts of the hash to generate RGB values
    r = int(hash_hex[0:2], 16)
    g = int(hash_hex[2:4], 16)
    b = int(hash_hex[4:6], 16)

    # Mix with white to make it pastel
    r = (r + 255) // 2
    g = (g + 255) // 2
    b = (b + 255) // 2

    return (r, g, b)


def create_cover_image(title, filename):
    # Check if image already exists
    image_filename = filename.replace('.md', '.webp')
    save_path = os.path.join(OUTPUT_DIR, image_filename)
    
    if os.path.exists(save_path):
        return f"/images/covers/{image_filename}"

    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color=get_color_from_string(title))
    d = ImageDraw.Draw(img)

    # Font setup
    try:
        font = ImageFont.truetype(FONT_PATH, 60)
    except OSError:
        font = ImageFont.load_default()
        print(f"Warning: Could not load {FONT_PATH}, using default font.")

    # Text wrapping (simple)
    max_char_per_line = 15
    import textwrap

    lines = []
    if len(title) > max_char_per_line:
        lines = textwrap.wrap(title, width=max_char_per_line)
    else:
        lines = [title]

    # Calculate text position
    total_height = 0
    line_heights = []
    for line in lines:
        try:
            # Pillow >= 10.0.0 uses textbbox
            bbox = d.textbbox((0, 0), line, font=font)
            h = bbox[3] - bbox[1]
        except AttributeError:
            # Older Pillow
            w, h = d.textsize(line, font=font)

        line_heights.append(h + 20)
        total_height += h + 20

    current_y = (IMAGE_HEIGHT - total_height) / 2

    for i, line in enumerate(lines):
        try:
            bbox = d.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
        except AttributeError:
            w, h = d.textsize(line, font=font)

        x = (IMAGE_WIDTH - w) / 2

        # Shadow
        shadow_offset = 2
        d.text((x + shadow_offset, current_y + shadow_offset), line, font=font, fill=(50, 50, 50))
        # Main text
        d.text((x, current_y), line, font=font, fill=(255, 255, 255))

        current_y += line_heights[i]

    # Save as WebP
    image_filename = filename.replace(".md", ".webp")
    save_path = os.path.join(OUTPUT_DIR, image_filename)

    # Clean up old png if exists
    old_png = save_path.replace(".webp", ".png")
    if os.path.exists(old_png):
        try:
            os.remove(old_png)
            pass
        except OSError:
            pass

    img.save(save_path, "WEBP", quality=85)
    return f"/images/covers/{image_filename}"


def update_markdown_file(filepath):
    with open(filepath) as f:
        content = f.read()

    sep = ""
    if content.startswith("+++"):
        sep = "+++"
    elif content.startswith("---"):
        sep = "---"
    else:
        return

    parts = content.split(sep)
    if len(parts) < 3:
        return

    frontmatter = parts[1]
    body = parts[2]

    lines = frontmatter.strip().split("\n")
    new_lines = []
    title = ""

    for line in lines:
        if line.strip().startswith("image"):
            continue
        if line.strip().startswith("title"):
            if "=" in line:
                title = line.split("=")[1].strip().strip('"')
            elif ":" in line:
                title = line.split(":")[1].strip().strip('"')
        new_lines.append(line)

    if not title:
        return

    # Generate WebP Image
    filename = os.path.basename(filepath)
    image_url = create_cover_image(title, filename)
    print(f"Generated WebP cover for '{title}': {image_url}")

    # Add new image key
    if sep == "+++":
        new_lines.append(f'image = "{image_url}"')
    else:
        new_lines.append(f'image: "{image_url}"')

    new_frontmatter = "\n".join(new_lines) + "\n"
    new_content = sep + "\n" + new_frontmatter + sep + body

    with open(filepath, "w") as f:
        f.write(new_content)


for filename in os.listdir(CONTENT_DIR):
    if filename.endswith(".md"):
        update_markdown_file(os.path.join(CONTENT_DIR, filename))
