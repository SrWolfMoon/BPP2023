import quandl
import dash
import dash_html_components as html
import plotly.express as px
import dash_core_components as dc


# 5nNxhxXVCTFy5px9us5A
quandl.ApiConfig.api_key = "5nNxhxXVCTFy5px9us5A"

dataGas = quandl.get("EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_NG_NA_SATL_Y13DLRPMCF_A", start_date="2018-01-01", end_date="2020-01-01")
dataElectricity = quandl.get("EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_ELC_NA_WENWPP_Y13CNTPKWH_A", ststart_date="2018-01-01", end_date="2020-01-01")
dataCoal = quandl.get("EIA/COAL_MARKET_SALES_MD_OPM_A", start_date="2018-01-01", end_date="2020-01-01")
dataPetroleum = quandl.get("EIA/PET_ESM_EPDXL0_SAE_R1Y_MBBL_A", start_date="2018-01-01", end_date="2020-01-01")
#mydata = quandl.get("FRED/GDP")

#print(data.head())


app = dash.Dash()

figure = px.line(dataGas, title="Natural Gas Delivered ; Commercial ; South Atlantic")
figureElec = px.line(dataElectricity, title="Electricity Delivered ; Commercial ; South Atlantic")
figureCoal = px.line(dataCoal, title="Coal Delivered ; Commercial ; South Atlantic")
figurePetroleum = px.line(dataPetroleum, title="Petroleum Delivered ; Commercial ; South Atlantic")


app.layout = html.Div(children=[
    html.H1("Pedidos de energia en Atlanta entre 2018 y 2020"),
    html.H2(children="Gas"),
    dc.Graph(figure=figure),
    html.H2(children="Electricity"),
    dc.Graph(figure=figureElec),
    html.H2(children="Coal"),
    dc.Graph(figure=figureCoal),
    html.H2(children="Petroleum"),
    dc.Graph(figure=figurePetroleum)
])


if __name__ == "__main__":
    app.run_server(debug=True)