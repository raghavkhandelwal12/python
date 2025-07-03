# Vector Spaces 

## Vector Space kya hota hai?

Ek **vector space** (jisko **linear space** bhi kehte hain) ek aisa set hota hai jisme **vectors** hote hain. Ye vectors:
- **Add** kiye ja sakte hain
- **Scalars** (jaise real ya complex number) se **multiply** kiye ja sakte hain

Aur ye sab ek certain **rules (properties/axioms)** ko follow karte hain.

## Vector Space Properties (with Data Science Use)

Assume karo:
- Vectors: `u, v, w ∈ V`
- Scalars: `a, b ∈ R (Real numbers)`

## 1. Closure Under Addition
```
If u, v ∈ V, then u + v ∈ V #here u and v are vector

**Example:**  
Let u = [1, 2], v = [3, 4]  
Then u + v = [1 + 3, 2 + 4] = [4, 6] ∈ V
```

**Matlab:** Agar do vectors add karo to result bhi vector hi hoga.

**Data Science Use:**  
NLP me **word embeddings** add karne par combined meaning milta hai.  
Example:  
`embedding("king") + embedding("woman") ≈ embedding("queen")`

## 2. Closure Under Scalar Multiplication
```
**Property:**  
If a ∈ ℝ and v ∈ V, then a · v ∈ V # here a is scalar and v is vector

**Example:**  
Let v = [2, 3], a = 4  
Then a · v = 4 · [2, 3] = [8, 12] ∈ V
```

**Matlab:** Vector ko scalar se multiply karne par result bhi vector hi hoga.

**Data Science Use:**  
- Feature Scaling aur Gradient Descent me use hota hai.

**Linear Regression equation:**  
`ŷ = w1x1 + w2x2 + ... + wnxn`  
- `xi`: input feature (e.g., age, salary)  
- `wi`: weight  
- `ŷ`: predicted output

Har feature ko ek scalar (weight) se multiply karte hain = scalar multiplication ho gaya

## 3. Associativity of Addition

```
**Property:**  
(u + v) + w = u + (v + w) # here v, u, and w are vectors

**Example:**  
Let u = [1, 0], v = [0, 2], w = [3, 3]  
Then:  
(u + v) + w = [1, 2] + [3, 3] = [4, 5]  
u + (v + w) = [1, 0] + [3, 5] = [4, 5]
```

**Matlab:** `(u + v) + w = u + (v + w)`

**Use in Data Science:**  
Multimodal models (image + text + audio) combine karte waqt order matter nahi karta.

## 4. Commutativity of Addition
```

**Property:**  
u + v = v + u #here v and u are vector

**Example:**  
Let u = [1, 2], v = [3, 4]  
Then u + v = [4, 6] = v + u
```

**Matlab:** `u + v = v + u`

**Use in Data Science:**  
Cosine similarity jisme vector order se result change nahi hota.

## 5. Additive Identity
```
**Property:**  
There exists a zero vector 0 ∈ V such that v + 0 = v # here v is vector

**Example:**  
Let v = [5, -3]  
Then v + [0, 0] = [5, -3]
```

**Matlab:** `v + 0 = v` (0 is zero vector)

**Use in Data Science:**  
- Weights initialization me zero vector use karte hain  
- NLP me one-hot vector: `[0, 0, 1, 0]` – yeh sparse vector hai

## 6. Additive Inverse
```
**Property:**  
For every v ∈ V, there exists -v ∈ V such that v + (-v) = 0 # here v is vector

**Example:**  
Let v = [2, -5]  
Then -v = [-2, 5], and v + (-v) = [0, 0]
```

**Matlab:** `v + (-v) = 0`

**Use in Data Science:**  
Gradient Descent me loss minimize karne ke liye opposite direction me weight update hota hai → yeh additive inverse ka concept hai

## 7. Distributivity of Scalar Over Vector Addition
```
**Property:**  
a · (u + v) = a · u + a · v # here u and v are vector and a is scalar

**Example:**  
Let u = [1, 2], v = [3, 4], a = 2  
Then:  
u + v = [4, 6]  
a · (u + v) = 2 · [4, 6] = [8, 12]  
a · u + a · v = [2, 4] + [6, 8] = [8, 12]
```

**Matlab:** `a(u + v) = au + av`

**Use in Neural Networks:**  
Linear layer:  
`Output = W.X + b`  
- `X`: input vector  
- `W`: weight matrix  
- Scalar har input pe apply hota hai → distributive property apply hoti hai

## 8. Distributivity of Vector Over Scalar Addition
```
**Property:**  
(a + b) · v = a · v + b · v # Here a and b are scalar and v is a vector

**Example:**  
Let v = [2, 1], a = 1, b = 3  
Then:  
(a + b) · v = 4 · [2, 1] = [8, 4]  
a · v + b · v = [2, 1] + [6, 3] = [8, 4]
```

**Matlab:** `(a + b)v = av + bv`

**Use in Data Science:**  
Regularization techniques me use hota hai (e.g., L2 regularization)

## 9. Associativity of Scalar Multiplication
```
**Property:**  
a · (b · v) = (a · b) · v # here a and b are scalar and v is vector

**Example:**  
Let v = [1, 2], a = 2, b = 3  
Then:  
b · v = [3, 6], a · (b · v) = [6, 12]  
(a · b) · v = 6 · [1, 2] = [6, 12] 
```

**Matlab:** `a(bv) = (ab)v`

**Use in Data Science:**  
Optimization me jab learning rate + momentum use hota hai

## 10. Scalar Multiplicative Identity
```
**Property:**  
1 · v = v

**Example:**  
Let v = [7, 9]  
Then 1 · v = [7, 9] # Here v for vector
```

**Matlab:** `1 * v = v`

**Use in Deep Learning:**  
Residual Networks me use hota hai:  
`Output = Input + f(Input)`

## Real World Use in Data Science

Data Science me vectors ka matlab hota hai: list of numbers

Example:  
`User vector = [4, 5, 2, 0, 1]`  
Yeh dikhata hai user ko movies kitni pasand hai. Har user ek point in space banata hai → Vector Space

## Vector Space Kyun Useful Hai?

1. Measure Similarity – Text ya users ke beech similarity check kar sakte ho  
2. Project Data – Important features pe focus karna  
3. Scale Features – Values ko normalize karna  
4. Combine Features – Machine learning model me features ko weighted combine karna

## Practical Examples

1. Customer Features (Retail)  
   `[frequency, recency, amount spent]` → vector form

2. Document Embeddings (NLP)  
   Text ko convert karte hain numeric vectors me → use for classification, clustering

3. Sensor Data (IoT)  
   Temperature, pressure, humidity etc. → all combined as vector
