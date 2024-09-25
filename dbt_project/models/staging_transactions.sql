-- models/staging_transactions.sql

WITH raw_transactions AS (
    SELECT
        transaction_id,
        user_id,
        amount,
        transaction_time
    FROM {{ source('raw', 'transactions') }}  -- Ensure that this source matches the definition in your sources.yml
)

SELECT
    transaction_id,
    user_id,
    amount,
    transaction_time
FROM raw_transactions