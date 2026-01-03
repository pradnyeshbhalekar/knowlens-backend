from app.services.claims_extractor_llm import extract_claims_from_text

text = """
RAM prices are experiencing an unprecedented surge, with consumer memory kits doubling or even tripling in cost since mid-year. Industry experts describe the current situation as a “memory apocalypse” driven primarily by the astronomical demands of the AI sector.
Why Prices Are Skyrocketing
The current shortage is caused by a massive reallocation of global manufacturing resources:
AI-Driven Demand: Major AI companies (e.g., Nvidia, OpenAI) are purchasing vast amounts of high-speed memory for data centers. Manufacturers like Samsung and SK Hynix are prioritizing high-profit HBM (High-Bandwidth Memory) for AI over standard consumer DDR5 and DDR4.
Supply Reallocation: To meet AI demands, chipmakers have redirected wafer capacity away from traditional DRAM. This has left standard PC and laptop memory in severe undersupply.
Micron’s Exit: In early December 2025, Micron announced it would retire its famous Crucial consumer brand by 2026 to focus entirely on enterprise and AI customers, further tightening the consumer market.
Hoarding and Panic Buying: Major system builders like Lenovo and Dell have reportedly begun stockpiling RAM to protect their supply chains, while retailers have seen consumers panic-buy existing stock.
Impact on Prices
Prices for common memory kits have seen vertical increases in just a few months:
DDR5 32GB Kits: Many kits that cost roughly $90-$110 in August 2025 now sell for over $360-$400.
DDR5 64GB Kits: High-end kits that were $170-$200 are now frequently listed between $500 and $880.
"""

claims = extract_claims_from_text(text)
print("TEXT LENGTH:", len(text))


for c in claims:
    print("-", c)
