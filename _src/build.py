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
    ("not-so-shite.html", "Not So Shite"),  # other shops' products we think are good (Scott, 14 Nov)
    ("wear-shite.html", "Wear Shite"),  # our own merch: our logo on clothes (Scott, 14 Nov)
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
     ["Telling us about the person getting the box is optional. If you do, we ask you to tick a box to say we may use your answers. "
      "We use them to write the jokes for that box, and for nothing else."]),
    ("Not So Shite",
     ["The things on the Not So Shite pages are not ours and we do not sell them. They are other shops' products that we think are good. "
      "The button takes you to that shop, you buy from them, and their prices and terms apply.",
      "We may earn a commission when you buy something this way. It does not change the price you pay."]),
    ("Wear Shite",
     ["Wear Shite is our own merchandise. Each item is printed to order, so it is sent separately and does not arrive inside a Shitebox."]),
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
    <div><h4>Shop</h4><ul><li><a href="index.html#boxes">The Little Shite</a></li><li><a href="index.html#boxes">The Big Shite</a></li><li><a href="ninja.html">Ninja Box</a></li><li><a href="not-so-shite.html">Not So Shite</a></li><li><a href="wear-shite.html">Wear Shite</a></li><li><a href="scan.html">Box Scan</a></li></ul></div>
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

# ---- Not So Shite and Wear Shite: the products ----
# EXAMPLES ONLY, for the design preview. Nothing here is agreed with any shop or supplier.
THUMB_ART = '<image href="../assets/brand/unlucky-dip-thumb.svg" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def _thumb(x, y, w):
    return THUMB_ART.format(x=x, y=y, w=w, h=round(w * 25 / 27, 1))


ART = {
    # other shops' things
    "pants": '<path d="M40 38h120v34q-34 6-46 56H86q-12-50-46-56z" fill="#fff"/><path d="M40 54h120"/>'
             '<g stroke="none"><circle cx="66" cy="76" r="6" fill="#F12BA5"/><circle cx="134" cy="76" r="6" fill="#7845F5"/>'
             '<circle cx="100" cy="72" r="6" fill="#A7F12B"/><circle cx="84" cy="96" r="5" fill="#7845F5"/><circle cx="116" cy="96" r="5" fill="#F12BA5"/></g>',
    "socks": '<path d="M78 26h36v62l28 20a15 15 0 0 1-9 27h-22a33 33 0 0 1-33-33z" fill="#fff"/><path d="M78 44h36M78 56h36"/>',
    "choc": '<rect x="42" y="46" width="116" height="72" rx="6" fill="#fff"/><path d="M71 46v72M100 46v72M129 46v72M42 82h116"/>',
    "hotchoc": '<rect x="58" y="62" width="74" height="74" rx="8" fill="#fff"/><path d="M132 78h12a18 18 0 0 1 0 40h-12"/><path d="M82 46q-9-11 0-22M108 46q-9-11 0-22"/>',
    "flowers": '<path d="M100 132V86M100 132 70 96M100 132l30-36"/><circle cx="100" cy="64" r="22" fill="#fff"/><circle cx="62" cy="82" r="18" fill="#fff"/>'
               '<circle cx="138" cy="82" r="18" fill="#fff"/><path d="M80 150h40l-8-30H88z" fill="#fff"/>',
    "plant": '<path d="M100 96V52"/><path d="M100 70q-34-4-36-36 34 2 36 36zM100 60q30-8 30-40-32 6-30 40z" fill="#fff"/><path d="M70 96h60l-8 42H78z" fill="#fff"/>',
    "candle": '<rect x="68" y="72" width="64" height="66" rx="6" fill="#fff"/><path d="M100 72V62"/><path d="M100 30q16 18 0 32-16-14 0-32z" fill="#F8FF37"/><path d="M68 94h64"/>',
    "opener": '<circle cx="66" cy="80" r="30" fill="#fff"/><circle cx="66" cy="80" r="12" fill="none"/><rect x="92" y="68" width="84" height="24" rx="12" fill="#fff"/>',
    # our merch
    "tee": '<path d="M70 28 50 38 26 66l20 18 12-10v62h84V74l12 10 20-18-24-28-20-10q-30 22-60 0z" fill="#fff"/>' + _thumb(80, 72, 40),
    "hoodie": '<path d="M68 36q32-26 64 0l34 22-14 30-16-8v58H64V80l-16 8-14-30z" fill="#fff"/><path d="M80 40q20 26 40 0"/><path d="M82 112h36v26H82z"/>' + _thumb(84, 70, 32),
    "sweat": '<path d="M72 32q28 16 56 0l22 10 26 72-22 8-18-44v58H64V78l-18 44-22-8 26-72z" fill="#fff"/>' + _thumb(80, 68, 40),
    "cap": '<path d="M46 104a52 50 0 0 1 104 0z" fill="#fff"/><path d="M148 104h30q10 0 6 9l-4 7q-16-9-36-7z" fill="#fff"/>' + _thumb(80, 64, 34),
    "beanie": '<circle cx="100" cy="40" r="11" fill="#fff"/><path d="M52 108a48 58 0 0 1 96 0z" fill="#fff"/><rect x="44" y="104" width="112" height="30" rx="6" fill="#fff"/>' + _thumb(84, 64, 32),
    "tote": '<path d="M76 62V44a24 24 0 0 1 48 0v18" fill="none"/><rect x="54" y="62" width="92" height="80" fill="#fff"/>' + _thumb(79, 82, 42),
}

# Not So Shite (meeting of 14 Nov, and Scott's voice note): other shops' products that we think are good.
# They are not ours and we never call them "affiliate" on the site. Each gets our own short write-up page,
# then a button to the shop. seller=None means the shop is still to be found.
# The shops named are the ones raised in the meeting as targets. None is a partner yet.
NSS = [
    dict(slug="very-loud-pants", seller="Oddballs", cat="wear", art="pants", name="Very Loud Pants",
         line="Underwear with more personality than whoever's wearing it.",
         pitch="The only loud thing we'd let near you. Bright, comfy, and nobody has to see them. Unless it goes well.",
         why=["Comfy. Properly comfy.", "Louder than your uncle at a wedding.", "A present they'll use every day. Imagine."],
         cta="Get them at Oddballs"),
    dict(slug="chocolate-you-wont-share", seller="Hotel Chocolat", cat="eat", art="choc", name="Chocolate You Won't Share",
         line="The kind you hide from people you love.",
         pitch="Actual good chocolate. You'll say you're saving it. You're not.",
         why=["Tastes like someone tried.", "Gone by Tuesday.", "Makes up for the Shitebox. Nearly."],
         cta="Get it at Hotel Chocolat"),
    dict(slug="flowers-that-say-sorry", seller="Interflora", cat="send", art="flowers", name="Flowers That Say Sorry",
         line="For when the Shitebox went down badly.",
         pitch="You sent them a box of shite. Now send the apology. Turns up at their door, looking like you meant it.",
         why=["Delivered, so you don't have to face them.", "Nicer than you are.", "Works on mums."],
         cta="Send them with Interflora"),
    dict(slug="socks-with-opinions", seller="Oddballs", cat="wear", art="socks", name="Socks With Opinions",
         line="The present you always got. Only good this time.",
         pitch="Everyone gets socks. Nobody gets socks like these. Wear them to something serious.",
         why=["Seen from across the room.", "Both of them match. Each other, at least.", "Still socks. Still useful."],
         cta="Get them at Oddballs"),
    dict(slug="hot-chocolate-that-isnt-dust", seller="Hotel Chocolat", cat="eat", art="hotchoc", name="Hot Chocolate That Isn't Dust",
         line="Actual chocolate. In a mug. Revolutionary.",
         pitch="Not the brown powder from the back of the cupboard. The real stuff, melted, like a grown-up would have it.",
         why=["Made of chocolate. We checked.", "Fixes most Sundays.", "Better than the tea you were going to make."],
         cta="Get it at Hotel Chocolat"),
    dict(slug="a-plant-thats-hard-to-kill", seller="Interflora", cat="send", art="plant", name="A Plant That's Hard To Kill",
         line="We tested this the obvious way.",
         pitch="Green, alive and likely to stay that way. For the friend who has killed everything else.",
         why=["Forgives neglect.", "Makes a room look like someone lives there.", "Outlasts the flowers."],
         cta="Send one with Interflora"),
    dict(slug="a-candle-that-smells-nice", seller=None, cat="house", art="candle", name="A Candle That Smells Nice",
         line="Of something pleasant. Not of a charity shop.",
         pitch="Light it and the room smells like you've got your life together. Nobody needs to know.",
         why=["Smells of something on purpose.", "Hides the smell of the Shitebox.", "Burns for ages."],
         cta="Get one at the shop"),
    dict(slug="a-proper-bottle-opener", seller=None, cat="house", art="opener", name="A Proper Bottle Opener",
         line="Opens bottles. First time. Imagine.",
         pitch="Heavy, simple, works. The opposite of everything else we sell.",
         why=["Opens the bottle.", "That's it.", "That's the whole feature."],
         cta="Get one at the shop"),
]

# Wear Shite (Scott's voice note, 14 Nov): our merch. Our logo and our lines on clothes, printed to order.
WEAR = [  # (art, name, one line, working price)
    ("tee", "The Thumbs-Down Tee", "The logo. On your chest. Says it all.", "£19.99"),
    ("hoodie", "You Get What You're Given Hoodie", "Warm. Smug. Has a pocket for your hands.", "£34.99"),
    ("sweat", "Sarcastic And Superb Sweatshirt", "For people who are both, or think they are.", "£29.99"),
    ("cap", "Just Blame Us Cap", "Wear it when the present goes badly.", "£16.99"),
    ("beanie", "Can't Be Arsed Beanie", "For bad hair days and bad attitudes.", "£14.99"),
    ("tote", "Nifty At Being Thrifty Tote", "For carrying shite home from charity shops.", "£12.99"),
]


def _svg(art, name):
    return (f'<svg viewBox="0 0 200 160" role="img" aria-label="Drawing: {name}" fill="none" stroke="#252525" '
            f'stroke-width="6" stroke-linejoin="round" stroke-linecap="round">{ART[art]}</svg>')


def _sold_by(prod):
    return f"From {prod['seller']}" if prod["seller"] else "Shop to be confirmed"


def nss_card(i):
    prod = NSS[i]
    href = f"nss-{prod['slug']}.html"
    return (f'<li class="prod c{i % 4 + 1}" data-cat="{prod["cat"]}">'
            f'<a class="art" href="{href}" tabindex="-1" aria-hidden="true">{_svg(prod["art"], prod["name"])}</a>'
            f'<div class="body"><p class="by">{_sold_by(prod)}</p><h3><a href="{href}">{prod["name"]}</a></h3>'
            f'<p>{prod["line"]}</p><a class="btn" href="{href}">See why &rarr;</a></div></li>')


def nss_cards(indexes=None):
    return "\n      ".join(nss_card(i) for i in (range(len(NSS)) if indexes is None else indexes))


def nss_page_tokens(i):
    prod = NSS[i]
    others = [(i + k) % len(NSS) for k in range(1, 5)]
    return {
        "P_NAME": prod["name"],
        "P_LINE": prod["line"],
        "P_PITCH": prod["pitch"],
        "P_ART": ART[prod["art"]],
        "P_C": str(i % 4 + 1),
        "P_SOLD": (f"Not ours. Sold by {prod['seller']}." if prod["seller"] else "Not ours. Shop to be confirmed."),
        "P_SELLER": prod["seller"] or "the shop",
        "P_REASONS": "".join(f"<li>{w}</li>" for w in prod["why"]),
        "P_CTA": prod["cta"],
        "P_MORE": nss_cards(others),
    }


def wear_cards():
    return "\n      ".join(
        f'<li class="prod c{(i + 1) % 4 + 1}"><div class="art">{_svg(art, name)}</div>'
        f'<div class="body"><h3>{name}</h3><p>{line}</p>'
        f'<p class="price">{price}<small>+ delivery</small></p>'
        f'<button class="btn" type="button" data-soon>Add to basket</button></div></li>'
        for i, (art, name, line, price) in enumerate(WEAR))


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
    "NAV_WEAR": nav("wear-shite.html"),
    "NSS_PRODUCTS": nss_cards(),
    "NSS_COUNT": str(len(NSS)),
    "WEAR_PRODUCTS": wear_cards(),
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


def fill(html, tokens, name):
    for k, v in tokens.items():
        html = html.replace("{{" + k + "}}", v)
    if "{{" in html:
        raise SystemExit(f"{name}: unresolved token {{{{{html.split('{{')[1][:20]}")
    return html


def build():
    for slug in LIVE:
        out = ROOT / slug
        out.mkdir(exist_ok=True)
        for f in sorted((SRC / slug).iterdir()):
            if f.name.startswith("_"):
                continue  # a template for generated pages, see below
            if f.suffix == ".html":
                (out / f.name).write_text(fill(f.read_text(encoding="utf-8"), TOKENS, f), encoding="utf-8")
            else:
                shutil.copyfile(f, out / f.name)
        # one page per Not So Shite product, from _nss-product.html
        template = (SRC / slug / "_nss-product.html").read_text(encoding="utf-8")
        for i, prod in enumerate(NSS):
            name = f"nss-{prod['slug']}.html"
            (out / name).write_text(fill(template, {**nss_page_tokens(i), **TOKENS}, name), encoding="utf-8")
        print("built", slug, sorted(q.name for q in out.iterdir()))


if __name__ == "__main__":
    build()
