# Culinara 🍳

A command-line kitchen management tool for tracking pantry inventory, browsing recipes, and planning meals based on what you actually have in stock.

## 🚀 Usage

Culinara runs in two modes:

**Plan Mode** — single command execution via CLI arguments:
```bash
python main.py plan recipe list
python main.py plan recipe view "pasta"
python main.py plan recipe gap "pasta"
python main.py plan recipe cook "pasta"
python main.py plan pantry add flour 500
```

**Manage Mode** — interactive REPL for running multiple commands in a session:
```bash
python main.py manage
> recipe list
> pantry add butter 200
> plan
> exit
```

## 📋 Commands

### Recipe Commands
| Command | Description |
|---------|-------------|
| `recipe list` | List all available recipes |
| `recipe view <name>` | View a recipe's ingredients and quantities |
| `recipe gap <name>` | Show missing ingredients for a recipe (gap analysis) |
| `recipe cook <name>` | Cook a recipe — checks availability and deducts ingredients from pantry |

### Pantry Commands
| Command | Description |
|---------|-------------|
| `pantry add <item> <qty>` | Add an ingredient to the pantry |
| `pantry use <item> <qty>` | Use an ingredient from the pantry |
| `pantry process <file>` | Batch process pantry operations from a text file |

### Planning
| Command | Description |
|---------|-------------|
| `plan` | Show all recipes that are cookable with current pantry stock |

## 🏗️ Project Structure

```
main.py                    → Entry point, CLI argument parsing
culinara/
├── culinara_manager.py    → Core controller: routes commands to recipe/pantry modules
├── recipie.py             → Recipe loading, viewing, and lookup from JSON
├── pantry.py              → Inventory management, gap analysis, batch processing
config.json                → Externalized file paths for recipes, pantry, and reports
data/
├── recipes.json           → Recipe definitions with ingredients and quantities
├── pantry.json            → Current pantry inventory state
└── shopping_list.txt      → Shopping list output
reports/                   → Auto-generated action logs
```

## 🛠️ Tech

- **Language:** Python 3
- **Dependencies:** None (standard library only)
- **Persistence:** JSON files for pantry state and recipe data