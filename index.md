- [Формулы](#formula)
- [Теория](#theory)
- [Калькуляторы](#calc)

<a name="formula"></a> 
### Формулы
![image](https://github.com/user-attachments/assets/d6b3b396-6a9e-49d4-a414-04e867c9fa3f)

![image](https://github.com/user-attachments/assets/122afef1-a7b6-4dd6-a7f2-b2c5ba5cd20d)

![image](https://github.com/user-attachments/assets/9f6d9991-bf0b-455c-9e1e-5b3cfc61c84d)

Дисперсия: Средний квадрат отклонений значений от их среднего.

![image](https://github.com/user-attachments/assets/7e662101-bc67-42dd-911d-0dab948af51b)

Стандартное отклонение: Квадратный корень из дисперсии, показывает разброс данных.

![image](https://github.com/user-attachments/assets/f6d4f597-6fb3-40c8-bf1c-ee7180abbbd5)

Квартиль: Значения, которые делят данные на четыре равные части.
Межквартильный размах: Разница между третьим (Q3) и первым (Q1) квартилями, показывает разброс средней половины данных.

![image](https://github.com/user-attachments/assets/9cfb74a6-0a6c-4633-a0e1-8e2e6f2caffb)

![image](https://github.com/user-attachments/assets/043f5d72-d908-4b0a-9ab7-01e8af34aee6)

![image](https://github.com/user-attachments/assets/22e5c7e2-6054-4979-a505-a6ef9cecd3ef)

![image](https://github.com/user-attachments/assets/01a9eada-6b65-480f-8b7b-568bbf868b5b)

![image](https://github.com/user-attachments/assets/fed792fd-ef9d-4a8f-9b79-609f256fe47e)

![image](https://github.com/user-attachments/assets/38bf04e2-ca72-4448-8739-503e9790bfd5)

![image](https://github.com/user-attachments/assets/9d0ecece-56d1-4304-a6f4-e88080037e6f)

Коэффициент Джини: Мера неравномерности распределения, где 0 — полное равенство, 1 — полное неравенство.

![image](https://github.com/user-attachments/assets/f4890640-5619-4878-bb6b-be81b9d101c6)



<a name="theory"></a> 
### Теория
## Решение задачи классификации. Часть 1

### Метод k-ближайших соседей (KNN)
- **Идея**: Классификация нового объекта по классам ближайших \( k \) соседей.
- **Как работает**:
  - Выбирается количество ближайших соседей \( k \).
  - Для нового объекта находится расстояние до всех объектов выборки.
  - Присваивается класс, наиболее часто встречающийся среди соседей.
- **Гиперпараметр**: число \( k \).

Гиперпараметры — это параметры модели, которые задаются до обучения и не изменяются в процессе. Они определяют, как именно модель будет обучаться и обрабатывать данные. Примеры: количество деревьев в случайном лесу, степень регуляризации в линейной регрессии, число кластеров в методе k-means.

---

### Деревья решений
- **Идея**: Построение дерева, где каждый узел — проверка условия, а листья — классы.
- **Как работает**:
  - Выбирается признак, который лучше всего разделяет данные.
  - Дерево строится рекурсивно, пока не достигнута заданная глубина или минимальное число объектов в узле.
- **Применение**: Удобны для интерпретации, но могут переобучаться.

---

### Случайный лес (Random Forest)
- **Идея**: Использует множество деревьев решений, каждое обучается на случайной подвыборке.
- **Особенности**:
  - Усредняет результаты всех деревьев (в классификации — голосование).
  - Устойчив к переобучению.
- **Гиперпараметры**: число деревьев, глубина дерева, случайные признаки.

---

### Метрики оценки качества
1. **Accuracy**: Доля правильно классифицированных объектов.
2. **Precision**: Доля объектов, предсказанных как положительные, которые действительно положительные.
3. **Recall**: Доля всех положительных объектов, которые были правильно найдены.
4. **F-мера**: Среднее гармоническое Precision и Recall.

---

## Решение задачи классификации. Часть 2

### Метод опорных векторов (SVM)
- **Идея**: Ищет гиперплоскость, которая максимально разделяет классы.
- **Особенности**:
  - Используется для линейных и нелинейных разделений.
  - Для нелинейных задач применяются ядра (например, RBF).
- **Гиперпараметры**: регуляризация, тип ядра.

---

### Логистическая регрессия
- **Идея**: Предсказывает вероятность принадлежности к классу с использованием логистической функции.
- **Особенности**:
  - Линейный метод.
  - Хорошо работает на простых задачах.

---

### Наивный Байесовский классификатор
- **Идея**: Основан на теореме Байеса. Предполагает независимость признаков.
- **Применение**: Простой и быстрый алгоритм для текстовой классификации.

---

### Метрики оценки качества
1. **Кросс-энтропия (Logloss)**: Используется для оценки качества вероятностных предсказаний.
2. **ROC-AUC**: Измеряет качество ранжирования объектов.

---

## Задача кластеризации

### Метод k-means
- **Идея**: Делит данные на \( k \) кластеров, минимизируя расстояния до центроидов.
- **Как работает**:
  - Инициализируются центроиды.
  - Объекты распределяются к ближайшим центроидам.
  - Центроиды пересчитываются, процесс повторяется.
- **Метод локтя**: Используется для выбора оптимального числа кластеров.

---

### Метод DBSCAN
- **Идея**: Выделяет плотные области и игнорирует выбросы.
- **Особенности**:
  - Хорошо работает с данными произвольной формы.
  - Требует задания радиуса \( \varepsilon \) и минимального числа точек для кластера.

---

### Иерархическая кластеризация
1. **Агломеративная**: Объединение кластеров снизу вверх.
2. **Дивизивная**: Разделение кластеров сверху вниз.
- **Применение**: Построение иерархической структуры данных.

---

### Метрики оценки качества
1. **Метрика силуэт**: Оценивает, насколько хорошо объекты принадлежат своему кластеру.
2. **Метод локтя**: Помогает определить оптимальное число кластеров, наблюдая за снижением внутрикластерной дисперсии.

---

<a name="calc"></a>
### Калькуляторы

#### 1. Среднее (Mean)
Среднее (или арифметическое) — это сумма всех чисел, деленная на их количество.

**Формула**:  
\[
\text{Среднее} = \frac{\sum_{i=1}^{n} x_i}{n}
\]

<form id="mean-form">
  <label for="mean-input">Введите числа (через запятую): </label>
  <input type="text" id="mean-input" placeholder="1, 2, 3, 4">
  <button type="submit">Вычислить</button>
  <p id="mean-result"></p>
</form>

#### 2. Медиана (Median)
Медиана — это срединное значение в отсортированном наборе данных.

**Формула**:
- Для нечетного числа элементов медианой будет центральное значение.
- Для четного числа элементов медианой будет среднее значение двух центральных чисел.

<form id="median-form">
  <label for="median-input">Введите числа (через запятую): </label>
  <input type="text" id="median-input" placeholder="1, 2, 3, 4">
  <button type="submit">Вычислить</button>
  <p id="median-result"></p>
</form>

#### 3. Мода (Mode)
Мода — это число, которое встречается наиболее часто.

<form id="mode-form">
  <label for="mode-input">Введите числа (через запятую): </label>
  <input type="text" id="mode-input" placeholder="1, 2, 2, 3">
  <button type="submit">Вычислить</button>
  <p id="mode-result"></p>
</form>

#### 4. Дисперсия (Variance)
Дисперсия измеряет, как сильно значения отклоняются от среднего.

**Формула**:
\[
\text{Дисперсия} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2
\]

<form id="variance-form">
  <label for="variance-input">Введите числа (через запятую): </label>
  <input type="text" id="variance-input" placeholder="1, 2, 3, 4">
  <button type="submit">Вычислить</button>
  <p id="variance-result"></p>
</form>

#### 5. Стандартное отклонение (Standard Deviation)
Стандартное отклонение — это квадратный корень из дисперсии.

**Формула**:
\[
\text{Стандартное отклонение} = \sqrt{\text{Дисперсия}}
\]

<form id="std-deviation-form">
  <label for="std-deviation-input">Введите числа (через запятую): </label>
  <input type="text" id="std-deviation-input" placeholder="1, 2, 3, 4">
  <button type="submit">Вычислить</button>
  <p id="std-deviation-result"></p>
</form>

#### Скрипт JavaScript для расчетов

```html
<script>
  // Среднее
  document.getElementById('mean-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('mean-input').value.split(',').map(Number);
    let sum = input.reduce((a, b) => a + b, 0);
    let mean = sum / input.length;
    document.getElementById('mean-result').innerText = `Среднее: ${mean}`;
  });

  // Медиана
  document.getElementById('median-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('median-input').value.split(',').map(Number);
    input.sort((a, b) => a - b);
    let median;
    if (input.length % 2 === 0) {
      median = (input[input.length / 2 - 1] + input[input.length / 2]) / 2;
    } else {
      median = input[Math.floor(input.length / 2)];
    }
    document.getElementById('median-result').innerText = `Медиана: ${median}`;
  });

  // Мода
  document.getElementById('mode-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('mode-input').value.split(',').map(Number);
    let frequency = {};
    let maxCount = 0;
    let mode = [];
    input.forEach(num => {
      frequency[num] = (frequency[num] || 0) + 1;
      if (frequency[num] > maxCount) {
        maxCount = frequency[num];
        mode = [num];
      } else if (frequency[num] === maxCount) {
        mode.push(num);
      }
    });
    document.getElementById('mode-result').innerText = `Мода: ${mode.join(', ')}`;
  });

  // Дисперсия
  document.getElementById('variance-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('variance-input').value.split(',').map(Number);
    let mean = input.reduce((a, b) => a + b, 0) / input.length;
    let variance = input.reduce((acc, num) => acc + Math.pow(num - mean, 2), 0) / input.length;
    document.getElementById('variance-result').innerText = `Дисперсия: ${variance}`;
  });

  // Стандартное отклонение
  document.getElementById('std-deviation-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('std-deviation-input').value.split(',').map(Number);
    let mean = input.reduce((a, b) => a + b, 0) / input.length;
    let variance = input.reduce((acc, num) => acc + Math.pow(num - mean, 2), 0) / input.length;
    let stdDeviation = Math.sqrt(variance);
    document.getElementById('std-deviation-result').innerText = `Стандартное отклонение: ${stdDeviation}`;
  });
</script>

