# AGENTS.md

Flat, stdlib-only Python console app (pet shelter + pet-shop catalog). No packaging, deps, tests, lint, or CI.

## Run & verify

- Run: `python3 main.py` (interactive, requires keyboard input).
- Verify without running interactively: `python3 -m compileall .` (syntax only).
- Manual end-to-end testing only — there is no test suite.

## Structure

- `main.py` — entrypoint; builds `pets`/`products` from `moc.py` mock data, main loop.
- `main_menu.py`, `buyer_menu.py`, `administrator_menu.py` — console menus (buyer/admin flows).
- `pets_functions.py`, `products_functions.py` — CRUD + printing helpers per entity.
- `pet.py`, `product.py` — `@dataclass(slots=True)` models.
- `moc.py` — hardcoded seed data (`mock_pets`, `mock_products`).
- `console_helper.py` — reusable `input_x()` + `print_devider()`/`wait_enter()` helpers.

## Conventions & gotchas

- All user-facing strings are Russian (Cyrillic); keep new UI text in Russian.
- The codebase relies on wildcard imports (`from console_helper import *`) and has circular imports (`buyer_menu` → `main_menu` → `pets_functions`, `buyer_menu` → `match` → `moc`, `match` → `pets_functions` → `moc`). Preserve these patterns; adding an import in the wrong direction can create a new cycle at startup.
- IDs are NOT stored in mock data — `Pet.id`/`Product.id` default to `None`. New records get IDs via module-global counters `get_next_pet_id()` / `get_next_product_id()`.
- `list_color` (the color-name list) exists only in `main.py`; `print_single_pet`/`print_color` and `work_with_buyer_menu` require it as an argument. `main.py` currently calls these without it, so the app crashes at startup (`TypeError: print_single_pet() missing 1 required positional argument: 'list_color'`). Calling conventions across menus are otherwise inconsistent (e.g. `print_single_pet` calls with/without `list_color`, `get_product_by_id` used where `get_pet_by_id` was intended).
- The list of breeds (`BREEDS`, ~660 entries) and `get_breed_name(breed)` live in `moc.py`. `Pet.breed` is a **1-based code** into that list (`get_breed_name` does `BREEDS[breed - 1]`); mock pets' codes already point at their intended breed names. `pets_functions.py` pulls them in via `from moc import *`.
- `administrator_menu.py`: the "Управление аксессуарами" submenu reads `choosen_action` only once before its loop — the inner loop has no re-prompt, so items 1–6 never dispatch correctly.