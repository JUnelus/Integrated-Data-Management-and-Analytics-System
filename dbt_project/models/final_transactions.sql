-- models/final_transactions.sql

SELECT
    transaction_id,
    user_id,
    amount,
    transaction_time,
    CASE
        WHEN amount > 500 THEN 'High'
        ELSE 'Normal'
    END AS transaction_category
FROM "MY_DB"."PUBLIC"."STAGING_TRANSACTIONS"
