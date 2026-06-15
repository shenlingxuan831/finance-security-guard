from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "skills/finance-security-guard/assets/user-flow.png"
ICON = ROOT / "skills/finance-security-guard/assets/icon.png"
FONT_PATH = Path("C:/Windows/Fonts/simhei.ttf")

WIDTH, HEIGHT = 1800, 1120
BACKGROUND = "#f7f5f0"
INK = "#20242b"
MUTED = "#6e7278"
YELLOW = "#ffd83d"
GREEN = "#277459"
DARK = "#22262c"


def make_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def render() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    def rounded(box, radius, fill, outline=None, width=1):
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

    def label(xy, value, size, fill=INK, anchor=None):
        draw.text(xy, value, font=make_font(size), fill=fill, anchor=anchor)

    label((90, 70), "经管保安.skill｜内置 Web 使用流程", 54)
    label((92, 145), "下载后打开本地网页，在一个界面里完成选择、检查和下一步处理", 28, MUTED)

    rounded((1420, 55, 1710, 145), 45, DARK)
    label((1565, 100), "本地运行 · 不自动发送", 24, "#ffffff", "mm")

    icon = Image.open(ICON).convert("RGB")
    icon = ImageOps.fit(icon, (250, 250), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", (250, 250), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 249, 249), radius=42, fill=255)
    image.paste(icon, (1450, 190), mask)
    label((1575, 465), "你决定何时继续", 28, INK, "mm")
    label((1575, 505), "上传、公开、发送前再次确认", 20, MUTED, "mm")

    steps = [
        ("01", "打开内置 Web", ["运行 start.ps1", "自动打开本地工作台", "无需注册或部署网站"], YELLOW),
        ("02", "选择任务与文件", ["申请、面试、检查、公开", "选择简历、JD 和项目", "原文件不会被修改"], "#ffffff"),
        ("03", "网页本地检查", ["登记可读与未读文件", "区分事实与岗位要求", "检查隐私、秘密和缺口"], DARK),
        ("04", "查看明确结论", ["READY：可以继续", "REVIEW：需要确认", "BLOCKED：必须先处理"], "#ffffff"),
        ("05", "继续安全处理", ["修改简历和项目表达", "准备面试或研究作品", "发送前再做一次预检"], "#dfeee8"),
    ]

    start_x, y, card_w, card_h, gap = 70, 590, 310, 390, 32
    for index, (number, title, bullets, fill) in enumerate(steps):
        x = start_x + index * (card_w + gap)
        dark_card = fill == DARK
        rounded(
            (x, y, x + card_w, y + card_h),
            18,
            fill,
            DARK if dark_card else "#d9d4cc",
            2,
        )
        rounded(
            (x + 22, y + 22, x + 80, y + 80),
            29,
            YELLOW if dark_card else DARK,
        )
        label(
            (x + 51, y + 51),
            number,
            22,
            DARK if dark_card else "#ffffff",
            "mm",
        )
        label((x + 24, y + 112), title, 30, "#ffffff" if dark_card else INK)

        bullet_y = y + 182
        for bullet in bullets:
            draw.ellipse(
                (x + 26, bullet_y + 10, x + 36, bullet_y + 20),
                fill=YELLOW if dark_card else GREEN,
            )
            label((x + 50, bullet_y), bullet, 21, "#e9e9e9" if dark_card else "#595d63")
            bullet_y += 55

        if index < len(steps) - 1:
            arrow_x = x + card_w + 8
            arrow_y = y + card_h // 2
            draw.line((arrow_x, arrow_y, arrow_x + 18, arrow_y), fill="#a6a198", width=5)
            draw.polygon(
                [
                    (arrow_x + 18, arrow_y - 9),
                    (arrow_x + 34, arrow_y),
                    (arrow_x + 18, arrow_y + 9),
                ],
                fill="#a6a198",
            )

    rounded((70, 1025, 1730, 1085), 30, "#fff3c3")
    label(
        (900, 1055),
        "内置 Web 仅运行于 127.0.0.1｜不虚构经历 · 不泄露秘密 · 不自动上传或发送",
        24,
        "#4e4530",
        "mm",
    )

    image.save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    render()
