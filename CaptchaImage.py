def RandomCharSet(charCount=4):
    import Definitions
    import random as rand

    charChoices = []

    for i in range(charCount):
        charChoices.append(str(rand.choice(Definitions.charSet)))

    return charChoices




def GetCaptchaTextAndImage(charCount=4):
    from captcha.image import ImageCaptcha
    import numpy as np
    from PIL import Image

    captcha = ImageCaptcha()
    charSet = RandomCharSet(charCount)
    image = captcha.generate(charSet)
    image = Image.open(image)
    image = np.array(image)

    return charSet, image


def TestCaptchaImage():
    from PIL import Image
    from matplotlib.pyplot import imshow
    text, image = GetCaptchaTextAndImage(4)

    print(text)
    imshow(image)
    print(type(image))
    print(image.shape)