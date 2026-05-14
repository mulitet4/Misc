from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import ListFlowable, ListItem

OUTPUT = "module2.pdf"

# ── Colours ───────────────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1a2744")
MID_BLUE    = colors.HexColor("#2c4a8c")
ACCENT_BLUE = colors.HexColor("#3d6bbf")
LIGHT_BLUE  = colors.HexColor("#dce8f5")
GOLD        = colors.HexColor("#c8a235")
BOX_BG      = colors.HexColor("#f0f4fb")
QUOTE_BG    = colors.HexColor("#fdf6e3")
WARN_BG     = colors.HexColor("#fff3cd")
GREEN_BG    = colors.HexColor("#e8f5e9")
RED_DARK    = colors.HexColor("#8b0000")
GREY_TEXT   = colors.HexColor("#444444")
LIGHT_GREY  = colors.HexColor("#f5f5f5")
CORRECT_GRN = colors.HexColor("#1b5e20")

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

# ── Styles ────────────────────────────────────────────────────────────────────
SS = getSampleStyleSheet()

def make_style(name, **kw):
    return ParagraphStyle(name, **kw)

sTitle = make_style("sTitle",
    fontName="Helvetica-Bold", fontSize=28, textColor=DARK_BLUE,
    alignment=TA_CENTER, spaceAfter=6, leading=34)
sSubtitle = make_style("sSubtitle",
    fontName="Helvetica", fontSize=14, textColor=MID_BLUE,
    alignment=TA_CENTER, spaceAfter=4, leading=18)
sModuleTag = make_style("sModuleTag",
    fontName="Helvetica-Bold", fontSize=11, textColor=GOLD,
    alignment=TA_CENTER, spaceAfter=2)
sH1 = make_style("sH1",
    fontName="Helvetica-Bold", fontSize=17, textColor=DARK_BLUE,
    spaceBefore=18, spaceAfter=6, leading=22)
sH2 = make_style("sH2",
    fontName="Helvetica-Bold", fontSize=13, textColor=MID_BLUE,
    spaceBefore=12, spaceAfter=4, leading=17)
sH3 = make_style("sH3",
    fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT_BLUE,
    spaceBefore=8, spaceAfter=3, leading=14)
sBody = make_style("sBody",
    fontName="Helvetica", fontSize=10, textColor=GREY_TEXT,
    alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=4, leading=14)
sBullet = make_style("sBullet",
    fontName="Helvetica", fontSize=10, textColor=GREY_TEXT,
    alignment=TA_LEFT, spaceBefore=1, spaceAfter=1, leading=13,
    leftIndent=14, firstLineIndent=-10)
sSubBullet = make_style("sSubBullet",
    fontName="Helvetica", fontSize=9.5, textColor=GREY_TEXT,
    alignment=TA_LEFT, spaceBefore=0, spaceAfter=1, leading=13,
    leftIndent=28, firstLineIndent=-10)
sQuote = make_style("sQuote",
    fontName="Helvetica-Oblique", fontSize=10.5, textColor=colors.HexColor("#5c4000"),
    alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=2, leading=14, leftIndent=12)
sQuoteAttr = make_style("sQuoteAttr",
    fontName="Helvetica-Bold", fontSize=9.5, textColor=colors.HexColor("#7a5500"),
    alignment=2, spaceAfter=2)
sKeyTerm = make_style("sKeyTerm",
    fontName="Helvetica-Bold", fontSize=10, textColor=DARK_BLUE,
    spaceBefore=2, spaceAfter=1, leading=13)
sDefn = make_style("sDefn",
    fontName="Helvetica", fontSize=10, textColor=GREY_TEXT,
    alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=4, leading=14, leftIndent=12)
sExample = make_style("sExample",
    fontName="Helvetica-Oblique", fontSize=9.5, textColor=colors.HexColor("#1a3a5c"),
    alignment=TA_JUSTIFY, spaceBefore=1, spaceAfter=1, leading=13, leftIndent=12)
sCaption = make_style("sCaption",
    fontName="Helvetica-Oblique", fontSize=8.5, textColor=colors.HexColor("#666666"),
    alignment=TA_CENTER, spaceAfter=4)
sQuizQ = make_style("sQuizQ",
    fontName="Helvetica-Bold", fontSize=10.5, textColor=DARK_BLUE,
    spaceBefore=10, spaceAfter=3, leading=14)
sQuizOpt = make_style("sQuizOpt",
    fontName="Helvetica", fontSize=10, textColor=GREY_TEXT,
    spaceBefore=1, spaceAfter=1, leading=13, leftIndent=14)
sQuizCorrect = make_style("sQuizCorrect",
    fontName="Helvetica-Bold", fontSize=10, textColor=CORRECT_GRN,
    spaceBefore=1, spaceAfter=1, leading=13, leftIndent=14)
sQuizExpl = make_style("sQuizExpl",
    fontName="Helvetica-Oblique", fontSize=9.5, textColor=colors.HexColor("#333333"),
    spaceBefore=2, spaceAfter=6, leading=13, leftIndent=14)
sDescQ = make_style("sDescQ",
    fontName="Helvetica-Bold", fontSize=11, textColor=DARK_BLUE,
    spaceBefore=10, spaceAfter=4, leading=14)
sDescA = make_style("sDescA",
    fontName="Helvetica", fontSize=10, textColor=GREY_TEXT,
    alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=4, leading=14)
sFooter = make_style("sFooter",
    fontName="Helvetica", fontSize=8, textColor=colors.grey,
    alignment=TA_CENTER)

# ── Helper builders ───────────────────────────────────────────────────────────
def hr(color=MID_BLUE, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def thin_hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=3, spaceBefore=3)

def sp(n=6):
    return Spacer(1, n)

def h1(text):
    return Paragraph(text, sH1)

def h2(text):
    return Paragraph(text, sH2)

def h3(text):
    return Paragraph(text, sH3)

def body(text):
    return Paragraph(text, sBody)

def bullet(text, sub=False):
    style = sSubBullet if sub else sBullet
    return Paragraph(f"&#8226; {text}", style)

def key_term(term, definition):
    return [Paragraph(term, sKeyTerm), Paragraph(definition, sDefn)]

def example(text):
    return Paragraph(f"<b>Example:</b> {text}", sExample)

def quote_box(text, attribution=""):
    rows = [[Paragraph(f'"{text}"', sQuote)]]
    if attribution:
        rows.append([Paragraph(f"— {attribution}", sQuoteAttr)])
    t = Table(rows, colWidths=[PAGE_W - 2*MARGIN - 1.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), QUOTE_BG),
        ("BOX",        (0,0), (-1,-1), 1.2, GOLD),
        ("LEFTPADDING",(0,0), (-1,-1), 12),
        ("RIGHTPADDING",(0,0),(-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

def info_box(title, content_paras, bg=BOX_BG, border=ACCENT_BLUE):
    rows = [[Paragraph(title, make_style("ibt", fontName="Helvetica-Bold",
                fontSize=10, textColor=DARK_BLUE, spaceAfter=4))]]
    rows += [[p] for p in content_paras]
    t = Table(rows, colWidths=[PAGE_W - 2*MARGIN - 1.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 1.2, border),
        ("LEFTPADDING",(0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0),(-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
    ]))
    return t

def two_col_table(rows, col_ratio=(0.35, 0.65), header_row=None):
    w = PAGE_W - 2*MARGIN - 0.6*cm
    col_widths = [w * r for r in col_ratio]
    style = [
        ("BACKGROUND", (0,0), (-1,0), MID_BLUE if header_row else BOX_BG),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white if header_row else DARK_BLUE),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 9.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_BLUE]),
        ("GRID",       (0,0), (-1,-1), 0.5, colors.HexColor("#bbbbbb")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",(0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]
    tbl_rows = []
    if header_row:
        tbl_rows.append([Paragraph(h, make_style("th", fontName="Helvetica-Bold",
            fontSize=9.5, textColor=colors.white)) for h in header_row])
    for r in rows:
        tbl_rows.append([Paragraph(str(c), make_style("td", fontName="Helvetica",
            fontSize=9.5, textColor=GREY_TEXT, leading=13, alignment=TA_LEFT)) for c in r])
    t = Table(tbl_rows, colWidths=col_widths)
    t.setStyle(TableStyle(style))
    return t

def section_divider(chapter_num, chapter_title):
    data = [[Paragraph(f"CHAPTER {chapter_num}", make_style("cn",
                fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
                alignment=TA_CENTER)),
             Paragraph(chapter_title, make_style("ct",
                fontName="Helvetica-Bold", fontSize=14, textColor=colors.white,
                alignment=TA_CENTER))]]
    t = Table(data, colWidths=[PAGE_W - 2*MARGIN - 0.6*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
        ("LEFTPADDING",(0,0), (-1,-1), 14),
        ("RIGHTPADDING",(0,0),(-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1), 10),
    ]))
    return t

def quiz_option(text, correct=False):
    if correct:
        return Paragraph(f"&#10003; {text}", sQuizCorrect)
    return Paragraph(f"&#9675; {text}", sQuizOpt)

# ── Page template (header/footer) ─────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, PAGE_H - 1.1*cm, PAGE_W, 1.1*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.white)
    canvas.drawString(MARGIN, PAGE_H - 0.7*cm,
        "Marketing in a Digital World  |  Module 2: Promotion")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.7*cm,
        "Gies College of Business, University of Illinois")
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, PAGE_W, 0.9*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GOLD)
    canvas.drawCentredString(PAGE_W/2, 0.3*cm, f"Page {doc.page}")
    canvas.restoreState()

def on_first_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, PAGE_W, 0.9*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GOLD)
    canvas.drawCentredString(PAGE_W/2, 0.3*cm, f"Page {doc.page}")
    canvas.restoreState()

# =============================================================================
# CONTENT
# =============================================================================
story = []

# ── COVER PAGE ────────────────────────────────────────────────────────────────
story += [
    sp(60),
    Paragraph("MARKETING IN A DIGITAL WORLD", sTitle),
    hr(GOLD, 3),
    sp(8),
    Paragraph("MODULE 2: PROMOTION", make_style("mc",
        fontName="Helvetica-Bold", fontSize=22, textColor=MID_BLUE,
        alignment=TA_CENTER, spaceAfter=6)),
    sp(8),
    Paragraph("Complete Study Notes — Textbook Edition", sSubtitle),
    sp(6),
    Paragraph("Gies College of Business · University of Illinois", sModuleTag),
    sp(60),
    thin_hr(),
    sp(6),
    Paragraph("Topics Covered: Promotion Overview · Advertising & Persuasion (ELM) · "
              "User Generated Content (UGC) · Doppelganger Brand Images · "
              "Case Study: GoPro · Wikipedia Exercise · Expert Interview: Rafael Schwarz",
        make_style("cov", fontName="Helvetica", fontSize=9.5,
            textColor=GREY_TEXT, alignment=TA_CENTER, leading=14)),
    sp(6),
    thin_hr(),
    PageBreak(),
]

# ── MODULE OVERVIEW ───────────────────────────────────────────────────────────
story += [
    sp(4),
    section_divider("OVERVIEW", "Module Introduction & Learning Framework"),
    sp(12),
    h1("Module 2 Overview"),
    body("This module examines how the digital revolution has fundamentally altered the way that "
         "products are promoted. New digital tools are enabling customers to take a more active "
         "role in promotion activities. The module introduces the concept of promotion, explores "
         "how promotion is changing, and then examines two core digital concepts: "
         "<b>User Generated Content (UGC)</b> and <b>Doppelganger Brands</b>. "
         "These concepts are applied through a real-world case study (GoPro) and a hands-on "
         "exercise (Wikipedia.org)."),
    sp(8),
    h2("Guiding Questions"),
    body("The following guiding questions frame the module's learning objectives:"),
    bullet("What is User Generated Content, and how can it enhance a firm's promotional activity?"),
    bullet("What is a Doppelganger Brand Image, and how can it hamper a firm's promotional activity?"),
    bullet("How are new digital tools changing the way firms promote their products?"),
    sp(8),
    h2("Key Concepts & Phrases"),
    two_col_table([
        ["Promotion",               "The methods of communication a marketer uses to provide information about its products or services"],
        ["Advertising",             "The most historically popular promotional technique; aims to elicit a response from consumers"],
        ["Persuasion",              "The primary goal of most promotional campaigns; convincing consumers to buy over competitors"],
        ["User Generated Content",  "Online ideas about a product created and disseminated by the product's customers, not the firm"],
        ["Doppelganger Brand Image","A collection of dispiriting images and stories about a brand circulated by anti-brand activists"],
        ["ELM",                     "Elaboration Likelihood Model — the leading theory of persuasion with two routes: central and peripheral"],
    ], header_row=["Term", "Brief Description"]),
    PageBreak(),
]

# ── CHAPTER 1: PROMOTION OVERVIEW ────────────────────────────────────────────
story += [
    section_divider("1", "Promotion Overview"),
    sp(12),
    h1("1. Promotion Overview"),
    sp(4),
    h2("1.1 What Is Promotion?"),
    body("Promotion is the second of the Four Ps of marketing. It encompasses the <b>methods of "
         "communication</b> that a marketer uses to provide information about its products or "
         "services. This information is typically <b>persuasive in nature</b>, with the goal of "
         "getting customers to buy a particular product instead of its competitors' offerings."),
    body("Promotional information can be both verbal and visual in nature. As a result, a promotion "
         "strategy can influence consumers by appealing to either their <b>intellect</b> (rational, "
         "fact-based) or to their <b>emotions</b> (feelings, desires, identity)."),
    sp(6),
    h2("1.2 Advertising"),
    body("Historically, the most popular promotional technique has been <b>advertising</b>, with "
         "television advertising accounting for the largest portion of most firms' promotional "
         "budgets. Although digital advertising now exceeds traditional advertising in total "
         "spending, TV advertising remains a major element in many firms' advertising budgets."),
    sp(4),
    info_box("Key Advertising Facts", [
        bullet("Many large firms pay over <b>$7 million</b> for a 30-second advertisement during the Super Bowl each year."),
        bullet("Most advertising focuses on existing and potential customers."),
        bullet("Advertising can also be targeted toward a firm's <b>distribution channel partners</b> (e.g., retailers) and used to <b>build morale among employees</b>."),
        bullet("The goal of advertising is to elicit some form of <b>response</b> — awareness, perception change, or purchase intent."),
        bullet("A new brand may focus on <b>developing awareness</b>; an established brand may focus on <b>changing perceptions</b>."),
    ]),
    sp(6),
    h3("The Advertising Process"),
    body("Most advertisements are carefully planned and thoroughly developed. The typical process involves:"),
    bullet("<b>Agency hire:</b> A firm typically hires a professional advertising agency to create an advertising campaign."),
    bullet("<b>Pre-testing:</b> Ads are carefully pre-tested before launching (e.g., copy testing), though this process is largely top-down — a small number of customers provide opinions."),
    bullet("<b>Tracking:</b> Once launched, a professional marketing research company tracks the ad to assess its effectiveness and helps decide when a new campaign is needed."),
    sp(6),
    example("Coke has built an incredible degree of awareness and interest in its brand through "
            "over 100 years of effective promotion campaigns. Coke spends approximately "
            "<b>$4 billion</b> each year on advertising, most of it on television. As a result of this "
            "sustained investment, 'Coke' is today the <b>second most recognized word on the "
            "planet</b>, just after the word 'okay.'"),
    sp(8),
    h2("1.3 Persuasion"),
    body("The primary goal of most promotional campaigns is to <b>persuade</b> consumers to buy a "
         "firm's products instead of its competitors'. Marketers employ a number of persuasion "
         "tactics, including:"),
    bullet("Celebrity endorsement"),
    bullet("Humor"),
    bullet("Scientific claims"),
    sp(6),
    h3("1.3.1 The Elaboration Likelihood Model (ELM)"),
    body("The most widely accepted and important theory of persuasion is the "
         "<b>Elaboration Likelihood Model (ELM)</b>. This theory proposes that there are "
         "<b>two main routes to persuasion</b>:"),
    sp(4),
    two_col_table([
        ["Central Route",
         "More cognitive (rational) in nature. Effective when consumers have the ability AND motivation "
         "to process a persuasion message. Persuasion occurs when they find the information to be "
         "newsworthy and believable. Focuses on the substance and logic of the message."],
        ["Peripheral Route",
         "More emotional in nature. Effective when consumers lack the ability or motivation to "
         "process a message. Persuasion occurs when they perceive the provider or the message as "
         "credible and/or attractive. Relies on cues such as a celebrity's appeal, music, or visual imagery."],
    ], header_row=["Route", "Characteristics & When It Works"]),
    sp(6),
    body("Regardless of which route is employed, a persuasion tactic focuses strongly on trying to "
         "convince customers that a product is appealing. It is based on the premise that a firm "
         "just needs to find the right message or the right message provider."),
    sp(8),
    h2("1.4 The Digital Shift: From Selling to Telling"),
    body("Historically, most large firms devoted the bulk of their promotion budget to advertising "
         "developed by professional advertising agencies and aired on television. This was a "
         "fundamentally <b>top-down</b> approach — designed by the firm and pushed to consumers."),
    body("This top-down approach is starting to break down due to the <b>democratization of "
         "digital tools</b>. In this new digital environment, marketing is moving from "
         "<b>'selling' to 'telling.'</b>"),
    sp(4),
    info_box("Case in Point: Tesla vs. General Motors", [
        body("Most large automobile companies spend billions of dollars per year advertising their "
             "products through traditional channels."),
        bullet("Tesla has built a very successful automobile company with <b>very little traditional advertising</b>, "
               "instead promoting its brand via social media channels."),
        bullet("Tesla has nearly <b>25 million followers on X</b> (formerly Twitter); Elon Musk personally "
               "has over <b>185 million followers</b>."),
        bullet("In contrast, General Motors — once the largest company in the world — has <b>fewer than "
               "800,000 followers</b> on X."),
        bullet("The Tesla brand and its products are widely promoted by <b>thousands of fans</b> via "
               "Twitter postings, YouTube videos, and other forms of user-generated content — "
               "without the firm appearing to 'sell' anything."),
    ]),
    PageBreak(),
]

# ── CHAPTER 2: USER GENERATED CONTENT PART 1 ─────────────────────────────────
story += [
    section_divider("2", "User Generated Content (Part 1)"),
    sp(12),
    h1("2. User Generated Content (Part 1)"),
    sp(4),
    quote_box("I'm a big believer in online communities and user-generated content.",
              "Michael Dell, Founder and CEO, Dell Computer Company"),
    sp(8),
    h2("2.1 Background: The Cost Revolution in Promotion"),
    body("Historically, most firms carefully managed the promotion of their products. One key "
         "reason is that promotion has been extremely expensive:"),
    bullet("A 30-second commercial on a national television channel in the US usually costs "
           "<b>hundreds of thousands of dollars</b> just to broadcast."),
    bullet("Since most commercials are shown multiple times, costs quickly <b>multiply into "
           "millions of dollars</b> — and this does not even include the cost of developing "
           "the commercial."),
    sp(4),
    body("The rise of new digital tools has dramatically changed this equation. "
         "Low-cost digital video cameras, free digital editing software, and online broadcasting "
         "platforms such as <b>YouTube</b>, <b>TikTok</b>, and <b>Twitter (X)</b> have made the "
         "creation and dissemination of promotional messages much cheaper and easier than ever before."),
    sp(4),
    body("As a result, a growing number of firms are reducing their promotional costs by leveraging "
         "these tools. Simultaneously, these tools have enabled <b>customers</b> to take a far "
         "more active role in the development and dissemination of promotional materials."),
    sp(4),
    info_box("Scale of Digital Promotion", [
        bullet("There are over <b>600 million Twitter (X) accounts</b> which produce over "
               "<b>500 million tweets per day</b>."),
        bullet("Approximately <b>20% of these tweets are brand-related</b>."),
        bullet("This means that every single day, there are approximately <b>100 million free "
               "promotional messages</b> on Twitter alone."),
        bullet("Today, anyone with an Internet connection, a computer, or an idea can create and "
               "disseminate a promotional message for virtually any product. Digital tools have "
               "<b>democratized the promotional landscape</b>."),
    ]),
    example("Old Milwaukee (a US beer brand) has dramatically reduced its promotional cost by "
            "airing their ads on YouTube instead of television."),
    sp(8),
    h2("2.2 Definition of User-Generated Content (UGC)"),
    body("<b>User-Generated Content (UGC)</b> occurs when a product's customers create and "
         "disseminate online ideas about a product or the firm that markets it. These ideas are "
         "often in the form of text, but also appear as music, photos, or videos."),
    sp(4),
    info_box("Three Key Characteristics of UGC", [
        bullet("<b>1. Contributed by users:</b> The contribution is by users of a product rather than "
               "the firm that sells the product."),
        bullet("<b>2. Creative and additive:</b> It is creative in nature and the user adds something "
               "new — it is not simply sharing or forwarding existing content."),
        bullet("<b>3. Online and accessible:</b> It is posted online and is generally accessible to others."),
        body("Note: An email that merely transmits a link to a YouTube video created by someone "
             "else is <b>NOT UGC</b>. Typically, UGC is non-commercial in nature and does not "
             "make any direct promotional appeals. It is therefore a very indirect and subtle "
             "form of product promotion."),
    ]),
    sp(8),
    h2("2.3 Examples of UGC in Practice"),
    body("The following are prominent real-world examples of firms that strategically encourage "
         "and leverage UGC. Note that UGC also occurs frequently without a firm's encouragement "
         "or approval — such as when travelers post restaurant or hotel reviews on sites like Travelocity."),
    sp(4),
    h3("GoPro"),
    body("GoPro is a California-based company that develops and sells <b>high-definition, compact, "
         "durable cameras</b> used by extreme sport enthusiasts such as mountain bikers, windsurfers, "
         "and skydivers to capture their adventures. GoPro's cameras are relatively inexpensive and "
         "often mounted on helmets or bodies for a first-person perspective."),
    body("GoPro's UGC strategy centers on <b>holding contests</b> that ask customers to submit "
         "photos or videos taken with their cameras. These submissions provide:"),
    bullet("A steady stream of fresh content to GoPro's social media channels."),
    bullet("A highly persuasive form of promotion by demonstrating the value of owning a GoPro camera "
           "through real user footage."),
    sp(4),
    h3("Warby Parker"),
    body("Warby Parker is a manufacturer and retailer of eyeglasses with few physical retail "
         "locations that conducts most of its business online. The company offers a service called "
         "<b>Home Try-On</b>, in which five different pairs of glasses are mailed to customers. "
         "Customers can try them for <b>five days</b> and then return the pairs they don't want."),
    body("Warby Parker actively encourages these customers to take photos of themselves and share "
         "these photos on social media using the hashtag <b>#WarbyHomeTryon</b>. Customers do this "
         "to get helpful feedback from their social networks. These shared photos simultaneously "
         "provide Warby Parker with <b>increased exposure and free promotion</b>."),
    sp(4),
    h3("Glossier"),
    body("Glossier is a skincare and beauty products brand (lotions, soaps, makeup) founded in "
         "<b>2014</b>. It is a relatively small brand competing in a very crowded market against "
         "well-established global brands such as <b>Revlon</b>, <b>Estee Lauder</b>, and "
         "<b>L'Oreal</b>. Unable to match these competitors' marketing budgets, Glossier turned "
         "to UGC to level the playing field."),
    body("Glossier leverages the enthusiasm of its loyal brand community by:"),
    bullet("Regularly posting heartwarming stories and selfies from customers."),
    bullet("Customer UGC accounts for approximately <b>one-third of Glossier's Instagram posts</b> "
           "and <b>nearly half of its TikTok videos</b>."),
    bullet("Actively engaging content creators through its blog <b>The Gloss</b>, a dedicated "
           "<b>Slack channel</b>, and a dedicated <b>Reddit forum</b>."),
    sp(8),
    h2("2.4 Three Key Issues Surrounding UGC"),
    sp(4),
    h3("Issue 1: What Are the Different Types of UGC?"),
    body("While most UGC appears on social media platforms such as <b>Facebook</b>, <b>Twitter</b>, "
         "and <b>YouTube</b>, it can also appear on:"),
    bullet("Blogs and discussion forums"),
    bullet("A firm's own website"),
    bullet("E-commerce review sections"),
    body("The most common types of UGC include:"),
    bullet("<b>Blog posts</b> — personal accounts and commentary related to a brand or product."),
    bullet("<b>Product reviews</b> — of all UGC types, product reviews have the "
           "<b>strongest impact on consumer purchasing decisions</b>."),
    bullet("<b>Firm-based invitation submissions</b> — such as Warby Parker's Home Try-On initiative "
           "where the firm explicitly solicits content from customers."),
    bullet("<b>UAIGC (User AI-Generated Content)</b> — a recent and growing development in which "
           "individuals use AI tools such as <b>Canva</b>, <b>ChatGPT</b>, and <b>Midjourney</b> "
           "to help create content."),
    sp(4),
    h3("Issue 2: What Motivates Users to Contribute?"),
    body("The factors that motivate customers to engage in UGC are very similar to the motives "
         "that encourage co-creation. The primary motivations are:"),
    bullet("<b>Social recognition:</b> Being an active contributor on social media platforms like "
           "Facebook or Twitter can provide fame and prestige. A firm profiling a customer's "
           "contribution on its webpage or in advertisements amplifies this recognition."),
    example("The yogurt company Chobani placed customers' tweets on billboard signs across the US."),
    bullet("<b>Financial incentives:</b> Some firms run contests that reward contributors with "
           "cash, gift cards, or other tangible prizes."),
    example("Dunkin' Donuts encourages UGC by holding contests in which consumers submit photos "
            "of themselves consuming its products. Winners receive prizes such as smartphones "
            "and televisions."),
    sp(4),
    h3("Issue 3: What Are the Benefits of UGC?"),
    body("UGC provides firms with several significant benefits:"),
    bullet("<b>Low cost:</b> The content is provided freely by customers, reducing promotional spend significantly."),
    bullet("<b>Drives sales:</b> UGC is positively correlated with product sales."),
    bullet("<b>Higher trust:</b> Research consistently shows that most customers trust UGC more "
           "than traditional paid advertising."),
    bullet("<b>Fresh content:</b> UGC helps meet the firm's need to keep its content fresh and "
           "its website interesting."),
    bullet("<b>Increased web traffic and page views:</b> Websites that feature UGC benefit from "
           "both higher traffic and longer session durations."),
    PageBreak(),
]

# ── CHAPTER 3: USER GENERATED CONTENT PART 2 ─────────────────────────────────
story += [
    section_divider("3", "User Generated Content (Part 2)"),
    sp(12),
    h1("3. User Generated Content (Part 2)"),
    sp(4),
    h2("3.1 Academic Insights on UGC"),
    body("A substantial body of academic research exists on the topic of UGC. The following "
         "two studies represent significant recent contributions to this domain."),
    sp(6),
    h3("Academic Insight 1: UGC vs. FGC on Brand Loyalty"),
    body("<b>Source:</b> Tyrvainen, A. et al. (2023). <i>Journal of Interactive Marketing.</i> "
         "University of Jyvaskyla, Finland."),
    sp(4),
    info_box("Study Overview", [
        body("This study examined the relative impact of <b>User-Generated Content (UGC)</b> versus "
             "<b>Firm-Generated Content (FGC)</b> on brand loyalty."),
        body("<b>Methodology:</b> The researchers conducted a <b>meta-analysis</b> — an extensive "
             "quantitative review of prior research. Specifically, they examined the results of "
             "<b>220 prior academic articles</b> in this domain."),
        body("<b>Key Findings:</b>"),
        bullet("Both UGC and FGC have <b>positive impacts on brand loyalty</b>."),
        bullet("Surprisingly, <b>FGC actually has a stronger impact on brand loyalty than UGC</b>."),
        bullet("The effects of both UGC and FGC are driven by the same three factors: "
               "<b>quality</b>, <b>credibility</b>, and <b>usefulness</b> of the information provided."),
        body("<b>Implication:</b> UGC and FGC are more similar than often assumed. For specific "
             "metrics such as fostering brand loyalty, <b>FGC may actually be preferable to UGC</b>. "
             "This challenges the assumption that UGC is always superior."),
    ]),
    sp(6),
    h3("Academic Insight 2: UGC as a Replacement for Traditional Marketing Research"),
    body("<b>Source:</b> Blasberg, T.R. et al. (2023). <i>International Journal of Marketing "
         "Research.</i> Marketing research executive in Mannheim, Germany."),
    sp(4),
    info_box("Study Overview", [
        body("This study examined the degree to which insights derived from UGC can serve as a "
             "<b>replacement for traditional marketing research techniques</b> such as conjoint analysis."),
        body("<b>Methodology:</b>"),
        bullet("Examined a large dataset of over <b>1 million online product reviews</b> across "
               "<b>50 different product categories</b>."),
        bullet("Developed an AI/machine learning technique to extract information about consumer "
               "evaluations of specific product attributes (e.g., taste, price) from these reviews."),
        bullet("Compared the AI-derived attribute evaluations against results from traditional "
               "<b>conjoint analysis</b> — a common research technique involving direct consumer surveys."),
        body("<b>Key Findings:</b>"),
        bullet("For some product categories (<b>sunglasses</b>, <b>toothbrushes</b>): the AI "
               "technique based on UGC closely matched the results from traditional conjoint analysis."),
        bullet("For other product categories (<b>energy drinks</b>, <b>toothpaste</b>): UGC "
               "provided a poor match to traditional research results."),
        body("<b>Implication:</b> An AI model based on a product's UGC reviews may provide a "
             "<b>quick and inexpensive alternative</b> to traditional consumer preference research, "
             "though it is far from a universal substitute."),
    ]),
    sp(8),
    h2("3.2 Four Practical Recommendations for UGC"),
    body("The following four recommendations provide actionable guidance for firms seeking to "
         "leverage UGC effectively as part of their promotional strategy."),
    sp(4),
    h3("Recommendation 1: Ask to Share"),
    body("Approximately <b>one in every three Internet users</b> has made at least one UGC "
         "contribution. With over <b>5 billion Internet users</b> globally, this means there are "
         "over <b>1.5 billion people</b> who have demonstrated a willingness to contribute their "
         "time, energy, and ideas on behalf of a brand."),
    body("Research on UGC suggests that consumers are <b>more likely to provide favorable "
         "contributions to firms that are active on social media</b> and explicitly encourage "
         "participation. Despite this, the majority of large firms — even those with Facebook "
         "pages and Twitter accounts — treat social media as a <b>one-way communication flow</b>. "
         "Ideally, promotional activity should be a <b>two-sided conversation</b> between a firm "
         "and its customers. The simplest starting point is to <b>directly ask customers to "
         "share their ideas</b>."),
    sp(4),
    h3("Recommendation 2: Be Responsive"),
    body("Once a firm asks for contributions and receives UGC, it must <b>close the loop</b> by "
         "being actively responsive. Failing to acknowledge user contributions discourages future participation."),
    bullet("<b>Dell Computers</b> maintains a dedicated team solely focused on monitoring its "
           "discussion boards and responding to customer postings."),
    bullet("<b>Taco Bell</b> sends gift cards to active social media users who make positive "
           "contributions to their brand."),
    body("By being responsive, firms are significantly more likely to generate higher levels of "
         "UGC in the future."),
    sp(4),
    h3("Recommendation 3: Remember the Pareto Principle"),
    body("The <b>Pareto Principle</b> (the 80/20 rule) originates from Italian economist "
         "<b>Vilfredo Pareto</b>, who observed in <b>1896</b> that 80% of the land in Italy was "
         "owned by 20% of the population. This principle has been found to apply broadly — for "
         "example, 80% of the world's income is controlled by 20% of its population."),
    body("In the context of UGC, this principle is even more concentrated: approximately "
         "<b>90% of UGC content is created by only 10% of contributors</b>. This means not all "
         "contributors are equal — some are far more influential than others."),
    body("Firms should: (a) keep this principle in mind, (b) <b>identify these high-value "
         "influencial contributors</b>, and (c) <b>reward them appropriately</b> to retain their engagement."),
    sp(4),
    h3("Recommendation 4: Integrate UGC with Traditional Promotion"),
    body("UGC and traditional promotions (e.g., TV advertising) are often treated as separate "
         "activities. However, firms can create powerful synergies by <b>linking these two forms "
         "of promotion together</b>."),
    example("Target highlighted its educational initiatives by creating a television advertising "
            "campaign that featured <b>customer-submitted videos</b> capturing the moment their "
            "children opened college admissions letters. This campaign was voted one of the "
            "<b>best ads of the year</b> and generated substantial attention and goodwill for the brand."),
    PageBreak(),
]

# ── CHAPTER 4: CASE STUDY — GOPRO ────────────────────────────────────────────
story += [
    section_divider("4", "Case Study: GoPro"),
    sp(12),
    h1("4. Case Study: GoPro"),
    sp(4),
    h2("4.1 Company Background"),
    body("GoPro is an American manufacturer of portable, high-definition video cameras. "
         "Its cameras are small, sturdy, and highly popular among extreme sports enthusiasts "
         "such as surfers, skateboarders, and skydivers. GoPro cameras are often attached to an "
         "individual's head or helmet, providing a <b>first-person perspective</b> that creates a "
         "vivid, vicarious viewing experience — viewers feel as though they are actually present."),
    sp(4),
    two_col_table([
        ["Founded",       "2002"],
        ["Headquarters",  "San Mateo, California, USA"],
        ["Founder / CEO", "Nick Woodman (holds a bachelor's degree in Visual Arts)"],
        ["First product", "2004 — GoPro Hero: a 35-millimeter camera worn on the wrist; waterproof and capable of underwater photography"],
        ["Video camera",  "2006 — Video version of the Hero camera, introduced alongside a range of mounting accessories (car mounts, bike mounts, helmet mounts)"],
        ["Global reach",  "Available in over 100 countries; field offices in Europe and Asia"],
        ["YouTube",       "Over 11 million subscribers on its YouTube channel"],
        ["Competitors",   "Polaroid, Sony, Xiaomi"],
    ], header_row=["Attribute", "Detail"]),
    sp(6),
    h3("The Funding Origin"),
    body("Nick Woodman raised the initial capital for GoPro by <b>selling beads and shells "
         "on the back of an old VW bus</b>."),
    sp(4),
    h3("The Core Challenge"),
    body("Although GoPro is a well-known and highly regarded brand, its financial performance "
         "has been relatively poor due to increasing competition. Given these financial constraints, "
         "it does not have the resources to invest in traditional marketing campaigns. "
         "Fortunately, thousands of GoPro users are willing to share their videos freely across "
         "social media platforms. GoPro has therefore made leveraging UGC a central component "
         "of its promotional strategy."),
    sp(8),
    h2("4.2 GoPro's UGC Strategy"),
    body("Although GoPro had benefited organically from UGC even before 2010, it was in "
         "<b>2010</b> that it formally made UGC a <b>strategic priority</b>. Its strategy consists "
         "of three pillars:"),
    sp(4),
    h3("Pillar 1: Distribute UGC via Social Media"),
    body("GoPro actively promotes user contributions through social media platforms, especially "
         "its <b>YouTube channel</b> (11+ million subscribers). The channel features a mix of:"),
    bullet("<b>Traditional UGC</b> — videos created independently by everyday users."),
    bullet("<b>Collaborative content</b> — videos produced in cooperation with social media "
           "influencers and extreme sports celebrities. "
           "Example: <b>Shaun White</b>, the famous American snowboarder and skateboarder, "
           "is a frequent GoPro contributor."),
    sp(4),
    h3("Pillar 2: Host UGC Contests"),
    body("GoPro incentivizes content creation through structured contests:"),
    bullet("<b>Million Dollar Challenge</b> — Users submit short videos for a chance to win "
           "a share of a <b>$1 million prize</b> distributed annually. This single contest "
           "attracts thousands of video submissions each year."),
    bullet("<b>GoPro Awards</b> — GoPro recognizes top contributors and showcases winners on "
           "its social media sites, often providing awards such as free GoPro devices. Users "
           "can enter through a dedicated portal on GoPro's website."),
    sp(4),
    h3("Pillar 3: Help Users Create Content"),
    body("To reduce the barrier to entry and improve the quality of UGC, GoPro:"),
    bullet("Provides useful <b>tips and tutorials</b> to potential contributors."),
    bullet("Offers a <b>free music library</b> that contributors can access to add soundtracks "
           "to their videos."),
    sp(8),
    h2("4.3 Case Study Assignment: Questions and Model Answers"),
    body("The following are the three key analytical questions for the GoPro case study, "
         "along with illustrative student responses."),
    sp(4),
    h3("Question 1: What are the secrets behind the success of GoPro's UGC strategy?"),
    body("GoPro's success with UGC stems from several interlocking factors:"),
    bullet("The product itself creates an <b>immersive, first-person perspective experience</b> "
           "that is inherently exciting, authentic, and shareable."),
    bullet("Videos were <b>strategically distributed across multiple social media platforms</b>, "
           "maximizing reach."),
    bullet("<b>Collaborations with celebrities and influencers</b> (e.g., Shaun White) lent the "
           "brand credibility and extended its reach to new audiences."),
    bullet("The <b>Million Dollar Challenge</b> provided strong financial incentives for participation, "
           "while GoPro Awards offered non-financial recognition to top contributors."),
    bullet("By making the product synonymous with extreme adventure, GoPro created a community "
           "of passionate users who were inherently motivated to showcase their experiences."),
    sp(4),
    h3("Question 2: What lessons can other firms learn from GoPro's UGC strategy?"),
    bullet("There is a critical difference between a <b>passive and a deliberate UGC strategy</b>. "
           "Firms should actively design and manage their approach rather than hoping organic "
           "content will appear."),
    bullet("Encouraging participation from <b>customers, influencers, and celebrities</b> can "
           "dramatically expand reach and credibility."),
    bullet("<b>Authentic, organic content</b> often outperforms polished, brand-created content "
           "in terms of consumer trust and engagement."),
    bullet("Providing <b>tools and resources</b> to UGC creators (like GoPro's music library) "
           "lowers the barrier to participation and improves content quality."),
    sp(4),
    h3("Question 3: How could GoPro improve its UGC strategy?"),
    bullet("GoPro could <b>expand beyond extreme sports</b> to appeal to everyday consumers — "
           "normalizing the camera's use in daily life activities such as travel, cooking, "
           "and family events — thus broadening its market."),
    bullet("GoPro could partner with more <b>diverse content communities</b> (e.g., travel vloggers, "
           "wildlife photographers) to diversify its brand image."),
    bullet("Implementing a more robust <b>community feedback loop</b> could help GoPro better "
           "understand what types of UGC resonate most with potential buyers."),
    PageBreak(),
]

# ── CHAPTER 5: DOPPELGANGER BRAND IMAGES PART 1 ──────────────────────────────
story += [
    section_divider("5", "Doppelganger Brand Images (Part 1)"),
    sp(12),
    h1("5. Doppelganger Brand Images (Part 1)"),
    sp(4),
    quote_box("Everyone carries a shadow.", "Carl Jung, Psychologist"),
    sp(8),
    h2("5.1 Introduction"),
    body("The German word <b>doppelganger</b> means <b>'Double Walker.'</b> According to German "
         "folklore, each person has a doppelganger — an evil twin or shadow self — and encountering "
         "it is an omen of misfortune. This concept has been applied to the world of marketing to "
         "describe a related phenomenon driven by the proliferation of digital tools."),
    body("Developing an appealing and distinctive <b>brand image</b> is a critical aspect of a "
         "firm's product strategy. Since few products have large differences in their tangible "
         "features, most branding efforts focus on <b>intangible features</b> and emotional appeals. "
         "While these appeals attract some customers, others may find them inauthentic or offensive."),
    body("In the pre-digital era, a dissatisfied consumer's options were limited: avoid the brand "
         "and tell friends and family. The democratization of digital tools — digital design "
         "software, cameras, editing programs, and the Internet — now allows anyone to "
         "<b>remix or create an alternative version of a brand</b> and broadcast it widely. "
         "This is the foundation of the <b>Doppelganger Brand Image</b>."),
    sp(8),
    h2("5.2 Definition of Doppelganger Brand Image (DBI)"),
    body("A <b>Doppelganger Brand Image (DBI)</b> is a collection of <b>dispiriting images and "
         "stories about a brand</b> circulated in popular culture by a <b>loosely organized "
         "network of anti-brand activists, bloggers, and opinion leaders</b>."),
    body("DBIs are typically directed at <b>well-known brands</b> that are perceived as "
         "<b>lacking authenticity</b> and attempting to create <b>false or misleading emotional "
         "appeals</b> through their promotional activities."),
    sp(8),
    h2("5.3 Three Notable Examples of Doppelganger Brand Images"),
    sp(4),
    h3("Example 1: The New Pepsi Logo (2009)"),
    body("In 2009, Pepsi introduced a new logo. The company paid a well-known design firm "
         "<b>$1 million</b> to create the redesign — which was widely perceived as merely a "
         "minor modification of the existing logo."),
    body("The new logo attracted immediate backlash:"),
    bullet("Several Internet blogs criticized it as a <b>waste of money</b>."),
    bullet("Multiple graphic artists created DBI versions of the logo to depict an <b>obese man</b>, "
           "symbolizing a protest against Pepsi's contribution to health problems."),
    bullet("The DBI initially appeared on the creator's blog with few followers, then was "
           "popularized on <b>BuzzFeed</b> in a feature called <b>'Logos That Look Like Other "
           "Things'</b> — receiving over <b>300,000 views</b>."),
    bullet("The campaign quickly became an <b>Internet meme</b> and significantly amplified "
           "attention on the negative health consequences of consuming Pepsi."),
    sp(4),
    h3("Example 2: United Airlines (2017)"),
    body("In 2017, a passenger on a United Airlines flight in Chicago was <b>forcibly removed</b> "
         "from his seat because he refused a flight attendant's request to give up his seat for a "
         "United employee. A fellow passenger recorded the incident on video and posted it on "
         "social media."),
    body("The video was highly disturbing — it showed a medical doctor being dragged off the "
         "plane by airport police while wildly screaming. The following day, United Airlines' CEO "
         "issued a statement on social media describing the passenger as having been "
         "<b>'re-accommodated.'</b> This euphemistic language attracted intense ridicule and a "
         "large number of DBI responses in both image and word form, significantly damaging the brand."),
    sp(4),
    h3("Example 3: Donald Trump"),
    body("Doppelganger brand images are not limited to corporate brands — they can also target "
         "<b>political brands</b>. Donald Trump has attracted a substantial volume of DBIs targeting:"),
    bullet("His appearance (hair, manner of speaking)"),
    bullet("His brand slogans — anti-Trump activists transformed his signature "
           "<b>'Make America Great Again'</b> slogan (displayed on his iconic red hats) into "
           "variants such as <b>'Make America Mexico Again'</b> and <b>'Make Red Hats Wearable Again.'</b>"),
    sp(8),
    h2("5.4 Three Key Issues Surrounding DBIs"),
    sp(4),
    h3("Issue 1: What Motivates Someone to Create a DBI?"),
    body("Creating a DBI requires a substantial investment of time and energy. The primary "
         "motivating factor is the <b>perception that a brand is being inauthentic</b> — "
         "claiming to be something it is not, or disguising its true nature."),
    body("The anti-Trump DBI campaigns, for example, appear to be motivated by the belief that "
         "he is a dishonest individual who prioritizes his own personal welfare over the welfare "
         "of everyday Americans."),
    body("An important emerging trend: <b>Generative AI</b> is making it significantly easier "
         "to create DBIs. With AI tools available to the general public, the production of "
         "sophisticated anti-brand content requires less skill and effort than ever before. "
         "As a result, brands are expected to face <b>even more doppelgangers in coming years</b>."),
    sp(4),
    h3("Issue 2: What Type of Brands Are Most Susceptible to DBIs?"),
    body("Most DBIs are directed against <b>large, well-known brands</b>, for two reasons:"),
    bullet("Large brands have higher visibility, meaning their business practices are more likely "
           "to attract the attention of anti-brand activists."),
    bullet("DBI campaigns targeting well-known brands attract significantly <b>more attention</b> "
           "than those targeting obscure brands — magnifying the impact."),
    example("Walmart has multiple anti-brand doppelganger initiatives, including viral 'People "
            "of Walmart' videos with millions of views. Target, by contrast, has far fewer such "
            "campaigns despite being a large retailer."),
    sp(4),
    h3("Issue 3: Where Are DBIs Found?"),
    body("DBIs exist at multiple levels of reach:"),
    bullet("<b>Individual-level:</b> Created as a form of personal protest and hosted on "
           "individual blogs, Twitter accounts, or Facebook pages."),
    bullet("<b>Aggregator platforms:</b> Individual content can be picked up by larger media "
           "outlets such as <b>Reddit</b>, <b>Digg</b>, <b>BuzzFeed</b>, or traditional news channels, "
           "dramatically increasing reach."),
    bullet("<b>Dedicated anti-brand sites:</b> Websites such as <b>Adbusters</b> are entirely "
           "dedicated to creating DBIs for a wide variety of brands (McDonald's, Starbucks, "
           "Calvin Klein, and others)."),
    bullet("<b>Brand-specific DBI sites:</b> Some brands attract entire websites dedicated "
           "against them. Walmart, for example, has over a dozen dedicated anti-brand websites "
           "including <b>hell-mart.com</b> and <b>walmartsucks.org</b>."),
    PageBreak(),
]

# ── CHAPTER 6: DOPPELGANGER BRANDS PART 2 ────────────────────────────────────
story += [
    section_divider("6", "Doppelganger Brands (Part 2)"),
    sp(12),
    h1("6. Doppelganger Brands (Part 2)"),
    sp(4),
    h2("6.1 Academic Insights on Doppelganger Brand Images"),
    sp(4),
    h3("Academic Insight 1: The Starbucks DBI Study"),
    body("<b>Source:</b> Eric Arnould and colleagues (University of Wisconsin). This paper "
         "<b>established the concept of the Doppelganger Brand Image</b> in academic literature."),
    sp(4),
    info_box("Study Overview", [
        body("<b>Context:</b> This qualitative study examined the DBI surrounding the "
             "Starbucks brand."),
        body("<b>Methodology:</b>"),
        bullet("Researchers observed and interviewed approximately <b>30 patrons of local "
               "coffee shops</b> in both <b>Wisconsin and Illinois</b>."),
        bullet("Participants were asked what they liked about their local coffee shop. "
               "Starbucks was deliberately <b>never mentioned</b> by the researchers."),
        body("<b>Key Finding:</b> Despite not being prompted, <b>all 30 participants</b> "
             "stated that one of the key reasons they preferred their local coffee shop was "
             "precisely because it was <b>NOT Starbucks</b>."),
        body("They held a negative impression of Starbucks based on the perception that it "
             "lacked authenticity by:"),
        bullet("Attempting to project the image of an intimate, local coffee shop"),
        bullet("While being, in reality, one of the <b>world's largest global brands</b>"),
        bullet("Having shops that lacked any form of local distinction or personality"),
        body("<b>Significance:</b> This study provided the <b>first empirical evidence</b> "
             "that a DBI can have a measurable negative impact on a customer's "
             "<b>willingness to buy a brand</b>."),
    ]),
    sp(6),
    h3("Academic Insight 2: DBIs in the Cannabis Market"),
    body("<b>Source:</b> Coskuner-Balli, G. et al. (2021). <i>Journal of Macromarketing.</i> "
         "Chapman University, California."),
    sp(4),
    info_box("Study Overview", [
        body("<b>Context:</b> The legalization of cannabis (marijuana) across many US states, "
             "including Illinois, has been driven partly by growing research showing it can "
             "treat conditions such as <b>glaucoma</b> and <b>epilepsy</b>. However, the cannabis "
             "industry has historically faced strong negative associations — particularly the "
             "stereotype of users as <b>'stoners'</b> (individuals perceived as constantly "
             "high, lazy, and unproductive). These negative associations constitute a DBI "
             "at the <b>product category level</b>."),
        body("<b>Case Study:</b> The cannabis company <b>MedMen</b>."),
        body("<b>Company's Response — The 'Forget Stoner' Campaign:</b>"),
        bullet("MedMen launched an advertising campaign explicitly designed to <b>reframe the "
               "cannabis user's identity</b> — from 'stoners' to everyday, relatable people."),
        bullet("A prominent example: a large <b>billboard on a Los Angeles highway</b> featured "
               "the image of a <b>stylish, gray-haired older woman</b> with the word <b>'stoner'</b> "
               "crossed out and replaced with the word <b>'grandmother.'</b>"),
        body("<b>Key Insight:</b> Sometimes firms must combat doppelganger brand images at the "
             "level of the <b>entire product category</b>, not just the individual brand. "
             "MedMen's campaign sought to normalize cannabis use and construct a new, "
             "mainstream identity for its users."),
    ]),
    sp(8),
    h2("6.2 Four Practical Recommendations for Managing DBIs"),
    sp(4),
    h3("Recommendation 1: Monitor Digital Cues"),
    body("Firms should view DBIs not only as a threat but also as an <b>opportunity to ensure "
         "brand relevance</b>. Brand managers should:"),
    bullet("Carefully and <b>regularly monitor</b> industry websites, brand-related websites, "
           "social media channels, and review sites for early signs of brand backlash."),
    bullet("Utilize dedicated tools for tracking brand-related conversations, including: "
           "<b>Google Alerts</b>, <b>Topsy</b>, and <b>Brandwatch</b>."),
    sp(4),
    h3("Recommendation 2: Identify and Track Brand Avoiders"),
    body("In addition to monitoring digital channels, firms should actively <b>identify consumers "
         "who are avoiding their brand</b> due to the presence of a DBI. Blogs and anti-brand "
         "websites are productive starting points."),
    body("Once avoiders are identified, firms can conduct targeted research — such as small "
         "in-depth interviews — to determine which specific DBI meanings are resonating most."),
    example("Through a series of small interviews, researchers were able to determine that "
            "coffee shop customers were avoiding Starbucks primarily due to its "
            "<b>lack of authentic personal touch</b>, rather than concerns about product quality."),
    sp(4),
    h3("Recommendation 3: Develop and Test a New Story"),
    body("Once a DBI is identified — even at an early stage — brand managers must be proactive "
         "and craft a <b>new narrative</b> that either directly addresses the DBI or redirects "
         "attention entirely."),
    body("This strategy must be handled carefully: the new story must remain <b>true to the brand</b>. "
         "An inauthentic response will be quickly detected and exploited by anti-brand activists, "
         "potentially amplifying the DBI."),
    example("When the wrinkle-reducing product Botox was first launched, anti-brand activists "
            "created a DBI focused on its potential health risks, propagating claims that Botox "
            "could be fatal. In response, Botox brand managers developed a new campaign that "
            "repositioned the product — not only as safe but as a <b>'miracle of modern medicine.'</b>"),
    sp(4),
    h3("Recommendation 4: Vaccinate Your Brand from the Threat of a DBI"),
    body("DBIs are fundamentally <b>viral campaigns that socially critique inauthentic brands</b>. "
         "A pre-emptive defense strategy is for firms to create their own viral content that "
         "<b>authentically showcases the brand</b>, making it harder for a DBI to gain traction."),
    example("The <b>Will It Blend?</b> campaign by US blender manufacturer <b>Blendtec</b> is a "
            "prime example. In these viral videos, founder <b>Tom Dickinson</b> conducts "
            "humorous experiments attempting to blend objects such as a baseball, a garden hose, "
            "and an iPhone in a Blendtec blender. The videos are simultaneously fun, authentic, "
            "and provide a clear demonstration of the blender's extraordinary performance, "
            "effectively inoculating the brand against criticism."),
    PageBreak(),
]

# ── CHAPTER 7: WIKIPEDIA EXERCISE ────────────────────────────────────────────
story += [
    section_divider("7", "Exercise: Wikipedia.org"),
    sp(12),
    h1("7. Exercise: Wikipedia.org"),
    sp(4),
    h2("7.1 Wikipedia as a UGC Platform"),
    body("Wikipedia is one of the world's most-visited websites, receiving over "
         "<b>10 billion page views every month</b>. It serves as a primary information source "
         "for both college students and academics. Wikipedia represents one of the most "
         "significant and successful examples of user-generated content in existence."),
    sp(4),
    two_col_table([
        ["Founded",          "2001"],
        ["Purpose",          "Free online encyclopedia in which entries can be made by anyone, unsolicited"],
        ["Contrast",         "Traditional encyclopedias (e.g., Encyclopedia Britannica) solicit entries exclusively from recognized experts such as scientists and professors"],
        ["Scale",            "Over 60 million entries across more than 300 different languages"],
        ["Equivalent size",  "It would require over 25,000 volumes of a printed encyclopedia to capture all the information on Wikipedia"],
        ["Monthly traffic",  "Over 10 billion page views per month"],
        ["Contributors",     "Only approximately 2% of Wikipedia users actually make a contribution"],
        ["Structure",        "Not a traditional firm, but has firm-like characteristics: multilevel management hierarchy, develops new product offerings, engages in marketing activity"],
    ], header_row=["Attribute", "Detail"]),
    sp(6),
    body("The statistic that only <b>2% of users contribute</b> while the remaining 98% simply "
         "consume content is a powerful illustration of the Pareto Principle applied to UGC."),
    sp(6),
    h2("7.2 The Wikipedia Exercise"),
    body("The purpose of this exercise is to gain first-hand experience with user-generated "
         "content and to develop a deeper appreciation of how UGC works in practice."),
    sp(4),
    h3("Exercise Steps"),
    bullet("1. Visit <b>wikipedia.org</b> and select a language."),
    bullet("2. Navigate to the <b>Help page</b> to understand how to edit an article."),
    bullet("3. Choose an article of interest and identify a gap or improvement opportunity. "
           "Research to confirm that the planned addition is unique to the entry."),
    bullet("4. Optionally <b>create an account</b> (requires: username, password, email). "
           "Registered accounts have a <b>greater chance</b> of edits being retained."),
    bullet("5. Make your edits to the existing entry."),
    bullet("6. Return approximately <b>one day later</b> to check whether the edit survived or was "
           "modified by other editors."),
    sp(4),
    h3("Assignment Reflection Questions"),
    bullet("Record the Wikipedia entry name and URL."),
    bullet("Explain why you chose this particular topic."),
    bullet("Describe what happened to your contribution — was it retained, modified, or removed?"),
    bullet("What did you learn about the nature of UGC from this exercise?"),
    sp(4),
    h3("Sample Student Response"),
    body("One student contributed a new entry on <b>finger tracking via laptop webcam</b> — "
         "a novel, instrument-free approach that had not yet been documented. The student noted "
         "that the exercise illustrated an important limitation of UGC: <i>\"people can post "
         "utter gibberish on it, so we must be careful as to what to trust.\"</i> This reflects "
         "a real tension in UGC platforms: <b>openness and accessibility come at the cost of "
         "accuracy and reliability</b>."),
    PageBreak(),
]

# ── CHAPTER 8: EXPERT INTERVIEW — RAFAEL SCHWARZ ─────────────────────────────
story += [
    section_divider("8", "Expert Interview: Rafael Schwarz on UGC"),
    sp(12),
    h1("8. Expert Interview: Rafael Schwarz on User-Generated Content"),
    sp(4),
    info_box("About the Expert", [
        bullet("<b>Name:</b> Rafael Schwarz"),
        bullet("<b>Role:</b> Managing Director, Territory Influence, Munich, Germany"),
        bullet("<b>Experience:</b> 15 years in marketing (industry side, leading consumer goods companies); "
               "7 years on the agency side, leading a team of approximately 40 people across Europe"),
        bullet("<b>Specialization:</b> Influencer marketing campaigns, UGC strategy"),
    ]),
    sp(8),
    h2("8.1 What Does UGC Mean to You?"),
    body("Rafael defines UGC broadly: any type of content that consumers <b>publish online based "
         "on actual usage</b> of a brand, product, or service. His definition encompasses:"),
    bullet("<b>Photos and videos</b> published on social media platforms"),
    bullet("<b>Ratings and reviews</b> published on e-commerce sites (e.g., Amazon) or "
           "dedicated review portals"),
    bullet("<b>Recommendations on social platforms</b> — including content shared in "
           "private Facebook groups, WhatsApp messages, messengers, and closed forums"),
    body("This broad definition is noteworthy: UGC is not limited to public social media posts. "
         "It includes all forms of peer-to-peer communication about a brand that occur online, "
         "even in closed or semi-private spaces."),
    sp(8),
    h2("8.2 Which Companies Use UGC Well?"),
    body("Rafael identifies multiple strong examples of firms leveraging UGC effectively:"),
    bullet("<b>Pampers:</b> Actively works with consumers and encourages them to publish "
           "product recommendations."),
    bullet("<b>Food brands:</b> Many encourage consumers to share <b>recipes online</b>, "
           "generating a constant stream of authentic, product-related content."),
    bullet("<b>Consumer electronics brands:</b> Encourage users to publish <b>how-to tutorials</b> "
           "and video tutorials, which serve as both promotion and customer education."),
    body("The common thread among these examples is that the firms <b>recognize UGC's ability "
         "to provide credibility, authenticity</b>, and superior conversion rates compared to "
         "brand-created content."),
    sp(8),
    h2("8.3 What Motivates Consumers to Create UGC?"),
    body("Rafael's organization conducted a dedicated research study on consumer motivations for UGC. "
         "The findings were illuminating:"),
    sp(4),
    info_box("Key Motivation Research Findings", [
        bullet("Over <b>80% of consumers</b> create UGC because they want to <b>help others "
               "make better decisions</b> — a fundamentally altruistic, intrinsic human motivation."),
        bullet("A significant portion create content to <b>support and praise brands they love</b>, "
               "expressing genuine enthusiasm."),
        bullet("Only <b>27% of consumers</b> publish content to express <b>dissatisfaction</b> "
               "with a product or service."),
        body("<b>Implication:</b> The common assumption that most online reviews are driven by "
             "negative experiences is <b>incorrect</b>. The majority of UGC is driven by positive "
             "motivations — a desire to help and to share enthusiasm."),
    ]),
    sp(8),
    h2("8.4 Key Tips for Marketers on UGC"),
    body("Rafael offers two primary strategic recommendations for marketers:"),
    sp(4),
    h3("Tip 1: Think About UGC Across the Entire Purchase Funnel"),
    body("Many companies recognize that UGC (particularly reviews) is important for driving "
         "<b>conversion at the bottom of the funnel</b> (i.e., at the point of purchase). "
         "However, UGC has value at every stage of the consumer journey:"),
    bullet("<b>Top of funnel:</b> Increases visibility through social media content."),
    bullet("<b>Middle of funnel:</b> Serves as a source of inspiration and education about "
           "how to use products and services."),
    bullet("<b>Bottom of funnel:</b> Drives purchase conversion through trusted peer reviews."),
    body("Firms should identify <b>all touch points</b> where UGC can be actively leveraged — "
         "not just at the final purchase stage."),
    sp(4),
    h3("Tip 2: Actively Motivate Consumers to Create UGC"),
    body("Rather than passively waiting for UGC to appear, firms should <b>actively reach out</b> "
         "to their loyal, enthusiastic customers and motivate them to publish positive "
         "recommendations online. One effective approach is to build entire "
         "<b>communities of brand advocates</b>:"),
    bullet("These communities continuously publish recommendations online."),
    bullet("They create a constant stream of UGC touch points across different social media "
           "platforms and relevant e-commerce platforms."),
    bullet("This ensures that the brand maintains high visibility and strong conversion rates across channels."),
    sp(8),
    h2("8.5 How Should Brands Handle Negative UGC?"),
    body("Rafael identifies two critical actions for managing negative UGC:"),
    sp(4),
    h3("Action 1: Make It Easy for Consumers to Raise Concerns Directly"),
    body("The more difficult a firm makes it for consumers to reach it directly (through hotlines, "
         "social media channels, or customer service), the <b>more likely consumers are to "
         "voice their dissatisfaction publicly</b>. Frictionless complaint channels keep "
         "negative feedback private and manageable."),
    sp(4),
    h3("Action 2: React Quickly and Visibly"),
    body("Consumers who share a negative experience <b>expect brands to respond</b> — and to "
         "do so within <b>24 to 48 hours</b>. A prompt, genuine response can have a positive effect:"),
    bullet("Consumers who feel heard may <b>voluntarily revise a negative rating upward</b> "
           "because the company demonstrated it was listening."),
    bullet("Consumers who learn something useful from the brand's response may leave a "
           "<b>more positive review</b> in the future."),
    sp(8),
    h2("8.6 The Future of UGC"),
    body("Rafael identifies two macro trends that will drive the continued growth of UGC:"),
    sp(4),
    h3("Trend 1: Growing Distrust in Traditional Media and Advertising"),
    body("Consumer distrust in <b>traditional media</b>, advertising, and official organizations "
         "is increasing. Because <b>people trust other people</b>, UGC will become an increasingly "
         "important and preferred source of information and guidance."),
    sp(4),
    h3("Trend 2: The Rise of E-Commerce and Social Commerce"),
    body("The shift toward e-commerce (accelerated significantly by the COVID-19 pandemic) has "
         "exposed how heavily brands relied on traditional content creation models. The pandemic "
         "also revealed an underutilized resource: millions of consumers who can create "
         "high-quality content <b>anytime, anywhere using their smartphones</b>."),
    body("Rafael's conclusion: <i>'Why should companies spend millions on advertising production "
         "when they could get much more authentic and credible content from users at a fraction "
         "of the cost?'</i>"),
    PageBreak(),
]

# ── CHAPTER 9: QUIZ QUESTIONS & ANSWERS ──────────────────────────────────────
story += [
    section_divider("9", "Quiz Questions & Answers"),
    sp(12),
    h1("9. Quiz Questions & Answers"),
    sp(4),
    h2("9.1 Quiz: Promotion Overview"),
    sp(4),
    Paragraph("Q1. Promotion is defined as the methods of communication that a marketer uses to provide information about its product.", sQuizQ),
    quiz_option("False"),
    quiz_option("True", correct=True),
    Paragraph("Explanation: Promotion encompasses the methods of communication a marketer uses to provide information about its products or services, typically persuasive in nature.", sQuizExpl),
    sp(4),
    Paragraph("Q2. According to the lecture, what is the second most recognized word in the world?", sQuizQ),
    quiz_option("Coke", correct=True),
    quiz_option("Fine"),
    quiz_option("OK"),
    quiz_option("Good"),
    Paragraph("Explanation: Due to over 100 years of sustained advertising spending (~$4 billion/year), 'Coke' is the second most recognized word on the planet, behind only the word 'okay.'", sQuizExpl),
    sp(6),
    h2("9.2 Quiz: User Generated Content"),
    sp(4),
    Paragraph("Q1. Which of the following is a characteristic of User-Generated Content (UGC)?", sQuizQ),
    quiz_option("The contribution is by users of a product rather than the firm that sells this product."),
    quiz_option("It is creative in nature and the user adds something new."),
    quiz_option("It is posted online and generally accessible."),
    quiz_option("All of the above.", correct=True),
    Paragraph("Explanation: UGC has all three characteristics: it must be by a user (not the firm), it must be creative/additive, and it must be posted online and publicly accessible.", sQuizExpl),
    sp(4),
    Paragraph("Q2. User-Generated Content (or UGC) is non-commercial in nature and doesn't make any direct promotional appeals.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: UGC is typically non-commercial and indirect. A direct promotional appeal (e.g., a paid sponsored post) would not qualify as true UGC.", sQuizExpl),
    sp(6),
    h2("9.3 Quiz: Doppelganger Brand Images"),
    sp(4),
    Paragraph("Q1. A Doppelganger Brand Image (DBI) is a collection of disparaging images and stories about a brand circulated in popular culture by a loosely organized network of anti-brand activists, bloggers, and opinion leaders.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: This is the formal academic definition of a DBI, established in the Starbucks study.", sQuizExpl),
    sp(4),
    Paragraph("Q2. Doppelganger brand images are usually focused on well-known brands that are viewed as lacking authenticity and trying to create false or misleading emotional appeals through their promotional activities.", sQuizQ),
    quiz_option("False"),
    quiz_option("True", correct=True),
    Paragraph("Explanation: DBIs target brands perceived as inauthentic. Large, well-known brands are most susceptible because their visibility makes inauthenticity more noticeable and anti-brand campaigns attract more attention.", sQuizExpl),
    sp(6),
    h2("9.4 Quiz: Wikipedia Exercise"),
    sp(4),
    Paragraph("Q1. Which of the following statement about Wikipedia is CORRECT?", sQuizQ),
    quiz_option("Wikipedia.org was launched in 2000."),
    quiz_option("Entries on Wikipedia.org can only be made by experts and scientists."),
    quiz_option("Wikipedia.org has about 100 million readers per month."),
    quiz_option("Wikipedia.org has cumulated over 60 million entries across over 300 different languages.", correct=True),
    Paragraph("Explanation: Wikipedia was launched in 2001 (not 2000), allows contributions from anyone (not only experts), and has over 10 billion monthly views (not 100 million). The 60 million entries across 300+ languages is the correct fact.", sQuizExpl),
    sp(4),
    Paragraph("Q2. Where can you find information on how to edit an article on wikipedia.org?", sQuizQ),
    quiz_option("Contact page"),
    quiz_option("Help", correct=True),
    quiz_option("Community portal"),
    quiz_option("About Wikipedia"),
    Paragraph("Explanation: The Help page contains all guidance on how to edit, create, and manage Wikipedia articles.", sQuizExpl),
    sp(4),
    Paragraph("Q3. You can only make edits to articles on wikipedia.org when you have an account.", sQuizQ),
    quiz_option("True"),
    quiz_option("False", correct=True),
    Paragraph("Explanation: Anyone can edit Wikipedia without an account, though creating an account increases the likelihood that edits will be retained by the community.", sQuizExpl),
    sp(4),
    Paragraph("Q4. How do you publish edits made on an existing entry on wikipedia.org?", sQuizQ),
    quiz_option("By clicking Publish changes", correct=True),
    quiz_option("Edits will be published automatically after a certain amount of time."),
    quiz_option("By clicking Show review"),
    quiz_option("By clicking Show changes"),
    Paragraph("Explanation: After making edits in the Wikipedia editor, you click 'Publish changes' to submit them for public view.", sQuizExpl),
    sp(4),
    Paragraph("Q5. What information do you need to provide in order to create a wikipedia.org account? (Select all that apply)", sQuizQ),
    quiz_option("Username", correct=True),
    quiz_option("Password", correct=True),
    quiz_option("Email", correct=True),
    quiz_option("Address"),
    Paragraph("Explanation: Creating a Wikipedia account requires a username, password, and email address. A physical address is not required.", sQuizExpl),
    sp(4),
    Paragraph("Q6. How does allowing users to contribute to its website help promote Wikipedia as an organization?", sQuizQ),
    Paragraph("Sample Answer: Allowing user contributions promotes community engagement and collective knowledge-building, strengthening Wikipedia's credibility and global reach. It enables Wikipedia to maintain a vastly larger and more current knowledge base than any expert-curated encyclopedia could, reinforcing its brand as the world's most accessible and comprehensive free information source.", sQuizExpl),
    sp(6),
    h2("9.5 Module 2 Comprehensive Quiz"),
    sp(4),
    Paragraph("Q1. Promotion entails which of the following activities?", sQuizQ),
    quiz_option("Personal selling"),
    quiz_option("Sales promotion"),
    quiz_option("Word of mouth"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: Promotion encompasses personal selling, sales promotion, and word of mouth, as well as advertising.", sQuizExpl),
    sp(4),
    Paragraph("Q2. Which of the following is NOT mentioned in the videos as a company that utilizes UGC?", sQuizQ),
    quiz_option("Little big planet"),
    quiz_option("Warby Parker"),
    quiz_option("Camelbak", correct=True),
    quiz_option("GoPro"),
    Paragraph("Explanation: Camelbak (the hydration products company) was not mentioned. GoPro, Warby Parker, Glossier, and Little Big Planet were all cited as UGC examples.", sQuizExpl),
    sp(4),
    Paragraph("Q3. Of all the different types of UGC, product reviews appear to have the strongest impact on consumer purchasing decisions.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: Among all UGC types (blog posts, social media posts, firm-based invitation submissions), product reviews are the most influential on purchase decisions.", sQuizExpl),
    sp(4),
    Paragraph("Q4. GoPro strategically uses UGC by holding contests that ask their customers to submit:", sQuizQ),
    quiz_option("Photos or videos that they have taken with their cameras", correct=True),
    quiz_option("Articles and papers"),
    quiz_option("Actual items"),
    quiz_option("None of the above"),
    Paragraph("Explanation: GoPro's Million Dollar Challenge and GoPro Awards contests specifically ask users to submit photos and videos captured with their GoPro cameras.", sQuizExpl),
    sp(4),
    Paragraph("Q5. Which of the following is NOT a benefit of User-Generated Content (UGC)?", sQuizQ),
    quiz_option("Enhanced technological performance", correct=True),
    quiz_option("Helps keep a firm's content fresh"),
    quiz_option("Low cost"),
    quiz_option("Positively related to product sales"),
    Paragraph("Explanation: The documented benefits of UGC are: low cost, positive correlation with sales, higher consumer trust than paid advertising, fresh content, and increased web traffic. Enhanced technological performance is not a benefit of UGC.", sQuizExpl),
    sp(4),
    Paragraph("Q6. The practical recommendations for managing Doppelganger Brand Images include which of the following?", sQuizQ),
    quiz_option("Monitor digital cues"),
    quiz_option("Identify and track brand avoiders"),
    quiz_option("Develop and test a new story"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: All four recommendations apply: (1) Monitor digital cues, (2) Identify and track brand avoiders, (3) Develop and test a new story, (4) Vaccinate your brand from the threat of a DBI.", sQuizExpl),
    sp(4),
    Paragraph("Q7. What is the meaning of the word 'Doppelganger'?", sQuizQ),
    quiz_option("Double person"),
    quiz_option("Double trouble"),
    quiz_option("Double walker", correct=True),
    quiz_option("None of the above"),
    Paragraph("Explanation: 'Doppelganger' is a German word meaning 'Double Walker.' In German folklore, it refers to a person's evil twin or shadow self.", sQuizExpl),
    sp(4),
    Paragraph("Q8. As discussed in the lecture, which of the following is NOT an example of a brand targeted by a Doppelganger Brand Image?", sQuizQ),
    quiz_option("New Pepsi Logo"),
    quiz_option("United Airlines"),
    quiz_option("FUH2 Campaign"),
    quiz_option("Coca Cola", correct=True),
    Paragraph("Explanation: The three DBI examples discussed in the lecture were the New Pepsi Logo (2009), United Airlines (2017 incident), and Donald Trump's brand slogans. Coca-Cola was not cited as a DBI target in this module.", sQuizExpl),
    sp(4),
    Paragraph("Q9. Approximately how many different languages is Wikipedia available in?", sQuizQ),
    quiz_option("100"),
    quiz_option("200"),
    quiz_option("10"),
    quiz_option("300", correct=True),
    Paragraph("Explanation: Wikipedia currently has over 60 million entries available across more than 300 different languages.", sQuizExpl),
    sp(4),
    Paragraph("Q10. As discussed in the reading by Holt (2016), in 2011 Coca-Cola announced a new marketing strategy called:", sQuizQ),
    quiz_option("Solid & Linked"),
    quiz_option("Liquid & Solid"),
    quiz_option("Liquid & Linked", correct=True),
    quiz_option("Chain & Linked"),
    Paragraph("Explanation: According to Holt's (2016) Harvard Business Review article 'Branding in the Age of Social Media,' Coca-Cola announced its 'Liquid & Linked' marketing strategy in 2011.", sQuizExpl),
    PageBreak(),
]

# ── CHAPTER 10: DESCRIPTIVE QUESTIONS ────────────────────────────────────────
story += [
    section_divider("10", "Descriptive Questions & Model Answers"),
    sp(12),
    h1("10. Descriptive Questions & Model Answers"),
    body("The following descriptive questions are representative of exam-style questions "
         "for 3–4 marks each. A comprehensive answer should address all components and "
         "demonstrate understanding of key terminology."),
    sp(8),
    Paragraph("DQ1. Define promotion and explain the two routes of persuasion described by the Elaboration Likelihood Model (ELM). [3 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("<b>Promotion</b> is the component of the marketing mix that encompasses the methods of "
         "communication a marketer uses to provide information about its products or services. "
         "This information is typically persuasive in nature, with the goal of getting customers "
         "to purchase a firm's products over competitors'. Promotional strategies can appeal to "
         "consumers' intellect (rational) or emotions."),
    body("The <b>Elaboration Likelihood Model (ELM)</b> is the most widely accepted theory of "
         "persuasion and proposes two routes:"),
    bullet("<b>Central Route:</b> Cognitive in nature. Effective when consumers have both the "
           "ability and motivation to process a persuasive message. Persuasion occurs when the "
           "message is found to be newsworthy and credible. This route relies on the quality "
           "and logic of the argument."),
    bullet("<b>Peripheral Route:</b> Emotional in nature. Effective when consumers lack the "
           "ability or motivation to carefully process a message. Persuasion occurs based on "
           "peripheral cues such as the attractiveness or credibility of the message source "
           "(e.g., celebrity endorsements), visual appeal, or background music."),
    body("Both routes ultimately lead to persuasion but through fundamentally different cognitive mechanisms."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ2. Define User-Generated Content (UGC). Explain its three key characteristics and three key benefits to firms. [3 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("<b>User-Generated Content (UGC)</b> occurs when a product's customers create and "
         "disseminate online ideas about a product or the firm that markets it. It typically "
         "takes the form of text, photos, or videos."),
    body("<b>Three Key Characteristics:</b>"),
    bullet("<b>1. User-created:</b> The content is contributed by users (consumers) of a product, "
           "not by the firm that sells it. This distinguishes UGC from firm-generated content (FGC)."),
    bullet("<b>2. Creative and additive:</b> The contributor must add something new and original. "
           "Simply sharing or forwarding existing content (e.g., forwarding a YouTube link via "
           "email) does not constitute UGC."),
    bullet("<b>3. Online and accessible:</b> The content must be posted online where it is "
           "generally accessible to other users."),
    body("<b>Three Key Benefits to Firms:</b>"),
    bullet("<b>1. Low cost:</b> Since content is created freely by customers, firms dramatically "
           "reduce their promotional expenditure."),
    bullet("<b>2. Higher consumer trust:</b> Research consistently shows that consumers trust "
           "UGC more than traditional paid advertising, making it a highly effective promotional vehicle."),
    bullet("<b>3. Drives sales:</b> UGC is positively correlated with product sales and also "
           "increases web traffic and session duration — keeping content fresh and websites engaging."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ3. Define Doppelganger Brand Image (DBI) and explain the three issues that surround it: motivation, susceptibility, and location. [4 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("A <b>Doppelganger Brand Image (DBI)</b> is a collection of dispiriting images and "
         "stories about a brand, circulated in popular culture by a loosely organized network "
         "of anti-brand activists, bloggers, and opinion leaders. DBIs typically target brands "
         "perceived as lacking authenticity and creating false or misleading emotional appeals."),
    body("The term derives from the German word meaning <b>'Double Walker'</b> — in German "
         "folklore, an evil twin or shadow self. The digital era has enabled anyone to remix "
         "or create alternative brand imagery using accessible tools and broadcast it globally."),
    body("<b>Three Key Issues:</b>"),
    bullet("<b>1. Motivation:</b> DBIs are typically motivated by the perception that a brand is "
           "being <b>inauthentic</b> — claiming to be something it is not, or concealing its true "
           "nature. With the rise of generative AI, creating DBIs is becoming significantly "
           "easier, making brands increasingly vulnerable. The Starbucks DBI (studied by Eric "
           "Arnould) exemplifies this: consumers avoided the chain precisely because it "
           "presented itself as a local, intimate coffee shop while being one of the world's "
           "largest global brands."),
    bullet("<b>2. Susceptibility:</b> Large, well-known brands are most susceptible because: "
           "(a) their practices receive greater public scrutiny, and (b) campaigns against "
           "well-known brands attract more attention and viral spread. For example, Walmart "
           "faces dozens of anti-brand initiatives ('People of Walmart' videos, hell-mart.com, "
           "walmartsucks.org), while smaller retailers face comparatively little."),
    bullet("<b>3. Location:</b> DBIs exist at multiple scales — from individual blogs and social "
           "media pages, to aggregator platforms like BuzzFeed and Reddit, to dedicated "
           "anti-brand websites (Adbusters), to brand-specific DBI sites. The Pepsi logo DBI "
           "began on a low-traffic personal blog but gained 300,000 views after being featured "
           "on BuzzFeed — illustrating how platform amplification dramatically increases impact."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ4. Describe GoPro's three-pillar UGC strategy. What were its key success factors, and how can other firms apply these lessons? [4 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("GoPro formally adopted UGC as a strategic priority in <b>2010</b>, despite having "
         "benefited from organic UGC prior to that decision. Its strategy rests on three pillars:"),
    bullet("<b>Pillar 1 — Distribute UGC via Social Media:</b> GoPro actively promotes "
           "user content through its YouTube channel (11+ million subscribers) and other "
           "social media platforms. Content includes both unsponsored everyday user videos "
           "and collaborations with influencers and celebrities such as snowboarder Shaun White."),
    bullet("<b>Pillar 2 — Host UGC Contests:</b> GoPro's Million Dollar Challenge invites "
           "users to submit short videos for a chance to share in a $1 million annual prize. "
           "GoPro Awards provide additional recognition and rewards (including free cameras) "
           "to top contributors. These programs generate thousands of submissions yearly."),
    bullet("<b>Pillar 3 — Help Users Create Content:</b> GoPro reduces the technical and "
           "creative barriers to contribution by providing tips, tutorials, and a free music "
           "library for video soundtracks."),
    body("<b>Key Success Factors:</b> The product itself generates inherently shareable "
         "first-person content; incentives (financial and recognition-based) drive participation; "
         "influencer partnerships extend credibility and reach; accessible creation tools lower "
         "entry barriers."),
    body("<b>Lessons for Other Firms:</b> Move from passive to deliberate UGC strategy; "
         "incentivize both intrinsic (recognition) and extrinsic (financial) motivations; "
         "embrace authentic content over polished brand-created advertising; provide resources "
         "to help users create better content."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ5. Explain the four practical recommendations for managing Doppelganger Brand Images, with examples for each. [4 marks]", sDescQ),
    body("<b>Answer:</b>"),
    bullet("<b>1. Monitor Digital Cues:</b> Brand managers must actively and regularly monitor "
           "social media, brand-related websites, review sites, and industry forums for early "
           "signs of emerging DBIs. Tools such as <b>Google Alerts</b>, <b>Topsy</b>, and "
           "<b>Brandwatch</b> can automate this process. Early detection is critical — a DBI "
           "in its nascent stage is far easier to address than one that has gone viral."),
    bullet("<b>2. Identify and Track Brand Avoiders:</b> Through blogs, anti-brand websites, "
           "and targeted qualitative research (e.g., interviews), firms should identify consumers "
           "who are actively avoiding the brand and understand precisely which aspects of the "
           "DBI resonate with them. Example: Starbucks' research revealed avoidance was "
           "driven by perceived inauthenticity, not product quality concerns."),
    bullet("<b>3. Develop and Test a New Story:</b> Once the DBI is identified, brand managers "
           "must craft a new, authentic counter-narrative. This story must genuinely represent "
           "the brand — inauthenticity will be detected and may amplify the DBI. Example: "
           "Botox countered health-risk claims by repositioning as a 'miracle of modern medicine.'"),
    bullet("<b>4. Vaccinate the Brand:</b> Pre-emptively create authentic viral content that "
           "establishes a positive, credible brand identity before a DBI can take hold. "
           "Example: Blendtec's 'Will It Blend?' series — founder Tom Dickinson humorously "
           "blending bizarre objects — authentically demonstrated product performance and built "
           "a loyal following that effectively inoculated the brand against criticism."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ6. Describe Rafael Schwarz's key insights on what motivates consumers to create UGC and how brands should handle negative UGC. [3 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("Rafael Schwarz, Managing Director of Territory Influence, Munich, has conducted "
         "dedicated research on UGC motivations. His key finding contradicts the popular "
         "assumption that UGC is primarily driven by complaints:"),
    body("<b>Consumer Motivations:</b>"),
    bullet("Over <b>80% of consumers</b> create UGC because they want to <b>help others "
           "make better decisions</b> — a fundamentally altruistic motivation rooted in human "
           "social nature. This finding highlights that the overwhelming majority of UGC "
           "is positively intentioned."),
    bullet("A significant minority create content to <b>express support and affection</b> "
           "for brands they genuinely love."),
    bullet("Only <b>27% create UGC to express dissatisfaction</b>. This figure is important "
           "because it means firms should focus more on activating positive advocates than on "
           "simply managing negative feedback."),
    body("<b>Handling Negative UGC — Two Critical Actions:</b>"),
    bullet("<b>Reduce friction for direct complaint channels:</b> If consumers cannot easily "
           "reach the firm directly, they will vent publicly. Accessible hotlines and social "
           "media channels keep complaints private and constructive."),
    bullet("<b>Respond quickly (within 24–48 hours):</b> Consumers who receive a genuine, "
           "timely response may voluntarily revise a negative rating upward or post a positive "
           "review in the future. Responsiveness signals that the firm is listening and cares "
           "about its customers."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ7. How has the digital revolution shifted the nature of promotion from 'selling' to 'telling'? Use examples to support your answer. [3 marks]", sDescQ),
    body("<b>Answer:</b>"),
    body("Historically, promotion was dominated by a <b>top-down, firm-controlled model</b>. "
         "Firms hired professional advertising agencies, developed expensive campaigns "
         "(a 30-second Super Bowl ad costs over $7 million), pre-tested them on small consumer "
         "samples, aired them on television, and tracked effectiveness through professional "
         "research firms. Consumers were passive recipients of promotional messages."),
    body("The proliferation of <b>digital tools</b> — including low-cost cameras, free editing "
         "software, YouTube, TikTok, and Twitter — has fundamentally disrupted this model by "
         "<b>democratizing the promotional landscape</b>. Today:"),
    bullet("Anyone with an Internet connection and an idea can create and broadcast a "
           "promotional message at negligible cost."),
    bullet("Over <b>600 million Twitter accounts</b> produce <b>500 million tweets per day</b>, "
           "with approximately 20% brand-related — generating roughly <b>100 million free "
           "promotional messages daily</b> on Twitter alone."),
    bullet("Firms like <b>Tesla</b> have built enormously successful brands with minimal "
           "traditional advertising, leveraging social media (25 million Twitter followers) and "
           "fan-generated content. Compare this to <b>General Motors</b>, which despite once "
           "being the world's largest company, has fewer than 800,000 followers."),
    body("The result is a fundamental shift in the nature of promotion: from a firm-controlled, "
         "one-way 'selling' model to a democratized, community-driven 'telling' model where "
         "authentic peer recommendations carry greater weight than polished advertisements. "
         "Firms that understand this shift — building communities, encouraging UGC, and engaging "
         "in genuine two-way dialogue — will be better positioned in the digital promotional landscape."),
    sp(12),
    hr(GOLD, 2),
    sp(8),
    Paragraph("END OF MODULE 2 COMPLETE STUDY NOTES", make_style("end",
        fontName="Helvetica-Bold", fontSize=14, textColor=DARK_BLUE,
        alignment=TA_CENTER, spaceAfter=6)),
    Paragraph("Marketing in a Digital World · Module 2: Promotion · Gies College of Business, University of Illinois",
        make_style("endsub", fontName="Helvetica", fontSize=9, textColor=GREY_TEXT,
            alignment=TA_CENTER, spaceAfter=4)),
    hr(GOLD, 2),
]

# =============================================================================
# BUILD PDF
# =============================================================================
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm,
)

doc.build(
    story,
    onFirstPage=on_first_page,
    onLaterPages=on_page,
)

print(f"PDF generated: {OUTPUT}")
