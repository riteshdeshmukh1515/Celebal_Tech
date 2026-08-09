
-- ============================================================

-- COHORT & RETENTION ANALYSIS
-- ============================================================


-- ============================================================
-- QUERY 1
-- FIRST PURCHASE MONTH FOR EACH CUSTOMER
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

)

SELECT

    customer_id,

    first_purchase_date,

    strftime(
        '%Y-%m',
        first_purchase_date
    ) AS cohort_month

FROM customer_first_purchase

ORDER BY first_purchase_date;


-- ============================================================
-- QUERY 2
-- CUSTOMER COHORT SIZE
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
)

SELECT

    cohort_month,

    COUNT(
        customer_id
    ) AS cohort_customers

FROM customer_cohorts

GROUP BY cohort_month

ORDER BY cohort_month;


-- ============================================================
-- QUERY 3
-- CUSTOMER MONTHLY ACTIVITY
-- ============================================================

SELECT DISTINCT

    customer_id,

    strftime(
        '%Y-%m',
        order_date
    ) AS activity_month

FROM orders

ORDER BY

    customer_id,

    activity_month;


-- ============================================================
-- QUERY 4
-- COHORT + MONTHLY ACTIVITY
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
)

SELECT

    cc.customer_id,

    cc.cohort_month,

    ca.activity_month

FROM customer_cohorts cc

JOIN customer_activity ca

    ON cc.customer_id = ca.customer_id

ORDER BY

    cc.cohort_month,

    ca.activity_month,

    cc.customer_id;


-- ============================================================
-- QUERY 5
-- COHORT MONTH NUMBER
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
)

SELECT

    cc.customer_id,

    cc.cohort_month,

    ca.activity_month,

    (
        (
            CAST(
                strftime(
                    '%Y',
                    ca.activity_month || '-01'
                ) AS INTEGER
            )
            -
            CAST(
                strftime(
                    '%Y',
                    cc.cohort_month || '-01'
                ) AS INTEGER
            )
        ) * 12
        +
        (
            CAST(
                strftime(
                    '%m',
                    ca.activity_month || '-01'
                ) AS INTEGER
            )
            -
            CAST(
                strftime(
                    '%m',
                    cc.cohort_month || '-01'
                ) AS INTEGER
            )
        )
    ) AS cohort_month_number

FROM customer_cohorts cc

JOIN customer_activity ca

    ON cc.customer_id = ca.customer_id

ORDER BY

    cc.cohort_month,

    cohort_month_number,

    cc.customer_id;


-- ============================================================
-- QUERY 6
-- ACTIVE CUSTOMERS PER COHORT MONTH
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
),

cohort_activity AS (

    SELECT

        cc.cohort_month,

        ca.activity_month,

        COUNT(
            DISTINCT cc.customer_id
        ) AS active_customers

    FROM customer_cohorts cc

    JOIN customer_activity ca

        ON cc.customer_id = ca.customer_id

    GROUP BY

        cc.cohort_month,

        ca.activity_month
)

SELECT

    cohort_month,

    activity_month,

    active_customers

FROM cohort_activity

ORDER BY

    cohort_month,

    activity_month;


-- ============================================================
-- QUERY 7
-- COHORT RETENTION RATE
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
),

cohort_sizes AS (

    SELECT

        cohort_month,

        COUNT(
            customer_id
        ) AS cohort_size

    FROM customer_cohorts

    GROUP BY cohort_month
),

cohort_activity AS (

    SELECT

        cc.cohort_month,

        ca.activity_month,

        COUNT(
            DISTINCT cc.customer_id
        ) AS active_customers

    FROM customer_cohorts cc

    JOIN customer_activity ca

        ON cc.customer_id = ca.customer_id

    GROUP BY

        cc.cohort_month,

        ca.activity_month
)

SELECT

    ca.cohort_month,

    ca.activity_month,

    cs.cohort_size,

    ca.active_customers,

    ROUND(
        (
            CAST(
                ca.active_customers AS REAL
            )
            /
            cs.cohort_size
        ) * 100,
        2
    ) AS retention_rate_percentage

FROM cohort_activity ca

JOIN cohort_sizes cs

    ON ca.cohort_month = cs.cohort_month

ORDER BY

    ca.cohort_month,

    ca.activity_month;


-- ============================================================
-- QUERY 8
-- RETENTION BY COHORT MONTH NUMBER
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
),

cohort_activity AS (

    SELECT

        cc.cohort_month,

        ca.activity_month,

        (
            (
                CAST(
                    strftime(
                        '%Y',
                        ca.activity_month || '-01'
                    ) AS INTEGER
                )
                -
                CAST(
                    strftime(
                        '%Y',
                        cc.cohort_month || '-01'
                    ) AS INTEGER
                )
            ) * 12
            +
            (
                CAST(
                    strftime(
                        '%m',
                        ca.activity_month || '-01'
                    ) AS INTEGER
                )
                -
                CAST(
                    strftime(
                        '%m',
                        cc.cohort_month || '-01'
                    ) AS INTEGER
                )
            )
        ) AS cohort_month_number,

        COUNT(
            DISTINCT cc.customer_id
        ) AS active_customers

    FROM customer_cohorts cc

    JOIN customer_activity ca

        ON cc.customer_id = ca.customer_id

    GROUP BY

        cc.cohort_month,

        ca.activity_month

),

cohort_sizes AS (

    SELECT

        cohort_month,

        COUNT(
            customer_id
        ) AS cohort_size

    FROM customer_cohorts

    GROUP BY cohort_month
)

SELECT

    ca.cohort_month,

    ca.cohort_month_number,

    ca.active_customers,

    cs.cohort_size,

    ROUND(
        (
            CAST(
                ca.active_customers AS REAL
            )
            /
            cs.cohort_size
        ) * 100,
        2
    ) AS retention_rate

FROM cohort_activity ca

JOIN cohort_sizes cs

    ON ca.cohort_month = cs.cohort_month

ORDER BY

    ca.cohort_month,

    ca.cohort_month_number;


-- ============================================================
-- QUERY 9
-- REPEAT VS ONE-TIME CUSTOMERS
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

    CASE

        WHEN total_orders = 1
            THEN 'One-Time'

        WHEN total_orders >= 2
            THEN 'Repeat'

    END AS customer_type,

    COUNT(
        customer_id
    ) AS customer_count

FROM customer_orders

GROUP BY

    CASE

        WHEN total_orders = 1
            THEN 'One-Time'

        WHEN total_orders >= 2
            THEN 'Repeat'

    END

ORDER BY customer_type;


-- ============================================================
-- QUERY 10
-- CHURNED CUSTOMERS
--
-- Definition used here:
-- Customers whose last purchase was more than
-- 90 days before the latest order date in the dataset.
-- ============================================================

WITH customer_last_purchase AS (

    SELECT

        customer_id,

        MAX(
            date(order_date)
        ) AS last_purchase_date

    FROM orders

    GROUP BY customer_id

),

dataset_latest_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders
)

SELECT

    clp.customer_id,

    clp.last_purchase_date,

    dld.latest_date,

    CAST(
        julianday(
            dld.latest_date
        )
        -
        julianday(
            clp.last_purchase_date
        )
        AS INTEGER
    ) AS days_since_purchase

FROM customer_last_purchase clp

CROSS JOIN dataset_latest_date dld

WHERE

    julianday(
        dld.latest_date
    )
    -
    julianday(
        clp.last_purchase_date
    ) > 90

ORDER BY

    days_since_purchase DESC;


-- ============================================================
-- QUERY 11
-- CHURN SUMMARY
-- ============================================================

WITH customer_last_purchase AS (

    SELECT

        customer_id,

        MAX(
            date(order_date)
        ) AS last_purchase_date

    FROM orders

    GROUP BY customer_id

),

dataset_latest_date AS (

    SELECT

        MAX(
            date(order_date)
        ) AS latest_date

    FROM orders

),

customer_status AS (

    SELECT

        clp.customer_id,

        CASE

            WHEN
                julianday(
                    dld.latest_date
                )
                -
                julianday(
                    clp.last_purchase_date
                ) > 90

            THEN 'Churned'

            ELSE 'Active'

        END AS customer_status

    FROM customer_last_purchase clp

    CROSS JOIN dataset_latest_date dld
)

SELECT

    customer_status,

    COUNT(
        customer_id
    ) AS customer_count

FROM customer_status

GROUP BY customer_status

ORDER BY customer_status;


-- ============================================================
-- QUERY 12
-- REPEAT CUSTOMER RATE
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

customer_classification AS (

    SELECT

        customer_id,

        CASE

            WHEN total_orders = 1
                THEN 'One-Time'

            ELSE 'Repeat'

        END AS customer_type

    FROM customer_orders
)

SELECT

    COUNT(
        CASE
            WHEN customer_type = 'Repeat'
            THEN customer_id
        END
    ) AS repeat_customers,

    COUNT(
        CASE
            WHEN customer_type = 'One-Time'
            THEN customer_id
        END
    ) AS one_time_customers,

    COUNT(
        customer_id
    ) AS total_customers,

    ROUND(

        CAST(
            COUNT(
                CASE
                    WHEN customer_type = 'Repeat'
                    THEN customer_id
                END
            ) AS REAL
        )
        /
        COUNT(customer_id)
        * 100,

        2

    ) AS repeat_customer_rate

FROM customer_classification;


-- ============================================================
-- QUERY 13
-- COHORT RETENTION SUMMARY
-- ============================================================

WITH customer_first_purchase AS (

    SELECT

        customer_id,

        MIN(
            date(order_date)
        ) AS first_purchase_date

    FROM orders

    GROUP BY customer_id

),

customer_cohorts AS (

    SELECT

        customer_id,

        strftime(
            '%Y-%m',
            first_purchase_date
        ) AS cohort_month

    FROM customer_first_purchase
),

customer_activity AS (

    SELECT DISTINCT

        customer_id,

        strftime(
            '%Y-%m',
            order_date
        ) AS activity_month

    FROM orders
),

cohort_sizes AS (

    SELECT

        cohort_month,

        COUNT(
            customer_id
        ) AS cohort_size

    FROM customer_cohorts

    GROUP BY cohort_month
),

retention_data AS (

    SELECT

        cc.cohort_month,

        ca.activity_month,

        COUNT(
            DISTINCT cc.customer_id
        ) AS active_customers

    FROM customer_cohorts cc

    JOIN customer_activity ca

        ON cc.customer_id = ca.customer_id

    GROUP BY

        cc.cohort_month,

        ca.activity_month

)

SELECT

    rd.cohort_month,

    cs.cohort_size,

    MIN(
        rd.activity_month
    ) AS first_activity_month,

    MAX(
        rd.activity_month
    ) AS last_activity_month,

    COUNT(
        DISTINCT rd.activity_month
    ) AS active_months,

    ROUND(

        CAST(
            COUNT(
                DISTINCT rd.activity_month
            ) AS REAL
        )
        /
        NULLIF(
            (
                (
                    CAST(
                        strftime(
                            '%Y',
                            MAX(rd.activity_month) || '-01'
                        ) AS INTEGER
                    )
                    -
                    CAST(
                        strftime(
                            '%Y',
                            MIN(rd.activity_month) || '-01'
                        ) AS INTEGER
                    )
                ) * 12
                +
                (
                    CAST(
                        strftime(
                            '%m',
                            MAX(rd.activity_month) || '-01'
                        ) AS INTEGER
                    )
                    -
                    CAST(
                        strftime(
                            '%m',
                            MIN(rd.activity_month) || '-01'
                        ) AS INTEGER
                    )
                )
                + 1
            ),
            0
        )
        * 100,

        2

    ) AS cohort_activity_rate

FROM retention_data rd

JOIN cohort_sizes cs

    ON rd.cohort_month = cs.cohort_month

GROUP BY

    rd.cohort_month,

    cs.cohort_size

ORDER BY rd.cohort_month;


-- ============================================================
-- END
-- ============================================================

