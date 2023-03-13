import pandas as pd
import plotly.express as px
from dagster_dbt import load_assets_from_dbt_project

from dagster import AssetIn, MetadataValue, asset, file_relative_path

DBT_PROJECT_PATH = file_relative_path(__file__, "../../jaffle_shop")
DBT_PROFILES = file_relative_path(__file__, "../../jaffle_shop/config")


@asset(key_prefix=["jaffle_shop"], group_name="staging")
def customers_raw() -> pd.DataFrame:
    data = pd.read_csv("https://docs.dagster.io/assets/customers.csv")
    return data

@asset(key_prefix=["jaffle_shop"], group_name="staging")
def orders_raw() -> pd.DataFrame:
    data = pd.read_csv("https://docs.dagster.io/assets/orders.csv")
    return data

    
dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["jaffle_shop"]
)

@asset(
    ins={"customers": AssetIn(key_prefix=["jaffle_shop"])},
    group_name="staging",
)
def order_count_chart(context, customers: pd.DataFrame) -> None:
    fig = px.histogram(customers, x="number_of_orders")
    fig.update_layout(bargap=0.2)
    save_chart_path = file_relative_path(__file__, "order_count_chart.html")
    fig.write_html(save_chart_path, auto_open=True)

    context.add_output_metadata({"plot_url": MetadataValue.url("file://" + save_chart_path)})