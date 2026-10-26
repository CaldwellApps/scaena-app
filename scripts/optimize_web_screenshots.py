import os
from PIL import Image

def optimize_image(src_path, out_path_webp, out_path_png, target_height):
    im = Image.open(src_path)
    aspect = im.width / im.height
    new_height = target_height
    new_width = int(new_height * aspect)
    
    resized = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    os.makedirs(os.path.dirname(out_path_webp), exist_ok=True)
    resized.save(out_path_webp, format='WEBP', quality=90, method=6)
    resized.save(out_path_png, format='PNG', optimize=True)
    
    webp_kb = os.path.getsize(out_path_webp) / 1024
    png_kb = os.path.getsize(out_path_png) / 1024
    print(f"Optimized: {os.path.basename(out_path_webp)} ({new_width}x{new_height}) -> WebP: {webp_kb:.1f} KB, PNG: {png_kb:.1f} KB")

def main():
    print("=== Optimizing Web Screenshots (Retina 2x) ===")
    
    # 1. iPhone 18 Pro (Height: 1100px for 2x Retina sharpness)
    iphone_src = "Screenshots/1.5.1/AppStoreBanners/iphone_6.3inch"
    iphone_tasks = [
        ("01_home.png", "home"),
        ("02_watchlist_hero.png", "watchlist"),
        ("03_show_detail.png", "show_detail"),
        ("04_movie_detail.png", "movie_detail"),
        ("05_calendar.png", "calendar"),
        ("07_custom_lists_detail.png", "custom_lists"),
        ("09_themes.png", "themes"),
        ("10_widgets.png", "widgets"),
    ]
    for src_file, name in iphone_tasks:
        src = os.path.join(iphone_src, src_file)
        webp = f"docs/screenshots/iphone/{name}.webp"
        png = f"docs/screenshots/iphone/{name}.png"
        optimize_image(src, webp, png, target_height=1100)
        
    # 2. iPad Pro 13" (Height: 1100px for 2x Retina sharpness)
    ipad_src = "Screenshots/1.5.1/AppStoreBanners/ipad_13inch"
    ipad_tasks = [
        ("01_home.png", "home"),
        ("02_watchlist_hero.png", "watchlist"),
        ("03_show_detail.png", "show_detail"),
        ("04_movie_detail.png", "movie_detail"),
        ("04_calendar.png", "calendar"),
        ("07_custom_lists_detail.png", "custom_lists"),
        ("08_themes.png", "themes"),
    ]
    for src_file, name in ipad_tasks:
        src = os.path.join(ipad_src, src_file)
        webp = f"docs/screenshots/ipad/{name}.webp"
        png = f"docs/screenshots/ipad/{name}.png"
        optimize_image(src, webp, png, target_height=1100)
        
    # 3. iPhone Duo
    duo_inner_src = "Screenshots/1.5.3/AppStoreBanners/iphoneduo_inner_landscape"
    duo_outer_src = "Screenshots/1.5.3/AppStoreBanners/iphoneduo_outer_portrait"
    duo_tasks = [
        (os.path.join(duo_inner_src, "01_home.png"), "inner_home", 950),
        (os.path.join(duo_inner_src, "02_watchlist_hero.png"), "inner_watchlist", 950),
        (os.path.join(duo_inner_src, "03_show_detail.png"), "inner_show_detail", 950),
        (os.path.join(duo_inner_src, "05_calendar.png"), "inner_calendar", 950),
        (os.path.join(duo_outer_src, "01_home_outer.png"), "outer_home", 1100),
        (os.path.join(duo_outer_src, "02_watchlist_hero_outer.png"), "outer_watchlist", 1100),
    ]
    for src, name, h in duo_tasks:
        webp = f"docs/screenshots/duo/{name}.webp"
        png = f"docs/screenshots/duo/{name}.png"
        optimize_image(src, webp, png, target_height=h)

    print("=== All Web Screenshots Optimized Successfully (Retina 2x) ===")

if __name__ == "__main__":
    main()
