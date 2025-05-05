from meme.captions import get_random_caption
from meme.images import get_random_image_url

def generate_meme():
    caption = get_random_caption()
    image_url = get_random_image_url()
    return {"caption": caption, "image_url": image_url}