
-- ============================================================
-- E-COMMERCE ANALYTICS SYSTEM
-- DATABASE SCHEMA
-- Database: SQLite
-- ============================================================


-- ============================================================
-- 1. CUSTOMERS TABLE
-- ============================================================

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (

    customer_id TEXT PRIMARY KEY,

    customer_name TEXT NOT NULL,

    email TEXT UNIQUE,

    registration_date DATE,

    customer_type TEXT NOT NULL,

    CHECK (
        customer_type IN (
            'REGULAR',
            'PREMIUM',
            'VIP'
        )
    )
);


-- ============================================================
-- 2. PRODUCTS TABLE
-- ============================================================

CREATE TABLE products (

    product_id TEXT PRIMARY KEY,

    product_name TEXT NOT NULL,

    category TEXT NOT NULL,

    subcategory TEXT NOT NULL,

    cost_price REAL NOT NULL,

    CHECK (
        cost_price > 0
    )
);


-- ============================================================
-- 3. ORDERS TABLE
-- ============================================================

CREATE TABLE orders (

    order_id TEXT PRIMARY KEY,

    customer_id TEXT NOT NULL,

    order_date DATETIME NOT NULL,

    status TEXT NOT NULL,

    region_code TEXT NOT NULL,

    CHECK (
        status IN (
            'PLACED',
            'SHIPPED',
            'DELIVERED',
            'CANCELLED',
            'RETURNED'
        )
    ),

    CHECK (
        region_code IN (
            'NORTH',
            'SOUTH',
            'EAST',
            'WEST',
            'CENTRAL'
        )
    ),

    FOREIGN KEY (
        customer_id
    )
    REFERENCES customers(customer_id)
);


-- ============================================================
-- 4. ORDER ITEMS TABLE
-- ============================================================

CREATE TABLE order_items (

    item_id TEXT PRIMARY KEY,

    order_id TEXT NOT NULL,

    product_id TEXT NOT NULL,

    quantity INTEGER NOT NULL,

    unit_price REAL NOT NULL,

    discount_percent REAL NOT NULL DEFAULT 0,

    CHECK (
        quantity > 0
    ),

    CHECK (
        unit_price > 0
    ),

    CHECK (
        discount_percent >= 0
        AND discount_percent <= 100
    ),

    FOREIGN KEY (
        order_id
    )
    REFERENCES orders(order_id),

    FOREIGN KEY (
        product_id
    )
    REFERENCES products(product_id)
);


-- ============================================================
-- 5. INDEXES
-- ============================================================

CREATE INDEX idx_orders_customer
ON orders(customer_id);


CREATE INDEX idx_orders_date
ON orders(order_date);


CREATE INDEX idx_order_items_order
ON order_items(order_id);


CREATE INDEX idx_order_items_product
ON order_items(product_id);


CREATE INDEX idx_products_category
ON products(category);


-- ============================================================
-- END OF SCHEMA
-- ============================================================

