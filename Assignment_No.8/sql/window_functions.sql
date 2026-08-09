
-- ============================================================
-- E-COMMERCE ANALYTICS SYSTEM
-- WINDOW FUNCTIONS & COMMON TABLE EXPRESSIONS
-- ============================================================


-- ============================================================
-- QUERY 1
-- CUSTOMER LIFETIME VALUE
-- ============================================================

WITH customer_revenue AS (

    SELECT

        c.customer_id,

        c.customer_name,

        c.customer_type,

        COUNT(
            DISTINCT o.order_id
        ) AS total_orders,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS lifetime_value

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        c.customer_id,
        c.customer_name,
        c.customer_type
)

SELECT

    customer_id,

    customer_name,

    customer_type,

    total_orders,

    ROUND(
        lifetime_value,
        2
    ) AS lifetime_value,

    RANK() OVER (
        ORDER BY lifetime_value DESC
    ) AS lifetime_rank

FROM customer_revenue

ORDER BY lifetime_rank;


-- ============================================================
-- QUERY 2
-- DENSE RANK BY CUSTOMER SPENDING
-- ============================================================

WITH customer_revenue AS (

    SELECT

        c.customer_id,

        c.customer_name,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS total_spend

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        c.customer_id,
        c.customer_name
)

SELECT

    customer_id,

    customer_name,

    ROUND(
        total_spend,
        2
    ) AS total_spend,

    DENSE_RANK() OVER (
        ORDER BY total_spend DESC
    ) AS spend_rank

FROM customer_revenue

ORDER BY spend_rank;


-- ============================================================
-- QUERY 3
-- ROW NUMBER FOR CUSTOMERS
-- ============================================================

WITH customer_revenue AS (

    SELECT

        c.customer_id,

        c.customer_name,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS total_spend

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        c.customer_id,
        c.customer_name
)

SELECT

    customer_id,

    customer_name,

    ROUND(
        total_spend,
        2
    ) AS total_spend,

    ROW_NUMBER() OVER (
        ORDER BY total_spend DESC
    ) AS customer_number

FROM customer_revenue

ORDER BY customer_number;


-- ============================================================
-- QUERY 4
-- MONTHLY REVENUE
-- ============================================================

WITH monthly_revenue AS (

    SELECT

        strftime(
            '%Y-%m',
            o.order_date
        ) AS month,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        strftime(
            '%Y-%m',
            o.order_date
        )
)

SELECT

    month,

    ROUND(
        revenue,
        2
    ) AS monthly_revenue

FROM monthly_revenue

ORDER BY month;


-- ============================================================
-- QUERY 5
-- RUNNING REVENUE TOTAL
-- ============================================================

WITH monthly_revenue AS (

    SELECT

        strftime(
            '%Y-%m',
            o.order_date
        ) AS month,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        strftime(
            '%Y-%m',
            o.order_date
        )
)

SELECT

    month,

    ROUND(
        revenue,
        2
    ) AS monthly_revenue,

    ROUND(
        SUM(revenue) OVER (
            ORDER BY month
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS running_revenue

FROM monthly_revenue

ORDER BY month;


-- ============================================================
-- QUERY 6
-- THREE-MONTH MOVING AVERAGE
-- ============================================================

WITH monthly_revenue AS (

    SELECT

        strftime(
            '%Y-%m',
            o.order_date
        ) AS month,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        strftime(
            '%Y-%m',
            o.order_date
        )
)

SELECT

    month,

    ROUND(
        revenue,
        2
    ) AS monthly_revenue,

    ROUND(
        AVG(revenue) OVER (
            ORDER BY month
            ROWS BETWEEN 2 PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS three_month_moving_average

FROM monthly_revenue

ORDER BY month;


-- ============================================================
-- QUERY 7
-- PREVIOUS MONTH REVENUE USING LAG
-- ============================================================

WITH monthly_revenue AS (

    SELECT

        strftime(
            '%Y-%m',
            o.order_date
        ) AS month,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        strftime(
            '%Y-%m',
            o.order_date
        )
)

SELECT

    month,

    ROUND(
        revenue,
        2
    ) AS current_revenue,

    ROUND(
        LAG(revenue) OVER (
            ORDER BY month
        ),
        2
    ) AS previous_month_revenue

FROM monthly_revenue

ORDER BY month;


-- ============================================================
-- QUERY 8
-- MONTH-OVER-MONTH REVENUE GROWTH
-- ============================================================

WITH monthly_revenue AS (

    SELECT

        strftime(
            '%Y-%m',
            o.order_date
        ) AS month,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        strftime(
            '%Y-%m',
            o.order_date
        )
),

revenue_with_previous AS (

    SELECT

        month,

        revenue,

        LAG(revenue) OVER (
            ORDER BY month
        ) AS previous_revenue

    FROM monthly_revenue
)

SELECT

    month,

    ROUND(
        revenue,
        2
    ) AS current_revenue,

    ROUND(
        previous_revenue,
        2
    ) AS previous_revenue,

    CASE

        WHEN previous_revenue IS NULL
            THEN NULL

        WHEN previous_revenue = 0
            THEN NULL

        ELSE ROUND(
            (
                (revenue - previous_revenue)
                / previous_revenue
            ) * 100,
            2
        )

    END AS growth_percentage

FROM revenue_with_previous

ORDER BY month;


-- ============================================================
-- QUERY 9
-- CUSTOMER SPENDING WITH RUNNING TOTAL
-- ============================================================

WITH customer_orders AS (

    SELECT

        c.customer_id,

        c.customer_name,

        date(o.order_date) AS order_date,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS order_value

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        c.customer_id,

        c.customer_name,

        o.order_id,

        date(o.order_date)
)

SELECT

    customer_id,

    customer_name,

    order_date,

    ROUND(
        order_value,
        2
    ) AS order_value,

    ROUND(
        SUM(order_value) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS customer_running_spend

FROM customer_orders

ORDER BY

    customer_id,

    order_date;


-- ============================================================
-- QUERY 10
-- RANK PRODUCTS WITHIN EACH CATEGORY
-- ============================================================

WITH product_sales AS (

    SELECT

        p.product_id,

        p.product_name,

        p.category,

        SUM(
            oi.quantity
        ) AS units_sold,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM products p

    JOIN order_items oi
        ON p.product_id = oi.product_id

    GROUP BY

        p.product_id,

        p.product_name,

        p.category
)

SELECT

    product_id,

    product_name,

    category,

    units_sold,

    ROUND(
        revenue,
        2
    ) AS revenue,

    RANK() OVER (
        PARTITION BY category
        ORDER BY revenue DESC
    ) AS category_rank

FROM product_sales

ORDER BY

    category,

    category_rank;


-- ============================================================
-- QUERY 11
-- TOP 3 PRODUCTS PER CATEGORY
-- ============================================================

WITH product_sales AS (

    SELECT

        p.product_id,

        p.product_name,

        p.category,

        SUM(
            oi.quantity
        ) AS units_sold,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM products p

    JOIN order_items oi
        ON p.product_id = oi.product_id

    GROUP BY

        p.product_id,

        p.product_name,

        p.category
),

ranked_products AS (

    SELECT

        *,

        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY revenue DESC
        ) AS product_rank

    FROM product_sales
)

SELECT

    product_id,

    product_name,

    category,

    units_sold,

    ROUND(
        revenue,
        2
    ) AS revenue,

    product_rank

FROM ranked_products

WHERE product_rank <= 3

ORDER BY

    category,

    product_rank;


-- ============================================================
-- QUERY 12
-- CUSTOMER ORDER SEQUENCE
-- ============================================================

WITH customer_orders AS (

    SELECT

        c.customer_id,

        c.customer_name,

        o.order_id,

        o.order_date,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS order_value

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        c.customer_id,

        c.customer_name,

        o.order_id,

        o.order_date
)

SELECT

    customer_id,

    customer_name,

    order_id,

    order_date,

    ROUND(
        order_value,
        2
    ) AS order_value,

    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS order_number

FROM customer_orders

ORDER BY

    customer_id,

    order_date;


-- ============================================================
-- END 
-- ============================================================
```
