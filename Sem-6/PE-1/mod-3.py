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

OUTPUT = "module3.pdf"

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

# ── Helpers ───────────────────────────────────────────────────────────────────
def hr(color=MID_BLUE, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def thin_hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=3, spaceBefore=3)

def sp(n=6):
    return Spacer(1, n)

def h1(text): return Paragraph(text, sH1)
def h2(text): return Paragraph(text, sH2)
def h3(text): return Paragraph(text, sH3)
def body(text): return Paragraph(text, sBody)

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

# ── Page template ─────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, PAGE_H - 1.1*cm, PAGE_W, 1.1*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.white)
    canvas.drawString(MARGIN, PAGE_H - 0.7*cm,
        "Marketing in a Digital World  |  Module 3: Placement")
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
    Paragraph("MODULE 3: PLACEMENT", make_style("mc",
        fontName="Helvetica-Bold", fontSize=22, textColor=MID_BLUE,
        alignment=TA_CENTER, spaceAfter=6)),
    sp(8),
    Paragraph("Complete Study Notes — Textbook Edition", sSubtitle),
    sp(6),
    Paragraph("Gies College of Business · University of Illinois", sModuleTag),
    sp(60),
    thin_hr(),
    sp(6),
    Paragraph("Topics Covered: Placement Overview · Distribution Channels · New Retail · "
              "Case Study: Tesla · Desktop Manufacturing (3D Printing) · "
              "Exercise: Thingiverse.com · Expert Interview: Alan Craig & Max Collins (AR/VR)",
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
    h1("Module 3 Overview"),
    body("This module examines how the digital revolution has fundamentally altered the "
         "<b>placement and distribution of products</b>. New digital tools are disrupting the "
         "traditional retail landscape and enabling both firms and consumers to bypass previously "
         "essential channel intermediaries. The module introduces placement, covers the transition "
         "from traditional to new retail, examines desktop manufacturing (3D printing) as a "
         "distribution-eliminating technology, and applies these concepts through the Tesla case "
         "study and the Thingiverse.com exercise."),
    sp(8),
    h2("Guiding Questions"),
    bullet("What is the 'new retail,' and how are physical retailers adapting to a digital world?"),
    bullet("What is desktop manufacturing (3D printing), and how will it change placement and distribution?"),
    bullet("How are new digital tools changing the way firms place their products?"),
    sp(8),
    h2("Key Concepts & Phrases"),
    two_col_table([
        ["Placement",              "The process of making a product conveniently accessible to potential customers"],
        ["Distribution",           "The physical movement of a product from manufacturer through channel intermediaries to the customer"],
        ["Retailing",              "The last step in the distribution chain; the point of direct consumer purchase"],
        ["New Retail",             "The collection of physical and digital strategies physical retailers use to react to operating in a digital world"],
        ["Desktop Manufacturing",  "The use of desktop devices (primarily 3D printers) to convert digital designs into physical products"],
        ["3D Printing",            "An additive manufacturing process that builds objects layer by layer from a digital design file (STL file)"],
        ["Omnichannel Marketing",  "An integrated strategy blending digital and physical retail channels to deliver a seamless customer experience"],
        ["Showrooming",            "Visiting a physical store to inspect a product, then purchasing it online"],
        ["Webrooming",             "Researching a product online first, then purchasing it in a physical store"],
        ["Thingiverse.com",        "An online library of free, downloadable 3D-printable design files, owned by Ultimaker (formerly MakerBot)"],
    ], header_row=["Term", "Brief Description"]),
    PageBreak(),
]

# ── CHAPTER 1: PLACEMENT OVERVIEW ────────────────────────────────────────────
story += [
    section_divider("1", "Placement Overview"),
    sp(12),
    h1("1. Placement Overview"),
    sp(4),
    h2("1.1 Definition of Placement"),
    body("Placement is the <b>third P of the Marketing Mix</b>. This aspect of marketing focuses "
         "on making a product <b>conveniently accessible to potential customers</b>. For most "
         "physical products, placement involves the movement of a product from manufacturer "
         "through a series of <b>marketing channel intermediaries</b>, ultimately ending with "
         "an independent retailer."),
    body("The retailer then performs critical functions, including:"),
    bullet("Displaying the product on shelves"),
    bullet("Educating staff about product features so they can assist customers"),
    bullet("Processing transactions and providing customer service"),
    sp(4),
    body("Key concepts within the placement portion of the marketing mix include: "
         "<b>inventory management</b>, <b>logistics</b>, and <b>salesforce management</b>. "
         "This module focuses on the two most fundamental: <b>distribution</b> and <b>retailing</b>."),
    sp(6),
    example("Coke distributes its products (its formula) to a network of over "
            "<b>225 bottling partners</b> across the planet. These distributors mix the Coke "
            "formula with water, bottle it, and ship it to a network of warehouses, which "
            "distribute to nearly <b>20 million retailers across the world</b> — in more than "
            "<b>200 different countries</b>. These retailers include grocery stores, convenience "
            "stores, restaurants, movie theaters, and vending machines. It is nearly impossible "
            "to walk into a store in most parts of the world and not find a Coke."),
    sp(8),
    h2("1.2 Distribution Channels"),
    body("The distribution channel used by most firms is typically <b>outsourced</b> to a "
         "series of independent firms: an importer, a wholesaler, and a retailer. This is known "
         "as the <b>traditional distribution channel</b>:"),
    sp(4),
    two_col_table([
        ["Manufacturer", "Produces the product"],
        ["Importer",     "Handles cross-border sourcing and initial customs clearance"],
        ["Wholesaler",   "Purchases in bulk and redistributes to smaller retailers"],
        ["Retailer",     "Sells directly to end consumers; last step in the channel"],
        ["Customer",     "The final recipient and consumer of the product"],
    ], header_row=["Channel Member", "Role"]),
    sp(4),
    body("The distribution process is often <b>lengthy</b> and requires substantial resources "
         "in both time and money. Since each member of the channel is typically independent, "
         "each participant tries to maximize their own revenue and minimize their own cost. "
         "This frequently causes <b>conflicts and misunderstandings</b> between channel members. "
         "A manufacturer must carefully select and monitor each channel partner — a difficult "
         "and costly process that ultimately <b>drives up the price of products</b> for consumers."),
    body("Typically, a manufacturer only receives about <b>60–70% of a product's retail price</b>. "
         "The remainder is consumed by channel intermediary margins. Thus, traditional product "
         "placement is an expensive proposition for both firms and consumers."),
    sp(8),
    h2("1.3 Retailing"),
    body("The retailer is typically the <b>last step in the distribution chain</b>. The type "
         "and number of retailers selected by a firm is a critical strategic decision because it "
         "directly affects the type and number of customers who can acquire its products."),
    sp(4),
    two_col_table([
        ["Intensive (Exclusive) Placement",
         "Products made available only through a small, exclusive set of retailers. "
         "Used for luxury goods. Example: Louis Vuitton distributes through carefully "
         "selected boutiques only, maintaining scarcity and brand prestige."],
        ["Extensive (Mass) Placement",
         "Products made available through as many different retailers as possible. "
         "Used for low-priced consumer goods. "
         "Example: Toothpaste and shampoo are sold in grocery stores, pharmacies, "
         "convenience stores, and online."],
    ], header_row=["Strategy", "Description & Example"]),
    sp(6),
    h3("Retailer Service Levels"),
    body("Retailers also vary in their degree of customer service:"),
    bullet("<b>Self-service retailers</b> (e.g., convenience stores): Customers locate, select, "
           "and sometimes purchase products with little or no staff assistance."),
    bullet("<b>Full-service retailers</b> (e.g., high-end department stores): Staff actively "
           "assess customer needs and guide them to appropriate products."),
    sp(8),
    h2("1.4 The Digital Disruption of Traditional Placement"),
    body("This traditional placement model is starting to break down due to the rise of "
         "digital tools. Most firms are now supplementing or <b>bypassing physical retailers</b> "
         "entirely by making their offerings available through:"),
    bullet("Online retailers such as <b>Amazon.com</b>"),
    bullet("Their own <b>direct-to-consumer websites</b>"),
    body("Online sales are growing rapidly. Even products that consumers traditionally want to "
         "touch or try in person are now being sold online."),
    example("Casper is a firm that sells mattresses entirely online. The first time a customer "
            "gets to try out the mattress is after it has been delivered to their home. If a "
            "mattress can be sold online, virtually any product can bypass traditional stores."),
    sp(6),
    h3("The Ultimate Disruptor: 3D Printing and the Elimination of the Entire Channel"),
    body("Digital tools are capable of not only replacing the retailer but potentially the "
         "<b>entire distribution channel</b>. Even Amazon must physically ship products from "
         "manufacturer to customer. However, emerging technologies such as <b>3D printers</b> "
         "may make it possible to eliminate the distributor by allowing firms to ship a "
         "<b>digital design rather than a physical product</b>."),
    body("This represents a shift from:"),
    two_col_table([
        ["Traditional (Long) Channel",  "Manufacturer → Importer → Wholesaler → Retailer → Customer (physical product shipped at each step)"],
        ["Digital (Short) Channel",     "Designer → Thingiverse.com → 3D Printer → Customer (digital file downloaded; object printed locally)"],
    ], header_row=["Channel Type", "Flow"]),
    sp(4),
    example("The <b>Baker's Cube</b> is an all-in-one measuring tool for baking (cookies, cakes). "
            "Its digital design file is freely available on Thingiverse.com. Anyone in the world "
            "with access to a desktop 3D printer can download and print it for free — with zero "
            "shipping, zero retail markup, and zero manufacturing overhead."),
    body("In this new digital marketing environment, we are moving from <b>long distribution "
         "channels for physical goods</b> to <b>short distribution channels for digital goods</b>."),
    PageBreak(),
]

# ── CHAPTER 2: NEW RETAIL PART 1 ─────────────────────────────────────────────
story += [
    section_divider("2", "New Retail (Part 1)"),
    sp(12),
    h1("2. New Retail (Part 1)"),
    sp(4),
    quote_box("The secret to successful retailing is to give your customers what they want.",
              "Sam Walton, Founder, Walmart"),
    sp(8),
    h2("2.1 The Threat of Online Retailing to Physical Stores"),
    body("Before the digital revolution, retailing was largely an analog activity in which "
         "customers visited a physical store. In today's digital world, just about any product "
         "can be purchased online. For example:"),
    bullet("<b>Amazon.com</b> sells over <b>350 million different products</b>."),
    bullet("Many of these products would be difficult or impossible to locate at a physical retailer."),
    bullet("In countries like the <b>US and China</b>, over <b>80% of consumers engage in "
           "online shopping</b>."),
    bullet("Low-priced items such as books and clothing are more likely to be purchased "
           "online than in a physical store."),
    bullet("Even large and expensive objects are being purchased online — it is now possible "
           "to <b>order a house online from Amazon</b> and other retailers."),
    sp(4),
    body("This growth in online retailing has become a considerable threat to traditional "
         "physical retailers. Online competition has forced several well-known retailers across "
         "categories including <b>music</b>, <b>books</b>, and <b>consumer electronics</b> out "
         "of business. Across the US, many indoor shopping malls are closing with numerous "
         "vacant storefronts."),
    sp(4),
    body("In response to these threats, physical retailers have begun adapting by:"),
    bullet("Establishing websites to allow customers to both obtain product information and "
           "purchase online"),
    bullet("Enabling <b>buy online, pick up in-store (BOPIS)</b> or home delivery "
           "(e.g., Walmart)"),
    bullet("Selling merchandise through online marketplaces such as Amazon or WeChat"),
    bullet("Using digital tools within physical stores to enhance the shopping experience"),
    sp(8),
    h2("2.2 Definition of New Retail"),
    body("<b>New Retail</b> is the collection of strategies — both physical and digital — that "
         "physical retailers are employing to react to the challenges of operating in a digital "
         "world. It represents the convergence of online and offline commerce to create "
         "a superior, integrated consumer experience."),
    sp(8),
    h2("2.3 Three Examples of New Retail"),
    sp(4),
    h3("Example 1: Unity Robots (Japan)"),
    body("Unity is a small <b>home improvement chain in Japan</b>. Japanese retailers are known "
         "for their intense focus on store cleanliness and tidiness — employees regularly mop "
         "and vacuum floors."),
    body("During the <b>COVID-19 pandemic</b>, these cleaning functions were transferred from "
         "human employees to <b>robot assistants</b>. These robots are manufactured by "
         "<b>Softbank Robotics</b> and are described as looking like a 'Roomba on steroids.'"),
    body("Beyond cleaning, Unity's management began using these robots to <b>promote products</b> "
         "in-store — often attaching paper eyes, noses, and mouths to make them appear friendlier "
         "and more approachable. The results were significant: these robots are effective "
         "in-store marketers and have helped <b>boost sales of promoted products by over 25%</b>."),
    sp(4),
    h3("Example 2: Geissler Smart Shopping Carts (USA)"),
    body("Geissler supermarkets is a small supermarket chain in the <b>New England region of "
         "the United States</b>. The chain has begun introducing <b>smart shopping carts</b> "
         "in all its stores."),
    body("These carts are developed by the online grocery retailer <b>Instacart</b> and use "
         "<b>computer vision technology</b> to digitally track the items that shoppers place "
         "into their cart. Key capabilities include:"),
    bullet("<b>Automatic item tracking:</b> The cart recognizes and logs each product placed inside."),
    bullet("<b>Personalized in-store promotions:</b> Based on a customer's past shopping "
           "behaviors, the cart offers tailored discounts and recommendations in real time."),
    bullet("<b>Recommended purchases:</b> As customers navigate the store, the cart proactively "
           "suggests items they may need."),
    body("These smart carts have proven popular and are being rapidly adopted by other grocery "
         "retailers around the world."),
    sp(4),
    h3("Example 3: Coach Smart Mirror (New York City)"),
    body("The luxury handbag brand <b>Coach</b> has installed a <b>smart mirror</b> in front "
         "of its flagship store in the <b>Soho neighborhood of New York City</b>. This digital "
         "mirror is enabled with <b>Augmented Reality (AR) technology</b> that allows customers "
         "to see how they would look wearing different versions of Coach's popular "
         "<b>tabby handbag</b> — without physically trying them on."),
    body("This mirror was created by a company called <b>ZERO 10</b>, which has installed "
         "similar AR-enabled mirrors in a variety of other retailers, including "
         "<b>Tommy Hilfiger</b>, <b>Macy's</b>, and <b>Ugg</b> stores."),
    sp(8),
    h2("2.4 Three Key Observations About the New Retail Landscape"),
    sp(4),
    h3("Observation 1: Location, Location, Location"),
    body("The classic real estate principle — <i>location is everything</i> — also applies "
         "to retailing in a digital world. A substantial body of research shows that "
         "<b>online retailing is heavily influenced by location</b>:"),
    bullet("Consumers who have easy access to well-priced physical stores are "
           "<b>less likely to shop online</b>."),
    bullet("Online shopping is therefore <b>more prevalent among consumers in small towns</b> "
           "(like Champaign, Illinois) than in large cities (like Chicago), where physical "
           "retail options are abundant and convenient."),
    body("Key implication: <b>The appeal of digital retail is strongly influenced by "
         "one's physical environment</b>. Digital and physical retail do not exist in isolation."),
    sp(4),
    h3("Observation 2: Purchase versus Information"),
    body("Digital retailers serve two distinct functions for consumers: they are used both "
         "for <b>purchasing</b> and for <b>gathering product information</b>. Amazon.com, "
         "for example, provides product descriptions, extensive technical information, and "
         "user reviews for most products."),
    body("This dual function gives rise to two important behavioral phenomena:"),
    sp(4),
    two_col_table([
        ["Showrooming",
         "Customer first visits a physical store to inspect a product, then purchases it "
         "online (often at a lower price). In the US, about 2 out of 3 customers who buy "
         "online first go to a physical store to look at the product."],
        ["Webrooming",
         "Customer first researches a product online, then purchases it in a physical "
         "store. Despite showrooming receiving more attention, webrooming is actually "
         "MORE common than showrooming."],
    ], header_row=["Behavior", "Description & Data"]),
    sp(4),
    body("The key implication is that <b>digital channels are as much information tools as "
         "they are transaction channels</b>, and physical stores benefit from web-informed, "
         "higher-intent shoppers."),
    sp(4),
    h3("Observation 3: Digital and Physical — The Omnichannel Integration"),
    body("While digital and physical retail are often thought of as entirely separate, a "
         "growing number of retailers are seeking ways to <b>blend the two together</b>. "
         "This blending is referred to as <b>omnichannel marketing</b> — an approach based "
         "on the idea that retailers must leverage the unique strengths of each channel."),
    sp(4),
    two_col_table([
        ["Physical Store Strengths",  "Product returns; customer service; touch and feel; "
                                      "immediate gratification; personal interaction"],
        ["Digital Channel Strengths", "Product research; user reviews; price comparison; "
                                      "wide selection; 24/7 availability; convenience"],
    ], header_row=["Channel", "Core Strengths"]),
    sp(4),
    body("A growing number of retailers are seeking to have a presence in both channels, "
         "linking them together so that customers can <b>move seamlessly between online "
         "and offline experiences</b>."),
    PageBreak(),
]

# ── CHAPTER 3: NEW RETAIL PART 2 ─────────────────────────────────────────────
story += [
    section_divider("3", "New Retail (Part 2)"),
    sp(12),
    h1("3. New Retail (Part 2)"),
    sp(4),
    h2("3.1 Academic Insights on New Retail"),
    sp(4),
    h3("Academic Insight 1: In-Store Technology and AI"),
    body("<b>Source:</b> Grewal, D. et al. (2023). <i>Journal of Retailing, 99(4), 487–504.</i> "
         "Babson College."),
    sp(4),
    info_box("Study Overview", [
        body("This study conducted a comprehensive review of the academic literature on "
             "in-store technology and AI, developing a framework for understanding the role "
             "of technology in physical retail settings."),
        body("<b>Key technologies identified as transforming the retail experience:</b>"),
        bullet("Smart shelves that automatically track inventory levels"),
        bullet("Interactive kiosks that provide product information to shoppers"),
        bullet("Mobile payment systems that streamline the checkout process"),
        bullet("AI-powered recommendation engines that personalize the shopping experience"),
        body("<b>Key Findings:</b>"),
        bullet("<b>Customer benefits:</b> Reduced wait times, personalized recommendations, "
               "and enhanced access to product information."),
        bullet("<b>Employee benefits:</b> Improved task efficiency, better inventory management, "
               "and reduced time on routine tasks (freeing staff for higher-value interactions)."),
        body("<b>Critical Principle:</b> Successful implementation requires careful attention "
             "to the <b>human-technology interface</b>. Technology should <b>augment rather "
             "than replace</b> human interaction. The most effective implementations enhance "
             "human service rather than eliminating it."),
    ]),
    sp(6),
    h3("Academic Insight 2: Autonomous Stores"),
    body("<b>Source:</b> Benoit, S. et al. (2024, forthcoming). <i>Journal of Retailing.</i> "
         "University of Surrey. Studies conducted across the US, UK, and Germany."),
    sp(4),
    info_box("Study Overview", [
        body("This research examined how different levels of in-store automation affect "
             "store patronage decisions — specifically, whether consumers choose to shop at "
             "a store based on its level of automation."),
        body("<b>Three Levels of Automation Studied:</b>"),
        bullet("<b>Level 1 — Low automation:</b> Traditional stores with human cashiers and "
               "standard checkout processes."),
        bullet("<b>Level 2 — Medium automation:</b> Self-checkout options available alongside "
               "human cashiers."),
        bullet("<b>Level 3 — High automation:</b> Fully autonomous stores such as "
               "<b>Amazon Go</b>, where customers simply pick up items and leave — the system "
               "automatically charges their account."),
        body("<b>Key Findings — Consumer responses to automation depend on:</b>"),
        bullet("<b>Shopping trip type:</b> For routine <b>utilitarian</b> purchases (e.g., "
               "buying milk), higher automation is preferred for speed and convenience. "
               "For <b>hedonic</b> purchases (e.g., browsing for a gift), lower automation "
               "with human assistance is valued."),
        bullet("<b>Purchase complexity:</b> Simple, straightforward purchases suit high "
               "automation; complex or high-involvement purchases benefit from human "
               "interaction."),
        bullet("<b>Technology readiness:</b> Individual differences in comfort with technology "
               "significantly affect preferences for automation levels."),
        body("<b>Strategic Implication:</b> Retailers should adopt a <b>flexible approach "
             "to automation</b>, offering multiple options to accommodate different customer "
             "needs and preferences rather than committing to a single automation level."),
    ]),
    sp(8),
    h2("3.2 Four Practical Recommendations for New Retail"),
    sp(4),
    h3("Recommendation 1: Embrace the Blend"),
    body("Do not treat digital and physical as separate, competing channels. Instead, "
         "actively seek to <b>integrate them seamlessly</b>:"),
    bullet("Allow customers to order online and pick up in-store (BOPIS)."),
    bullet("Accept returns of online purchases at physical locations."),
    bullet("Use physical stores as <b>showrooms</b> where customers can experience products "
           "and then purchase at their convenience (online or in-store)."),
    bullet("Use digital channels to drive traffic to physical locations through localized "
           "promotions and events."),
    sp(4),
    h3("Recommendation 2: Leverage Data Across Channels"),
    body("One of the greatest advantages of digital retail is the <b>wealth of behavioral "
         "data</b> it generates about customer preferences. Firms should use this data to "
         "<b>personalize the in-store experience</b>:"),
    bullet("When a loyal online customer visits a physical store, equip staff with knowledge "
           "of that customer's preferences so they can provide tailored recommendations."),
    bullet("Use <b>loyalty programs</b> to track customer behavior across channels and "
           "reward omnichannel engagement, strengthening retention."),
    sp(4),
    h3("Recommendation 3: Enhance, Don't Replace"),
    body("When introducing technology into physical stores, the goal should be to "
         "<b>enhance the customer experience</b>, not simply replace human interaction. "
         "Technology should free employees to provide higher-value assistance by automating "
         "routine tasks:"),
    bullet("Use <b>smart shelves</b> to automate inventory tracking, allowing employees to "
           "spend more time with customers rather than counting stock."),
    bullet("Use <b>self-checkout</b> for simple, low-complexity transactions so that "
           "cashiers can focus attention on customers who require assistance."),
    sp(4),
    h3("Recommendation 4: Experiment and Iterate"),
    body("The new retail landscape is evolving rapidly. There is no one-size-fits-all "
         "solution. Firms should:"),
    bullet("Be willing to <b>experiment</b> with different technologies and approaches."),
    bullet("Start with <b>small pilots</b>, measure results carefully, and scale up what works."),
    bullet("Accept that <b>failure is part of the learning process</b> — not every "
           "innovation will succeed, but each experiment provides valuable insights for "
           "future decisions."),
    PageBreak(),
]

# ── CHAPTER 4: CASE STUDY — TESLA ────────────────────────────────────────────
story += [
    section_divider("4", "Case Study: Tesla"),
    sp(12),
    h1("4. Case Study: Tesla"),
    sp(4),
    h2("4.1 Company Background"),
    two_col_table([
        ["Founded",           "2003"],
        ["Original location", "California; now headquartered in Texas"],
        ["CEO",               "Elon Musk — one of the world's best-known CEOs; has appeared in films (e.g., Iron Man); holds nearly 200 million followers on X (formerly Twitter) — the largest social media following of any CEO in the world"],
        ["Product",           "Electric automobiles — no engine, no transmission, no radiator, no muffler, no gas tank"],
        ["Most popular model","Model Y — the most popular automobile on the planet"],
        ["Other products",    "Cybertruck; manufacturing plants in Asia and Europe"],
        ["US avg. car price", "Nearly $50,000"],
        ["Market position",   "One of the world's largest automobile manufacturers despite recent founding"],
    ], header_row=["Attribute", "Detail"]),
    sp(6),
    body("Tesla is noteworthy as a brand because automobiles are both <b>highly functional</b> "
         "and <b>highly symbolic</b> products. People drive them daily, and their large, "
         "visible nature means they often serve as <b>social signals to others</b>. "
         "For example, the symbolic meaning of a BMW is very different from that of a Subaru."),
    body("Despite Tesla's success in growing sales and expanding globally, its stock price "
         "has experienced <b>dramatic ups and downs</b>. Both Tesla and Elon Musk face "
         "substantial skepticism from business leaders, academic experts, and the mass media."),
    sp(8),
    h2("4.2 Tesla's Three Key Retail Differentiators"),
    body("Tesla's retail strategy is dramatically different from the way automobiles have "
         "historically been sold. Three key differences stand out:"),
    sp(4),
    h3("Differentiator 1: Number of Retail Locations"),
    body("Tesla has <b>far fewer retail locations</b> than traditional automobile manufacturers, "
         "despite comparable or greater sales volumes."),
    example("In Illinois, there are <b>28 Volkswagen dealers</b> but only <b>9 Tesla retail "
            "stores</b> — all of which are located exclusively in the Chicago metropolitan area. "
            "Yet Tesla sells approximately <b>twice as many cars</b> in the US as Volkswagen."),
    sp(4),
    h3("Differentiator 2: Size and Design of Retail Locations"),
    body("Traditional automobile dealerships are typically <b>large buildings at the edge "
         "of towns or cities</b>, with dozens of cars displayed in expansive parking lots "
         "and large, glitzy showrooms."),
    body("In contrast, Tesla retail stores are typically <b>much smaller</b>, located in "
         "high-traffic retail areas (often in malls), and feature only <b>two or three "
         "vehicles</b> in a small, minimalist showroom. The emphasis is on education "
         "and brand experience, not inventory display."),
    sp(4),
    h3("Differentiator 3: The Role of the Retailer"),
    body("Traditional car dealerships exist primarily to <b>make a sale</b>. This typically "
         "involves a persuasive salesperson and a lengthy negotiation and paperwork process "
         "that can take several hours."),
    body("Tesla retail stores serve a fundamentally different purpose: their primary role is "
         "to <b>provide information and facilitate brand experience</b>. Key distinctions:"),
    bullet("<b>Non-negotiable pricing:</b> All Tesla prices are fixed and uniform — "
           "there is no negotiation."),
    bullet("<b>Online purchasing:</b> A Tesla can be purchased <b>within five minutes</b> "
           "on its website — or even from within another Tesla vehicle."),
    bullet("<b>Over 70% of Tesla sales</b> are made online, away from physical retail stores."),
    sp(8),
    h2("4.3 Case Study Questions and Model Answers"),
    sp(4),
    h3("Question 1: What role do digital tools play in Tesla's retailing strategy?"),
    body("Digital tools are <b>central</b> to Tesla's entire retail model:"),
    bullet("The Tesla website and mobile app handle the complete purchase process — "
           "vehicle configuration, pricing, financing, payment, and delivery coordination."),
    bullet("Retail stores function primarily as <b>informational showrooms</b> rather "
           "than transactional spaces — reducing overhead and improving efficiency."),
    bullet("Fixed, transparent online pricing eliminates friction and the need for "
           "negotiation, shortening the purchase process from hours to minutes."),
    bullet("Social media channels (particularly X/Twitter) serve as a primary promotional "
           "vehicle, with Elon Musk's personal following of ~200 million effectively acting "
           "as free advertising."),
    body("This approach reduces distribution costs dramatically and aligns with the digital "
         "preferences of Tesla's customer base."),
    sp(4),
    h3("Question 2: What are the pros and cons of Tesla's retail strategy?"),
    body("<b>Advantages:</b>"),
    bullet("Lower overhead costs (fewer, smaller locations)"),
    bullet("Pricing transparency and consistency — no dealer markup, no negotiation"),
    bullet("Faster, frictionless transactions — purchases completed in minutes online"),
    bullet("Stronger brand control — Tesla controls the entire customer experience"),
    bullet("Scalable global reach through online sales without proportional infrastructure growth"),
    body("<b>Disadvantages:</b>"),
    bullet("Limited physical presence — customers in non-urban areas face significant "
           "geographic barriers to visiting a store"),
    bullet("Reduced personal interaction for customers who prefer traditional guided "
           "purchasing experiences"),
    bullet("Regulatory challenges — some US states have laws requiring automobile sales "
           "through licensed dealerships, creating legal friction for Tesla"),
    bullet("Potential service bottlenecks — with fewer retail locations, servicing "
           "vehicles can be more difficult and time-consuming"),
    sp(4),
    h3("Question 3: How can Tesla improve its retailing strategy?"),
    bullet("Expand <b>service infrastructure</b> to address the service accessibility "
           "bottleneck, particularly in suburban and rural areas."),
    bullet("Improve <b>localized customer support</b> through digital tools (chat, remote "
           "diagnostics) to compensate for limited physical locations."),
    bullet("Offer more <b>experiential test-drive opportunities</b> — pop-up events, "
           "mobile showrooms — to reach consumers who cannot easily access a Tesla store."),
    bullet("Strengthen <b>post-purchase digital engagement</b> through the app, OTA "
           "(over-the-air) updates, and community features to maintain brand loyalty."),
    bullet("Consider a hybrid approach: <b>maintain digital efficiency</b> while selectively "
           "increasing physical touchpoints to improve accessibility and customer trust."),
    PageBreak(),
]

# ── CHAPTER 5: DESKTOP MANUFACTURING PART 1 ──────────────────────────────────
story += [
    section_divider("5", "Desktop Manufacturing (Part 1)"),
    sp(12),
    h1("5. Desktop Manufacturing (Part 1)"),
    sp(4),
    quote_box("The future is already here — it's just not evenly distributed.",
              "William Gibson, Science Fiction Author"),
    sp(8),
    h2("5.1 Introduction to Desktop Manufacturing"),
    body("Desktop manufacturing refers to the use of <b>digitally enabled desktop devices</b> — "
         "including milling machines, laser cutters, and 3D printers — to convert digital "
         "designs into physical products. These machines are becoming increasingly available, "
         "affordable, and easy to use. Among these various devices, <b>desktop 3D printers</b> "
         "are by far the most common, most affordable, and easiest to use."),
    body("According to leading sources including <b>Wired magazine</b>, <b>The Economist</b>, "
         "and the <b>New York Times</b>, 3D printing will lead to a <b>new industrial "
         "revolution</b> and dramatically alter the global economy."),
    sp(4),
    info_box("The Illinois Maker Lab", [
        body("Professor Eric Arnould co-founded the <b>Illinois Maker Lab</b> at the "
             "University of Illinois — the world's <b>first 3D printing lab in a business "
             "school</b>. Located on the third floor of the Business Instructional Facility "
             "(BIF), the lab features approximately a dozen desktop 3D printers and a "
             "collection of printed objects including: a model of the Eiffel Tower, a shower "
             "head in the shape of a T-rex, and a six-foot tall 3D-printed man. The lab's "
             "mission is to help students and faculty understand and leverage this new digital tool."),
    ]),
    sp(6),
    body("An important perspective: most people's favorite objects were not their own idea — "
         "they were designed by someone else, manufactured by an unknown person in a distant "
         "location (often China), distributed through a long supply chain, and the consumer "
         "simply happened to want them. Desktop manufacturing fundamentally changes this: "
         "anyone with access to a 3D printer can <b>turn their own ideas into physical objects</b>."),
    sp(8),
    h2("5.2 Three Key Examples of 3D Printing in Practice"),
    sp(4),
    h3("Example 1: The Functional Hand"),
    body("Designed by <b>Linda Mary and Molly Gardner</b> — two designers in Chicago — the "
         "Functional Hand is a simple 3D-printed device designed to assist people with "
         "<b>hand mobility challenges</b> caused by conditions such as arthritis, carpal "
         "tunnel syndrome, or multiple sclerosis."),
    body("The device holds small objects (such as spoons and pencils) in place, enabling "
         "people who cannot grip normally to use them. It was manufactured at the "
         "<b>Illinois Maker Lab in Champaign</b>. This is a compelling example of 3D printing "
         "enabling <b>democratized access to medical assistive devices</b> at minimal cost."),
    sp(4),
    h3("Example 2: The Baker Cube"),
    body("In <b>2017</b>, a designer named <b>Iom AA (IAMA)</b> created the Baker Cube — "
         "an all-in-one measuring tool for baking. The traditional problem: baking requires "
         "multiple measuring cups and spoons (for flour, sugar, baking powder, etc.), which "
         "must be purchased separately, stored, and cleaned."),
    body("The Baker Cube solves this by fitting all necessary measurements — from a "
         "<b>quarter teaspoon to a full cup</b> — in a single device that fits in the palm "
         "of your hand. The designer posted the digital file on <b>Thingiverse.com</b>, "
         "making it freely available to anyone in the world with access to a 3D printer."),
    sp(4),
    h3("Example 3: NanoHack — COVID-19 Response Mask"),
    body("In <b>March 2020</b>, during the global COVID-19 pandemic, global supply chains "
         "were severely disrupted, causing critical shortages of medical supplies including "
         "respiratory masks. A small team from <b>Chile</b> responded by:"),
    bullet("Designing a 3D-printable mask made from <b>copper-infused thermoplastic</b>"),
    bullet("Uploading the design file (an <b>STL file</b>) to a public website — free for "
           "anyone worldwide with a 3D printer"),
    bullet("The mask took approximately <b>2 hours to print</b>; materials cost approximately "
           "<b>$10</b>"),
    body("A similar case: a group of <b>Italian volunteers</b> designed 3D-printable "
         "ventilator connector valves. Medical supply companies had been charging up to "
         "<b>$10,000</b> per valve. These critical valves could be 3D printed for "
         "approximately <b>$1</b>. This is a powerful example of how desktop manufacturing "
         "enables <b>digital democracy</b> — distributing life-saving technology globally "
         "at near-zero cost."),
    sp(8),
    h2("5.3 Definition of Desktop 3D Printing"),
    body("A <b>desktop 3D printer</b> is an electronic device — usually approximately the "
         "size of a microwave oven — capable of turning digital designs into physical objects "
         "through an <b>additive process</b>. A 3D printer creates an object <b>one layer at "
         "a time</b>, in a manner similar to how construction workers build a skyscraper "
         "(floor by floor from the ground up)."),
    sp(4),
    two_col_table([
        ["Materials",       "Plastics, metals, ceramics, carbon fiber, and even chocolate — "
                            "any material that can be hardened or softened can be 3D printed"],
        ["Input",           "A digital design file (typically an STL file)"],
        ["Process",         "The STL file is read by slicing software, which converts it into "
                            "layer-by-layer instructions for the printer's motherboard"],
        ["Output",          "A physical, three-dimensional object"],
        ["Cost",            "Desktop 3D printers are now available for less than $200"],
        ["History",         "3D printers have existed since the mid-1980s, but were previously "
                            "very large and very expensive; size and cost have dramatically "
                            "shrunk over the past decade"],
    ], header_row=["Attribute", "Detail"]),
    sp(6),
    h3("How to Get a Design File"),
    body("A design file can come from three sources:"),
    bullet("Created using <b>3D modeling software</b> such as Google SketchUp"),
    bullet("Generated from a <b>3D digital scan</b> of a physical object"),
    bullet("Downloaded from a <b>file-sharing website</b> such as Thingiverse.com"),
    body("The implication is profound: <b>if you can download a file, you can create a "
         "3D-printed object</b>."),
    sp(8),
    h2("5.4 Deeper Dive: Three Important Topics"),
    sp(4),
    h3("Topic 1: How Does 3D Printing Work?"),
    body("There are multiple 3D printing technologies, including:"),
    bullet("<b>Selective Laser Sintering (SLS)</b>"),
    bullet("<b>Stereolithography (SLA)</b>"),
    bullet("<b>Fused Deposition Modeling (FDM)</b> — the most common desktop type"),
    body("Despite these variations, nearly all 3D printers work in one of two fundamental ways:"),
    bullet("Take a <b>soft material and make it hard</b> (e.g., liquid resin cured by UV light in SLA)"),
    bullet("Take a <b>hard material and make it soft</b> (e.g., solid plastic filament melted "
           "in FDM, then re-solidified)"),
    body("3D printers are computer-controlled devices with a <b>printhead</b> and electric "
         "motors that move the printhead or print platform in three dimensions. The movement "
         "is determined entirely by the digital design file read by the printer's motherboard."),
    sp(4),
    h3("Topic 2: What Are the Advantages of 3D Printing?"),
    body("3D printing offers several key advantages over traditional manufacturing:"),
    bullet("<b>No additional setup cost:</b> The same printer can produce many different "
           "objects with no retooling or setup cost between different products."),
    bullet("<b>No economies of scale constraint:</b> Making one object costs the same "
           "per unit as making many. Traditional manufacturing requires large production "
           "runs to achieve cost efficiency; 3D printing does not."),
    bullet("<b>Complex geometries at no extra cost:</b> Objects with internal structures, "
           "undercuts, and complex shapes that would be impossible or prohibitively expensive "
           "with traditional manufacturing can be 3D printed at standard cost."),
    bullet("<b>Easy customization:</b> Modify the digital file and print a customized version "
           "immediately — no tooling changes required."),
    bullet("<b>No inventory required:</b> Print on demand — eliminate warehousing costs "
           "and the risk of obsolete inventory."),
    sp(4),
    h3("Topic 3: How Is 3D Printing Disrupting Traditional Businesses?"),
    body("3D printing has the potential to disrupt multiple traditional industries:"),
    bullet("<b>Logistics and shipping:</b> If products can be downloaded and printed locally, "
           "there is no need to ship physical goods across long supply chains. Shipping firms "
           "such as <b>DHL</b> and <b>UPS</b> are reportedly concerned about this disruption."),
    bullet("<b>Retail:</b> If consumers can print products at home or at local print shops, "
           "they no longer need to purchase physical goods from stores."),
    bullet("<b>Manufacturing:</b> Small-scale, locally based production can compete directly "
           "with large-scale global manufacturing — without requiring factories."),
    bullet("<b>Inventory management:</b> Digital inventories replace physical inventories — "
           "designs are stored as files and printed only when needed."),
    body("The analogy: <b>3D printers alter physical goods just as the Internet and the "
         "laptop altered digital goods</b> such as music, text, and video. Physical music "
         "stores were replaced by iTunes — the 3D printer has the same potential to replace "
         "physical product distribution."),
    PageBreak(),
]

# ── CHAPTER 6: DESKTOP MANUFACTURING PART 2 ──────────────────────────────────
story += [
    section_divider("6", "Desktop Manufacturing (Part 2)"),
    sp(12),
    h1("6. Desktop Manufacturing (Part 2)"),
    sp(4),
    h2("6.1 Academic Insights on Desktop Manufacturing"),
    sp(4),
    h3("Academic Insight 1: Consumer Responses to Self-Printing"),
    body("<b>Source:</b> Wiecek, A. et al. (2020). <i>Journal of the Academy of Marketing "
         "Science, 48, 795–811.</i> Erlangen-Nuremberg University, Germany. Four experimental "
         "studies conducted in Germany."),
    sp(4),
    info_box("Study Overview", [
        body("<b>Core Research Question:</b> How do consumers evaluate objects they have "
             "made themselves via a desktop 3D printer, compared to objects made for them?"),
        body("<b>Central Hypothesis:</b> Individuals who 3D print their own objects feel "
             "more closely connected to them, display a higher sense of <b>perceived "
             "ownership</b>, and consequently evaluate these products more positively."),
        body("<b>Study 1 Methodology:</b>"),
        bullet("77 participants divided into three conditions:"),
        bullet("  (1) No print — received a pre-made keychain", sub=True),
        bullet("  (2) Print but don't watch — the keychain was printed for them without "
               "their observation", sub=True),
        bullet("  (3) Print and watch — participants observed their keychain being "
               "printed layer by layer", sub=True),
        bullet("Participants evaluated: how much they liked the keychain, willingness "
               "to pay (WTP), and degree of perceived ownership."),
        body("<b>Key Findings:</b>"),
        bullet("Participants who printed the keychain (regardless of whether they "
               "watched or not) reported <b>higher liking</b> and <b>higher willingness "
               "to pay</b> than those who did not print."),
        bullet("This effect was <b>mediated by perceived ownership</b> — the act of "
               "printing made participants feel it was truly 'theirs,' which drove "
               "the more positive evaluation."),
        bullet("In a subsequent study: <b>these effects were stronger for hedonic products</b> "
               "(products consumed for pleasure/enjoyment) than for utilitarian products."),
        body("<b>Strategic Implication:</b> Firms that allow consumers to 3D print their "
             "own products should achieve better outcomes in terms of greater product liking "
             "and higher willingness to pay — unlocking a new model of consumer-manufacturer "
             "engagement."),
    ]),
    sp(6),
    h3("Academic Insight 2: Desktop Manufacturing During COVID-19"),
    body("<b>Source:</b> Rindeisch, A. & Kim, M.H. (2021). <i>Journal of Public Policy &amp; "
         "Marketing, 40(1), 111–112.</i>"),
    sp(4),
    info_box("Study Overview", [
        body("<b>Context:</b> During the COVID-19 pandemic, global supply chains were "
             "severely disrupted, creating critical shortages of health products. In response, "
             "a broad range of firms, institutions, and individuals employed local desktop "
             "manufacturing (3D printing) to rapidly design, manufacture, and distribute "
             "ventilator parts, masks, swabs, and other essential items."),
        body("<b>Core Insight of the Paper:</b>"),
        bullet("Because 3D printers convert digital designs into physical products, "
               "<b>objects can be downloaded instead of transported</b>."),
        bullet("Production can occur in <b>small batches rather than large quantities</b>, "
               "without the constraints of economies of scale."),
        bullet("Desktop manufacturing is therefore <b>unconstrained by the demands of "
               "economies of scale</b> and <b>freed from the burden of physical form</b> "
               "— a radical departure from traditional manufacturing."),
        body("<b>Key Conclusion:</b> Small-scale, locally based manufacturing techniques "
             "such as desktop 3D printing may, under some conditions, be <b>more economically "
             "feasible than traditional large-scale global manufacturing</b>. The COVID crisis "
             "demonstrated this potential at global scale."),
    ]),
    sp(8),
    h2("6.2 Four Practical Recommendations for Desktop Manufacturing"),
    sp(4),
    h3("Recommendation 1: Make the Physical Digital"),
    body("The core value proposition of desktop manufacturing is that it <b>blurs the "
         "dividing line between physical and digital</b>. All objects created via 3D printing "
         "start with a digital model. Once a model is digital, it can be easily stored, "
         "transported globally, and modified to meet specific customer demands."),
    body("Practical steps:"),
    bullet("Create new objects using <b>3D modeling software</b> such as Google SketchUp."),
    bullet("Use <b>3D scanners</b> to convert existing physical products into digital design files."),
    bullet("These digital files are especially valuable for <b>replacement parts</b>, which "
           "are costly to store and difficult to transport physically."),
    example("NASA uses 3D printers to replace parts that break on its spacecraft while "
            "in space — printing replacement components in orbit rather than launching "
            "new parts from Earth."),
    sp(4),
    h3("Recommendation 2: Let Customers Customize Your Design"),
    body("Once products exist as digital files, <b>customization becomes cheap and easy</b>. "
         "Physical goods are difficult and expensive to customize (e.g., tailor-made suits, "
         "custom furniture). With digital products, a customer simply modifies the file."),
    body("A future possibility: firms will offer a <b>basic digital template</b> and allow "
         "customers to design a product to fit their specific needs — eliminating the concept "
         "of 'off-the-shelf' entirely. Thousands of examples of such unique designs are "
         "already available on <b>Thingiverse.com</b>."),
    sp(4),
    h3("Recommendation 3: Cut Out the Middleman"),
    body("Just as the Internet and the laptop disrupted the distribution of digital goods "
         "(music stores were replaced by iTunes), <b>the 3D printer has the potential to "
         "disrupt the distribution of physical goods</b>. Products shipped digitally save "
         "both time and money and give firms greater control over the distribution process."),
    body("A firm can execute this strategy by:"),
    bullet("Posting digital files of products or parts on its own <b>website for direct "
           "download</b> by customers."),
    bullet("Posting files on a <b>digital 3D printing service</b> such as "
           "<b>Craftcloud 3D.com</b>, enabling customers to order customized physical prints."),
    sp(4),
    h3("Recommendation 4: Done Is the Engine of More"),
    body("This recommendation draws on the <b>Cult of Done Manifesto</b> — a document "
         "written by <b>Brie Pettis</b> and <b>Kio Stark</b> containing principles for "
         "getting things done. This manifesto is displayed on the wall of the Illinois Maker Lab."),
    body("The final principle of the manifesto: <b>'Done is the engine of more.'</b> "
         "This deceptively simple statement emphasizes the importance of <b>doing rather "
         "than planning</b>. Traditional business education focuses heavily on planning. "
         "This principle challenges that orientation."),
    body("Applied to 3D printing: because desktop printing is relatively cheap and easy, "
         "there is no need for extensive planning before prototyping:"),
    bullet("Have an idea → design it → print an initial prototype"),
    bullet("Evaluate the physical prototype → identify improvements → modify the digital file"),
    bullet("Print a modified version → evaluate → repeat"),
    body("This iterative, low-cost cycle enables rapid innovation with minimal risk. "
         "<b>Done is the engine of more.</b>"),
    PageBreak(),
]

# ── CHAPTER 7: THINGIVERSE EXERCISE ──────────────────────────────────────────
story += [
    section_divider("7", "Exercise: Thingiverse.com"),
    sp(12),
    h1("7. Exercise: Thingiverse.com"),
    sp(4),
    h2("7.1 What Is Thingiverse?"),
    body("<b>Thingiverse.com</b> is an online library of digital design files that can be "
         "3D printed. It was originally launched by <b>MakerBot</b> and is currently owned "
         "by <b>Ultimaker</b>, a 3D printing company."),
    body("The platform can be understood as: <b>'the Apple iTunes Store, except it contains "
         "object designs rather than songs — and all files can be downloaded for free.'</b>"),
    sp(4),
    two_col_table([
        ["Owner",         "Ultimaker (formerly MakerBot)"],
        ["Content",       "Files for millions of objects across categories including artistic creations, household objects, toys and games, medical devices, and more"],
        ["Cost",          "All files are free to download"],
        ["Creators",      "Nearly all files are created and uploaded by individuals, not firms — a UGC-driven design repository"],
        ["Navigation",    "The 'Explore' tab is used to browse things submitted by users across categories"],
        ["ID system",     "Each 'thing' has a unique ID number located in its web URL"],
        ["Interaction",   "Visitors can like things, leave comments, and view the 3D printing settings used by the creator; creators can share design files and print settings"],
        ["Object types",  "Replacement (recreating a broken part), Substitute (alternative to an existing product), Solution (solving a new problem), Creation (new artistic/functional object)"],
    ], header_row=["Attribute", "Detail"]),
    sp(8),
    h2("7.2 Exercise Instructions"),
    body("The purpose of this exercise is to gain hands-on experience with 3D printing "
         "and to understand how this technology impacts marketing — specifically "
         "product placement."),
    sp(4),
    bullet("1. Visit <b>Thingiverse.com</b>."),
    bullet("2. Use the pull-down menu to find a category of things you find interesting."),
    bullet("3. Scroll through the category to find an object you would like to print."),
    bullet("4. Click on the 'thing' to learn more about it."),
    bullet("5. Record the thing's name and URL (the ID number is embedded in the URL)."),
    sp(4),
    h3("Assignment Questions"),
    bullet("Record the thing's name and URL."),
    bullet("Is this thing a new creation, a replacement, a substitute, or a solution?"),
    bullet("Why did you select this particular object?"),
    bullet("<b>How might Thingiverse (or a service like it) impact product placement?</b>"),
    sp(6),
    h3("Model Answer: How Thingiverse Impacts Product Placement"),
    body("Thingiverse represents a radical transformation of the placement function. "
         "By enabling anyone to download a digital design file and print a physical object "
         "locally, it:"),
    bullet("<b>Decentralizes product placement</b> — products no longer need to move "
           "physically from manufacturer to distributor to retailer to consumer. The "
           "'product' travels as a digital file."),
    bullet("<b>Eliminates channel intermediaries</b> — importers, wholesalers, and "
           "retailers are removed from the chain for 3D-printable items."),
    bullet("<b>Shifts the distribution channel from physical to digital</b> — converting "
           "a long physical channel into a short digital channel (Designer → Thingiverse "
           "→ 3D Printer → Customer)."),
    bullet("<b>Democratizes manufacturing and distribution</b> — anyone can design, "
           "share, and 'place' a product globally at zero distribution cost."),
    bullet("<b>Enables on-demand, local production</b> — eliminating warehousing costs, "
           "stockouts, and shipping delays."),
    sp(6),
    h3("Sample Student Assignment Response"),
    body("Object selected: <b>Psyduck X Gandalf — Pokemon &amp; Lord of the Rings mashup</b> "
         "(Thingiverse ID: 7287427). Type: Creation. This is a figurine of the Pokemon "
         "Psyduck dressed as Gandalf from Lord of the Rings — a purely creative mashup "
         "with no functional equivalent in commercial retail. Thingiverse enables creators "
         "to 'place' such niche, personalized designs directly to a global audience at zero "
         "cost — a distribution channel that would be completely uneconomical through "
         "traditional physical retail."),
    PageBreak(),
]

# ── CHAPTER 8: EXPERT INTERVIEW — ALAN CRAIG & MAX COLLINS ───────────────────
story += [
    section_divider("8", "Expert Interview: AR/VR & Distribution"),
    sp(12),
    h1("8. Expert Interview: Alan Craig & Max Collins on AR/VR and Distribution"),
    sp(4),
    info_box("About the Experts", [
        body("<b>Alan Craig:</b> Retired from the University of Illinois (National Center "
             "for Supercomputing Applications — 30 years). Independent consultant in "
             "Virtual Reality (VR) and Augmented Reality (AR) development. Author of "
             "several books and textbooks on VR and AR. Teaches courses and training "
             "programs on these technologies."),
        body("<b>Max Collins:</b> PhD researcher specializing in <b>collaborative AR</b>. "
             "Industry experience through internships at <b>Facebook</b> and <b>Oculus</b>. "
             "Currently at the <b>PlayStation Magic Lab</b>."),
    ]),
    sp(8),
    h2("8.1 Defining Virtual Reality (VR) and Augmented Reality (AR)"),
    sp(4),
    h3("Virtual Reality (VR)"),
    body("<b>Virtual Reality (VR)</b> is an interactive computer simulation that the user "
         "is placed <b>inside</b> of. The real world is completely blocked out — the user "
         "sees only synthetic, computer-generated digital information. This is achieved by:"),
    bullet("Placing the user in a <b>darkened room</b> with projections surrounding them, or"),
    bullet("Using <b>VR headsets (glasses)</b> that shut out the real world and feed "
           "the eyes specific digital signals."),
    body("VR is best thought of as an <b>event</b> — like going to a movie. The user sets "
         "aside dedicated time, enters the VR experience (for entertainment, training, etc.), "
         "and then returns to normal life."),
    sp(4),
    h3("Augmented Reality (AR)"),
    body("<b>Augmented Reality (AR)</b> leaves the user in the real world and <b>adds "
         "digital information to it</b>. Rather than replacing reality, it enhances it. "
         "There are <b>three key technological paradigms</b> for AR:"),
    sp(4),
    two_col_table([
        ["Magic Lens Paradigm",
         "The user wears glasses that are transparent (allowing normal vision) while "
         "simultaneously displaying computer-generated objects and entities overlaid "
         "on the real world. The glasses act as a lens through which both reality "
         "and digital content are visible simultaneously."],
        ["Magic Mirror Paradigm",
         "The user sees themselves reflected in a digital display (like a mirror), "
         "but their reflection appears within a computer-generated environment. "
         "This is the paradigm used in Zoom virtual backgrounds — you appear to "
         "be in a different location."],
        ["Projected AR Paradigm",
         "Projectors worn on or near the body project digital imagery directly out "
         "into the real physical world — the digital content appears on real surfaces "
         "and objects in the environment."],
    ], header_row=["AR Paradigm", "Description"]),
    sp(6),
    body("A critical difference between VR and AR: AR has the potential to be available "
         "<b>24/7</b> — just as smartphones are always with us. VR is an event; "
         "AR can be a continuous layer on the world."),
    body("An important concept unique to VR and AR (versus all other media): "
         "<b>proprioception</b>. Proprioception is the body's internal sense of how "
         "it is configured — awareness of limb position, movement, and orientation. "
         "Unlike video, audio, or text, VR and AR engage proprioception, making them "
         "uniquely immersive media."),
    sp(8),
    h2("8.2 Marketing and Product Placement Applications of AR/VR"),
    sp(4),
    h3("Advertising Insertion"),
    body("In VR and AR environments, <b>advertisements can be inserted into experiences</b> "
         "in ways analogous to billboards on a highway — present in the environment "
         "without disrupting it. Just as product placement occurs in movies, branded "
         "objects can be placed naturally in virtual worlds."),
    sp(4),
    h3("Value-Add AR Applications (Alan Craig's Framework)"),
    body("The most significant opportunity for AR in marketing is the concept of "
         "<b>value-add</b> — using AR to provide additional value around a product "
         "that would be impossible through physical retail:"),
    bullet("<b>Car manufacturer example:</b> A user could view a full-scale, interactive "
           "3D model of a vehicle in AR — walking around it, examining the interior, "
           "watching it drive on a virtual track. More practically: AR could guide the "
           "user step-by-step through an oil change, with arrows pointing to the exact "
           "components to interact with. This is a significant value-add to the product."),
    bullet("<b>Amazon AR View:</b> When browsing Amazon, a user can view furniture items "
           "at full scale in their own living space using AR — seeing exactly how a "
           "kitchen table would look in their home before purchasing."),
    bullet("<b>Coach Smart Mirror (Soho, NYC):</b> The AR mirror enables customers to "
           "see themselves wearing different handbag styles without physically trying "
           "them on — a retail experience enhancement enabled by AR."),
    sp(8),
    h2("8.3 Advice for Marketers Using AR/VR Technologies"),
    sp(4),
    h3("Alan Craig's Three Key Pieces of Advice"),
    bullet("<b>Value-add first:</b> Focus on AR/VR applications that genuinely add value "
           "to the product or customer experience — not just novelty. The technology "
           "should solve a real consumer problem or meaningfully enhance engagement."),
    bullet("<b>Stay in front of the curve, but know where you are on the curve:</b> "
           "VR and AR are rapidly evolving. If a firm designs a marketing campaign "
           "using today's technology and it takes months to launch, the technology will "
           "likely look outdated by the time it goes live. Move fast and stay current."),
    bullet("<b>Reality wins:</b> Despite the immersive potential of VR, the physical "
           "world remains paramount. A VR environment may show a user walking on a "
           "solid floor — but if there is a physical hole in the real floor, they will "
           "fall. Marketers must never forget that real-world physics and constraints "
           "override virtual perceptions."),
    sp(4),
    h3("Max Collins' Key Advice"),
    bullet("<b>Consider the collaboration aspect:</b> Think about what AR/VR can do to "
           "<b>bring people together</b> — whether physically co-located or remotely "
           "distributed. Competitions, collaborative design experiences, and shared "
           "virtual spaces can create marketing opportunities that no other medium can."),
    bullet("<b>Ethical responsibility:</b> Developers and marketers working with AR/VR "
           "are <b>directly manipulating people's perceptions of the world and of other "
           "people</b>. This carries serious legal and ethical responsibilities that must "
           "be thoughtfully addressed."),
    sp(8),
    h2("8.4 The Future of AR/VR Technology"),
    sp(4),
    h3("Alan Craig's Predictions"),
    bullet("<b>Faster, better, cheaper:</b> Hardware will improve in resolution, speed, "
           "and interaction complexity. The trajectory of improvement is clear."),
    bullet("<b>Always-on AR glasses are unlikely:</b> Despite predictions, Craig does not "
           "believe people will wear AR glasses 24/7. People already pay significant sums "
           "to avoid wearing glasses (contacts for aesthetics and convenience). "
           "'It's a really tough sell to expect people to be wearing augmented reality "
           "glasses 24/7.'"),
    bullet("<b>Projection-based AR is more promising:</b> If AR is <b>passively projected</b> "
           "from the body into the real world (without requiring a device to be actively "
           "held or worn), adoption barriers are dramatically reduced."),
    bullet("<b>Multi-sensory VR:</b> Future VR will go beyond sight and sound to include "
           "touch, smell, and realistic terrain simulation (e.g., walking on a beach "
           "feeling like an actual beach surface). Coupling with 3D printing will become "
           "more prevalent."),
    sp(4),
    h3("Max Collins' Prediction"),
    body("As AR/VR capabilities expand, the responsibility of <b>ethical and legal "
         "governance</b> becomes increasingly critical. These technologies are manipulating "
         "people's perceptions of reality and of other people — requiring frameworks that "
         "protect users from harm."),
    PageBreak(),
]

# ── CHAPTER 9: QUIZ QUESTIONS & ANSWERS ──────────────────────────────────────
story += [
    section_divider("9", "Quiz Questions & Answers"),
    sp(12),
    h1("9. Quiz Questions & Answers"),
    sp(4),
    h2("9.1 Quiz: Placement Overview"),
    sp(4),
    Paragraph("Q1. Which of the following are concepts that belong to the placement part of the marketing mix?", sQuizQ),
    quiz_option("Inventory management"),
    quiz_option("Logistics"),
    quiz_option("Sales force management"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: The placement portion of the marketing mix encompasses inventory management, logistics, and salesforce management, in addition to the core concepts of distribution and retailing.", sQuizExpl),
    sp(4),
    Paragraph("Q2. What is the definition of the placement portion of the marketing mix?", sQuizQ),
    quiz_option("Displaying a product in a store"),
    quiz_option("It is a measure of ranking a product in the marketplace"),
    quiz_option("The process of making a product accessible to potential customers", correct=True),
    quiz_option("None of the above"),
    Paragraph("Explanation: Placement focuses on making a product conveniently accessible to potential customers — spanning the entire distribution channel from manufacturer to consumer.", sQuizExpl),
    sp(4),
    Paragraph("Q3. Which one is an example of exclusive (intensive) retailing?", sQuizQ),
    quiz_option("Small convenience store selling goods at discount prices"),
    quiz_option("Mercedes Benz selling its luxury cars through chosen distribution channels", correct=True),
    quiz_option("Shopping at Costco with membership card"),
    quiz_option("Walmart selling products in large quantities"),
    Paragraph("Explanation: Exclusive placement means making products available only through a small, carefully selected set of retailers. Louis Vuitton and Mercedes Benz are classic examples — deliberately limiting availability to maintain brand prestige.", sQuizExpl),
    sp(6),
    h2("9.2 Quiz: New Retail"),
    sp(4),
    Paragraph("Q1. Physical retailers are implementing new retail strategies as a reaction to the challenges of operating in a digital world.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: New retail is by definition the collection of strategies physical retailers use to react to the digital world. Examples include Unity Robots, Geissler Smart Carts, and Coach's AR mirror.", sQuizExpl),
    sp(4),
    Paragraph("Q2. Omnichannel marketing is based on the idea of:", sQuizQ),
    quiz_option("Mixing digital and physical retailing"),
    quiz_option("Obtaining the information about a product online and buying it in a physical store"),
    quiz_option("Being strongly influenced by physical environment"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: Omnichannel marketing integrates all aspects: blending digital and physical channels, recognizing webrooming behavior, and acknowledging that digital appeal is shaped by one's physical context.", sQuizExpl),
    sp(6),
    h2("9.3 Quiz: Desktop Manufacturing"),
    sp(4),
    Paragraph("Q1. What are the main advantages of 3D printing compared to traditional manufacturing techniques?", sQuizQ),
    quiz_option("This technology is widely accessible."),
    quiz_option("No additional setup cost", correct=True),
    quiz_option("There are economies of scale in 3D printing."),
    quiz_option("It requires additional assembly to print the objects."),
    Paragraph("Explanation: The key advantage cited is no additional setup cost — the same printer produces different objects with no retooling. Note: 3D printing does NOT have economies of scale (it costs the same per unit regardless of quantity), and it is NOT yet widely accessible to everyone.", sQuizExpl),
    sp(4),
    Paragraph("Q2. With 3D printing technology, products can be digitized and downloaded.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: This is the fundamental transformative property of 3D printing for placement — products exist as digital files (STL files) that can be downloaded and printed locally, eliminating physical shipping.", sQuizExpl),
    sp(6),
    h2("9.4 Quiz: Thingiverse Exercise"),
    sp(4),
    Paragraph("Q1. Which of the following statement about Thingiverse is CORRECT?", sQuizQ),
    quiz_option("Thingiverse was launched in 2018."),
    quiz_option("Thingiverse library has over 100,000 objects."),
    quiz_option("Thingiverse was launched by MakerBot.", correct=True),
    quiz_option("Thingiverse library objects can be downloaded with affordable price."),
    Paragraph("Explanation: Thingiverse was launched by MakerBot and is now owned by Ultimaker. All files are free (not merely 'affordable'). The library contains files for millions of objects (not just 100,000).", sQuizExpl),
    sp(4),
    Paragraph("Q2. Where do you click to explore things submitted by users on Thingiverse.com?", sQuizQ),
    quiz_option("Create"),
    quiz_option("Education"),
    quiz_option("Dashboard"),
    quiz_option("Explore", correct=True),
    Paragraph("Explanation: The 'Explore' tab on Thingiverse.com provides access to user-submitted design files across categories.", sQuizExpl),
    sp(4),
    Paragraph("Q3. Where can you obtain the ID number of a thing on Thingiverse.com?", sQuizQ),
    quiz_option("From the thing's web URL", correct=True),
    quiz_option("Under the summary section"),
    quiz_option("By looking at the tags"),
    quiz_option("By reaching out to the creator"),
    Paragraph("Explanation: Each thing's unique ID number is embedded directly in its web URL on Thingiverse.com.", sQuizExpl),
    sp(4),
    Paragraph("Q4. In what ways does Thingiverse.com allow visitors to understand the product and interact with the creator? (Select all that apply)", sQuizQ),
    quiz_option("Creators can share the thing's files with visitors.", correct=True),
    quiz_option("Visitors can print the thing tag if they choose to print the thing and display it publicly."),
    quiz_option("Visitors can like and leave comments about the thing they are visiting.", correct=True),
    quiz_option("Creators can share the 3D printing setting with visitors.", correct=True),
    Paragraph("Explanation: Three options are correct: file sharing, liking/commenting, and sharing print settings. The 'print the thing tag' option was not mentioned in the course material.", sQuizExpl),
    sp(4),
    Paragraph("Q5. Maker files can be downloaded for free.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: All design files on Thingiverse.com are available for free download — this is one of its defining characteristics.", sQuizExpl),
    sp(4),
    Paragraph("Q6. What impact(s) might a service like Thingiverse.com have on product placement?", sQuizQ),
    Paragraph("Sample Answer: Thingiverse decentralizes product placement by enabling creators to directly share and distribute designs globally, eliminating channel intermediaries. It transforms placement from a physical, logistically intensive process to a digital, instantaneous one — shifting from long distribution channels for physical goods to short channels for digital goods.", sQuizExpl),
    sp(6),
    h2("9.5 Module 3 Comprehensive Quiz"),
    sp(4),
    Paragraph("Q1. How does the digital marketing environment impact placement?", sQuizQ),
    quiz_option("Shift from long distribution channels for physical goods to short distribution channels for digital goods", correct=True),
    quiz_option("Higher cost for transportation and logistics"),
    quiz_option("Increasing number of channel members"),
    quiz_option("None of the above"),
    Paragraph("Explanation: The core digital shift in placement is from long physical distribution channels (Manufacturer → Importer → Wholesaler → Retailer → Customer) to short digital channels (Designer → Thingiverse → 3D Printer → Customer).", sQuizExpl),
    sp(4),
    Paragraph("Q2. Digital tools such as 3D printers have the potential to shrink the supply chain and replace retailers.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: Yes. 3D printing can eliminate the need for physical retailers (and even distributors) by allowing customers to download and print products locally. The Baker Cube on Thingiverse is a direct example.", sQuizExpl),
    sp(4),
    Paragraph("Q3. Which of the following is NOT observed in the new retailing landscape?", sQuizQ),
    quiz_option("Online retailing is heavily influenced by location."),
    quiz_option("Physical retailing is most effective in terms of conducting product research and getting the best price.", correct=True),
    quiz_option("Digital retail channels provide considerable product information, technical information, and user reviews."),
    quiz_option("Retailers are adapting to omnichannel marketing."),
    Paragraph("Explanation: The FALSE statement is that physical retailing is superior for product research and best price — it is ONLINE retailing that excels at product research and price comparison. Physical retail excels at returns, service, and the tactile experience.", sQuizExpl),
    sp(4),
    Paragraph("Q4. What is the advantage of the Power of Touch for physical stores?", sQuizQ),
    quiz_option("Helps retailers lower the cost of goods sold"),
    quiz_option("Helps keep customers in a store for a longer period of time", correct=True),
    quiz_option("Sells slow-moving products"),
    quiz_option("Increases customer retention"),
    Paragraph("Explanation: The tactile experience — touching, feeling, and trying products physically — is a key differentiator of physical retail and is associated with longer in-store dwell time.", sQuizExpl),
    sp(4),
    Paragraph("Q5. 3D printers create products in an additive manner.", sQuizQ),
    quiz_option("True", correct=True),
    quiz_option("False"),
    Paragraph("Explanation: By definition, 3D printing is an additive manufacturing process — it builds objects one layer at a time, adding material progressively, rather than removing material from a block (subtractive manufacturing).", sQuizExpl),
    sp(4),
    Paragraph("Q6. How can 3D printers disrupt traditional businesses?", sQuizQ),
    quiz_option("They can turn the physical good into a digital file that can be created by anyone"),
    quiz_option("3D printers can significantly lower the cost of manufacturing"),
    quiz_option("3D printing may be a threat to logistics companies"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: All three disruptions are valid. 3D printing: (1) democratizes manufacturing by allowing anyone to create objects from digital files; (2) lowers manufacturing costs significantly for low-volume production; (3) threatens logistics companies like DHL and UPS by enabling local production that eliminates the need for physical shipping.", sQuizExpl),
    sp(4),
    Paragraph("Q7. Why do physical stores use a Marketing to Shoppers strategy?", sQuizQ),
    quiz_option("To understand and influence customer behavior"),
    quiz_option("To keep the customers in-store for a longer period"),
    quiz_option("To promote self-service"),
    quiz_option("All of the above", correct=True),
    Paragraph("Explanation: Marketing to Shoppers is a holistic in-store strategy that combines behavioral understanding, extended dwell time, and appropriate levels of self-service to maximize both customer satisfaction and sales.", sQuizExpl),
    sp(4),
    Paragraph("Q8. Which of the following is NOT true about 3D printers?", sQuizQ),
    quiz_option("Different materials such as metal, plastic, and rubber can be 3D printed"),
    quiz_option("It requires high set-up costs", correct=True),
    quiz_option("This technology allows users to make complex assembled objects"),
    quiz_option("It allows a small manufacturer to compete with a large corporation"),
    Paragraph("Explanation: 3D printing does NOT require high setup costs — in fact, having NO additional setup cost is one of its key advantages. The same printer can produce different objects with zero retooling. Desktop 3D printers are available for less than $200.", sQuizExpl),
    sp(4),
    Paragraph("Q9. Which of the following is NOT an example of 'Enhancing the Physical by Adding the Digital'?", sQuizQ),
    quiz_option("Using high-tech hangers that display the number of 'likes' received by an item in a clothing store"),
    quiz_option("Installing AR devices that allow customers to see themselves in different makeup in a beauty store"),
    quiz_option("Increasing the number of electronic devices sold in a store", correct=True),
    quiz_option("Virtual store where a customer can make purchases and pick up later at a physical store"),
    Paragraph("Explanation: Simply increasing the number of electronic devices sold is a product decision, not an example of using digital technology to enhance the in-store physical experience. The other three options all represent genuine integrations of digital tools into the physical retail environment.", sQuizExpl),
    sp(4),
    Paragraph("Q10. According to McCue (2015, HBR): How can the tipping point of 3D printing be reached?", sQuizQ),
    quiz_option("When the technology's overall output rises."),
    quiz_option("It happens when enough people see a huge potential and new possibilities of this technology.", correct=True),
    quiz_option("When big companies install this technology and start using it widely."),
    quiz_option("When the technology becomes accessible in a large number of neighborhoods."),
    Paragraph("Explanation: Per McCue's HBR article, the tipping point for 3D printing is driven by a critical mass of people recognizing and acting on the technology's potential — not by output levels, corporate adoption, or geographic availability alone.", sQuizExpl),
    PageBreak(),
]

# ── CHAPTER 10: DESCRIPTIVE QUESTIONS ────────────────────────────────────────
story += [
    section_divider("10", "Descriptive Questions & Model Answers"),
    sp(12),
    h1("10. Descriptive Questions & Model Answers"),
    body("The following questions are exam-representative at 3–4 marks each. "
         "Complete answers address all sub-components and use key terminology precisely."),
    sp(8),
    Paragraph("DQ1. Define placement and explain the traditional distribution channel. Why is it costly, and how is the digital revolution disrupting it? [3 marks]", sDescQ),
    body("<b>Placement</b> is the component of the marketing mix focused on making a product "
         "conveniently accessible to potential customers. For most physical products, this "
         "involves moving the product through a <b>traditional distribution channel</b>: "
         "Manufacturer → Importer → Wholesaler → Retailer → Customer."),
    body("The channel is costly for three reasons: (1) Each member is an independent firm "
         "maximizing its own profit, consuming margin at every step — typically, a manufacturer "
         "receives only <b>60–70% of a product's retail price</b>. (2) Managing multiple "
         "independent partners requires significant oversight, creating conflicts and "
         "misunderstandings. (3) Physical logistics (shipping, storage, handling) at each "
         "step add both time and financial cost."),
    body("The digital revolution is disrupting this channel in two ways. First, <b>online "
         "retail</b> (Amazon, brand websites) bypasses physical retailers, allowing "
         "direct-to-consumer selling. Second, and more radically, <b>3D printing and "
         "digital design file sharing</b> (Thingiverse.com) can eliminate the entire "
         "physical distribution chain — replacing it with a short digital channel "
         "(Designer → File Repository → 3D Printer → Customer). Products travel as "
         "data rather than as physical objects."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ2. Define 'New Retail' and explain the three key observations about the new retail landscape, with examples. [4 marks]", sDescQ),
    body("<b>New Retail</b> is the collection of strategies — both physical and digital — "
         "that physical retailers are employing to react to the challenges of operating in "
         "a digital world. It represents the convergence of online and offline commerce."),
    body("<b>Three Key Observations:</b>"),
    bullet("<b>1. Location, Location, Location:</b> Despite the digital revolution, physical "
           "location remains critically important. Research shows online retail adoption is "
           "higher in areas with poor physical retail access (e.g., small towns like "
           "Champaign) than in cities with abundant physical options (e.g., Chicago). "
           "The appeal of digital retail is shaped by one's physical context."),
    bullet("<b>2. Purchase vs. Information:</b> Digital retailers serve dual roles — "
           "as transactional channels AND as information channels. This creates two "
           "important consumer behaviors: (a) <b>Showrooming</b> — visiting a physical "
           "store first, then buying online (approximately 2 in 3 US online buyers first "
           "visit a physical store); and (b) <b>Webrooming</b> — researching online, "
           "then buying in-store. Despite receiving less press, webrooming is MORE common "
           "than showrooming."),
    bullet("<b>3. Digital and Physical Integration (Omnichannel):</b> Digital and physical "
           "retail are not opposites — they are complementary. <b>Omnichannel marketing</b> "
           "integrates both by leveraging each channel's strengths: physical retail excels "
           "at returns, service, and touch-and-feel; digital channels excel at research, "
           "reviews, and price comparison. Examples: Geissler's Instacart smart shopping "
           "carts, Coach's AR mirror in Soho, and Unity's Softbank robots that boosted "
           "promoted product sales by over 25%."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ3. Define desktop 3D printing. Explain how it works and describe three key advantages over traditional manufacturing, with reference to a real example. [3 marks]", sDescQ),
    body("A <b>desktop 3D printer</b> is an electronic device (approximately the size of a "
         "microwave oven) that converts digital designs into physical objects through an "
         "<b>additive process</b> — building objects one layer at a time, analogous to "
         "how a skyscraper is built floor by floor."),
    body("<b>How it works:</b> A digital design file (an <b>STL file</b>) is created "
         "using 3D modeling software (e.g., Google SketchUp), generated from a 3D scan, "
         "or downloaded from a file-sharing site (e.g., Thingiverse). Slicing software "
         "converts the STL file into layer-by-layer instructions. The printer's motherboard "
         "reads these instructions and moves the printhead in three dimensions, depositing "
         "or curing material layer by layer. Almost any material that can be hardened or "
         "softened can be printed — plastics, metals, ceramics, carbon fiber, even chocolate."),
    body("<b>Three Key Advantages:</b>"),
    bullet("<b>No additional setup cost:</b> The same printer produces different objects "
           "with no retooling. Traditional manufacturing requires expensive molds, dies, "
           "and setup changes between products."),
    bullet("<b>No economies of scale constraint:</b> The per-unit cost is the same "
           "whether printing 1 or 100 objects. Traditional manufacturing requires "
           "large production runs to justify setup costs."),
    bullet("<b>No inventory required:</b> Print on demand — products are created only "
           "when needed, eliminating warehousing costs and stockout risk."),
    body("Real example: During <b>COVID-19</b>, Italian volunteers 3D-printed ventilator "
         "connector valves that medical companies were selling for <b>$10,000 each</b> — "
         "printable for approximately <b>$1</b>. This demonstrates both the cost advantage "
         "and the democratizing power of desktop manufacturing."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ4. Describe Tesla's unique retail strategy using three key differentiators. Analyze its pros and cons. [4 marks]", sDescQ),
    body("Tesla's retail strategy is fundamentally different from all traditional automobile "
         "manufacturers in three key ways:"),
    bullet("<b>1. Number of locations:</b> Tesla has far fewer retail locations relative "
           "to sales volume. In Illinois, there are 28 Volkswagen dealers but only 9 Tesla "
           "stores — yet Tesla sells approximately twice as many cars. All 9 Illinois "
           "Tesla locations are in the Chicago metropolitan area."),
    bullet("<b>2. Size and design:</b> Traditional dealerships are large, expansive "
           "facilities with dozens of vehicles in parking lots and large showrooms. "
           "Tesla stores are small, minimalist showrooms typically containing only "
           "2–3 vehicles, often located in high-traffic shopping areas."),
    bullet("<b>3. Role of the retailer:</b> Traditional dealerships exist to make a sale "
           "through persuasive salespeople — a process that can take hours. Tesla stores "
           "exist to provide information. Prices are non-negotiable, fixed, and publicly "
           "listed. A Tesla can be purchased in 5 minutes on its website, or from inside "
           "another Tesla. Over 70% of Tesla sales occur online."),
    body("<b>Pros:</b> Lower operating costs; transparent fixed pricing; rapid, frictionless "
         "transactions; stronger brand control; scalable global reach through digital sales; "
         "25 million X followers provide massive free promotional reach."),
    body("<b>Cons:</b> Limited physical presence (geographic access barriers for non-urban "
         "customers); regulatory conflict with dealership laws in some US states; limited "
         "personal guidance for high-involvement buyers; potential service bottlenecks."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ5. Explain the four practical recommendations for desktop manufacturing, with a focus on 'Done is the Engine of More.' [3 marks]", sDescQ),
    bullet("<b>1. Make the Physical Digital:</b> Convert physical products into digital "
           "design files using 3D modeling software or 3D scanners. Once digital, products "
           "can be stored, transmitted, and modified at near-zero cost. Particularly "
           "valuable for replacement parts (e.g., NASA uses 3D printers to replace "
           "broken spacecraft parts in orbit)."),
    bullet("<b>2. Let Customers Customize Your Design:</b> Digital products can be "
           "customized cheaply — modify the file and print a new version. Firms can "
           "offer templates and allow customers to design products to their specific "
           "needs, eliminating one-size-fits-all products."),
    bullet("<b>3. Cut Out the Middleman:</b> Post digital files on a company website "
           "or service like Craftcloud 3D.com for direct download and printing by customers. "
           "Just as iTunes eliminated physical music stores, 3D printing can eliminate "
           "physical product distribution."),
    bullet("<b>4. Done is the Engine of More:</b> From the <b>Cult of Done Manifesto</b> "
           "(Brie Pettis & Kio Stark), displayed on the Illinois Maker Lab wall. This "
           "principle says: act on your ideas, don't over-plan. Because 3D printing is "
           "cheap and fast, design → print → evaluate → modify → reprint cycles can "
           "occur rapidly with minimal cost. Action generates insight, which generates "
           "more action. This iterative, prototype-driven innovation cycle is a core "
           "advantage of desktop manufacturing over traditional manufacturing."),
    sp(6),
    thin_hr(),
    sp(6),
    Paragraph("DQ6. Compare and contrast Virtual Reality (VR) and Augmented Reality (AR). How can each be used in marketing and product placement? [4 marks]", sDescQ),
    body("<b>Virtual Reality (VR)</b> completely replaces the real world with a digital "
         "simulation. The user is immersed inside the virtual environment, which blocks "
         "out all real-world sensory input. Best understood as an <b>event</b> — dedicated, "
         "time-boxed experiences for entertainment, training, or exploration."),
    body("<b>Augmented Reality (AR)</b> overlays digital information on the real world — "
         "the user remains in their physical environment. AR has three technological "
         "paradigms: (1) <b>Magic Lens</b> (transparent glasses with digital overlays), "
         "(2) <b>Magic Mirror</b> (digital reflection in a modified environment), and "
         "(3) <b>Projected AR</b> (digital imagery projected directly onto real surfaces). "
         "AR is potentially a <b>24/7 presence</b> in daily life, unlike VR."),
    body("<b>Marketing and Placement Applications:</b>"),
    bullet("<b>VR:</b> Product placement within virtual worlds (like movie product placement); "
           "immersive brand experience events; virtual test-drives or property tours."),
    bullet("<b>AR value-add:</b> Amazon AR View allows furniture visualization at full "
           "scale in the customer's own home; Coach's AR mirror in Soho lets customers "
           "virtually try on handbags; automotive AR can guide step-by-step maintenance "
           "with directional arrows on the actual vehicle."),
    bullet("<b>Unique advantage — proprioception:</b> VR and AR engage the body's sense "
           "of position and movement (proprioception), which no other medium does. This "
           "creates uniquely immersive and memorable brand experiences."),
    bullet("<b>Key caution (Alan Craig):</b> 'Reality wins.' No matter how immersive the "
           "virtual experience, the physical world remains paramount. Marketing campaigns "
           "using AR/VR must account for real-world constraints."),
    sp(12),
    hr(GOLD, 2),
    sp(8),
    Paragraph("END OF MODULE 3 COMPLETE STUDY NOTES", make_style("end",
        fontName="Helvetica-Bold", fontSize=14, textColor=DARK_BLUE,
        alignment=TA_CENTER, spaceAfter=6)),
    Paragraph("Marketing in a Digital World · Module 3: Placement · Gies College of Business, University of Illinois",
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
