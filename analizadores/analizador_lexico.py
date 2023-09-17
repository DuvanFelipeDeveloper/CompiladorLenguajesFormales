import ahocorasick

def build_automata():
    A = ahocorasick.Automaton()
    keywords = {
        "ruby": ["def ", "puts ", "end ","print "],
        "julia": ["function", "println"],
        "perl": ["sub ", "print "]
    }

    for lang, words in keywords.items():
        for word in words:
            A.add_word(word, (lang, word))
    A.make_automaton()
    return A

def detect_language(code):
    automata = build_automata()
    results = []
   
    for _, (lang, word) in automata.iter(code):
        results.append(lang)
    return results



#ruby julia perl 

examples = [
    '''
    require 'money'
require 'money/bank/currencylayer_bank'

# Configurar el conversor de divisas con la API de currencylayer (requiere una clave API válida)
Money::Rails.configure do |config|
  config.default_bank = Money::Bank::Currencylayer.new
  config.default_currency = 'USD'
  config.locale_backend = :i18n
end

# Mostrar las monedas disponibles para conversión
currencies = Money::Currency.table.keys
puts "Monedas disponibles para conversión:"
currencies.each { |currency| puts currency }

# Solicitar al usuario ingresar la moneda de origen y destino
print "Ingresa la moneda de origen (ejemplo: USD): "
from_currency = gets.chomp.upcase

print "Ingresa la moneda de destino (ejemplo: EUR): "
to_currency = gets.chomp.upcase

# Verificar si las monedas ingresadas son válidas
if currencies.include?(from_currency) && currencies.include?(to_currency)
  print "Ingresa la cantidad en #{from_currency}: "
  amount = gets.chomp.to_f

  # Realizar la conversión de divisas
  money = Money.new(amount * 100, from_currency)
  converted_money = money.exchange_to(to_currency)
  converted_amount = converted_money.to_f / 100

  puts "#{amount} #{from_currency} es igual a #{converted_amount} #{to_currency}"
else
  puts "Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos."
end
    ''',
    '''
    using Money
using Money.CurrencyLayer

# Configurar el conversor de divisas con la API de CurrencyLayer (requiere una clave API válida)
Money.Rails.configure do config
    config.default_bank = Money.Bank.CurrencyLayer()
    config.default_currency = "USD"
    config.locale_backend = :i18n
end

# Mostrar las monedas disponibles para conversión
currencies = keys(Money.Currency.table)
println("Monedas disponibles para conversión:")
for currency in currencies
    println(currency)
end

# Solicitar al usuario ingresar la moneda de origen y destino
println("Ingresa la moneda de origen (ejemplo: USD): ")
from_currency = uppercase(strip(readline()))

println("Ingresa la moneda de destino (ejemplo: EUR): ")
to_currency = uppercase(strip(readline()))

# Verificar si las monedas ingresadas son válidas
if from_currency in keys(Money.Currency.table) && to_currency in keys(Money.Currency.table)
    println("Ingresa la cantidad en $from_currency: ")
    amount = parse(Float64, strip(readline()))

    # Realizar la conversión de divisas
    money = Money(amount * 100, from_currency)
    converted_money = exchange_to(money, to_currency)
    converted_amount = to_float(converted_money) / 100

    println("$amount $from_currency es igual a $converted_amount $to_currency")
else
    println("Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos.")
end

    ''',
    '''
    use Money;
use Money::Bank::CurrencyLayer;

# Configurar el conversor de divisas con la API de CurrencyLayer (requiere una clave API válida)
Money::Rails->configure(
    default_bank => Money::Bank::CurrencyLayer->new,
    default_currency => 'USD',
    locale_backend => 'i18n'
);

# Mostrar las monedas disponibles para conversión
my %currencies = %{Money::Currency->table};
print "Monedas disponibles para conversión:\n";
foreach my $currency (keys %currencies) {
    print "$currency\n";
}

# Solicitar al usuario ingresar la moneda de origen y destino
print "Ingresa la moneda de origen (ejemplo: USD): ";
my $from_currency = uc(<STDIN>);
chomp($from_currency);

print "Ingresa la moneda de destino (ejemplo: EUR): ";
my $to_currency = uc(<STDIN>);
chomp($to_currency);

# Verificar si las monedas ingresadas son válidas
if (exists $currencies{$from_currency} && exists $currencies{$to_currency}) {
    print "Ingresa la cantidad en $from_currency: ";
    my $amount = <STDIN>;
    chomp($amount);

    # Realizar la conversión de divisas
    my $money = Money->new($amount * 100, $from_currency);
    my $converted_money = $money->exchange_to($to_currency);
    my $converted_amount = $converted_money->to_f / 100;

    print "$amount $from_currency es igual a $converted_amount $to_currency\n";
} else {
    print "Moneda de origen o destino no válida. Asegúrate de usar códigos de moneda válidos.\n";
}

    ''',
    '''
    Text
    ''',

]

# for idx, example in enumerate(examples):

    
#     if detected_languages:
#         print(f" {idx + 1}: es {detected_languages}")
#     else:
#         print(f" {idx + 1}: no detectado")

