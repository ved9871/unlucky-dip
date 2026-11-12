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
EMAIL = "hello@unluckydip.com"

PAGES = [  # (file, nav label)
    ("index.html#boxes", "The boxes"),
    ("ninja.html", "Ninja Box"),
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
    <div><h4>Shop</h4><ul><li><a href="index.html#boxes">The Little Shite</a></li><li><a href="index.html#boxes">The Big Shite</a></li><li><a href="ninja.html">Ninja Box</a></li><li><a href="scan.html">Box Scan</a></li></ul></div>
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


PREVIEW = "Design preview, 12 November 2026. Nothing is for sale yet and the prices are working numbers."

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
    "FOOTER": footer(),
    "FOOTER_PLAIN": footer(short=False),
    "FAQ": faq_html(),
    "SMALL_SHORT": SMALL_SHORT,
    "SMALL_FULL": small_full_html(),
    "CHARITY_LI": "".join(f"<li>{c}</li>" for c in CHARITIES),
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
