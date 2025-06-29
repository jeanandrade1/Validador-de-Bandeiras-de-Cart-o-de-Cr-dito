import re

def get_credit_card_company(card_number: str) -> str:
    # Remove qualquer caractere que não seja número
    card_number = re.sub(r"\D", "", card_number)

    # Padrões das principais bandeiras
    card_patterns = {
        "Visa": r"^4\d{12}(\d{3})?$",
        "MasterCard": r"^(5[1-5]\d{14}|2[2-7]\d{14})$",
        "American Express": r"^3[47]\d{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68]\d)\d{11}$",
        "Discover": r"^6(?:011|5\d{2}|4[4-9]\d)\d{12}$",
        "EnRoute": r"^(2014|2149)\d{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699\d{12}$",
        "HiperCard": r"^(606282\d{10}(\d{3})?|3841\d{15})$",
        "Aura": r"^50\d{14,17}$"
    }

    # Verifica com cada padrão
    for company, pattern in card_patterns.items():
        if re.fullmatch(pattern, card_number):
            return company

    return "Unknown or Invalid"

if __name__ == "__main__":
    card_input = input("Digite o número do cartão de crédito: ")
    company = get_credit_card_company(card_input)
    print(f"Bandeira identificada: {company}")