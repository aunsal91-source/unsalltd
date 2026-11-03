"""Builds blog/index.html, blog/<slug>.html and the Insights cards on the home page.

Edit POSTS below, then run:  python tools/build_blog.py
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent

POSTS = [
    {
        "slug": "uk-toy-market",
        "tag": "Toys",
        "date": "November 2026",
        "title": "The UK toy market: what brands need to know before entering",
        "summary": "One of Europe's largest toy markets — concentrated retail, a brutal Q4, a growing adult buyer and its own post-Brexit compliance rules.",
        "body": """
<p class="intro">The UK is one of the largest toy markets in Europe, and one of the most concentrated. For a brand or distributor coming from abroad, the opportunity is real — but the route to shelf, the calendar and the compliance rules all work differently from continental markets.</p>

<h2>A market shaped by a handful of buyers</h2>
<p>UK toy retail runs through a short list of gatekeepers: the specialist chain Smyths Toys, Argos, Amazon, The Entertainer, the big four supermarkets and the discount and variety chains such as B&amp;M, Home Bargains and The Range. Hamleys, John Lewis, Next and independent toy shops add depth at the premium end.</p>
<p>That concentration cuts both ways. A single national listing can transform volumes; losing one can do the same in reverse. Buyers expect a clear range plan, a marketing commitment and confidence that you can supply consistently through peak — not just a good product.</p>

<h2>Q4 decides the year</h2>
<p>A disproportionate share of annual toy sales happens between October and December. Most range reviews and listings are agreed far earlier, around Toy Fair London at Olympia in January and the buying cycle that follows. Stock for Christmas is typically shipped from the Far East over the summer.</p>
<ul>
  <li>Plan the year backwards from Black Friday and Christmas, not forwards from January.</li>
  <li>Late stock is often worse than no stock: retailers will cancel, and marketing money is wasted.</li>
  <li>Forecast replenishment carefully — a hit product sells out in November and cannot be re-shipped in time.</li>
</ul>

<h2>Kidults, licences and collectibles</h2>
<p>Industry trackers consistently report adults buying for themselves as one of the fastest-growing segments: construction sets, collectible figures, die-cast models, trading cards and nostalgia brands. These buyers shop all year rather than only at Christmas, are less price-sensitive and buy heavily online — which smooths some of the seasonality.</p>
<p>Licensed products continue to take a large share of sales. A strong licence opens doors with buyers, but royalty rates and minimum guarantees need to be modelled against realistic sell-through, not the best case.</p>

<h2>Compliance after Brexit</h2>
<p>In Great Britain, toys are regulated by the Toys (Safety) Regulations 2011. Products need UKCA marking or, under the government's continued recognition, CE marking, plus a UK-based importer or manufacturer address on the product or packaging. Northern Ireland follows EU rules under the Windsor Framework, and the EU's new Toy Safety Regulation — adopted in 2025, with a multi-year transition — brings stricter chemical limits and a digital product passport.</p>
<p>Marketplaces and major retailers increasingly ask for test reports, technical files and a named responsible person before listing. Having these ready shortens onboarding considerably.</p>

<div class="takeaways">
  <h2>Key takeaways</h2>
  <ul>
    <li>Win a small number of the right accounts rather than chasing every channel at once.</li>
    <li>Work to the buying calendar: listings are decided in Q1 for Q4.</li>
    <li>Treat compliance paperwork as a sales asset, not an afterthought.</li>
  </ul>
</div>
""",
    },
    {
        "slug": "uk-wholesale-market",
        "tag": "Wholesale",
        "date": "November 2026",
        "title": "Selling wholesale in the UK: channels, terms and margins",
        "summary": "From national retail buyers to cash & carry, discounters and online wholesale platforms — how goods actually reach UK shelves.",
        "body": """
<p class="intro">"Wholesale" in the UK covers very different routes to market. Choosing the right one — and pricing for it — matters more than finding the most buyers.</p>

<h2>The main routes</h2>
<ul>
  <li><b>Direct to national retail.</b> Selling straight to chains and supermarkets gives volume and visibility, but buyers expect marketing support, promotional funding and tight service levels.</li>
  <li><b>Distributors and agents.</b> A distributor holds stock, sells and collects payment; an agent sells on commission while you ship. Both give you an existing book of accounts in exchange for margin.</li>
  <li><b>Discount and variety retail.</b> B&amp;M, Home Bargains, The Range, Poundland and similar chains buy in volume, often direct from the factory, and move fast on value-led ranges.</li>
  <li><b>Cash &amp; carry and symbol groups.</b> Booker, Bestway, Parfetts and the buying groups serve thousands of convenience and independent stores — strong for impulse categories.</li>
  <li><b>Online wholesale platforms.</b> Faire and Ankorstore make it easy to reach independent shops across the UK and Europe with low minimums, at the cost of a platform commission.</li>
</ul>

<h2>Price architecture first</h2>
<p>Every channel takes its own margin, so the recommended retail price has to carry the whole chain: factory cost, freight and duty, warehousing, your margin, the distributor's margin, the retailer's margin and VAT. Brands that set a wholesale price without modelling this end up either unprofitable or uncompetitive on shelf. A consistent price ladder also avoids channel conflict — a retailer will not stay listed if the same product is cheaper on your own website or on a marketplace.</p>

<h2>Terms and working capital</h2>
<p>Large retailers commonly pay on 30 to 60 days, sometimes longer, and may deduct for promotions, damages or late deliveries. Meanwhile the factory wants paying before shipment. The gap between paying for stock and being paid for it is where many growing suppliers run short of cash. Trade credit insurance, invoice finance and careful deposit terms with factories all help — but they need to be in place before the big order arrives.</p>

<h2>Logistics expectations</h2>
<p>Retail distribution centres run to booked delivery slots, strict pallet and labelling specifications and service-level penalties. Using a 3PL that already delivers into those networks avoids expensive rejections. For smaller independent accounts, efficient pick-and-pack of mixed cartons matters more than full-pallet handling.</p>

<div class="takeaways">
  <h2>Key takeaways</h2>
  <ul>
    <li>Pick channels deliberately; each one changes your price ladder.</li>
    <li>Model cash flow from factory deposit to retailer payment, including deductions.</li>
    <li>Retail compliance — slots, labels, pallets — is part of the product.</li>
  </ul>
</div>
""",
    },
    {
        "slug": "uk-ecommerce-market",
        "tag": "E-commerce",
        "date": "November 2026",
        "title": "UK e-commerce: a mature market with demanding customers",
        "summary": "Roughly a quarter of UK retail spend happens online. Next-day delivery, easy returns and new consumer law set the bar.",
        "body": """
<p class="intro">The UK is one of the most developed online retail markets in the world: according to ONS data, roughly a quarter of all retail spending now happens online. That maturity brings scale — and customers whose expectations are already set by the largest players.</p>

<h2>Delivery and returns are the product</h2>
<p>UK shoppers expect fast, cheap or free delivery, real-time tracking and simple returns. Next-day is standard for many categories, and out-of-home options — parcel lockers and collection points from InPost, Evri, DPD and others — have grown rapidly. Every one of these promises has a cost that needs to be built into the price and the fulfilment set-up.</p>
<ul>
  <li>Under the Consumer Contracts Regulations, most online purchases can be cancelled within 14 days of delivery.</li>
  <li>Returns rates vary sharply by category; fashion is far higher than toys or homeware.</li>
  <li>A reliable 3PL with good carrier rates is usually cheaper than self-fulfilment once volumes grow.</li>
</ul>

<h2>Own site or marketplace?</h2>
<p>A direct-to-consumer site gives you the customer data, the brand experience and better margin. Marketplaces give you traffic on day one. Most successful brands run both, with the own site holding the full range and the marketplaces carrying the fastest sellers. The decision is less about either/or and more about how much margin you are willing to trade for reach.</p>

<h2>New consumer rules</h2>
<p>The Digital Markets, Competition and Consumers Act 2024 gave the Competition and Markets Authority power to fine businesses directly for consumer law breaches. Since April 2025 it has also banned fake reviews and hidden "drip" pricing, where mandatory fees appear only at checkout. Online sellers should review how they collect reviews, display prices and run subscription offers.</p>

<h2>Selling from abroad</h2>
<p>Overseas sellers shipping directly to UK customers face import VAT rules introduced in 2021: for consignments up to £135, VAT is charged at the point of sale, and online marketplaces are responsible for collecting it. The government has also announced that it will remove the customs duty relief on low-value imports. For most established brands, holding stock in a UK warehouse remains the faster and cleaner model.</p>

<div class="takeaways">
  <h2>Key takeaways</h2>
  <ul>
    <li>Price in delivery and returns from the start.</li>
    <li>Use marketplaces for reach and your own site for margin and data.</li>
    <li>Check reviews, pricing and subscriptions against the 2024 Act.</li>
  </ul>
</div>
""",
    },
    {
        "slug": "uk-online-marketplaces",
        "tag": "Marketplaces",
        "date": "November 2026",
        "title": "UK online marketplaces: Amazon, eBay, TikTok Shop and beyond",
        "summary": "Where UK shoppers buy, what each platform rewards, and why retailers are opening their own marketplaces.",
        "body": """
<p class="intro">Marketplaces are the starting point for a large share of UK online shopping journeys. Each platform has its own audience, fee structure and rules — and the operational demands of running them well are often underestimated.</p>

<h2>The main platforms</h2>
<ul>
  <li><b>Amazon</b> — the largest by some distance. Winning the Buy Box depends on price, stock availability and fulfilment performance; Fulfilment by Amazon (FBA) or Seller Fulfilled Prime make a significant difference.</li>
  <li><b>eBay</b> — strong for collectibles, refurbished and value ranges, and still an important channel for many small businesses.</li>
  <li><b>TikTok Shop</b> — content-driven discovery, where sales come through creators and live shopping rather than search. It can scale fast, but needs a steady flow of video and affiliate partnerships.</li>
  <li><b>Temu and Shein</b> — low-price, cross-border platforms that have reset price expectations in several categories.</li>
  <li><b>Etsy, OnBuy, Fruugo</b> — niche or growing alternatives worth testing for specific ranges.</li>
</ul>

<h2>Retailers becoming marketplaces</h2>
<p>A growing number of UK retailers — Debenhams, B&amp;Q, Next and others — now let third-party brands sell through their websites. For a brand, this can mean the reach of a household retail name without a traditional wholesale listing, though commissions and service standards are demanding.</p>

<h2>The operational side</h2>
<p>Marketplace success is mostly operational: accurate stock across channels, fast dispatch, low cancellation and late-shipment rates, and well-structured listings. Inventory synchronisation becomes critical once you sell on more than two platforms. Fees also add up quickly — referral fees, fulfilment fees, storage fees, advertising — so margin should be calculated per SKU, per platform.</p>

<h2>Compliance is tightening</h2>
<p>Marketplaces are already responsible for collecting VAT on many sales by overseas sellers, and are asking more of sellers on product safety. The Product Regulation and Metrology Act 2025 allows the government to place new product safety obligations on online marketplaces, and for toys and other regulated categories platforms increasingly request test reports and a UK responsible person before listing.</p>

<div class="takeaways">
  <h2>Key takeaways</h2>
  <ul>
    <li>Choose platforms by audience and category fit, not by size alone.</li>
    <li>Measure profitability per SKU after all platform fees and advertising.</li>
    <li>Keep safety and VAT documentation ready — platforms will ask for it.</li>
  </ul>
</div>
""",
    },
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="../assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=DM+Sans:opsz,wght@9..40,400..700&display=swap">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

<header>
  <div class="wrap bar">
    <a class="brand" href="../" aria-label="Unsal Ltd home"><img src="../assets/icon.png" alt="">UNSAL</a>
    <nav aria-label="Main">
      <a href="../#about">About</a>
      <a href="../#services">Services</a>
      <a href="../#approach">Approach</a>
      <a href="./">Insights</a>
      <a class="cta" href="../#contact">Let's talk</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer>
  <div class="wrap">
    <p class="big">UNSAL<span>.</span></p>
    <p class="site">Sales consultancy · www.unsalltd.com</p>
    <div class="legal">
      <span>Unsal Ltd · Registered in England &amp; Wales · Company no. 13789687</span>
      <span>© <span id="yr">2026</span> Unsal Ltd</span>
    </div>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear()</script>
</body>
</html>
"""


def card(p, prefix):
    return f"""  <a class="post" href="{prefix}{p['slug']}.html">
    <div class="tag">{p['tag']}</div>
    <h3>{html.escape(p['title'])}</h3>
    <p>{html.escape(p['summary'])}</p>
    <span class="more">Read →</span>
  </a>"""


def cards(prefix):
    return '<div class="posts">\n' + "\n".join(card(p, prefix) for p in POSTS) + "\n</div>"


def main():
    out = ROOT / "blog"
    out.mkdir(exist_ok=True)

    index = HEAD.format(title="Insights — Unsal Ltd",
                        desc="Unsal Ltd insights on the UK toy, wholesale, e-commerce and marketplace landscape.")
    index += f"""
<div class="page-head">
  <div class="wrap">
    <p class="eyebrow">Insights</p>
    <h1>Notes on the UK market.</h1>
    <p class="lede">Practical reading on UK toys, wholesale, e-commerce and marketplaces — for brands and distributors entering or scaling here.</p>
  </div>
</div>
<main class="wrap" style="padding-block:64px 96px">
{cards("")}
</main>
""" + FOOT
    (out / "index.html").write_text(index, encoding="utf-8")

    for p in POSTS:
        page = HEAD.format(title=f"{html.escape(p['title'])} — Unsal Ltd", desc=html.escape(p["summary"]))
        page += f"""
<div class="page-head">
  <div class="wrap"><div class="article">
    <a class="back" href="./">← All insights</a>
    <h1>{html.escape(p['title'])}</h1>
    <div class="byline"><span class="tag">{p['tag']}</span> Unsal Ltd · {p['date']}</div>
  </div></div>
</div>
<main class="wrap">
  <article class="article">
{p['body'].strip()}
    <p class="note">This article is general information, not legal, tax or financial advice.</p>
    <div class="ask">
      <p><b>Launching in the UK or looking to grow your sales here?</b> <a href="../#contact">Get in touch</a> — we'd like to hear about it.</p>
    </div>
  </article>
</main>
""" + FOOT
        (out / f"{p['slug']}.html").write_text(page, encoding="utf-8")

    home = ROOT / "index.html"
    s = home.read_text(encoding="utf-8")
    a, b = s.index("<!--posts-->") + len("<!--posts-->"), s.index("<!--/posts-->")
    home.write_text(s[:a] + "\n" + cards("blog/") + "\n" + s[b:], encoding="utf-8")
    print(f"built {len(POSTS)} posts")


if __name__ == "__main__":
    main()
