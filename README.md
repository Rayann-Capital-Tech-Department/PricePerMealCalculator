# PricePerMealCalculator

#### Calculates price per meal for FitBento.

### Run the program

in your terminal, run: `python PricePerMealCalculator.py`

---

### Inputs and Outputs

(Italicized == columns used for calculation)

#### Sample Input① : Recipe Nutrition Facts

this file has multiple sheets; below is an example sheet titled "An Amazing Recipe"

| _Name_ | _Tags_   | Cooking Method | Zone Blocks | _Needed_   | calories (kcal) | carbohydrates (g) | fats (g) | protein (g) | sodium (mg) | sugar (g)        |
| ------ | -------- | -------------- | ----------- | ---------- | --------------- | ----------------- | -------- | ----------- | ----------- | ---------------- |
| Pork   | Shoulder |                | 5           | 100 g      | 405             | 0                 | 30       | 35          | 0           | 0                |
| Pork   | Belly    |                | 0           | 50 g       | 0               | 0                 | 0        | 0           | 0           | 0                |
|        |          |                |             | TOTAL      | 666             | 45                | 38       | 40          | 125         | 10               |
|        |          |                |             |            |                 |                   |          |             |             |                  |
|        |          | sugar-free     | vegan       | vegetarian | gluten-free     | lactose-free      | paleo    | whole 30    | zone        | zone-Unfavorable |
|        |          | no             | yes         | no         | yes             | yes               | yes      | yes         | yes         | Garlic           |

#### Sample Input②: Ingredient list: Price Data

| _Ingredient_ | _Tags_   | _Supplier_ | Storage | Official English Name    | Official Japanese Name                       | _Price (¥)_ | _Amount_ | _Units_ | Shelf Life (Days) |
| ------------ | -------- | ---------- | ------- | ------------------------ | -------------------------------------------- | ----------- | -------- | ------- | ----------------- |
| Pork         | Shoulder | Costco     | Chilled | Canada Pork Katarosu BBQ | カナダ産チルド豚肉・三元豚・肩ロース・焼肉用 | 10          | 100      | g       |                   |
| Pork         | Belly    | Costco     | Chilled | Canada Pork Belly VP     | カナダ産チルド豚肉・三元豚・バラ・真空パック | 20          | 10       | g       |                   |

#### Sample Output:

| Meal Name         | Total Price |       |          |
| ----------------- | ----------- | ----- | -------- |
| An Amazing Recipe | 110         |       |          |
| Ingredient        | Tag         | Price | Supplier |
| Pork              | Shoulder    | 10    | Costco   |
| Pork              | Belly       | 100   | Costco   |
