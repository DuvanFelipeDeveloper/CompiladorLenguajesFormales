my %exchange_rates = (
    'USD' => {
        'JPY' => 110.65,
        'BGN' => 1.71,
        'CZK' => 22.26,
        'DKK' => 6.20,
        'GBP' => 0.72,
        'HUF' => 278.58,
        'PLN' => 3.96,
        'RON' => 4.08
    },
    'JPY' => {
        'USD' => 0.0090,
        'BGN' => 0.015,
        'CZK' => 0.19,
        'DKK' => 0.052,
        'GBP' => 0.006,
        'HUF' => 2.31,
        'PLN' => 0.033,
        'RON' => 0.034
    },
    'BGN' => {
        'USD' => 0.59,
        'JPY' => 68.17,
        'CZK' => 1.29,
        'DKK' => 3.60,
        'GBP' => 0.42,
        'HUF' => 159.90,
        'PLN' => 2.27,
        'RON' => 2.34
    },
    'CZK' => {
        'USD' => 0.045,
        'JPY' => 5.23,
        'BGN' => 0.78,
        'DKK' => 0.28,
        'GBP' => 0.032,
        'HUF' => 12.31,
        'PLN' => 0.18,
        'RON' => 0.18
    },
    'DKK' => {
        'USD' => 0.16,
        'JPY' => 18.97,
        'BGN' => 0.28,
        'CZK' => 3.57,
        'GBP' => 0.11,
        'HUF' => 42.57,
        'PLN' => 0.61,
        'RON' => 0.63
    },
    'GBP' => {
        'USD' => 1.39,
        'JPY' => 161.94,
        'BGN' => 2.38,
        'CZK' => 30.62,
        'DKK' => 8.81,
        'HUF' => 385.31,
        'PLN' => 5.48,
        'RON' => 5.66
    },
    'HUF' => {
        'USD' => 0.0036,
        'JPY' => 0.43,
        'BGN' => 0.0063,
        'CZK' => 0.081,
        'DKK' => 0.023,
        'GBP' => 0.0026,
        'PLN' => 0.014,
        'RON' => 0.014
    },
    'PLN' => {
        'USD' => 0.25,
        'JPY' => 28.97,
        'BGN' => 0.43,
        'CZK' => 5.59,
        'DKK' => 1.55,
        'GBP' => 0.18,
        'HUF' => 71.53,
        'RON' => 1.03
    },
    'RON' => {
        'USD' => 0.24,
        'JPY' => 27.66,
        'BGN' => 0.41,
        'CZK' => 5.33,
        'DKK' => 1.48,
        'GBP' => 0.17,
        'HUF' => 67.95,
        'PLN' => 0.97
    }
);

my $from_currency = 'USD';
my $to_currency = 'JPY';
my $amount = 100;

if (exists $exchange_rates{$from_currency} && exists $exchange_rates{$from_currency}{$to_currency}) {
    my $converted_amount = $amount * $exchange_rates{$from_currency}{$to_currency};
    print "$converted_amount";
} else {
    print "No se encontró la tasa de cambio de $from_currency a $to_currency"
}