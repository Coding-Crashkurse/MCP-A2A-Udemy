from fastmcp import FastMCP

mcp = FastMCP(name="TagFilterDemo")

@mcp.tool(tags={"math"})
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(tags={"math"})
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool(tags={"search"})
def search(item: str):
    db1 = {
        "iphone_15_pro_128gb": {"name": "Apple iPhone 15 Pro (128GB)", "price_usd": 999},
        "ps5_slim": {"name": "Sony PlayStation 5 Slim", "price_usd": 499},
    }
    return db1.get(item) or "Item nicht gefunden"

@mcp.tool(tags={"search"})
def search_suggest(item: str):
    db2 = {
        "switch_oled": {"name": "Nintendo Switch OLED", "price_usd": 349},
        "galaxy_s24_ultra_256gb": {"name": "Samsung Galaxy S24 Ultra (256GB)", "price_usd": 1299},
    }
    return db2.get(item) or "Item nicht gefunden"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8052, path="/mcp/")
