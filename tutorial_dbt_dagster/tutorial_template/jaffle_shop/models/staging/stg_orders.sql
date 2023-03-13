# /tutorial_template/jaffle_shop/models/staging/stg_orders.sql

select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from {{ source('jaffle_shop', 'orders_raw') }}
