
-- ============================================================
-- E-COMMERCE ANALYTICS SYSTEM
-- SQL ANALYTICS
-- JOINs & AGGREGATIONS
-- Database: SQLite
-- ============================================================


-- ============================================================
-- QUERY 1
-- OVERALL BUSINESS SUMMARY
-- ============================================================

SELECT

    COUNT(DISTINCT o.order_id) AS total_orders,

    COUNT(DISTINCT o.customer_id) AS total_customers,

    SUM(
        oi.quantity
    ) AS total_units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS total_revenue

FROM orders o

JOIN order_items oi
    ON o.order_id = oi.order_id;


-- ============================================================
-- QUERY 2
-- TOTAL REVENUE PER CUSTOMER
-- ============================================================

SELECT

    c.customer_id,

    c.customer_name,

    c.customer_type,

    COUNT(DISTINCT o.order_id) AS total_orders,

    SUM(oi.quantity) AS total_units,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS total_revenue

FROM customers c

JOIN orders o
    ON c.customer_id = o.customer_id

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    c.customer_id,
    c.customer_name,
    c.customer_type

ORDER BY

    total_revenue DESC;


-- ============================================================
-- QUERY 3
-- REVENUE PER PRODUCT CATEGORY
-- ============================================================

SELECT

    p.category,

    COUNT(DISTINCT p.product_id) AS total_products,

    SUM(oi.quantity) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM products p

JOIN order_items oi
    ON p.product_id = oi.product_id

JOIN orders o
    ON oi.order_id = o.order_id

GROUP BY

    p.category

ORDER BY

    revenue DESC;


-- ============================================================
-- QUERY 4
-- REVENUE PER SUBCATEGORY
-- ============================================================

SELECT

    p.category,

    p.subcategory,

    SUM(oi.quantity) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM products p

JOIN order_items oi
    ON p.product_id = oi.product_id

GROUP BY

    p.category,
    p.subcategory

ORDER BY

    revenue DESC;


-- ============================================================
-- QUERY 5
-- MONTHLY REVENUE
-- ============================================================

SELECT

    strftime(
        '%Y-%m',
        o.order_date
    ) AS month,

    COUNT(
        DISTINCT o.order_id
    ) AS total_orders,

    SUM(
        oi.quantity
    ) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM orders o

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    strftime(
        '%Y-%m',
        o.order_date
    )

ORDER BY

    month;


-- ============================================================
-- QUERY 6
-- TOP PRODUCTS BY QUANTITY SOLD
-- ============================================================

SELECT

    p.product_id,

    p.product_name,

    p.category,

    SUM(
        oi.quantity
    ) AS quantity_sold

FROM products p

JOIN order_items oi
    ON p.product_id = oi.product_id

GROUP BY

    p.product_id,
    p.product_name,
    p.category

ORDER BY

    quantity_sold DESC

LIMIT 10;


-- ============================================================
-- QUERY 7
-- TOP PRODUCTS BY REVENUE
-- ============================================================

SELECT

    p.product_id,

    p.product_name,

    p.category,

    SUM(
        oi.quantity
    ) AS quantity_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM products p

JOIN order_items oi
    ON p.product_id = oi.product_id

GROUP BY

    p.product_id,
    p.product_name,
    p.category

ORDER BY

    revenue DESC

LIMIT 10;


-- ============================================================
-- QUERY 8
-- AVERAGE ORDER VALUE
-- ============================================================

SELECT

    ROUND(
        AVG(order_total),
        2
    ) AS average_order_value

FROM (

    SELECT

        o.order_id,

        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ) AS order_total

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    GROUP BY

        o.order_id

);


-- ============================================================
-- QUERY 9
-- AOV BY CUSTOMER SEGMENT
-- ============================================================

SELECT

    c.customer_type,

    COUNT(
        DISTINCT o.order_id
    ) AS total_orders,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        )
        /
        COUNT(
            DISTINCT o.order_id
        ),
        2
    ) AS average_order_value

FROM customers c

JOIN orders o
    ON c.customer_id = o.customer_id

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    c.customer_type

ORDER BY

    average_order_value DESC;


-- ============================================================
-- QUERY 10
-- CUSTOMER ORDER STATISTICS
-- ============================================================

SELECT

    c.customer_id,

    c.customer_name,

    COUNT(
        DISTINCT o.order_id
    ) AS order_count,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS total_spend,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        )
        /
        COUNT(
            DISTINCT o.order_id
        ),
        2
    ) AS customer_aov

FROM customers c

JOIN orders o
    ON c.customer_id = o.customer_id

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    c.customer_id,
    c.customer_name

ORDER BY

    total_spend DESC;


-- ============================================================
-- QUERY 11
-- REVENUE BY REGION
-- ============================================================

SELECT

    o.region_code,

    COUNT(
        DISTINCT o.order_id
    ) AS total_orders,

    COUNT(
        DISTINCT o.customer_id
    ) AS unique_customers,

    SUM(
        oi.quantity
    ) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM orders o

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    o.region_code

ORDER BY

    revenue DESC;


-- ============================================================
-- QUERY 12
-- ORDER STATUS ANALYSIS
-- ============================================================

SELECT

    o.status,

    COUNT(
        DISTINCT o.order_id
    ) AS order_count,

    COUNT(
        DISTINCT o.customer_id
    ) AS unique_customers,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM orders o

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    o.status

ORDER BY

    order_count DESC;


-- ============================================================
-- QUERY 13
-- PRODUCT PERFORMANCE
-- ============================================================

SELECT

    p.product_id,

    p.product_name,

    p.category,

    p.cost_price,

    SUM(
        oi.quantity
    ) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue,

    ROUND(
        SUM(
            oi.quantity
            * (
                oi.unit_price
                * (1 - oi.discount_percent / 100.0)
                - p.cost_price
            )
        ),
        2
    ) AS estimated_profit

FROM products p

JOIN order_items oi
    ON p.product_id = oi.product_id

GROUP BY

    p.product_id,
    p.product_name,
    p.category,
    p.cost_price

ORDER BY

    estimated_profit DESC;


-- ============================================================
-- QUERY 14
-- CUSTOMER SEGMENT REVENUE
-- ============================================================

SELECT

    c.customer_type,

    COUNT(
        DISTINCT c.customer_id
    ) AS customers,

    COUNT(
        DISTINCT o.order_id
    ) AS orders,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

LEFT JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    c.customer_type

ORDER BY

    revenue DESC;


-- ============================================================
-- QUERY 15
-- DAILY REVENUE
-- ============================================================

SELECT

    date(
        o.order_date
    ) AS order_day,

    COUNT(
        DISTINCT o.order_id
    ) AS orders,

    SUM(
        oi.quantity
    ) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM orders o

JOIN order_items oi
    ON o.order_id = oi.order_id

GROUP BY

    date(
        o.order_date
    )

ORDER BY

    order_day;


-- ============================================================
-- QUERY 16
-- DISCOUNT ANALYSIS
-- ============================================================

SELECT

    CASE

        WHEN oi.discount_percent = 0
            THEN 'No Discount'

        WHEN oi.discount_percent < 10
            THEN 'Low Discount'

        WHEN oi.discount_percent < 25
            THEN 'Medium Discount'

        ELSE 'High Discount'

    END AS discount_category,

    COUNT(*) AS order_items,

    SUM(
        oi.quantity
    ) AS units_sold,

    ROUND(
        SUM(
            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS revenue

FROM order_items oi

GROUP BY

    discount_category

ORDER BY

    revenue DESC;


-- ============================================================
-- END 
-- ============================================================

