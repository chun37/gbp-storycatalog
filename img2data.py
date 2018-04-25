import pyocr
import pyocr.builders
from PIL import Image, ImageOps
import glob
from io import BytesIO
import base64
import json

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
# OCRツールを探し、選択

data = []

for file in glob.glob("./images/*"):
    image = Image.open(file)
    croped = image.crop((150, 595, 1195, 729))  # 会話部分のみを切り出し
    croped.paste(Image.new("RGB", (40, 80), "black"), (1000, 75))  # 右下の羽？を隠す
    res = tool.image_to_string(
        ImageOps.grayscale(croped),
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    thumb = image.resize((145, 81))  # サムネ取得
    buffered = BytesIO()
    thumb.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue())  # サムネを文字として保存するためbase64encode
    buffered.close()
    data.append([
        file.split("\\")[-1],  # ファイル名
        res.replace("\n", "[br]").replace(" ", ""),  # OCRで読み取ったテキスト
        img_str.decode('utf-8')  # サムネ(base64encoded)をjsonに保存するためdecode
    ])
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
