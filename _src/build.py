"""Build the three Unlucky Dip design previews.

Each design keeps its own templates and stylesheet in _src/<design>/.
Copy that must stay identical across designs (FAQ, small print, charities,
the order brief) lives here once and is injected into {{TOKENS}}.

Run:  python _src/build.py
"""
import json
import pathlib
import shutil

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
DESIGNS = {"rave": "Rave Flyer", "dip": "Night Dip", "pop": "Pop Shite"}

CHARITIES = ["British Heart Foundation", "Mind", "YMCA", "Oxfam", "St Barnabas"]

FAQ = [
    ("What is inside?",
     "Stuff. Mostly. Some mundane shite and some novelty shite: three or four items in the Little Shite, five to seven in the Big Shite. "
     "Random, low-value goods. You are paying for the laugh, and we say so before you pay."),
    ("Is any of it second-hand?",
     "Yes. Around 40% of what we send is rescued from charity shops, so some items have had a previous life. "
     "Nothing that could be a hygiene risk is ever second-hand."),
    ("I don't know what to get someone.",
     "Then stop. That's the whole idea. You pick a size, we take the decision, and if it's rubbish you tell them to blame us."),
    ("Can I make it personal?",
     "Yes. Tell us their name, what they're shite at and how harsh we can be, out of 10. We aim the insults accordingly. "
     "Or tell us nothing and take pot luck."),
    ("Will they know what it is before they open it?",
     "Not if you choose incognito mode. The box goes out with nothing on the outside to give it away."),
    ("Which charities?",
     "So far we shop at British Heart Foundation, Mind, YMCA, Oxfam and St Barnabas. We buy from their shops like anyone else. "
     "They haven't endorsed us, and frankly who would."),
    ("Can I return it?",
     "Yes. You have 14 days from delivery to change your mind, and anything faulty or damaged is put right. "
     "This does not affect your statutory rights."),
]

SMALL_SHORT = (
    "<p><strong>The small print.</strong> Some items in every box are second-hand, bought from charity shops. "
    "Nothing that could be a hygiene risk is second-hand. Contents are random and low in value; you are paying for the laugh.</p>"
    "<p>You have 14 days from delivery to change your mind, and faulty or damaged items are put right. "
    "<strong>None of this affects your statutory rights.</strong> <a href=\"small-print.html\">Read all of the small print</a>.</p>"
)

SMALL_FULL = [
    ("What you are buying",
     ["A Shitebox is a mystery box. We choose what goes in it and you do not. The contents are random, low in value and "
      "different every time. Photos and descriptions on this site show the idea, not your box."]),
    ("Second-hand items",
     ["Around 40% of what we send is bought from charity shops, so some items in every box are second-hand.",
      "Nothing that could be a hygiene risk is ever second-hand. Everything is checked and sent intact and safe, if not useful."]),
    ("The charities",
     ["We buy stock from charity shops, including British Heart Foundation, Mind, YMCA, Oxfam and St Barnabas. "
      "The money we spend in their shops is how your order supports them.",
      "We are not partnered with these charities and they have not endorsed us. We do not promise a fixed donation per box."]),
    ("Making it personal",
     ["Telling us about the person getting the box is optional. We use what you tell us to write the jokes for that box, "
      "and for nothing else."]),
    ("Changing your mind",
     ["You can cancel for any reason up to 14 days after your box is delivered. Tell us, send it back, and we refund you."]),
    ("If something is wrong",
     ["If an item arrives broken or the box is damaged, tell us and we will put it right. Disappointing is the product. Broken is not."]),
    ("Who can buy",
     ["Boxes are sold to adults. They are gifts for adults, not toys."]),
]

RIGHTS = "Nothing in this small print affects your statutory rights."

# What comes out of the tub on the Night Dip design. Real finds from the first charity-shop run where we have them.
DIP_ITEMS = [
    "One mug. It says CRAZY UNICORN LADY.",
    "A rubber duck with a troubled expression.",
    "Left glove. Leather. Red. Just the left.",
    "An ornament of a child holding a goose.",
    "A DVD. You have seen it. You did not enjoy it.",
    "A strawberry. It is a cushion. It is damp with shame.",
    "A snow globe about golf.",
    "Somebody's Nan's teacup. No saucer.",
    "A tie. Paisley. Aggressive.",
    "A carved wooden zebra with trust issues.",
    "A money box shaped like a cow.",
    "Novelty glasses. You cannot see out of them.",
]


def logo(href="index.html"):
    return (f'<a class="ud-logo" href="{href}" aria-label="Unlucky Dip, home">'
            '<img src="../assets/brand/unlucky-dip-thumb.svg" alt="" width="36" height="33">'
            '<span>UNLUCKY DIP</span></a>')


def faq_html():
    out = []
    for i, (q, a) in enumerate(FAQ):
        out.append(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>')
    return "\n    ".join(out)


def small_full_html():
    out = []
    for h, paras in SMALL_FULL:
        out.append(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in paras))
    out.append(f'<p class="rights">{RIGHTS}</p>')
    return "\n    ".join(out)


BRIEF = """<form class="brief" onsubmit="event.preventDefault();this.querySelector('[data-done]').hidden=false">
        <div class="f"><label for="b-name">Who is it for?</label><input id="b-name" name="name" autocomplete="off" placeholder="Lucy"></div>
        <div class="f"><label for="b-shite">What are they shite at?</label><input id="b-shite" name="shite" autocomplete="off" placeholder="Running. Bad knee. Won't shut up about it."></div>
        <div class="f range"><label for="b-harsh">How harsh can we be? <output id="b-out">7</output>/10</label><input id="b-harsh" name="harsh" type="range" min="1" max="10" value="7" oninput="document.getElementById('b-out').textContent=this.value"></div>
        <div class="f check"><input id="b-incog" name="incognito" type="checkbox"><label for="b-incog">Incognito mode: nothing on the outside to give it away</label></div>
        <button class="btn" type="submit">Save the brief</button>
        <p class="done" data-done hidden role="status">Brief saved. They have no idea what's coming.</p>
      </form>"""

WA = ('<a class="wa" href="https://wa.me/447000000000?text=Hi%20Unlucky%20Dip" aria-label="Chat on WhatsApp">'
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.1.7a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>'
      "<span>Ask us. We'll try.</span></a>")

# Mailing list: Scott (10 and 11 Nov) wants emails collected this month to test interest before launch.
SIGNUP = """<form class="signup" onsubmit="event.preventDefault();this.querySelector('[data-done]').hidden=false;this.querySelector('input').value=''">
        <label for="su-email">Your email</label>
        <div class="row"><input id="su-email" name="email" type="email" required autocomplete="email" placeholder="you@example.co.uk"><button class="btn" type="submit">Warn me at launch</button></div>
        <p class="fine">One email when we launch. Maybe one more if we think of a joke. Unsubscribe any time.</p>
        <p class="done" data-done hidden role="status">You're on the list. Lower your expectations.</p>
      </form>"""

# Real category counts from the eight till receipts of Saturday 7 November 2026 (83 lines in all).
RECEIPT = [("Ornaments", 16), ("Kitchenware", 15), ("Toys and teddies", 13), ("Homeware", 10),
           ("Accessories", 8), ("Bric-a-brac", 6), ("Books and DVDs", 6), ("Ties and one shirt", 5), ("Odds", 4)]
assert sum(n for _, n in RECEIPT) == 83

TOKENS = {
    "SIGNUP": SIGNUP,
    "RECEIPT_ROWS": "".join(f"<div><dt>{k}</dt><dd>{n}</dd></div>" for k, n in RECEIPT),
    "LOGO": logo(),
    "FAQ": faq_html(),
    "SMALL_SHORT": SMALL_SHORT,
    "SMALL_FULL": small_full_html(),
    "CHARITY_LI": "".join(f"<li>{c}</li>" for c in CHARITIES),
    "CHARITY_TEXT": ", ".join(CHARITIES[:-1]) + " and " + CHARITIES[-1],
    "BRIEF": BRIEF,
    "WA": WA,
    "DIP_ITEMS": json.dumps(DIP_ITEMS, ensure_ascii=False),
    # Item counts are still open (Scott, 7 and 8 Nov: 4 and 7, or 3 and 5, or unstated), so the site gives ranges.
    "COUNT_S": "3 to 4 items",
    "COUNT_B": "5 to 7 items",
    "PRICE_S": "£18.99",
    "PRICE_B": "£27.99",
    "DELIVERY": "UK delivery included",
    "EMAIL": "hello@unluckydip.com",
    "PREVIEW": "Design preview, 11 November 2026. Nothing is for sale yet and the prices are working numbers.",
}


def build():
    for slug in DESIGNS:
        out = ROOT / slug
        out.mkdir(exist_ok=True)
        for f in sorted((SRC / slug).iterdir()):
            if f.name == "extra.css":
                continue
            if f.suffix == ".html":
                html = f.read_text(encoding="utf-8")
                for k, v in TOKENS.items():
                    html = html.replace("{{" + k + "}}", v)
                left = [t for t in html.split("{{")[1:]]
                if left:
                    raise SystemExit(f"{f}: unresolved token {{{{{left[0][:20]}")
                (out / f.name).write_text(html, encoding="utf-8")
            else:
                shutil.copyfile(f, out / f.name)
        print("built", slug, sorted(p.name for p in out.iterdir()))


if __name__ == "__main__":
    build()
