# The Logic Lode 💎

> **Visualizing the hidden logic of the universe.**

Welcome to **The Logic Lode**, a collection of high-quality mathematical, physical, and computational visualizations. This project aims to simplify complex concepts through elegant animations, providing "aha!" moments through visual intuition.

All animations are created using [Manim (Community Edition)](https://www.manim.community/), a mathematical animation engine for explanatory math videos.

## 📽️ Project Portfolio

### 1. [Fraction Addition](./projects/fraction_addition/)
An intuitive guide to adding fractions using area-based models. Covers:
- Same denominators.
- Related denominators (multiples).
- Universal method (grid division).
- Lowest Common Multiple (LCM) visualization.

### 2. [Percentage Swap](./projects/percentage_swap/)
Visual proof of why $a\%$ of $b$ is always equal to $b\%$ of $a$. Uses geometric area transformations to make the commutative property of multiplication obvious.

### 3. [Square Ending in 5](./projects/square_ending_in_5/)
A mental math trick visualized. Shows why $(10n + 5)^2 = 100n(n+1) + 25$ using a geometric decomposition of a square.

### 4. [Successive Increases](./projects/successive_increases/)
Explaining why a $+30\%$ increase followed by a $+20\%$ increase results in a $+56\%$ total increase (not $50\%$). Uses additive area growth to show the "interest on interest" effect.

### 5. [Metric Spaces](./projects/metric_spaces/)
*Status: In Progress*
Exploring how the definition of "distance" changes the shape of a circle. Visualizes Euclidean ($L_2$), Taxicab ($L_1$), and Chebyshev ($L_\infty$) metrics.

### 6. [Pi Visual](./pi_vizual_eng.py)
Visualizing the fundamental constant $\pi$ by rolling circles and unrolling their circumferences onto a number line. Shows:
- Definition of $\pi$ as the constant ratio $\frac{Circumference}{Diameter}$.
- Dynamic variation of diameter while maintaining the ratio.
- Focused zoom on the number line at $x = \pi \approx 3.14159\dots$.

## 🛠️ Requirements

- Python 3.8+
- [Manim](https://docs.manim.community/en/stable/installation.html)
- LaTeX (for mathematical formulas)

## 🚀 Usage

To render a specific project in 4K Vertical (9:16) format:

```bash
manim -pqh projects/folder_name/file_name.py SceneName
```

---
**Follow the journey:**
[YouTube](https://youtube.com/@thelogiclode) | [Instagram](https://instagram.com/thelogiclode) | [TikTok](https://tiktok.com/@thelogiclode)
