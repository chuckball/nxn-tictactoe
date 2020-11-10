import colorama

# colorama fixes color in Windows Powershell
colorama.init()
def color_symbol(symbol: str) -> str:
    if symbol.lower() == 'x':
        return Colors.CYAN + "  " + symbol + "  " + Colors.RESET
    elif symbol.lower() == 'o':
        return Colors.RED + "  " + symbol + "  " + Colors.RESET
    else:
        return symbol


class Colors:
    RED = '\033[31m'
    CYAN = '\033[36m'
    RESET = '\033[0m'
