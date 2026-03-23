import os
import django
import sys

# Set up Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ec.settings")
django.setup()

from app.models import Product
from PIL import Image

try:
    from rembg import remove
    USE_REMBG = True
except ImportError:
    print("rembg not installed. We will install it.")
    sys.exit(1)

for product in Product.objects.all():
    if not product.product_image:
         continue
         
    img_path = product.product_image.path
    if not os.path.exists(img_path):
        continue
        
    if img_path.lower().endswith(".png"):
        print(f"Skipping {product.title}, already PNG.")
        continue
         
    try:
        input_img = Image.open(img_path)
        output_img = remove(input_img)
        
        base, _ = os.path.splitext(img_path)
        new_path = base + ".png"
        output_img.save(new_path, "PNG")
        
        new_name = "product/" + os.path.basename(new_path)
        product.product_image.name = new_name
        product.save()
        print(f"Successfully processed {product.title} -> {new_name}")
    except Exception as e:
        print(f"Error processing {product.title}: {e}")
