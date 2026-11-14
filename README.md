# unluckydip.com

Website for **unluckydip.com**, home of **Shitebox**: a mystery box of deliberately disappointing presents, around 60% of it upcycled from charity shops. This is a design preview. Nothing is for sale and no form stores anything yet.

**Rave Flyer is the chosen design** (Scott, 11 Nov 2026). Version 5 in `rave/` has his reviews of 11 and 12 Nov applied. The other five designs are kept as they were for reference.

Preview: https://unlucky-dip.prakashved155.workers.dev/

| Page | Link |
| --- | --- |
| Home | [rave/](https://unlucky-dip.prakashved155.workers.dev/rave/) |
| Order ("Set the trap") | [rave/order](https://unlucky-dip.prakashved155.workers.dev/rave/order) |
| Ninja Box | [rave/ninja](https://unlucky-dip.prakashved155.workers.dev/rave/ninja) |
| Box Scan | [rave/scan](https://unlucky-dip.prakashved155.workers.dev/rave/scan) |
| Not So Shite (merch and partner picks) | [rave/not-so-shite](https://unlucky-dip.prakashved155.workers.dev/rave/not-so-shite) |
| WTF is Shitebox? | [rave/wtf](https://unlucky-dip.prakashved155.workers.dev/rave/wtf) |
| Small print | [rave/small-print](https://unlucky-dip.prakashved155.workers.dev/rave/small-print) |

Not chosen, unchanged since 11 Nov: `dip/` (Night Dip), `pop/` (Pop Shite, Scott's second choice), `os/` (Unlucky Dip 98), `maison/` (Maison Shite), `bric/` (Bric-a-Brac).

## What version 4 changed (Scott's review, 11 Nov 2026)

Home page
- Hero is shorter and leads with "You get what you're given." on a purple paint texture (the WTF page keeps the yellow one).
- "Sarcastic and superb." is a tagline under the headline, not an attributed quote.
- "Three sizes of disappointment", with the third shown as coming soon.
- Item counts are gone. Each box card has a size line ready for the real box dimensions.
- No "delivered" or "delivery included" next to a price. Postage (£4.70) is left to the checkout.
- Removed from the home page: the charity shopping run and till-receipt numbers, the certificate, the review quotes, the "not on sale yet" sign-up section and the questions about the victim.
- The second-hand disclaimer is centred.
- The home page is now hero, ticker, the three boxes, one calm white block ("We're nifty at being thrifty!") and the FAQ.

Menu and new pages
- Menu: The boxes, Ninja Box, Box Scan, WTF is Shitebox?, Basket.
- **Ninja Box** (`ninja.html`): the unbranded box. Deep purple page with a black box in the middle and the line "Don't let them know what shite they're about to get."
- **Box Scan** (`scan.html`): replaces "Got a box?". Where people land after scanning, with a box-number field. It does not show or mention what is scanned.
- **Order** (`order.html`): the buying experience. Pick a size, choose loud or Ninja, then the questions about the victim (who, what they're shite at, what they think they're great at, the stupidest thing they've done, harshness out of 10) with a large Randomise button.
- **Not on sale yet** is a pop-up with the email sign-up. It opens from the basket and from "Go to checkout".

WTF page
- Three wording changes as written by Scott, and the 14-day line removed from the short small print.

Copy
- The name is always unluckydip.com, one word, including the logo.
- 40% is now 60%.
- "Upcycled" and "We're nifty at being thrifty!" run through the pages.

## What version 5 changed (Scott's review of version 4, 12 Nov 2026)

- Prices show "+ £4.70 postage" beside them on the home and order pages. Scott confirmed the 14-day wording, and that a Ninja Box costs no extra.
- The Absolute Shite is "£???", the ticker says "Just blame us", and the Ninja Box banner reads "Want to make the shite more of a surprise? Make it a Ninja Box".
- FAQ order: upcycled, what's inside, make it personal, then the rest. One question uses "gift ideas".
- Footer tape redrawn so it no longer cuts off, with torn ends and the unluckydip.com name.
- Ninja Box: new section saying boxes are branded as standard and why you might hide one, "no extra cost", and a more mysterious box (lid open a crack, light leaking, eyes in a slot, blacked-out label).
- Box Scan: Scott's new intro (full Shitebox experience, easter eggs) and "Then there's nothing to scan idiot…".
- WTF page: the five charities show their own logos, set as shop signs (Ved, 12 Nov: use the logos directly). The files in `assets/charities/` come from each charity's own website. The line underneath still says they have not endorsed us.
- A "Shitebox." wordmark sits on the hero picture as a stand-in until Scott's new picture arrives.

## Added 14 November 2026: Not So Shite

- `not-so-shite.html` is the merch and partner section (Ved, 14 Nov). It is the fifth menu link, so the menu drops to its own row below 1080px.
- Products are a list in `_src/build.py` (`PRODUCTS`). Each is either `merch` (sold by us, sent by a supplier: drop shipping or print on demand) or `partner` (an affiliate link out to another shop).
- The twelve products are **examples** with drawn pictures. The real products, suppliers and affiliate partners are not chosen.
- Partner cards carry "Affiliate link. We may earn a commission." and the links use `rel="sponsored nofollow"`. UK advertising rules need affiliate links to be labelled, so keep that when the real ones go in.
- The small print gained a "Not So Shite" section explaining both kinds. That wording was written for the preview and has not been checked legally.
- Scott's feedback from the meetings of 13 and 14 November is **not** applied: the meeting notes could not be read when this was built.

## Rules that still apply

- Logo: the thumbs-down in the four colours, always on white.
- Founders only at the bottom of the WTF page. No names, no location.
- Say "shite", never the other word.
- What is in a box, and what is printed inside it, stays secret.
- Charities: say we buy from their shops. Never imply a donation, partnership or endorsement.

## Before anything is sold

- **Charity logos.** They are on the WTF page without the charities having been asked. They are registered trademarks; if a charity objects, swap its logo for the name in `CHARITY_LOGOS` in `_src/build.py`.
- **Cancelling.** The small print states the 14-day right to cancel, with the buyer paying return postage, and says personalised boxes cannot be cancelled once packing starts. Scott has agreed the wording; it has not been checked by anyone legal.
- **Forms.** The sign-up, order and box-number forms are mock-ups.
- `hello@unluckydip.com` and the WhatsApp number are placeholders.

## Building

Templates and the stylesheet are in `_src/rave/`. Shared copy (menu, footer, FAQ, small print, the pop-up) is in `_src/build.py`.

```
python _src/build.py
```

Deploy the preview to Cloudflare from this folder with `npx wrangler deploy`. `.assetsignore` keeps `_src`, the README and the git folder off the public site.
