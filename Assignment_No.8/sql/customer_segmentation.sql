
-- ============================================================
-- E-COMMERCE ANALYTICS SYSTEM
-- CUSTOMER SEGMENTATION & RFM ANALYSIS
-- ============================================================


-- ============================================================
-- QUERY 1
-- CUSTOMER PURCHASE FREQUENCY
--
-- Segments:
-- One-Time  = 1 order
-- Occasional = 2-5 orders
-- Loyal      = 6+ orders
-- ============================================================

WITH customer_orders AS (

    SELECT

        customer_id,

        COUNT(
            DISTINCT order_id
        ) AS total_orders

    FROM orders

    GROUP BY customer_id
)

SELECT

    customer_id,

    total_orders,

    CASE

        WHEN total_orders = 1
            THEN 'One-Time'

        WHEN total_orders BETWEEN 2 AND 5
            THEN 'Occasional'

        WHEN total_orders >= 6
            THEN 'Loyal'

    END AS purchase_frequency_segment

FROM customer_orders

ORDER BY total_orders DESC;


-- ============================================================
-- QUERY 2
-- PURCHASE FREQUENCY SEGMENT SUMMARY
-- ============================================================

WITH customer_orders AS (

    SELECT

        customer_id,

        COUNT(
            DISTINCT order_id
        ) AS total_orders

    FROM orders

    GROUP BY customer_id
),

customer_segments AS (

    SELECT

        customer_id,

        total_orders,

        CASE

            WHEN total_orders = 1
                THEN 'One-Time'

            WHEN total_orders BETWEEN 2 AND 5
                THEN 'Occasional'

            WHEN total_orders >= 6
                THEN 'Loyal'

        END AS purchase_frequency_segment

    FROM customer_orders
)

SELECT

    purchase_frequency_segment,

    COUNT(
        customer_id
    ) AS customer_count,

    ROUND(
        AVG(
            total_orders
        ),
        2
    ) AS average_orders

FROM customer_segments

GROUP BY purchase_frequency_segment

ORDER BY customer_count DESC;


-- ============================================================
-- QUERY 3
-- CUSTOMER TOTAL SPEND
-- ============================================================

WITH customer_spending AS (

    SELECT

        o.customer_id,

        SUM(
            oi.quantity * oi.unit_price
        ) AS total_spend

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
)

SELECT

    customer_id,

    ROUND(
        total_spend,
        2
    ) AS total_spend

FROM customer_spending

ORDER BY total_spend DESC;


-- ============================================================
-- QUERY 4
-- SPEND TIER SEGMENTATION
--
-- Low    = below 33rd percentile
-- Medium = 33rd to 66th percentile
-- High   = above 66th percentile
-- ============================================================

WITH customer_spending AS (

    SELECT

        o.customer_id,

        SUM(
            oi.quantity * oi.unit_price
        ) AS total_spend

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

spend_ranked AS (

    SELECT

        customer_id,

        total_spend,

        NTILE(3) OVER (
            ORDER BY total_spend
        ) AS spend_bucket

    FROM customer_spending
)

SELECT

    customer_id,

    ROUND(
        total_spend,
        2
    ) AS total_spend,

    CASE

        WHEN spend_bucket = 1
            THEN 'Low'

        WHEN spend_bucket = 2
            THEN 'Medium'

        WHEN spend_bucket = 3
            THEN 'High'

    END AS spend_tier

FROM spend_ranked

ORDER BY total_spend DESC;


-- ============================================================
-- QUERY 5
-- SPEND TIER SUMMARY
-- ============================================================

WITH customer_spending AS (

    SELECT

        o.customer_id,

        SUM(
            oi.quantity * oi.unit_price
        ) AS total_spend

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

spend_ranked AS (

    SELECT

        customer_id,

        total_spend,

        NTILE(3) OVER (
            ORDER BY total_spend
        ) AS spend_bucket

    FROM customer_spending
),

spend_segments AS (

    SELECT

        customer_id,

        total_spend,

        CASE

            WHEN spend_bucket = 1
                THEN 'Low'

            WHEN spend_bucket = 2
                THEN 'Medium'

            WHEN spend_bucket = 3
                THEN 'High'

        END AS spend_tier

    FROM spend_ranked
)

SELECT

    spend_tier,

    COUNT(
        customer_id
    ) AS customer_count,

    ROUND(
        AVG(total_spend),
        2
    ) AS average_spend,

    ROUND(
        SUM(total_spend),
        2
    ) AS total_segment_revenue

FROM spend_segments

GROUP BY spend_tier

ORDER BY

    CASE spend_tier

        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3

    END;


-- ============================================================
-- QUERY 6
-- RFM BASE METRICS
--
-- RECENCY:
-- Days since customer's latest purchase
--
-- FREQUENCY:
-- Number of orders
--
-- MONETARY:
-- Total amount spent
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

rfm_base AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
)

SELECT

    rb.customer_id,

    rb.last_purchase_date,

    CAST(

        julianday(
            dd.latest_date
        )
        -
        julianday(
            rb.last_purchase_date
        )

        AS INTEGER

    ) AS recency,

    rb.frequency,

    ROUND(
        rb.monetary,
        2
    ) AS monetary

FROM rfm_base rb

CROSS JOIN dataset_date dd

ORDER BY monetary DESC;


-- ============================================================
-- QUERY 7
-- RFM SCORES
--
-- Recency:
-- Lower recency is better
--
-- Frequency:
-- Higher frequency is better
--
-- Monetary:
-- Higher monetary value is better
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

rfm_base AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

rfm_metrics AS (

    SELECT

        rb.customer_id,

        CAST(

            julianday(
                dd.latest_date
            )
            -
            julianday(
                rb.last_purchase_date
            )

            AS INTEGER

        ) AS recency,

        rb.frequency,

        rb.monetary

    FROM rfm_base rb

    CROSS JOIN dataset_date dd
),

rfm_scores AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS recency_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS frequency_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS monetary_score

    FROM rfm_metrics
)

SELECT

    customer_id,

    recency,

    frequency,

    ROUND(
        monetary,
        2
    ) AS monetary,

    recency_score,

    frequency_score,

    monetary_score

FROM rfm_scores

ORDER BY

    monetary_score DESC,

    frequency_score DESC,

    recency_score DESC;


-- ============================================================
-- QUERY 8
-- RFM TOTAL SCORE
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

rfm_base AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

rfm_metrics AS (

    SELECT

        rb.customer_id,

        CAST(

            julianday(
                dd.latest_date
            )
            -
            julianday(
                rb.last_purchase_date
            )

            AS INTEGER

        ) AS recency,

        rb.frequency,

        rb.monetary

    FROM rfm_base rb

    CROSS JOIN dataset_date dd
),

rfm_scores AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS recency_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS frequency_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS monetary_score

    FROM rfm_metrics
)

SELECT

    customer_id,

    recency,

    frequency,

    ROUND(
        monetary,
        2
    ) AS monetary,

    recency_score,

    frequency_score,

    monetary_score,

    (
        recency_score
        +
        frequency_score
        +
        monetary_score
    ) AS rfm_total_score

FROM rfm_scores

ORDER BY rfm_total_score DESC;


-- ============================================================
-- QUERY 9
-- RFM CUSTOMER SEGMENTS
--
-- Champions:
-- High RFM score
--
-- Loyal Customers:
-- High frequency and good monetary value
--
-- Potential Loyalists:
-- Good recency and moderate frequency
--
-- At Risk:
-- Poor recency but historically valuable
--
-- Lost:
-- Very poor recency
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

rfm_base AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

rfm_metrics AS (

    SELECT

        rb.customer_id,

        CAST(

            julianday(
                dd.latest_date
            )
            -
            julianday(
                rb.last_purchase_date
            )

            AS INTEGER

        ) AS recency,

        rb.frequency,

        rb.monetary

    FROM rfm_base rb

    CROSS JOIN dataset_date dd
),

rfm_scores AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS r_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS f_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS m_score

    FROM rfm_metrics
),

rfm_final AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        r_score,

        f_score,

        m_score,

        (
            r_score
            +
            f_score
            +
            m_score
        ) AS rfm_score

    FROM rfm_scores
)

SELECT

    customer_id,

    recency,

    frequency,

    ROUND(
        monetary,
        2
    ) AS monetary,

    r_score,

    f_score,

    m_score,

    rfm_score,

    CASE

        WHEN
            r_score >= 4
            AND f_score >= 4
            AND m_score >= 4
        THEN 'Champions'

        WHEN
            f_score >= 4
            AND m_score >= 4
        THEN 'Loyal Customers'

        WHEN
            r_score >= 4
            AND f_score >= 3
        THEN 'Potential Loyalists'

        WHEN
            r_score <= 2
            AND m_score >= 4
        THEN 'At Risk'

        WHEN
            r_score <= 2
            AND f_score <= 2
        THEN 'Lost'

        ELSE 'Regular Customers'

    END AS customer_segment

FROM rfm_final

ORDER BY

    rfm_score DESC;


-- ============================================================
-- QUERY 10
-- RFM SEGMENT SUMMARY
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

rfm_base AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

rfm_metrics AS (

    SELECT

        rb.customer_id,

        CAST(

            julianday(
                dd.latest_date
            )
            -
            julianday(
                rb.last_purchase_date
            )

            AS INTEGER

        ) AS recency,

        rb.frequency,

        rb.monetary

    FROM rfm_base rb

    CROSS JOIN dataset_date dd
),

rfm_scores AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS r_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS f_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS m_score

    FROM rfm_metrics
),

rfm_segments AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        r_score,

        f_score,

        m_score,

        CASE

            WHEN
                r_score >= 4
                AND f_score >= 4
                AND m_score >= 4
            THEN 'Champions'

            WHEN
                f_score >= 4
                AND m_score >= 4
            THEN 'Loyal Customers'

            WHEN
                r_score >= 4
                AND f_score >= 3
            THEN 'Potential Loyalists'

            WHEN
                r_score <= 2
                AND m_score >= 4
            THEN 'At Risk'

            WHEN
                r_score <= 2
                AND f_score <= 2
            THEN 'Lost'

            ELSE 'Regular Customers'

        END AS customer_segment

    FROM rfm_scores
)

SELECT

    customer_segment,

    COUNT(
        customer_id
    ) AS customer_count,

    ROUND(
        AVG(recency),
        2
    ) AS average_recency,

    ROUND(
        AVG(frequency),
        2
    ) AS average_frequency,

    ROUND(
        AVG(monetary),
        2
    ) AS average_monetary,

    ROUND(
        SUM(monetary),
        2
    ) AS segment_revenue

FROM rfm_segments

GROUP BY customer_segment

ORDER BY segment_revenue DESC;


-- ============================================================
-- QUERY 11
-- COMBINED PURCHASE FREQUENCY + SPEND SEGMENT
-- ============================================================

WITH customer_metrics AS (

    SELECT

        o.customer_id,

        COUNT(
            DISTINCT o.order_id
        ) AS total_orders,

        SUM(
            oi.quantity * oi.unit_price
        ) AS total_spend

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

spend_ranked AS (

    SELECT

        customer_id,

        total_orders,

        total_spend,

        NTILE(3) OVER (
            ORDER BY total_spend
        ) AS spend_bucket

    FROM customer_metrics
)

SELECT

    customer_id,

    total_orders,

    ROUND(
        total_spend,
        2
    ) AS total_spend,

    CASE

        WHEN total_orders = 1
            THEN 'One-Time'

        WHEN total_orders BETWEEN 2 AND 5
            THEN 'Occasional'

        ELSE 'Loyal'

    END AS frequency_segment,

    CASE

        WHEN spend_bucket = 1
            THEN 'Low'

        WHEN spend_bucket = 2
            THEN 'Medium'

        ELSE 'High'

    END AS spend_segment

FROM spend_ranked

ORDER BY total_spend DESC;


-- ============================================================
-- QUERY 12
-- HIGH-VALUE CUSTOMERS
-- ============================================================

WITH customer_metrics AS (

    SELECT

        o.customer_id,

        COUNT(
            DISTINCT o.order_id
        ) AS total_orders,

        SUM(
            oi.quantity * oi.unit_price
        ) AS total_spend

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
)

SELECT

    customer_id,

    total_orders,

    ROUND(
        total_spend,
        2
    ) AS total_spend

FROM customer_metrics

WHERE

    total_orders >= 6

    AND total_spend >= 1000000

ORDER BY total_spend DESC;


-- ============================================================
-- QUERY 13
-- FINAL CUSTOMER SEGMENT REPORT
-- ============================================================

WITH dataset_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
),

customer_metrics AS (

    SELECT

        o.customer_id,

        MAX(
            date(o.order_date)
        ) AS last_purchase_date,

        COUNT(
            DISTINCT o.order_id
        ) AS frequency,

        SUM(
            oi.quantity * oi.unit_price
        ) AS monetary

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    GROUP BY o.customer_id
),

rfm_metrics AS (

    SELECT

        cm.customer_id,

        CAST(

            julianday(
                dd.latest_date
            )
            -
            julianday(
                cm.last_purchase_date
            )

            AS INTEGER

        ) AS recency,

        cm.frequency,

        cm.monetary

    FROM customer_metrics cm

    CROSS JOIN dataset_date dd
),

rfm_scores AS (

    SELECT

        customer_id,

        recency,

        frequency,

        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS r_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS f_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS m_score

    FROM rfm_metrics
)

SELECT

    customer_id,

    recency,

    frequency,

    ROUND(
        monetary,
        2
    ) AS monetary,

    r_score,

    f_score,

    m_score,

    (
        r_score
        +
        f_score
        +
        m_score
    ) AS rfm_score,

    CASE

        WHEN
            r_score >= 4
            AND f_score >= 4
            AND m_score >= 4
        THEN 'Champions'

        WHEN
            f_score >= 4
            AND m_score >= 4
        THEN 'Loyal Customers'

        WHEN
            r_score >= 4
            AND f_score >= 3
        THEN 'Potential Loyalists'

        WHEN
            r_score <= 2
            AND m_score >= 4
        THEN 'At Risk'

        WHEN
            r_score <= 2
            AND f_score <= 2
        THEN 'Lost'

        ELSE 'Regular Customers'

    END AS customer_segment

FROM rfm_scores

ORDER BY

    rfm_score DESC,

    monetary DESC;


-- ============================================================
-- END 
-- ============================================================

