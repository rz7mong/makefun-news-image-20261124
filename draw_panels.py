"""Code-drawn flat-vector illustrations for the 24 Nov 2026 front page.

Every panel is drawn with PIL primitives only (rectangles, ellipses,
polygons, lines) — no photos, no AI image generation, no gradients,
no text inside the illustrations. Deterministic: fixed coordinates,
no randomness, no network. Palette matches the page: cream paper,
navy, red, gold, teal, orange, blue, green.

Lead panels are 317x148; small-story panels are 156x40 (wide, short
bands — each scene is one bold symbol on a flat background).
"""

from PIL import Image, ImageDraw

CREAM = (250, 244, 228)
NAVY = (13, 32, 61)
SKY = (20, 48, 88)
SEA = (16, 48, 84)
DARK = (8, 20, 40)
RED = (178, 34, 34)
GOLD = (232, 176, 44)
GOLD_D = (210, 150, 30)
TEAL = (0, 128, 128)
TEAL_D = (0, 96, 104)
ORANGE = (214, 120, 20)
ORANGE_R = (220, 80, 30)
BLUE = (40, 90, 160)
GREEN = (60, 140, 70)
GREEN_D = (34, 100, 52)
BROWN = (122, 72, 32)
WHITE = (255, 255, 255)
INK = (25, 25, 25)
PALE = (255, 214, 110)
BUILD = (238, 232, 214)
BUILD_D = (216, 208, 186)


def _star(d, cx, cy, r, color):
    """Small 4-point star."""
    q = max(1, int(r * 0.28))
    d.polygon([(cx, cy - r), (cx + q, cy - q), (cx + r, cy),
               (cx + q, cy + q), (cx, cy + r), (cx - q, cy + q),
               (cx - r, cy), (cx - q, cy - q)], fill=color)


def _arrow(d, x0, y0, x1, y1, width, color):
    """Thick rising arrow from (x0, y0) to (x1, y1) with a head."""
    import math
    d.line([(x0, y0), (x1, y1)], fill=color, width=width)
    dx, dy = x1 - x0, y1 - y0
    ln = math.hypot(dx, dy)
    ux, uy = dx / ln, dy / ln
    px, py = -uy, ux
    bx, by = x1 - 26 * ux, y1 - 26 * uy
    hw = 13
    d.polygon([(x1 + 6 * ux, y1 + 6 * uy),
               (bx + hw * px, by + hw * py),
               (bx - hw * px, by - hw * py)], fill=color)


# ------------------------------------------------------------------ leads
def lead_ulleung():
    """Night sky, jet silhouette, lighthouse with red beacon (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    # stars
    for (sx, sy, r, c) in [(20, 14, 3, WHITE), (58, 30, 2, GOLD),
                           (92, 10, 3, WHITE), (140, 18, 2, WHITE),
                           (180, 10, 3, GOLD), (225, 26, 2, WHITE),
                           (262, 12, 3, WHITE), (296, 34, 2, GOLD),
                           (38, 52, 2, WHITE), (300, 62, 2, WHITE),
                           (118, 44, 2, GOLD), (205, 48, 2, WHITE),
                           (250, 40, 2, WHITE), (160, 8, 2, WHITE)]:
        _star(d, sx, sy, r, c)
    # sea
    d.rectangle([0, 118, 317, 148], fill=SEA)
    for wx in (30, 90, 150):
        d.line([(wx, 130), (wx + 22, 130)], fill=(200, 220, 240), width=2)
    for wx in (60, 130, 200):
        d.line([(wx, 140), (wx + 22, 140)], fill=(200, 220, 240), width=2)
    # island, bottom right
    d.polygon([(212, 148), (232, 120), (252, 112), (272, 120),
               (298, 132), (317, 140), (317, 148)], fill=DARK)
    # lighthouse: tapered cream tower, red bands, beacon
    d.polygon([(240, 120), (245, 88), (259, 88), (264, 120)], fill=CREAM)
    d.rectangle([241, 104, 263, 109], fill=RED)
    d.rectangle([243, 94, 261, 97], fill=RED)
    d.rectangle([240, 80, 264, 88], fill=RED)
    # light beams
    d.polygon([(252, 76), (186, 58), (186, 86)], fill=PALE)
    d.polygon([(252, 76), (306, 60), (306, 88)], fill=PALE)
    # beacon glow: pale ring, red ring, gold core
    d.ellipse([238, 62, 266, 90], outline=PALE, width=2)
    d.ellipse([243, 67, 261, 85], outline=RED, width=3)
    d.ellipse([247, 71, 257, 81], fill=GOLD)
    # two small jet silhouettes in the sky (a big jet reads as a paper
    # plane at this size; small darts read as aircraft) + contrails
    _jet(d, 52, 34, 74, CREAM)
    d.line([(52, 38), (18, 34)], fill=(200, 220, 240), width=2)
    d.line([(52, 42), (22, 44)], fill=(200, 220, 240), width=2)
    _jet(d, 168, 18, 48, CREAM)
    d.line([(168, 21), (144, 18)], fill=(200, 220, 240), width=1)
    return img


def _jet(d, x, y, s, color):
    """Small jet silhouette pointing right, length s, top at (x, y)."""
    d.polygon([(x, y + 3), (x + 0.6 * s, y), (x + s, y + 5),
               (x + 0.6 * s, y + 9), (x, y + 7)], fill=color,
              outline=NAVY)
    d.polygon([(x + 0.45 * s, y + 7), (x + 0.75 * s, y + 6),
               (x + 0.85 * s, y + 16)], fill=color, outline=NAVY)
    d.polygon([(x + 0.05 * s, y + 6), (x + 0.15 * s, y - 6),
               (x + 0.25 * s, y + 5)], fill=color, outline=NAVY)
    d.ellipse([x + 0.78 * s, y + 2, x + 0.88 * s, y + 6], fill=NAVY)


def lead_pyongyang():
    """Classical government building, red gate, Swiss flag, moon (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    # stars + crescent moon
    for (sx, sy, r) in [(24, 16, 2), (60, 34, 2), (100, 12, 3),
                        (200, 14, 2), (240, 40, 2), (296, 60, 2)]:
        _star(d, sx, sy, r, WHITE)
    d.ellipse([272, 12, 300, 40], fill=GOLD)
    d.ellipse([280, 8, 304, 36], fill=NAVY)
    # ground
    d.rectangle([0, 128, 317, 148], fill=DARK)
    # steps
    d.rectangle([58, 126, 259, 130], fill=BUILD)
    d.rectangle([63, 122, 254, 126], fill=BUILD)
    d.rectangle([68, 118, 249, 122], fill=BUILD)
    # building body + pediment + columns
    d.rectangle([68, 62, 249, 118], fill=BUILD)
    d.polygon([(68, 62), (158, 38), (249, 62)], fill=BUILD)
    d.ellipse([150, 46, 166, 58], fill=NAVY)
    for cx in (78, 108, 138, 168, 198, 228):
        d.rectangle([cx, 70, cx + 11, 118], fill=BUILD_D)
    d.rectangle([68, 62, 249, 68], fill=CREAM)
    # red gate in front, centre
    d.rectangle([140, 96, 148, 122], fill=RED)
    d.rectangle([169, 96, 177, 122], fill=RED)
    for gx in range(150, 168, 4):
        d.rectangle([gx, 98, gx + 2, 120], fill=RED)
    d.rectangle([138, 94, 179, 98], fill=RED)
    # flag pole on the pediment apex + Swiss flag
    d.line([(158, 38), (158, 16)], fill=CREAM, width=2)
    d.rectangle([158, 16, 178, 34], fill=RED)
    d.rectangle([166, 19, 170, 31], fill=WHITE)
    d.rectangle([161, 23, 175, 27], fill=WHITE)
    return img


def lead_tokyo():
    """Tokyo tower silhouette, gold rising arrow, bars (317x148)."""
    img = Image.new("RGB", (317, 148), NAVY)
    d = ImageDraw.Draw(img)
    for (sx, sy, r) in [(24, 18, 3), (70, 34, 2), (120, 14, 2),
                        (160, 40, 2), (290, 14, 3), (40, 60, 2)]:
        _star(d, sx, sy, r, WHITE)
    d.ellipse([28, 22, 50, 44], fill=GOLD)
    # skyline silhouettes along the bottom
    for (bx, bw, bh) in [(0, 26, 34), (30, 18, 48), (52, 30, 26),
                         (86, 16, 40), (106, 24, 30), (260, 22, 44),
                         (286, 31, 30)]:
        d.rectangle([bx, 148 - bh, bx + bw, 148], fill=SKY)
    # Tokyo tower: orange lattice — slanted legs, crossbars, X bracing
    d.line([(182, 148), (196, 56)], fill=ORANGE_R, width=5)
    d.line([(218, 148), (204, 56)], fill=ORANGE_R, width=5)
    for y, x0, x1 in [(120, 186, 214), (100, 189, 211), (80, 193, 207)]:
        d.line([(x0, y), (x1, y)], fill=ORANGE_R, width=4)
    d.line([(187, 120), (210, 100)], fill=ORANGE_R, width=3)
    d.line([(213, 120), (190, 100)], fill=ORANGE_R, width=3)
    d.line([(190, 100), (207, 80)], fill=ORANGE_R, width=3)
    d.line([(210, 100), (193, 80)], fill=ORANGE_R, width=3)
    # spire + observation decks
    d.line([(200, 56), (200, 28)], fill=ORANGE_R, width=4)
    d.rectangle([186, 72, 214, 78], fill=ORANGE_R)
    d.rectangle([184, 108, 216, 114], fill=ORANGE_R)
    # rising bar chart, bottom right
    for (bx, bh, c) in [(240, 16, RED), (256, 26, GOLD), (272, 36, RED),
                        (288, 48, GOLD)]:
        d.rectangle([bx, 140 - bh, bx + 12, 140], fill=c)
    # big gold rising arrow over everything
    _arrow(d, 34, 132, 252, 30, 11, GOLD)
    return img


LEAD_DRAW = {
    "ulleung": lead_ulleung,
    "pyongyang": lead_pyongyang,
    "tokyo": lead_tokyo,
}


# ------------------------------------------------------------------ small panels (156x40)
def _ball(d, cx, cy, r):
    """Soccer ball: white circle, black centre pentagon, small patches."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE,
              outline=INK, width=1)
    import math
    pts = []
    for k in range(5):
        a = math.radians(-90 + k * 72)
        pts.append((cx + 0.38 * r * math.cos(a),
                    cy + 0.38 * r * math.sin(a)))
    d.polygon(pts, fill=INK)
    for (px, py) in [(cx - r, cy - 2), (cx + r, cy - 2), (cx, cy + r)]:
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=INK)


def small_pmi():
    """Factory with sawtooth roof + rising bars (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # factory body + sawtooth roof
    d.polygon([(8, 40), (8, 20), (20, 10), (32, 20), (44, 10), (56, 20),
               (68, 10), (70, 20), (70, 40)], fill=NAVY)
    d.rectangle([74, 6, 82, 40], fill=NAVY)
    for (sx, sy) in [(78, 2), (84, 0)]:
        pass
    d.ellipse([75, 0, 81, 6], fill=(200, 200, 200))
    d.ellipse([80, -3, 86, 3], fill=(200, 200, 200))
    # windows
    for wx in (16, 34, 52):
        d.rectangle([wx, 26, wx + 8, 32], fill=GOLD)
    # rising bars, right
    for (bx, bh, c) in [(96, 12, RED), (110, 18, NAVY), (124, 25, GOLD),
                        (138, 32, RED)]:
        d.rectangle([bx, 38 - bh, bx + 10, 38], fill=c)
    return img


def small_ucl():
    """Stadium bowl + soccer ball, night (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 14, 8, 2, WHITE)
    _star(d, 142, 8, 2, GOLD)
    # stadium bowl: cream outline ellipse + green pitch
    d.ellipse([12, 6, 144, 46], outline=CREAM, width=2)
    d.ellipse([34, 18, 122, 40], fill=GREEN)
    d.ellipse([34, 18, 122, 40], outline=CREAM, width=1)
    d.line([(78, 18), (78, 40)], fill=CREAM, width=1)
    # floodlights
    for fx in (26, 130):
        d.line([(fx, 6), (fx, 12)], fill=GOLD, width=2)
        d.ellipse([fx - 3, 3, fx + 3, 9], fill=GOLD)
    _ball(d, 78, 14, 7)
    return img


def small_nba():
    """Jumping player silhouette + ball + hoop (156x40)."""
    img = Image.new("RGB", (156, 40), ORANGE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 32, 156, 40], fill=CREAM)
    d.line([(0, 32), (156, 32)], fill=RED, width=1)
    # hoop: backboard + rim, right
    d.rectangle([128, 4, 140, 20], fill=WHITE, outline=NAVY, width=1)
    d.ellipse([124, 20, 144, 26], outline=RED, width=2)
    d.line([(134, 26), (130, 32)], fill=RED, width=1)
    d.line([(134, 26), (138, 32)], fill=RED, width=1)
    # player silhouette, centre-left: head, torso, arm up to the ball,
    # two legs — drawn as separate parts so the figure reads
    d.ellipse([56, 4, 65, 13], fill=NAVY)
    d.polygon([(56, 14), (65, 14), (68, 28), (54, 28)], fill=NAVY)
    d.polygon([(63, 16), (77, 8), (80, 12), (67, 21)], fill=NAVY)
    d.polygon([(56, 28), (60, 28), (58, 40), (54, 40)], fill=NAVY)
    d.polygon([(62, 28), (66, 28), (68, 40), (64, 40)], fill=NAVY)
    # ball in the raised hand
    d.ellipse([76, 6, 88, 18], fill=(120, 60, 20), outline=INK, width=1)
    d.line([(76, 12), (88, 12)], fill=INK, width=1)
    d.line([(82, 6), (82, 18)], fill=INK, width=1)
    return img


def small_treasury():
    """Classical treasury building + gold coins, night (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 12, 8, 2, WHITE)
    _star(d, 144, 10, 2, GOLD)
    # building, left-centre
    d.polygon([(18, 20), (52, 8), (86, 20)], fill=CREAM)
    d.rectangle([18, 20, 86, 24], fill=CREAM)
    for cx in (24, 44, 64):
        d.rectangle([cx, 24, cx + 8, 38], fill=CREAM)
    d.rectangle([16, 38, 88, 40], fill=CREAM)
    # gold coins, right
    for (cx, cy) in [(108, 30), (120, 24), (132, 30)]:
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=GOLD,
                  outline=GOLD_D, width=1)
    d.ellipse([114, 18, 126, 30], fill=GOLD, outline=GOLD_D, width=1)
    return img


def small_stocks():
    """Rising bars + gold arrow + coins (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    for (bx, bh, c) in [(14, 12, RED), (28, 18, NAVY), (42, 24, GOLD),
                        (56, 30, RED)]:
        d.rectangle([bx, 36 - bh, bx + 10, 36], fill=c)
    _arrow(d, 12, 32, 84, 6, 4, GOLD_D)
    for (cx, cy) in [(102, 28), (116, 22), (130, 28)]:
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=GOLD,
                  outline=GOLD_D, width=1)
    return img


def small_mnf():
    """American football on a green field (156x40)."""
    img = Image.new("RGB", (156, 40), GREEN_D)
    d = ImageDraw.Draw(img)
    for lx in (24, 52, 104, 132):
        d.line([(lx, 0), (lx, 40)], fill=WHITE, width=2)
    # football: brown ellipse + white laces
    d.ellipse([58, 12, 98, 28], fill=BROWN, outline=INK, width=1)
    d.line([(70, 20), (86, 20)], fill=WHITE, width=2)
    for lx in (73, 78, 83):
        d.line([(lx, 16), (lx, 24)], fill=WHITE, width=1)
    return img


def small_ifo():
    """Gauge dial pointing up-right (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # dial: navy arc, gold upper arc, ticks, red needle
    d.arc([46, 2, 110, 66], start=180, end=360, fill=NAVY, width=3)
    d.arc([46, 2, 110, 66], start=300, end=360, fill=GOLD, width=3)
    import math
    for deg in (180, 210, 240, 270, 300, 330, 360):
        a = math.radians(deg)
        x0 = 78 + 30 * math.cos(a)
        y0 = 34 + 30 * math.sin(a)
        x1 = 78 + 25 * math.cos(a)
        y1 = 34 + 25 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=NAVY, width=2)
    d.line([(78, 34), (100, 12)], fill=RED, width=3)
    d.ellipse([74, 30, 82, 38], fill=NAVY)
    # small building, left
    d.rectangle([8, 20, 30, 36], fill=NAVY)
    d.polygon([(8, 20), (19, 12), (30, 20)], fill=NAVY)
    for wx in (13, 21):
        d.rectangle([wx, 26, wx + 4, 32], fill=GOLD)
    return img


def _maple_leaf(d, cx, cy, s, color):
    """Chunky maple leaf: five fat lobes fanning from the centre plus a
    stem. Drawn as overlapping triangles so the lobes stay bold and
    the notches between them read at small size."""
    u = s / 40.0

    def p(dx, dy):
        return (cx + dx * u, cy + dy * u)

    # top lobe, upper lobes, lower lobes (each a triangle from centre)
    d.polygon([p(0, -20), p(-6, -2), p(6, -2)], fill=color)
    d.polygon([p(-16, -12), p(-2, -2), p(-4, 6)], fill=color)
    d.polygon([p(16, -12), p(2, -2), p(4, 6)], fill=color)
    d.polygon([p(-14, 8), p(-2, 4), p(0, 14)], fill=color)
    d.polygon([p(14, 8), p(2, 4), p(0, 14)], fill=color)
    d.rectangle([p(-2, 12)[0], p(-2, 12)[1], p(2, 20)[0], p(2, 20)[1]],
                fill=color)


def small_bank():
    """Bank building + red maple leaf, night (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 12, 8, 2, WHITE)
    d.polygon([(14, 20), (44, 8), (74, 20)], fill=CREAM)
    d.rectangle([14, 20, 74, 24], fill=CREAM)
    for cx in (20, 40, 60):
        d.rectangle([cx, 24, cx + 7, 38], fill=CREAM)
    d.rectangle([12, 38, 76, 40], fill=CREAM)
    _maple_leaf(d, 118, 19, 36, RED)
    return img


def small_u17():
    """Soccer ball + gold trophy (156x40)."""
    img = Image.new("RGB", (156, 40), GREEN)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=GREEN_D)
    d.ellipse([10, 22, 30, 36], fill=WHITE, outline=INK, width=1)
    d.ellipse([17, 27, 23, 33], fill=INK)
    _ball(d, 52, 20, 11)
    # trophy, right
    d.polygon([(108, 6), (140, 6), (134, 22), (114, 22)], fill=GOLD)
    d.ellipse([100, 8, 112, 22], outline=GOLD, width=2)
    d.ellipse([136, 8, 148, 22], outline=GOLD, width=2)
    d.rectangle([121, 22, 127, 30], fill=GOLD)
    d.rectangle([112, 30, 136, 36], fill=GOLD)
    return img


def small_adp():
    """Briefcase + checklist + rising bars (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # briefcase, left
    d.rectangle([10, 14, 62, 36], fill=BROWN, outline=INK, width=1)
    d.rectangle([30, 8, 44, 14], outline=BROWN, width=2)
    d.rectangle([33, 22, 41, 27], fill=GOLD)
    d.line([(10, 25), (62, 25)], fill=INK, width=1)
    # checklist paper, centre
    d.rectangle([76, 6, 106, 34], fill=WHITE, outline=NAVY, width=1)
    for (cy, tx) in [(13, 88), (21, 88), (29, 88)]:
        d.line([(80, cy), (85, cy + 3), (90, cy - 3)], fill=GREEN, width=2)
        d.line([(94, cy), (102, cy)], fill=NAVY, width=1)
    # rising bars, right
    for (bx, bh, c) in [(118, 10, RED), (130, 16, GOLD), (142, 24, NAVY)]:
        d.rectangle([bx, 36 - bh, bx + 8, 36], fill=c)
    return img


def small_chips():
    """Microchip + gold up arrow, night (156x40)."""
    img = Image.new("RGB", (156, 40), NAVY)
    d = ImageDraw.Draw(img)
    _star(d, 12, 8, 2, WHITE)
    # chip body + pins
    d.rectangle([52, 6, 92, 34], fill=(20, 45, 85), outline=GOLD, width=2)
    for py in (10, 18, 26):
        d.rectangle([46, py, 52, py + 3], fill=GOLD)
        d.rectangle([92, py, 98, py + 3], fill=GOLD)
    for px in (60, 72, 84):
        d.rectangle([px, 2, px + 3, 6], fill=GOLD)
        d.rectangle([px, 34, px + 3, 38], fill=GOLD)
    d.rectangle([64, 14, 80, 26], fill=GOLD)
    d.rectangle([68, 18, 76, 22], fill=NAVY)
    # up arrow, right
    _arrow(d, 112, 32, 140, 8, 4, GOLD)
    return img


def small_vote():
    """Ballot box + paper + big check (156x40)."""
    img = Image.new("RGB", (156, 40), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 30, 156, 40], fill=(226, 218, 200))
    # paper going into the slot
    d.polygon([(74, 2), (94, 2), (88, 14), (68, 14)], fill=WHITE,
              outline=NAVY)
    # ballot box
    d.rectangle([18, 16, 72, 38], fill=RED, outline=INK, width=1)
    d.rectangle([30, 14, 60, 16], fill=INK)
    # big check, right
    d.line([(88, 26), (100, 36), (134, 8)], fill=RED, width=5)
    return img


SMALL_DRAW = {
    "pmi": small_pmi,
    "ucl": small_ucl,
    "nba": small_nba,
    "treasury": small_treasury,
    "stocks": small_stocks,
    "mnf": small_mnf,
    "ifo": small_ifo,
    "bank": small_bank,
    "u17": small_u17,
    "adp": small_adp,
    "chips": small_chips,
    "vote": small_vote,
}
