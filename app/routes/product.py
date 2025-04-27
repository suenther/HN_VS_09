from fastapi import Request, FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.product_service import get_products, add_product, delete_product, update_product, get_product
from app.models.product import ProductCreate, Product, ProductUpdate

router = APIRouter()
templates = Jinja2Templates(directory="app/views/templates")

@router.get("/view", response_class=HTMLResponse)
async def view_products(request: Request):
    products = await get_products()
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

@router.get("/form", response_class=HTMLResponse)
async def show_products_form(request: Request):
    products = await get_products()
    return templates.TemplateResponse("product_form.html", {"request": request, "products": products})

@router.post("/", response_model=Product)
async def handle_add_product(product: ProductCreate):
   return await add_product(product)

@router.get("/", response_model=list[Product])
async def handle_get_products():
   return await get_products()

@router.delete("/{id}")
async def handle_delete_product(id: str):
    return await delete_product(id)

@router.put("/{id}", response_model=Product)
async def handle_update_product(id: str, product: ProductUpdate):
    return await update_product(id, product)


@router.get("/edit/{id}")
async def edit_product(request: Request, id: str):
    product = await get_product(id)
    return templates.TemplateResponse("product_edit.html", {
        "request": request, "product": product
    })