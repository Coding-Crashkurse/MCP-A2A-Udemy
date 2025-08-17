from fastapi import FastAPI, HTTPException
from fastmcp import FastMCP
from pydantic import BaseModel

# pre-v2.10: only needed when restoring semantic GET→Resource mapping
from fastmcp.server.openapi import RouteMap, MCPType

app = FastAPI(title="Product API")
_products: dict[int, dict] = {}


class Product(BaseModel):
    name: str
    price: float


@app.get("/products")
def list_products():
    """List all products"""
    return list(_products.values())


@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Get a product by its ID"""
    if product_id not in _products:
        raise HTTPException(status_code=404, detail="Product not found")
    return _products[product_id]


@app.post("/products")
def create_product(p: Product):
    """Create a new product"""
    new_id = len(_products) + 1
    _products[new_id] = {"id": new_id, **p.model_dump()}
    return _products[new_id]


# pre-v2.8.0: GET routes become Resources/ResourceTemplates; everything else → Tool
semantic_maps = [
    RouteMap(methods=["GET"], pattern=r".*\{.*\}.*", mcp_type=MCPType.RESOURCE_TEMPLATE),
    RouteMap(methods=["GET"], pattern=r".*", mcp_type=MCPType.RESOURCE),
    # pre-v2.8.0: explicit fallback for non-GET routes → Tool
    RouteMap(mcp_type=MCPType.TOOL),
]

# pre-v2.8.0: enable semantic GET→Resource behavior (active)
# mcp = FastMCP.from_fastapi(app=app, name="ProductMCP", route_maps=semantic_maps)

# v2.8.0+: tools-by-default (inactive)
mcp = FastMCP.from_fastapi(app=app, name="ProductMCP")


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=3000, path="/mcp/")
