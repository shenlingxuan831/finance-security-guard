from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "skills/finance-security-guard/assets/methodology.png"
ICON = ROOT / "skills/finance-security-guard/assets/icon.png"
FONT_PATH = Path("C:/Windows/Fonts/simhei.ttf")

WIDTH, HEIGHT = 1800, 1220
BG = "#f7f5f0"
INK = "#20242b"
MUTED = "#6e7278"
YELLOW = "#ffd83d"
GREEN = "#277459"
DARK = "#22262c"
CORAL = "#d86652"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def render() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)

    def rounded(box, radius, fill, outline=None, width=1):
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

    def text(xy, value, size, fill=INK, anchor=None):
        draw.text(xy, value, font=font(size), fill=fill, anchor=anchor)

    text((86, 62), "不是敏感词扫描，而是一套内置方法论", 54)
    text((88, 138), "八层规则共同约束 Agent：先判断边界，再处理材料，最后通过验收门槛", 27, MUTED)

    rounded((1390, 48, 1715, 140), 46, DARK)
    text((1552, 94), "经管求职安全方法论", 23, "#ffffff", "mm")

    icon = Image.open(ICON).convert("RGB")
    icon = ImageOps.fit(icon, (230, 230), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", (230, 230), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 229, 229), radius=40, fill=255)
    image.paste(icon, (1455, 180), mask)
    text((1570, 438), "规则先于润色", 29, INK, "mm")
    text((1570, 480), "安全结论先于“听起来不错”", 20, MUTED, "mm")

    layers = [
        ("01", "边界层", "明确适合与不适合做什么", YELLOW, INK),
        ("02", "身份层", "按阶段切换引导、审计、发布与投递角色", "#ffffff", INK),
        ("03", "质量标准层", "规定什么程度才算合格", "#dfeee8", INK),
        ("04", "工作流层", "先登记和核验，再生成与行动", DARK, "#ffffff"),
        ("05", "硬规则层", "把真实踩坑写成不可越过的红线", "#ffe5df", INK),
        ("06", "反模式层", "明确 AI 不能偷懒、脑补或越权", "#ffffff", INK),
        ("07", "输出模式层", "申请、面试、审查、公开分别处理", "#e9e5f4", INK),
        ("08", "验收与参考库", "交付前自测，并沉淀可复用规则", YELLOW, INK),
    ]

    card_w, card_h = 790, 180
    positions = []
    for row in range(4):
        for col in range(2):
            positions.append((70 + col * 850, 550 + row * 155))

    for (number, title, description, fill, color), (x, y) in zip(layers, positions):
        rounded((x, y, x + card_w, y + 128), 16, fill, "#d7d2ca", 2)
        rounded((x + 20, y + 22, x + 82, y + 84), 31, DARK if fill != DARK else YELLOW)
        text((x + 51, y + 53), number, 22, "#ffffff" if fill != DARK else DARK, "mm")
        text((x + 108, y + 23), title, 29, color)
        text((x + 108, y + 72), description, 21, "#e7e7e7" if fill == DARK else MUTED)

    rounded((70, 1160, 1730, 1205), 22, DARK)
    text(
        (900, 1182),
        "最终输出必须给出：证据、隐私风险、动作门槛、产物、下一步，以及 READY / REVIEW / BLOCKED",
        21,
        "#ffffff",
        "mm",
    )

    image.save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    render()
