
# 🛒 eCommerce FastAPI Backend

This is a sample **eCommerce backend application** built using **FastAPI** and **MongoDB**.  
It was created as part of the **HROne Backend Intern Hiring Task** by **Panuku Sairam**.

---

## 📦 Features

- ✅ Create Products
- ✅ List Products with filters (`name`, `size`, pagination)
- ✅ Get Product by ID or Name
- ✅ Create Orders
- ✅ Get Orders by User or Order ID
- ✅ Delete Order by Order ID

---

## 🚀 Technologies Used

- **Python 3.10+**
- **FastAPI** (High-performance web framework)
- **MongoDB Atlas** (Free-tier cloud database)
- **PyMongo** (MongoDB driver for Python)
- **Render** (Cloud deployment platform)

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/Sairam-Panuku/ecommerce-fastapi-backend
cd ecommerce-fastapi-backend
python -m venv .venv
source .venv/Scripts/activate  # or `source .venv/bin/activate` on Linux/mac
pip install -r requirements.txt
uvicorn main:app --reload
````

Make sure to create a `.env` file with your MongoDB URI:

```
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
```

---

## 🧪 API Endpoints

### 📁 Products

#### ✅ Create Product

URL: `POST /products`
Body:

```json
{
  "name": "Leather Jacket",
  "price": 7999,
  "description": "Stylish black leather jacket",
  "size": "L",
  "tags": ["fashion", "winter"]
}
```

#### ✅ Get All Products

URL: `GET /products`

#### ✅ Get Product by ID

URL: `GET /products/{id}`

#### ✅ Get Product by Name

URL: `GET /products/name/{name}`

---

### 🧾 Orders

#### ✅ Create Order

URL: `POST /orders`
Body:

```json
{
  "user_id": "user123",
  "product_ids": ["product_id1", "product_id2"],
  "total_amount": 1499.99
}
```

#### ✅ Get All Orders

URL: `GET /orders`

#### ✅ Get Order by Order ID

URL: `GET /orders/{order_id}`

#### ✅ Get Orders by User ID

URL: `GET /orders/user/{user_id}`

#### ❌ Delete Order by ID

URL: `DELETE /orders/{order_id}`

---

## 📡 Hosted Backend URL

> 🔗 [https://hrone-backend-ecommerce.onrender.com](https://hrone-backend-ecommerce.onrender.com)

---

## 🧑‍💻 Author

 Panuku Sairam

 🎓 B.Tech CSE (AI & ML)
 🌐 GitHub: [Sairam-Panuku](https://github.com/Sairam-Panuku)

---

## 🙌 Acknowledgements

Thanks to HROne for the opportunity.
Inspired by real-world backend design challenges.

