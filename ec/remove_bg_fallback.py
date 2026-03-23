import os
import django
import sys
from PIL import Image

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ec.settings")
django.setup()

from app.models import Product

for product in Product.objects.all():
    if not product.product_image:
        continue
    
    img_path = product.product_image.path
    if not os.path.exists(img_path):
        continue
        
    if img_path.lower().endswith(".png"):
        print(f"Skipped {product.title}, already png")
        continue
        
    try:
        img = Image.open(img_path).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            if item[0] > 235 and item[1] > 235 and item[2] > 235:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
                
        img.putdata(newData)
        
        base, _ = os.path.splitext(img_path)
        new_path = base + ".png"
        img.save(new_path, "PNG")
        
        new_name = "product/" + os.path.basename(new_path)
        product.product_image.name = new_name
        product.save()
        print(f"Fallback processed {product.title} -> {new_name}")
    except Exception as e:
        print(f"Error processing {product.title}: {e}")
