# Product Marketplace Backend

This is the backend for the Product Marketplace project built with **Django REST Framework**.  
It provides an API for managing products and business workflows.

## Features

- CRUD operations for products
- Business scoping: users only see products from their own business
- Product approval workflow (draft → pending → approved)
- Optional AI chatbot integration (future)

## Tech Stack

- Django 6.0
- Django REST Framework
- SQLite (default database)
- CORS Headers

## Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/Hawa4123/product-marketplace.git
cd product-marketplace