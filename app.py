# Currency converter with real-time rates using Streamlit

import streamlit as st
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

# Initialize the currency rate and code converters
cr = CurrencyRates()
cc = CurrencyCodes()
btc_converter = BtcConverter()

# Streamlit App Layout
st.title("💰 Currency Converter 💱")
st.write("Convert between different currencies in real-time")

# List of available currencies
currencies = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'JPY', 'CNY', 'BTC']

# Input fields for selecting base currency and target currency
from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)

# Input field for the amount to convert
amount = st.number_input(f"Enter amount in {from_currency}:", min_value=0.0, value=1.0, format="%.2f")

# Function to perform conversion
def convert_currency(from_curr, to_curr, amt):
    if from_curr == "BTC":
        result = btc_converter.convert_btc_to_cur(amt, to_curr)
    elif to_curr == "BTC":
        result = btc_converter.convert_to_btc(amt, from_curr)
    else:
        result = cr.convert(from_curr, to_curr, amt)
    return result

# Display conversion when 'Convert' button is clicked
if st.button("Convert"):
    try:
        converted_amount = convert_currency(from_currency, to_currency, amount)
        symbol = cc.get_symbol(to_currency) or ""
        st.success(f"💵 {amount} {from_currency} = {symbol}{converted_amount:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Extra info - currency symbols
st.write("### Currency Symbols:")
for currency in currencies:
    st.write(f"{currency}: {cc.get_symbol(currency)}")

# Footer
st.write("Powered by Forex-Python & Streamlit | Exchange rates provided by public APIs")
