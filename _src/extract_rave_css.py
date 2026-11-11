"""One-off: lift the Rave Flyer v2 stylesheet out of the Sitebox repo, drop the
blocks Scott asked to remove (founders strip on the home page, Not So Shy,
Hall of Fame) and append the v3 additions in extra.css."""
import re, pathlib

here = pathlib.Path(__file__).parent
v2 = pathlib.Path(r"C:\Users\Dell\Documents\Shitebox Project\Sitebox\designs\04-rave-flyer-v2.html").read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", v2, re.S).group(1).strip()

keep = []
skip_block = False
for line in css.splitlines():
    if line.startswith("/* not so shy */"):
        skip_block = True
    if line.startswith("/* hall + faq + footer */"):
        skip_block = False
    if skip_block:
        continue
    if line.startswith((".calm .founders", ".calm .faces", ".hall")):
        continue
    if "@media (max-width:860px){.calm .founders" in line or "@media (max-width:760px){.hall" in line:
        continue
    keep.append(line)

out = "\n".join(keep) + "\n" + (here / "rave" / "extra.css").read_text(encoding="utf-8")
(here / "rave" / "style.css").write_text(out, encoding="utf-8")
print("rave/style.css", len(out), "bytes")
