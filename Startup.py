import datetime
from PIL import Image, ImageDraw, ImageFont
import unicornhathd
import time

COLOR = (200, 0, 0)

width, height = unicornhathd.get_shape()

unicornhathd.rotation(0)

# フォントの定義
font = ImageFont.truetype('/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf', 16) 

def main():
    # カウンタ
    counter = 0

    # 無限ループ
    while True:
        # 描写用キャンバスの新規作成
        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        # 現在時刻の取得
        now = datetime.datetime.now()

        # キャンバスに時、分の描写
        # draw.text((0, -2), '{0:02}'.format(now.hour), fill=COLOR)
        # draw.text((0, 7), '{0:02}'.format(now.minute), fill=COLOR)
        if counter == 0:
            counter = 1
            draw.text((0, 0), u'三', fill=COLOR, font=font)
        elif counter == 1:
            counter = 2
            draw.text((0, 0), u'菱', fill=COLOR, font=font)
        elif counter == 2:
            counter = 3
            draw.text((0, 0), u'電', fill=COLOR, font=font)
        elif counter == 3:
            counter = 4
            draw.text((0, 0), u'機', fill=COLOR, font=font)
        elif counter == 4:
            counter = 5
            draw.text((0, 0), u'ビ', fill=COLOR, font=font)
        elif counter == 5:
            counter = 6
            draw.text((0, 0), u'ジ', fill=COLOR, font=font)
        elif counter == 6:
            counter = 7
            draw.text((0, 0), u'ネ', fill=COLOR, font=font)
        elif counter == 7:
            counter = 8
            draw.text((0, 0), u'ス', fill=COLOR, font=font)
        elif counter == 8:
            counter = 9
            draw.text((0, 0), u'シ', fill=COLOR, font=font)
        elif counter == 9:
            counter = 10
            draw.text((0, 0), u'ス', fill=COLOR, font=font)
        elif counter == 10:
            counter = 11
            draw.text((0, 0), u'テ', fill=COLOR, font=font)
        elif counter == 11:
            counter = 12
            draw.text((0, 0), u'ム', fill=COLOR, font=font)
        else:
            counter = 0
            draw.text((0, 0), u'　', fill=COLOR, font=font)

        # ここからunicornhatへキャンバス描写作業
        unicornhathd.clear()

        # x, yを指定して1ドットずつ描写する
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                # ここの部分でx軸を反転させている
                unicornhathd.set_pixel(width-x-1, y, r, g, b)

        # コロンの代わりに2x2のドットを描写する
        #if now.second % 2:
        #    unicornhathd.set_pixel(0, height-1, *COLOR)
        #    unicornhathd.set_pixel(1, height-1, *COLOR)
        #    unicornhathd.set_pixel(0, height-2, *COLOR)
        #    unicornhathd.set_pixel(1, height-2, *COLOR)

        # 画面のリフレッシュ命令
        unicornhathd.show()

        time.sleep(0.3)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        pass

    finally:
        unicornhathd.off()
