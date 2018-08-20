#パッケージをインポート
import qrcode
#QRコード生成
img = qrcode.make('http://kujirahand.com/')
#ファイルに保存
img.save('qrcode-test.png')
