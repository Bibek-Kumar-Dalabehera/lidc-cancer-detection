"""Web routes for frontend pages."""
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="",
    tags=["web"]
)

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

def _read_template(file_name: str, fallback: str) -> str:
    """Read an HTML template using UTF-8 on all platforms."""
    template_path = TEMPLATE_DIR / file_name
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    return fallback


@router.get("/", response_class=HTMLResponse)
@router.get("/home", response_class=HTMLResponse)
async def home():
    """Home page."""
    return _read_template("home.html", "<h1>Home Page</h1>")

@router.get("/login", response_class=HTMLResponse)
async def login_page():
    """Login page."""
    return _read_template("login.html", "<h1>Login Page</h1>")

@router.get("/signup", response_class=HTMLResponse)
async def signup_page():
    """Signup page."""
    return _read_template("signup.html", "<h1>Signup Page</h1>")

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    """Dashboard page (after login)."""
    return _read_template("dashboard.html", "<h1>Dashboard Page</h1>")
