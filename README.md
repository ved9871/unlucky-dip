# Unlucky Dip design previews

Six website directions for **Unlucky Dip**, home of **Shitebox** (a mystery box of deliberately disappointing presents, around 40% of it rescued from charity shops). These are design previews for review. Nothing is for sale and no form stores anything yet.

| Design | Home | WTF is Shitebox? | Small print |
| --- | --- | --- | --- |
| 1. Rave Flyer (selected 6 Nov 2026) | [rave/](https://ved9871.github.io/unlucky-dip/rave/) | [wtf](https://ved9871.github.io/unlucky-dip/rave/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/rave/small-print.html) |
| 2. Night Dip | [dip/](https://ved9871.github.io/unlucky-dip/dip/) | [wtf](https://ved9871.github.io/unlucky-dip/dip/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/dip/small-print.html) |
| 3. Pop Shite | [pop/](https://ved9871.github.io/unlucky-dip/pop/) | [wtf](https://ved9871.github.io/unlucky-dip/pop/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/pop/small-print.html) |
| 4. Unlucky Dip 98 (round two) | [os/](https://ved9871.github.io/unlucky-dip/os/) | [wtf](https://ved9871.github.io/unlucky-dip/os/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/os/small-print.html) |
| 5. Maison Shite (round two) | [maison/](https://ved9871.github.io/unlucky-dip/maison/) | [wtf](https://ved9871.github.io/unlucky-dip/maison/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/maison/small-print.html) |
| 6. Bric-a-Brac (round two) | [bric/](https://ved9871.github.io/unlucky-dip/bric/) | [wtf](https://ved9871.github.io/unlucky-dip/bric/wtf.html) | [small print](https://ved9871.github.io/unlucky-dip/bric/small-print.html) |

Gallery: https://ved9871.github.io/unlucky-dip/

## The three directions

1. **Rave Flyer.** A flyer pinned to a wall: hard grid, Anton headlines, yellow, pink, purple and lime. This is the design Scott chose over the pink one because it "needs to be abnormal".
2. **Night Dip.** A lucky-dip stall at a fairground after dark, in the dark teal, cyan and pink of Scott's new background artwork. The hero is a tub you can dip into (press the button), the boxes are raffle tickets and the first shopping run is shown as a till receipt.
3. **Pop Shite.** The site as a comic, matching the pop-art founder portraits. Sections are panels with gutters, narration sits in caption boxes, the boxes are comic covers with the price in the corner and the founders talk in speech bubbles.

### Round two (11 Nov, after the first three were judged too alike)

The second round takes each look from a different kind of real site, using the galleries listed in the `pengsonal/design-inspo` directory as the search space.

4. **Unlucky Dip 98.** The site as an old computer desktop (the Poolsuite and Vacation Inc school). Sections are windows, the menu is the taskbar, the 40% lives in the Recycle Bin, the calm stretch is a Notepad file and the small print is the blue error screen.
5. **Maison Shite.** A luxury house with a straight face: black box on a plinth, fine serif type, roman numerals, hairlines and space. It matches the real packaging plan, a premium black magnetic box with shite inside.
6. **Bric-a-Brac.** The charity shop itself: cardboard, masking tape, price-gun stickers, swing tags on a rail, a clipboard and a till receipt.

Round two also adds two pieces of content from the project notes: a free-box offer for creators, and a line that Shitebox is the first of several Unlucky Dip ranges.

## Feedback applied (Scott, 30 Oct to 11 Nov 2026)

- Rave Flyer selected; a calm stretch about a third of the way down every design, then the loud treatment returns.
- Opening line is the gift problem: "Don't know what to get them? Blame us."
- Founders removed from the home page. They sit at the bottom of the WTF page with the line "We're the founders. Our goal is to help charities and have fun." No names, no location, and every "we're shy" reference is gone.
- "WTF is Shitebox?" replaces the About and Not So Shy naming. The 40% figure and "Having fun. Helping charities." lead that page.
- "How we shop for shite" uses Scott's wording: "Our poorly trained team hunt out the best shite for your boxes from charity shops throughout the UK. When you buy a Shitebox you are supporting charities."
- Charities listed: British Heart Foundation, Mind, YMCA, Oxfam, St Barnabas.
- The line about the card at the bottom of the box is removed. Inserts and jokes stay a surprise.
- The Not So Shy merchandise section and the Hall of Fame are removed for now.
- Small print moved to the footer with its own page, including "This does not affect your statutory rights."
- Two quotes added: "Sarcastic and superb." and the insult-my-husband one. They are labelled "Reviews we're expecting" because nobody has said them yet.
- Logo: thumbs-down in the four colours with the Unlucky Dip text, always on a white background.
- New from the 8 Nov voice notes: an optional order brief (who it's for, what they're shite at, harshness out of 10) and incognito mode (nothing on the outside of the box).
- New from the 10 and 11 Nov voice notes: an email sign-up band, so interest can be tested before launch.
- "Got a box?" is for after opening only: type the box number from the Certificate of Approval. It does not reveal contents on the sales pages.

## Before any of this goes live

- **Reviews.** Publishing invented customer reviews is banned in the UK. Replace the two expected quotes with real ones, or keep the "expecting" label.
- **Charity wording.** We buy stock from charity shops; that is the support. The pages say the charities have not endorsed us and promise no fixed donation. Any "£X per box goes to charity" claim needs a written agreement with that charity first.
- **Delivery.** The pages say UK delivery is included in the price. The current pricing model has no postage line, so either the prices or that sentence has to change.
- **Items per box.** Shown as "3 to 4" and "5 to 7" until the count is decided.
- **Forms.** Sign-up, brief and box-number forms are front-end mock-ups.
- **Contact.** `hello@unluckydip.com` and the WhatsApp number are placeholders.

## How it is built

Plain HTML and CSS, no framework. Words that must match across designs (FAQ, small print, charities, prices, the order brief) live once in `_src/build.py` and are injected into each design's templates.

```
_src/build.py            shared copy and the build step
_src/<design>/           templates and stylesheet for each design
rave/ dip/ pop/ os/ maison/ bric/   built pages (what GitHub Pages serves)
assets/                  logo, founder portraits, backgrounds, certificate, previews
index.html               gallery
```

Rebuild after editing anything in `_src`:

```bash
python _src/build.py
```

Asset credits: founder portraits, splash backgrounds and the Certificate of Approval are by Scott. The thumbs-down shape is adapted from Material Icons (Apache 2.0).
