# /tutorial_template/jaffle_shop/models/staging/stg_customers.sql

select
    id as customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop', 'customers_raw') }}
