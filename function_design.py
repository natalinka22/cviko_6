def analyze_password(
    password,
    min_length=8,
    require_digit=True,
    require_upper=True,
    require_symbol=False,
    banned_words=None,
):

    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    rules = []
    results = {}

    rules.append('min_length')
    results['min_length'] = len(password) >= min_length

    if require_digit:
        rules.append('digit')
        digit_found = False
        for char in password:
            if char.isdigit():
                digit_found = True
                break
        results['digit'] = digit_found

    if require_upper:
        rules.append('upper')
        upper_found = False
        for char in password:
            if char.isupper():
                upper_found = True
                break
        results['upper'] = upper_found

    symbols = "!@#$%^&*()-=+[]{};:,.?"
    if require_symbol:
        rules.append('symbol')
        symbol_found = False
        for char in password:
            if char in symbols:
                symbol_found = True
                break
        results['symbol'] = symbol_found

    rules.append('banned_word')
    lower_password = password.lower()
    banned_word_found = False
    for word in banned_words:
        if word.lower() in lower_password:
            banned_word_found = True
            break
    results['banned_word'] = not banned_word_found

    passed = 0
    for rule in rules:
        if results[rule]:
            passed += 1
    total = len(rules)

    is_strong = passed == total
    score_percent = int((passed / total) * 100)
    missing_rules = []
    for rule in rules:
        if not results[rule]:
            missing_rules.append(rule)

    return is_strong, score_percent, missing_rules

print(analyze_password("Test1234"))
print("Čisto pozičné volanie je krátke, ale menej čitateľné, pretože nie je jasné, čo jednotlivé parametre znamenajú.")

print(analyze_password("Test1234", 10, require_symbol=True))
print("Mix zlepšuje čitateľnosť - dôležité parametre sú pomenované, ale stále zostáva stručné.")

print(analyze_password("Test1234", require_symbol=False))
print("Pomenovaný argument jasne ukazuje, že pravidlo pre symbol je vypnuté.")

print(analyze_password("Admin123!", banned_words=["admin", "root"]))
print("Použitie vlastného zoznamu je prehľadné vďaka pomenovanému argumentu, ale predlžuje volanie.")




















