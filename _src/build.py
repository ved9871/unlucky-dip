"""Build the unluckydip.com site (Rave Flyer, the design Scott chose on 11 Nov 2026).

Templates and the stylesheet live in _src/rave/. Copy that repeats across
pages (nav, footer, FAQ, small print, the sign-up pop-up) lives here once and
is injected into {{TOKENS}}.

The five other designs (dip, pop, os, maison, bric) are kept as built on
11 Nov for reference. They are frozen: this script no longer rebuilds them.

Run:  python _src/build.py
"""
import pathlib
import shutil

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
LIVE = ["rave"]

# Scott, 11 Nov: the company is always written unluckydip.com, one word, with the .com.
BRAND = "unluckydip.com"
# Scott, 11 Nov: 60%, measured by the value of what goes in a box (was 40%).
PCT = "60%"
CHARITIES = ["British Heart Foundation", "Mind", "YMCA", "Oxfam", "St Barnabas"]
# Logos taken from each charity's own website on 12 Nov 2026 (Ved: use their logos directly).
# (file in assets/charities, width, height)
CHARITY_LOGOS = {
    "British Heart Foundation": ("british-heart-foundation.svg", 124, 35),
    "Mind": ("mind.png", 500, 216),
    "YMCA": ("ymca.svg", 134, 39),
    "Oxfam": ("oxfam.svg", 185, 70),
    "St Barnabas": ("st-barnabas.svg", 189, 36),
}
EMAIL = "hello@unluckydip.com"

PAGES = [  # (file, nav label)
    ("index.html#boxes", "The boxes"),
    ("ninja.html", "Ninja Box"),
    ("not-so-shite.html", "Not So Shite"),  # Ved, 14 Nov: the merch and partner section
    ("scan.html", "Box Scan"),
    ("wtf.html", "WTF is Shitebox?"),
]

# Order set by Scott, 12 Nov: upcycled first, what's inside second, personal third, then the rest.
FAQ = [
    ("What do you mean, upcycled?",
     f"Around {PCT} of what goes in a box is rescued from charity shops and given one more chance to disappoint. "
     "So yes, some items have had a previous life. Nothing that could be a hygiene risk is ever second-hand."),
    ("What is inside?",
     "Stuff. Mostly. Some upcycled shite, some mundane shite and some novelty shite. Random, low-value goods. "
     "You are paying for the laugh, and we say so before you pay."),
    ("Can I make it personal?",
     "Yes. When you order we ask who it's for, what they're shite at and how harsh we can be, and we aim the insults. "
     "Or hit Randomise and take pot luck."),
    ("I'm out of gift ideas.",
     "Good. Stop having them. Gift ideas are how you ended up buying your dad socks again. You pick a size, we take the decision, "
     "and they get what they're given. If it's rubbish, just blame us."),
    ("What is a Ninja Box?",
     "The same shite in a plain box, with our name nowhere on the outside, at no extra cost. They won't know what it is until it's open. "
     "<a href=\"ninja.html\">Meet the Ninja Box</a>."),
    ("What is Box Scan?",
     "Every box has a place to scan. Scan it once the box is open and we explain ourselves, item by item. "
     "<a href=\"scan.html\">Box Scan is here</a>."),
    ("Which charities?",
     "We shop at British Heart Foundation, Mind, YMCA, Oxfam and St Barnabas, and we're adding more. We buy from their shops like anyone else. "
     "They haven't endorsed us, and frankly who would..."),
    # Scott, 11 Nov: do not invite "I didn't like it" returns. The legal detail lives on the small print page.
    ("It's shite. Can I have my money back?",
     "It's meant to be shite. That's not a fault, that's the product, and you get what you're given. "
     "If something turns up broken, tell us and we put it right. Your legal rights are set out in <a href=\"small-print.html\">the small print</a>."),
]

# Scott, 11 Nov: the 14-day line comes out of the short version. It stays in the FAQ and on the small print page.
SMALL_SHORT = (
    "<p><strong>The small print.</strong> Some items in every box are second-hand, upcycled from charity shops. "
    "Nothing that could be a hygiene risk is second-hand. Contents are random and low in value; you are paying for the laugh. "
    "<strong>None of this affects your statutory rights.</strong> <a href=\"small-print.html\">Read all of the small print</a>.</p>"
)

SMALL_FULL = [
    ("What you are buying",
     ["A Shitebox is a mystery box. We choose what goes in it and you do not. The contents are random, low in value and "
      "different every time. Photos and descriptions on this site show the idea, not your box."]),
    ("Second-hand and upcycled items",
     [f"Around {PCT} of the items we send are upcycled: bought from charity shops and given a second go. "
      "So some items in every box are second-hand.",
      "Nothing that could be a hygiene risk is ever second-hand. Everything is checked and sent intact and safe, if not useful."]),
    ("The charities",
     ["We buy stock from charity shops, including British Heart Foundation, Mind, YMCA, Oxfam and St Barnabas. "
      "The money we spend in their shops is how your order supports them.",
      "We are not partnered with these charities and they have not endorsed us. We do not promise a fixed donation per box."]),
    ("Postage",
     ["UK postage is £4.70 a box, sent Royal Mail tracked, and is added to the price at the checkout."]),
    ("Ninja Box",
     ["Boxes are branded on the outside as standard. A Ninja Box is sent in a plain box with no Shitebox or unluckydip.com branding on the outside. "
      "The contents are the same and it costs no more."]),
    ("Making it personal",
     ["Telling us about the person getting the box is optional. We use what you tell us to write the jokes for that box, "
      "and for nothing else."]),
    ("Not So Shite",
     ["Not So Shite is the part of the shop where the products are meant to be good. Our merch is sent straight from our suppliers, "
      "so it arrives on its own and not inside a Shitebox.",
      "Partner picks are sold by other shops. The button takes you to their site, you buy from them, and their terms apply. "
      "We may earn a commission when you do. It does not change the price you pay."]),
    ("Disappointing is not a fault",
     ["The contents are meant to be rubbish. Not liking what you were given does not make an item faulty."]),
    ("Your right to cancel",
     ["The law gives you 14 days from delivery to cancel an online order. To use it, tell us, then send the whole box back at your own cost. "
      "We refund you when it arrives.",
      "Boxes we have personalised for you are made to order and cannot be cancelled once we have started packing them."]),
    ("If something is wrong",
     ["If an item arrives broken or the box is damaged, tell us and we will put it right. Disappointing is the product. Broken is not."]),
    ("Who can buy",
     ["Boxes are sold to adults. They are gifts for adults, not toys."]),
]

RIGHTS = "Nothing in this small print affects your statutory rights."


def logo():
    return ('<a class="ud-logo" href="index.html" aria-label="unluckydip.com, home">'
            '<img src="../assets/brand/unlucky-dip-thumb.svg" alt="" width="36" height="33">'
            '<span>UNLUCKY<b>DIP</b><i>.COM</i></span></a>')


def nav(current=""):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in PAGES)
    return ('<nav class="main" aria-label="Main"><div class="wrap">' + logo() +
            f'<div class="links">{links}</div>'
            '<button class="cart" type="button" data-soon>Basket 0</button></div></nav>')


def footer(short=True):
    small = f'<div class="wrap small">{SMALL_SHORT}</div>' if short else ""
    return f"""<footer>
  <div class="wrap">
    <div><a class="wordmark" href="index.html">{BRAND}<small>Home of Shitebox</small></a><p>Making gift giving worse. On purpose.</p><img class="tape" src="../assets/brand/unlucky-dip-tape.svg" alt="Parcel tape that reads: beware, crap inside. unluckydip.com"></div>
    <div><h4>Shop</h4><ul><li><a href="index.html#boxes">The Little Shite</a></li><li><a href="index.html#boxes">The Big Shite</a></li><li><a href="ninja.html">Ninja Box</a></li><li><a href="not-so-shite.html">Not So Shite</a></li><li><a href="scan.html">Box Scan</a></li></ul></div>
    <div><h4>Help</h4><ul><li><a href="wtf.html">WTF is Shitebox?</a></li><li><a href="index.html#faq">FAQ</a></li><li><a href="small-print.html">The small print</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
    <div><h4>Follow</h4><ul><li><a href="#">TikTok</a></li><li><a href="#">Instagram</a></li><li><a href="#">YouTube</a></li></ul></div>
  </div>
  {small}
  <div class="wrap legal">Shitebox is a product of {BRAND}. {PREVIEW}</div>
</footer>"""


def faq_html():
    return "\n    ".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(FAQ))


def small_full_html():
    out = [f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in paras) for h, paras in SMALL_FULL]
    out.append(f'<p class="rights">{RIGHTS}</p>')
    return "\n    ".join(out)


PREVIEW = "Design preview, 14 November 2026. Nothing is for sale yet and the prices are working numbers."

# Scott, 11 Nov: "Not on sale yet" is no longer a section. It pops up when someone tries to buy.
SOON = """<dialog class="soon" id="soon" aria-labelledby="soon-h">
  <form method="dialog"><button class="x" aria-label="Close">Close</button></form>
  <p class="eyebrow">Not on sale yet</p>
  <h2 id="soon-h">Steady on.</h2>
  <p>We're still filling the boxes. Leave an email and you'll be the first to be disappointed.</p>
  <form class="signup" onsubmit="event.preventDefault();this.querySelector('[data-done]').hidden=false;this.querySelector('input').value=''">
    <label for="su-email">Your email</label>
    <div class="row"><input id="su-email" name="email" type="email" required autocomplete="email" placeholder="you@example.co.uk"><button class="btn" type="submit">Warn me at launch</button></div>
    <p class="fine">One email when we launch. Maybe one more if we think of a joke. Unsubscribe any time.</p>
    <p class="done" data-done hidden role="status">You're on the list. Lower your expectations.</p>
  </form>
</dialog>
<script>
(function(){var d=document.getElementById('soon');if(!d||!d.showModal)return;
document.addEventListener('click',function(e){var t=e.target.closest('[data-soon]');if(t){e.preventDefault();d.showModal();return}
if(e.target===d)d.close()});})();
</script>"""

# ---- Not So Shite: the products ----
# EXAMPLES ONLY, for the design preview. Each row is one product; in Shopify each becomes a product with the
# same fields (title, one-line description, price, type). kind "merch" = we sell it and a supplier sends it
# (drop shipping / print on demand). kind "partner" = an affiliate link out to another shop.
THUMB_ART = '<image href="../assets/brand/unlucky-dip-thumb.svg" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def _thumb(x, y, w):
    return THUMB_ART.format(x=x, y=y, w=w, h=round(w * 25 / 27, 1))


ART = {
    "mug": '<rect x="58" y="38" width="74" height="86" rx="8" fill="#fff"/><path d="M132 58h12a20 20 0 0 1 0 44h-12" fill="none"/>' + _thumb(74, 62, 42),
    "tee": '<path d="M70 28 50 38 26 66l20 18 12-10v62h84V74l12 10 20-18-24-28-20-10q-30 22-60 0z" fill="#fff"/>' + _thumb(80, 72, 40),
    "tote": '<path d="M76 62V44a24 24 0 0 1 48 0v18" fill="none"/><rect x="54" y="62" width="92" height="80" fill="#fff"/>' + _thumb(79, 82, 42),
    "stickers": '<circle cx="70" cy="74" r="38" fill="#fff"/><circle cx="132" cy="92" r="38" fill="#fff"/>' + _thumb(50, 56, 40) + _thumb(112, 74, 40),
    "cap": '<path d="M46 104a52 50 0 0 1 104 0z" fill="#fff"/><path d="M148 104h30q10 0 6 9l-4 7q-16-9-36-7z" fill="#fff"/>' + _thumb(80, 64, 34),
    "card": '<g transform="rotate(-6 100 80)"><rect x="58" y="24" width="84" height="112" fill="#fff"/></g>' + _thumb(78, 58, 44),
    "candle": '<rect x="68" y="72" width="64" height="66" rx="6" fill="#fff"/><path d="M100 72V62"/><path d="M100 30q16 18 0 32-16-14 0-32z" fill="#F8FF37"/><path d="M68 94h64"/>',
    "socks": '<path d="M78 26h36v62l28 20a15 15 0 0 1-9 27h-22a33 33 0 0 1-33-33z" fill="#fff"/><path d="M78 44h36M78 56h36"/>',
    "opener": '<circle cx="66" cy="80" r="30" fill="#fff"/><circle cx="66" cy="80" r="12" fill="none"/><rect x="92" y="68" width="84" height="24" rx="12" fill="#fff"/>',
    "book": '<rect x="54" y="30" width="92" height="104" rx="4" fill="#fff"/><path d="M72 30v104M88 58h42M88 76h42M88 94h26"/>',
    "choc": '<rect x="42" y="46" width="116" height="72" rx="6" fill="#fff"/><path d="M71 46v72M100 46v72M129 46v72M42 82h116"/>',
    "plant": '<path d="M100 96V52"/><path d="M100 70q-34-4-36-36 34 2 36 36zM100 60q30-8 30-40-32 6-30 40z" fill="#fff"/><path d="M70 96h60l-8 42H78z" fill="#fff"/>',
}

PRODUCTS = [  # (kind, art, name, one line, price)
    ("merch", "mug", "The Given Mug", "Says \"You get what you're given.\" Holds tea. That's the lot.", "£11.99"),
    ("partner", "candle", "A candle that smells nice", "Of something pleasant, for once. Not of a charity shop.", "about £14"),
    ("merch", "tee", "Sarcastic And Superb Tee", "For people who are both, or think they are.", "£19.99"),
    ("partner", "socks", "Socks that are actually good", "The present you used to get. Only decent this time.", "about £9"),
    ("merch", "tote", "Nifty At Being Thrifty Tote", "For carrying shite home from charity shops.", "£12.99"),
    ("partner", "opener", "A proper bottle opener", "Opens bottles. First time. Imagine.", "about £12"),
    ("merch", "stickers", "Thumbs-Down Stickers", "Review everything you own. Sheet of twelve.", "£3.99"),
    ("partner", "book", "A book they might finish", "No promises. But it's a good one.", "about £9"),
    ("merch", "cap", "Just Blame Us Cap", "Wear it when the present goes badly.", "£16.99"),
    ("partner", "choc", "Decent chocolate", "The kind you don't share.", "about £6"),
    ("merch", "card", "You Get What You're Given Card", "A greetings card that manages expectations.", "£3.49"),
    ("partner", "plant", "A plant that's hard to kill", "We tested this the obvious way.", "about £15"),
]


def products_html():
    out = []
    for i, (kind, art, name, line, price) in enumerate(PRODUCTS):
        merch = kind == "merch"
        tag = "Our merch" if merch else "Partner pick"
        small = "+ delivery" if merch else "price set by the seller"
        button = ('<button class="btn" type="button" data-soon>Add to basket</button>' if merch else
                  '<a class="btn" href="#" rel="sponsored nofollow noopener" data-soon>View at the shop &rarr;</a>'
                  '<span class="aff">Affiliate link. We may earn a commission.</span>')
        out.append(
            f'<li class="prod {kind} c{i % 4 + 1}" data-kind="{kind}"><span class="tag">{tag}</span>'
            f'<div class="art"><svg viewBox="0 0 200 160" role="img" aria-label="Drawing: {name}" fill="none" stroke="#252525" '
            f'stroke-width="6" stroke-linejoin="round" stroke-linecap="round">{ART[art]}</svg></div>'
            f'<div class="body"><h3>{name}</h3><p>{line}</p>'
            f'<p class="price">{price}<small>{small}</small></p>{button}</div></li>')
    return "\n      ".join(out)


WA = ('<a class="wa" href="https://wa.me/447000000000?text=Hi%20unluckydip.com" aria-label="Chat on WhatsApp">'
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.1.7a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>'
      "<span>Ask us. We'll try.</span></a>")

HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<link rel="icon" href="../assets/brand/unlucky-dip-thumb.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo+Black&family=Inter:wght@400;500;600;700;900&display=swap">
<link rel="stylesheet" href="style.css">"""

TOKENS = {
    "HEAD": HEAD,
    "NAV": nav(),
    "NAV_NINJA": nav("ninja.html"),
    "NAV_SCAN": nav("scan.html"),
    "NAV_WTF": nav("wtf.html"),
    "NAV_NSS": nav("not-so-shite.html"),
    "NSS_PRODUCTS": products_html(),
    "NSS_COUNT": str(len(PRODUCTS)),
    "FOOTER": footer(),
    "FOOTER_PLAIN": footer(short=False),
    "FAQ": faq_html(),
    "SMALL_SHORT": SMALL_SHORT,
    "SMALL_FULL": small_full_html(),
    "CHARITY_LI": "".join(
        f'<li><img src="../assets/charities/{CHARITY_LOGOS[c][0]}" width="{CHARITY_LOGOS[c][1]}" height="{CHARITY_LOGOS[c][2]}" loading="lazy" alt="{c}"></li>'
        for c in CHARITIES),
    "SOON": SOON,
    "WA": WA,
    "BRAND": BRAND,
    "PCT": PCT,
    # Postage is on top of these prices and shown beside them (Scott, 12 Nov: "yes, add £4.70 postage").
    "POST": "£4.70",
    "PRICE_S": "£18.99",
    "PRICE_B": "£27.99",
    "EMAIL": EMAIL,
}


def build():
    for slug in LIVE:
        out = ROOT / slug
        out.mkdir(exist_ok=True)
        for f in sorted((SRC / slug).iterdir()):
            if f.suffix == ".html":
                html = f.read_text(encoding="utf-8")
                for k, v in TOKENS.items():
                    html = html.replace("{{" + k + "}}", v)
                if "{{" in html:
                    raise SystemExit(f"{f}: unresolved token {{{{{html.split('{{')[1][:20]}")
                (out / f.name).write_text(html, encoding="utf-8")
            else:
                shutil.copyfile(f, out / f.name)
        print("built", slug, sorted(p.name for p in out.iterdir()))


if __name__ == "__main__":
    build()
