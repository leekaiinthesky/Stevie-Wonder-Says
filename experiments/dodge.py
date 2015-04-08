import PIL.Image as Image
import PIL.ImageFilter as ImageFilter
import PIL.ImageOps as ImageOps
import PIL.ImageDraw as ImageDraw

def dodge(a, b, alpha):
    return min(int(a*255/(256-b*alpha)), 255)
def drawing(infile, outfile, blur=10, alpha=0.9):
    im1 = Image.open(infile).convert("L")
    print 'hi'
    im2 = im1.copy()
    im2 = ImageOps.invert(im2)
    print 'hi'
    for i in range(blur):
        im2 = im2.filter(ImageFilter.BLUR)
    print 'hi'
    width, height = im1.size
    for x in range(width):
        for y in range(height):
            a = im1.getpixel((x, y))
            b = im2.getpixel((x, y))
            im1.putpixel((x, y), dodge(a, b, alpha))
    im1.save(outfile)

drawing('images/stevie-wonder-at-the-wave.jpg', 'images/dodge10-point9.jpg')