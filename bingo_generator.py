from html2image import Html2Image
import random
hti = Html2Image()


def generate_bingo(bingo_phrases):
    bingo_phrases = random.sample(bingo_phrases, len(bingo_phrases))
    with open("bingo.html") as f:
        html = f.read().format(*bingo_phrases)
    with open("bingo.css") as f:
        css = f.read()
    hti.screenshot(html_str=html, css_str=css, save_as='bingo_card.png', size=(800, 1000))
